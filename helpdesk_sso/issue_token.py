import frappe
from frappe.utils import random_string


def issue(user_email="Administrator"):
	token = random_string(48)
	if frappe.db.exists("Support User Token", {"user_id": user_email}):
		frappe.db.set_value("Support User Token", {"user_id": user_email}, {"user_token": token, "enabled": 1})
	else:
		frappe.get_doc({
			"doctype": "Support User Token",
			"user_id": user_email,
			"user_token": token,
			"enabled": 1,
		}).insert(ignore_permissions=True)
	frappe.db.commit()
	print(token)
