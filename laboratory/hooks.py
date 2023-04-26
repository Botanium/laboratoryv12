# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "laboratory"
app_title = "Laboratory"
app_publisher = "www.fwrat.com"
app_description = "Laboratory App by Fwrat.com"
app_icon = "octicon octicon-beaker"
app_color = "#33FF93"
app_email = "admin@fwrat.com"
app_license = "GNU General Public License"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/laboratory/css/laboratory.css"
# app_include_js = "/assets/laboratory/js/laboratory.js"

# include js, css files in header of web template
# web_include_css = "/assets/laboratory/css/laboratory.css"
# web_include_js = "/assets/laboratory/js/laboratory.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "laboratory.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "laboratory.install.before_install"
# after_install = "laboratory.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "laboratory.notifications.get_notification_config"

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
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"laboratory.tasks.all"
# 	],
# 	"daily": [
# 		"laboratory.tasks.daily"
# 	],
# 	"hourly": [
# 		"laboratory.tasks.hourly"
# 	],
# 	"weekly": [
# 		"laboratory.tasks.weekly"
# 	]
# 	"monthly": [
# 		"laboratory.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "laboratory.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "laboratory.event.get_events"
# }

