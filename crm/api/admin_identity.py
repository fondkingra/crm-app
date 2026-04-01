import frappe
from frappe.utils.password import get_decrypted_password

@frappe.whitelist(allow_guest=True)
def get_admin_identity(admin_name):
    admin = frappe.db.get_value(
        "admin",
        admin_name,
        [
            "admin_name",
            "admin_code",
            "contact_email",
            "contact_phone",
            "msp_id",
            "status",
            "custom_password"
        ],
        as_dict=True
    )

    if not admin:
        frappe.throw("Admin not found")

    if admin.status != "Active":
        frappe.throw("Admin is inactive")

    admin["certificate_pem"] = get_decrypted_password(
        "admin", admin_name, "certificate_pem"
    )
    admin["private_key"] = get_decrypted_password(
        "admin", admin_name, "private_key"
    )

    return admin
