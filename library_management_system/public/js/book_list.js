frappe.listview_settings['Book'] = {
    onload: function(listview) {
        listview.page.add_inner_button('Import Books', function() {
            let d = new frappe.ui.Dialog({
                title: 'Import Books',
                fields: [
                    {
                        label: 'Title',
                        fieldname: 'title',
                        fieldtype: 'Data'
                    },
                    {
                        label: 'Number of Books',
                        fieldname: 'num_books',
                        fieldtype: 'Int',
                        reqd: 1
                    }
                ],
                primary_action_label: 'Import',
                primary_action(values) {
                    frappe.call({
                        method: 'library_management_system.api.import_books.import_books',
                        args: values,
                        callback: function(response) {
                            frappe.msgprint(response.message);
                            d.hide();
                        }
                    });
                }
            });
            d.show();
        });
    }
};
