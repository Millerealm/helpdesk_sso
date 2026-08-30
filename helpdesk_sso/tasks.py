import frappe
from helpdesk.utils import is_agent


@frappe.whitelist()
def get_linked_tasks(ticket: str):
	if not is_agent(frappe.session.user):
		frappe.throw("Not permitted", frappe.PermissionError)
	return frappe.get_all(
		"Task",
		filters={"custom_hd_ticket": ticket},
		fields=["name", "subject", "status"],
		order_by="creation desc",
	)
