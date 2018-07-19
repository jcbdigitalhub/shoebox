frappe.ui.form.on("Payment Entry", {
	shoebox_reference: function(frm) {
		frappe.call({
		        method: "frappe.client.get",
		        args: {
		            doctype: frm.doc.shoebox_ref_type,
		            name: frm.doc.shoebox_reference,
		        },
 		       callback(r) {
 		           if(r.message) {
 		               var trans = r.message;
				if(frm.doc.shoebox_ref_type == "Payment Transaction"){
				frappe.run_serially([
		               		() => frm.set_value("naming_series", "PE-"),
	                                () => frm.set_value("payment_type", "Pay"),
					() => frappe.timeout(1),
                                        () => frm.set_value("posting_date", trans.date),
                                        () => frm.set_value("party_type", "Supplier"),
                                        () => frm.set_value("party", trans.sold_to),
					() => frappe.timeout(1),
					() => frm.set_value("paid_from", trans.bank_gl_account),
                                        () => frappe.timeout(1),
                                        () => frm.set_value("paid_amount", trans.amount),
                                        () => frm.set_value("reference_no", trans.invoice_no),
					() => frm.set_value("reference_date", trans.date),
					() => done()
				]);
				}

                                if(frm.doc.shoebox_ref_type == "Receipt Transaction"){
                                frappe.run_serially([
                                        () => frm.set_value("naming_series", "OR-"),
                                        () => frm.set_value("payment_type", "Receive"),
                                        () => frappe.timeout(1),
                                        () => frm.set_value("posting_date", trans.date),
                                        () => frm.set_value("party_type", "Customer"),
                                        () => frm.set_value("party", trans.sold_to),
                                        () => frappe.timeout(1),
                                        () => frm.set_value("paid_to", trans.bank_gl_account),
                                        () => frappe.timeout(1),
                                        () => frm.set_value("paid_amount", trans.amount),
                                        () => frm.set_value("reference_no", trans.invoice_no),
                                        () => frm.set_value("reference_date", trans.date),
                                        () => done()
                                ]);
                                }

		            }
		        }
		});
	}


});
