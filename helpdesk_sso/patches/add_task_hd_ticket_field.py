import frappe


def execute():
	if frappe.db.exists("Custom Field", {"dt": "Task", "fieldname": "custom_hd_ticket"}):
		return

	if not frappe.db.exists("DocType", "Task"):
		return

	frame_doc = frappe.get_doc(
		{
			"doctype": "Custom Field",
			"dt": "Task",
			"fieldname": "custom_hd_ticket",
			"fieldtype": "Link",
			"options": "HD Ticket",
			"label": "Helpdesk Ticket",
			"insert_after": "project",
			"in_standard_filter": 1,
			"description": "The support ticket this task was created for, if any.",
		}
	)
	frame_doc.insert(ignore_permissions=True)
	frappe.db.commit()
