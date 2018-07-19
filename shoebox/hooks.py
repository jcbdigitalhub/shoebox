# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "shoebox"
app_title = "Shoebox"
app_publisher = "JCB Accounting Services"
app_description = "Shoebox for Bookkeping"
app_icon = "octicon octicon-inbox"
app_color = "blue"
app_email = "info@jcbaccountingservices.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/shoebox/css/shoebox.css"
# app_include_js = "/assets/shoebox/js/shoebox.js"

# include js, css files in header of web template
# web_include_css = "/assets/shoebox/css/shoebox.css"
# web_include_js = "/assets/shoebox/js/shoebox.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
#doctype_js = {"Payment Entry" : "custom_scripts/payment_entry.js"}
doctype_js = {"Journal Entry" : "custom_scripts/journal_entry.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "shoebox.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "shoebox.install.before_install"
# after_install = "shoebox.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "shoebox.notifications.get_notification_config"

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

doc_events = {
	"Journal Entry": {
		"on_submit": "shoebox.api.on_submit",
#		"on_cancel": "api.py",
#		"on_trash": "api.py"
	}
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"shoebox.tasks.all"
# 	],
# 	"daily": [
# 		"shoebox.tasks.daily"
# 	],
# 	"hourly": [
# 		"shoebox.tasks.hourly"
# 	],
# 	"weekly": [
# 		"shoebox.tasks.weekly"
# 	]
# 	"monthly": [
# 		"shoebox.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "shoebox.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "shoebox.event.get_events"
# }

