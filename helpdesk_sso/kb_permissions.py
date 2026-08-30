import frappe

from helpdesk.utils import get_customers, is_agent


def _user_customers(user=None):
	"""Return None if user is an agent (no restriction), else a list of
	HD Customer names the user belongs to (may be empty list)."""
	user = user or frappe.session.user
	if is_agent(user):
		return None
	return get_customers(user)


def _category_condition(customers):
	if not customers:
		return "`tabHD Article Category`.`customer` is null"
	customer_list = ", ".join(frappe.db.escape(c) for c in customers)
	return (
		"(`tabHD Article Category`.`customer` is null "
		f"or `tabHD Article Category`.`customer` in ({customer_list}))"
	)


def article_category_query_conditions(user=None):
	customers = _user_customers(user)
	if customers is None:
		return ""
	return _category_condition(customers)


def article_category_has_permission(doc, user=None):
	customers = _user_customers(user)
	if customers is None:
		return True
	if not doc.get("customer"):
		return True
	return doc.get("customer") in customers


def article_query_conditions(user=None):
	customers = _user_customers(user)
	if customers is None:
		return ""
	condition = _category_condition(customers)
	return (
		"(`tabHD Article`.`category` is null or `tabHD Article`.`category` in ("
		"select `name` from `tabHD Article Category` where " + condition + "))"
	)


def article_has_permission(doc, user=None):
	customers = _user_customers(user)
	if customers is None:
		return True
	category = doc.get("category")
	if not category:
		return True
	category_customer = frappe.db.get_value(
		"HD Article Category", category, "customer"
	)
	if not category_customer:
		return True
	return category_customer in customers
