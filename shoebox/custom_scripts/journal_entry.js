frappe.ui.form.on("Journal Entry", {
	shoebox_document_no: function(frm) {
		frappe.call({
		        method: "frappe.client.get",
		        args: {
		            doctype: frm.doc.shoebox_doctype,
		            name: frm.doc.shoebox_document_no,
		        },
 		        callback(r) {
 		            if(r.message) {
					var trans = r.message;
					
						if(frm.doc.shoebox_doctype == "Payment Transaction"){
							frappe.run_serially([
								() => frm.set_value("naming_series", "CV-"),
								() => frm.set_value("voucher_type", "Cash Disbursement"),
								() => frm.set_value("posting_date", trans.date),
								() => frm.set_value("amount", trans.amount),
								() => frm.set_value("cheque_no", trans.invoice_no),
								() => frm.set_value("cheque_date", trans.date),
								() => frm.set_value("party_type", "Supplier"),
								() => frm.set_value("registered_name", trans.sold_to),
								() => frm.set_value("tin", trans.tin),
								() => frm.set_value("address_1", trans.address_1),
								() => frm.set_value("address_2", trans.address_2),
								() => done()
							]);
						}

						if(frm.doc.shoebox_doctype == "Receipt Transaction"){
							frappe.run_serially([
								() => frm.set_value("naming_series", "OR-"),
								() => frm.set_value("voucher_type", "Cash Receipt"),
								() => frm.set_value("posting_date", trans.date),
								() => frm.set_value("amount", trans.amount),
								() => frm.set_value("cheque_no", trans.invoice_no),
								() => frm.set_value("cheque_date", trans.date),
								() => frm.set_value("party_type", "Customer"),
								() => frm.set_value("registered_name", trans.sold_to),
								() => frm.set_value("tin", trans.tin),
								() => frm.set_value("address_1", trans.address_1),
								() => frm.set_value("address_2", trans.address_2),
								() => done()
							]);
						}
						
						if(frm.doc.shoebox_doctype == "Sales Transaction"){
							frappe.run_serially([
								() => frm.set_value("naming_series", "INV-"),
								() => frm.set_value("voucher_type", "Sales"),
								() => frm.set_value("posting_date", trans.date),
								() => frm.set_value("amount", trans.amount),
								() => frm.set_value("cheque_no", trans.invoice_no),
								() => frm.set_value("cheque_date", trans.date),
								() => frm.set_value("party_type", "Customer"),
								() => frm.set_value("registered_name", trans.sold_to),
								() => frm.set_value("tin", trans.tin),
								() => frm.set_value("address_1", trans.address_1),
								() => frm.set_value("address_2", trans.address_2),
								() => done()
							]);
						}
						
						if(frm.doc.shoebox_doctype == "Purchase Transaction"){
							frappe.run_serially([
								() => frm.set_value("naming_series", "APV-"),
								() => frm.set_value("voucher_type", "Purchase"),
								() => frm.set_value("posting_date", trans.date),
								() => frm.set_value("amount", trans.amount),
								() => frm.set_value("cheque_no", trans.invoice_no),
								() => frm.set_value("cheque_date", trans.date),
								() => frm.set_value("party_type", "Customer"),
								() => frm.set_value("registered_name", trans.sold_to),
								() => frm.set_value("tin", trans.tin),
								() => frm.set_value("address_1", trans.address_1),
								() => frm.set_value("address_2", trans.address_2),
								() => done()
							]);
						}

		            }
		        }


		});
	},

	shoebox_doctype: function(frm){
		frm.set_query("shoebox_document_no", function() {
			return {
				filters: {"docstatus": 0}
			};
		});
	}
});
