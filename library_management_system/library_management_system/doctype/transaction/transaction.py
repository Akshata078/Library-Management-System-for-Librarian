# Copyright (c) 2025, Akshata Khadse and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from datetime import datetime
from dateutil.relativedelta import relativedelta

class Transaction(Document):
    def validate(self):
        self.validate_dates()

        fine_per_day = 2  

        book = frappe.get_doc("Book", self.book)
        member = frappe.get_doc("Member", self.member)

        if self.due_date and self.return_date:
            due_date = datetime.strptime(self.due_date, "%Y-%m-%d").date()
            return_date = datetime.strptime(self.return_date, "%Y-%m-%d").date()
            difference = (return_date - due_date).days
            self.fine = max(difference * fine_per_day, 0)
        else:
            self.fine = 0  

        if self.status == "Issued":
            if book.stock > 0:
                book.stock -= 1
                book.save()
            else:
                frappe.throw("Book is out of stock!")

        elif self.status == "Returned":
            book.stock += 1
            book.save()

            if not member.outstanding_debt:
                member.outstanding_debt = 0

            member.outstanding_debt += self.fine
            member.save()

            if member.outstanding_debt > 500:
                frappe.throw("Member's outstanding debt exceeds Rs. 500. No more books can be issued!")

    def validate_dates(self):
        """Ensure issue date is today or later (only if status is not already Issued),
        due date is auto-set, and return date is valid"""
        
        today = datetime.today().date()
        issue_date = datetime.strptime(self.issue_date, "%Y-%m-%d").date()

        if self.status != "Issued" and issue_date < today:
            frappe.throw("Issue Date cannot be before today's date.")

        self.due_date = (issue_date + relativedelta(months=1)).strftime("%Y-%m-%d")

        if self.return_date:
            return_date = datetime.strptime(self.return_date, "%Y-%m-%d").date()
            if return_date < issue_date:
                frappe.throw("Return Date cannot be before the Issue Date.")
