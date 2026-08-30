import frappe
from frappe import _
from frappe.rate_limiter import rate_limit


@frappe.whitelist(allow_guest=True)
@rate_limit(limit=20, seconds=60)
def helpdesk_auto_login():
	token = frappe.form_dict.get("token")
	if not token:
		frappe.throw(_("Missing token"))

	row = frappe.db.get_value(
		"Support User Token",
		{"user_token": token, "enabled": 1},
		["user_id"],
		as_dict=True,
	)
	if not row:
		frappe.throw(_("Invalid or disabled link"))

	# Device already has a live Frappe session for this exact user (sid cookie
	# sent automatically by the browser) - reuse it instead of forcing a new
	# login. Only skip re-login when the session belongs to the SAME user the
	# token maps to, so a stale session for a different account on a shared
	# device can't silently be reused.
	if frappe.session.user and frappe.session.user not in ("Guest", None) and frappe.session.user == row.user_id:
		frappe.local.response["type"] = "redirect"
		frappe.local.response["location"] = "/helpdesk"
		return

	if not frappe.db.get_value("User", row.user_id, "enabled"):
		frappe.throw(_("User account disabled"))

	frappe.local.login_manager.user = row.user_id
	frappe.local.login_manager.post_login()

	frappe.local.response["type"] = "redirect"
	frappe.local.response["location"] = "/helpdesk"
