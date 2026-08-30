import frappe


def after_install():
	create_support_user_token_doctype()


def create_support_user_token_doctype():
	if frappe.db.exists("DocType", "Support User Token"):
		return

	frappe.get_doc(
		{
			"doctype": "DocType",
			"name": "Support User Token",
			"module": "Helpdesk SSO",
			"custom": 1,
			"fields": [
				{
					"fieldname": "user_id",
					"fieldtype": "Link",
					"options": "User",
					"label": "User",
					"reqd": 1,
				},
				{
					"fieldname": "user_token",
					"fieldtype": "Data",
					"label": "Token",
					"unique": 1,
					"no_copy": 1,
				},
				{
					"fieldname": "enabled",
					"fieldtype": "Check",
					"label": "Enabled",
					"default": "0",
				},
			],
			"permissions": [
				{"role": "System Manager", "read": 1, "write": 1, "create": 1, "delete": 1}
			],
		}
	).insert(ignore_permissions=True)
	frappe.db.commit()
