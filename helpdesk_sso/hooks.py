app_name = "helpdesk_sso"
after_install = "helpdesk_sso.install.after_install"
app_title = "Helpdesk SSO"
app_publisher = "Millerealm"
app_description = "Auto-login bridge from CRM to Helpdesk"
app_email = "developer@app.millerealm.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "helpdesk_sso",
# 		"logo": "/assets/helpdesk_sso/logo.png",
# 		"title": "Helpdesk SSO",
# 		"route": "/helpdesk_sso",
# 		"has_permission": "helpdesk_sso.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/helpdesk_sso/css/helpdesk_sso.css"
# app_include_js = "/assets/helpdesk_sso/js/helpdesk_sso.js"

# include js, css files in header of web template
# web_include_css = "/assets/helpdesk_sso/css/helpdesk_sso.css"
# web_include_js = "/assets/helpdesk_sso/js/helpdesk_sso.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "helpdesk_sso/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "helpdesk_sso/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# automatically load and sync documents of this doctype from downstream apps
# importable_doctypes = [doctype_1]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "helpdesk_sso.utils.jinja_methods",
# 	"filters": "helpdesk_sso.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "helpdesk_sso.install.before_install"
# after_install = "helpdesk_sso.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "helpdesk_sso.uninstall.before_uninstall"
# after_uninstall = "helpdesk_sso.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "helpdesk_sso.utils.before_app_install"
# after_app_install = "helpdesk_sso.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "helpdesk_sso.utils.before_app_uninstall"
# after_app_uninstall = "helpdesk_sso.utils.after_app_uninstall"

# Build
# ------------------
# To hook into the build process

# after_build = "helpdesk_sso.build.after_build"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "helpdesk_sso.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"helpdesk_sso.tasks.all"
# 	],
# 	"daily": [
# 		"helpdesk_sso.tasks.daily"
# 	],
# 	"hourly": [
# 		"helpdesk_sso.tasks.hourly"
# 	],
# 	"weekly": [
# 		"helpdesk_sso.tasks.weekly"
# 	],
# 	"monthly": [
# 		"helpdesk_sso.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "helpdesk_sso.install.before_tests"

# Extend DocType Class
# ------------------------------
#
# Specify custom mixins to extend the standard doctype controller.
# extend_doctype_class = {
# 	"Task": "helpdesk_sso.custom.task.CustomTaskMixin"
# }

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "helpdesk_sso.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "helpdesk_sso.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["helpdesk_sso.utils.before_request"]
# after_request = ["helpdesk_sso.utils.after_request"]

# Job Events
# ----------
# before_job = ["helpdesk_sso.utils.before_job"]
# after_job = ["helpdesk_sso.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"helpdesk_sso.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

# Translation
# ------------
# List of apps whose translatable strings should be excluded from this app's translations.
# ignore_translatable_strings_from = []


# --- Knowledge Base customer scoping (added) ---
permission_query_conditions = {
	"HD Article Category": "helpdesk_sso.kb_permissions.article_category_query_conditions",
	"HD Article": "helpdesk_sso.kb_permissions.article_query_conditions",
}

has_permission = {
	"HD Article Category": "helpdesk_sso.kb_permissions.article_category_has_permission",
	"HD Article": "helpdesk_sso.kb_permissions.article_has_permission",
}

override_whitelisted_methods = {
	"helpdesk.api.knowledge_base.get_article": "helpdesk_sso.kb_overrides.get_article",
	"helpdesk.api.knowledge_base.get_category_articles": "helpdesk_sso.kb_overrides.get_category_articles",
	"helpdesk.api.knowledge_base.create_category": "helpdesk_sso.kb_overrides.create_category",
}

override_doctype_dashboards = {
	"HD Ticket": "helpdesk_sso.dashboard.get_dashboard_data",
}
