import frappe
from frappe.utils.password import get_decrypted_password

@frappe.whitelist(allow_guest=True)
def get_vendor_identity(vendor_name):

    vendor = frappe.db.get_value(
        "Vendor",
        vendor_name,
        [
            "vendor_name",
            "vendor_code",
            "msp_id",
            "status",
            "custom_password"
        ],
        as_dict=True
    )

    if not vendor:
        frappe.throw("Vendor not found")

    if vendor.status != "Active":
        frappe.throw("Vendor is inactive")

    vendor["certificate_pem"] = get_decrypted_password("vendor", vendor_name, "certificate_pem")
    vendor["private_key"] = get_decrypted_password("vendor", vendor_name, "private_key")

    return vendor
