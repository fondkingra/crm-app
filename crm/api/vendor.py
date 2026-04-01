import frappe
import jwt

@frappe.whitelist(allow_guest=True)
def get_my_vendor_data():
    token = (
        frappe.get_request_header("X-Vendor-Token")
        or frappe.get_request_header("x-vendor-token")
    )

    if not token:
        frappe.throw("Missing vendor token")

    try:
        payload = jwt.decode(
            token,
            frappe.conf.jwt_secret or frappe.conf.secret_key,
            algorithms=["HS256"]
        )
    except jwt.ExpiredSignatureError:
        frappe.throw("Token expired")
    except jwt.InvalidTokenError:
        frappe.throw("Invalid token")

    if payload.get("role") != "Vendor":
        frappe.throw("Unauthorized")

    vendor_code = payload.get("vendor_code")
    if not vendor_code:
        frappe.throw("Invalid token payload")

    products = frappe.get_all(
        "Item",
        filters={"vendor": vendor_code},
        fields=["name", "item_name", "item_code", "price"]
    )

    purchase_orders = frappe.get_all(
        "Purchase Order",
        filters={"vendor": vendor_code},
        fields=["name", "transaction_date", "status", "grand_total"]
    )

    return {
        "products": products,
        "purchase_orders": purchase_orders
    }
