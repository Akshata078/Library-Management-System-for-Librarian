# Copyright (c) 2025, Akshata Khadse and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Member(Document):
    def before_save(self):
        if self.outstanding_debt > 500:
            frappe.throw("Member cannot have outstanding fees above Rs.500!")