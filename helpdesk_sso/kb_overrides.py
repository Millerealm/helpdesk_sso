import frappe

from helpdesk.api.knowledge_base import create_category as _original_create_category
from helpdesk.api.knowledge_base import get_article as _original_get_article
from helpdesk.api.knowledge_base import (
	get_category_articles as _original_get_category_articles,
)


@frappe.whitelist(allow_guest=True)
def get_article(name: str):
	frappe.has_permission("HD Article", ptype="read", doc=name, throw=True)
	return _original_get_article(name)


@frappe.whitelist()
def get_category_articles(category: str):
	frappe.has_permission(
		"HD Article Category", ptype="read", doc=category, throw=True
	)
	return _original_get_category_articles(category)


@frappe.whitelist()
def create_category(title: str, customer: str | None = None):
	result = _original_create_category(title)
	if customer:
		frappe.db.set_value(
			"HD Article Category", result["category"], "customer", customer
		)
	return result
