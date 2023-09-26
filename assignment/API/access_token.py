import frappe
from frappe.utils.password import check_password
from assignment.utils import success_response, error_response

@frappe.whitelist(allow_guest=True)
def get_access_token(usr, pwd):
    try:
        # Check if the username and password are valid
        if not usr or not pwd:
            return error_response("Username and password are required.")
        
        # Verify the password
        if not check_password(usr, pwd):
            return error_response("Invalid username or password.")
        
        # Get the user's API key and API secret
        user = frappe.get_doc("User", usr)
        api_key = user.api_key
        api_secret = user.get_password('api_secret')
        
        if api_key and api_secret:
            api_token = "token " + api_key + ":" + api_secret
            access_api_token = {"access_token": api_token}
            return success_response(data=access_api_token)
        else:
            return error_response("API key or API secret not found for the user.")
    
    except Exception as e:
        frappe.logger('token').exception(e)
        return error_response(str(e))
