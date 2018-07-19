from __future__ import unicode_literals
from frappe import _

def get_data():
        return [
                {
                        "label": _("My Transactions"),
                        "items": [
                                {
                                        "type": "doctype",
                                        "name": "Sales Transaction",
					"label": "Sales"
                                },
                                {
                                        "type": "doctype",
                                        "name": "Purchase Transaction",
					"label": "Purchases"
                                },
				{
				        "type": "doctype",
                                        "name": "Receipt Transaction",
					"label": "Receipts"
				},
				{
				        "type": "doctype",
                                        "name": "Payment Transaction",
					"label": "Payments"
				},
                        ]
                },
                {
                        "label": _("My Compliance"),
                        "items": [
                                {
                                        "type": "doctype",
                                        "name": "Tax Return"
                                },
                                {
                                        "type": "doctype",
                                        "name": "Books of Accounts"
                                },
                                {
                                        "type": "doctype",
                                        "name": "Registration"
                                },
                        ]
                },
                {
                        "label": _("My Accountant"),
                        "items": [
                                {
                                        "type": "doctype",
                                        "name": "Journal Entry"
                                },
				{
					"type": "doctype",
					"name": "Account",
					"icon": "fa fa-sitemap",
					"label": _("Chart of Accounts"),
					"route": "Tree/Account",
					"description": _("Tree of financial accounts."),
				},
                                {
                                        "type": "doctype",
                                        "name": "Customer"
                                },
                                {
                                        "type": "doctype",
                                        "name": "Supplier"
                                },
				{
					"type": "doctype",
					"name": "Bank Reconciliation",
					"label": _("Bank Reconciliation"),
					"description": _("Update bank transaction clearing dates."),
				},

                        ]
                },
		{
			"label": _("Reports"),
			"items": [
				{
					"type": "report",
					"name": "Trial Balance",
					"doctype": "GL Entry",
					"is_query_report": True,
				},
				{
					"type": "report",
					"name": "Balance Sheet",
					"doctype": "GL Entry",
					"is_query_report": True
				},
				{
					"type": "report",
					"name": "Cash Flow",
					"doctype": "GL Entry",
					"is_query_report": True
				},
				{
					"type": "report",
					"name": "Profit and Loss Statement",
					"doctype": "GL Entry",
					"is_query_report": True
				},
				{
					"type": "report",
					"name":"General Ledger",
					"doctype": "GL Entry",
					"is_query_report": True,
				},

			]
		},
		]
