# your_app_name/api.py
import frappe
from frappe import _
from frappe.utils.response import build_response

@frappe.whitelist(allow_guest=True)
def get_specific(name1):
    our_user = frappe.get_list("Assignment", filters={'name': name1} ,fields=["name1","age","gender","designation","address","company_name"])
    response_data = {
        "specific_user": our_user,
    
    }

    return build_response("success", data=response_data)

def build_response(status, data=None, message=None):
    response = {
        "status": status
    }
    if data is not None:
        response["data"] = data

    if message is not None:
        response["message"] = message

    return response

