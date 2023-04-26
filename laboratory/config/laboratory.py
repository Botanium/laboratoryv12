from __future__ import unicode_literals
from frappe import _
"""

Adding doctypes and displaying it 
		{
			"label": _("Custom Reports"),
			"items": [
				{
					"type": "report",
					"is_query_report": True,
					"name": "Stock Ledger",
					"doctype": "Stock Ledger Entry",
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Stock Balance",
					"doctype": "Stock Ledger Entry"
				},

			]
		},
		
		{
			"label": _("Production"),
			"icon": "fa fa-star",
			"items": [
				{
					"type": "doctype",
					"name": "Production Order",
					"description": _("Orders released for production."),
				},
				
			]
		}
		
"""
		
# this allows customization
def get_data():
	return [
		{
			"label": _("Help"),
			"icon": "fa fa-facetime-video",
			"items": [
				{
					"type": "help",
					"label": _("How to Use"),
					"youtube_id": "eX7LbhJ7oAU"
				},	
			{
					"type": "doctype",
					"name": "Laboratory Module Feedback",
					"description": _("You can provide future developments here"),
				},
				{
					"type": "help",
					"label": _("Reporting an Issue"),
					"youtube_id": "p_4UPdFqgIQ"
				},
			]
		}
		
	]