# -*- coding: utf-8 -*-
# Copyright (c) 2015, Frappe Technologies and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
import json
from frappe import _
from frappe.model.mapper import get_mapped_doc
from frappe.utils import flt, cstr
from frappe.email.doctype.email_group.email_group import add_subscribers

def on_submit(doc, method):
	if doc.voucher_type != "Journal":
		d = frappe.get_doc(doc.shoebox_doctype, doc.shoebox_document_no)
		d.submit()
