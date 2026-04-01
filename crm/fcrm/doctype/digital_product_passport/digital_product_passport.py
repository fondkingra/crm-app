# Copyright (c) 2026, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class DigitalProductPassport(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		block_number: DF.Data | None
		blockchain_hash: DF.Data | None
		blockchain_network: DF.Data | None
		dpp_id: DF.Data | None
		dpp_status: DF.Literal["Active", "Inactive", "Revoked", "Expired"]
		lifecycle_state: DF.Literal["Draft", "Created", "Commissioned", "Shipped", "Cancelled"]
		product: DF.Link | None
		purchase_order: DF.Link | None
		transaction_id: DF.Data | None
		vendor: DF.Link | None
	# end: auto-generated types
	pass
