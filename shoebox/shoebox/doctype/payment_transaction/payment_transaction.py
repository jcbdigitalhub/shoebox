# -*- coding: utf-8 -*-
# Copyright (c) 2018, JCB Accounting Services and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.model.mapper import get_mapped_doc
from erpnext.accounts.utils import get_outstanding_invoices, get_account_currency, get_balance_on
from erpnext.accounts.party import get_party_account

class PaymentTransaction(Document):
	pass

