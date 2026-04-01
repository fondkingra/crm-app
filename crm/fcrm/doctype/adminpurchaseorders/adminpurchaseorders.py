# Copyright (c) 2026, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Adminpurchaseorders(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		expected_arrival: DF.Date | None
		materialscomponents: DF.Link
		order_date: DF.Date | None
		order_id: DF.Data | None
		supplier: DF.Link | None
	# end: auto-generated types
	pass
