// Copyright (c) 2025, Akshata Khadse and contributors
// For license information, please see license.txt

frappe.ui.form.on('Transaction', {
    onload: function(frm) {
        if (!frm.doc.issue_date) {
            frm.set_value('issue_date', frappe.datetime.get_today());
        }
    },
    issue_date: function(frm) { 
        if (frm.doc.issue_date) {
            let one_month_later = frappe.datetime.add_months(frm.doc.issue_date, 1);
            frm.set_value('due_date', one_month_later);
        }
    }
});
