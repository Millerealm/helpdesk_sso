import frappe


def execute():
	if frappe.db.exists(
		"Custom Field", {"dt": "HD Article Category", "fieldname": "customer"}
	):
		return

	frappe.get_doc(
		{
			"doctype": "Custom Field",
			"dt": "HD Article Category",
			"fieldname": "customer",
			"fieldtype": "Link",
			"options": "HD Customer",
			"label": "Customer",
			"insert_after": "description",
			"description": (
				"Restrict this category (and its articles) to one customer. "
				"Leave blank to make it visible to all customers."
			),
		}
	).insert(ignore_permissions=True)
	frappe.db.commit()
