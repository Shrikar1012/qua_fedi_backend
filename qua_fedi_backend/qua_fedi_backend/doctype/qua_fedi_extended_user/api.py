import frappe

# @frappe.whitelist()
# def trigger_send_credentials(recipient_email,cc_email, password, sent_by, subject):
#     user = frappe.get_doc("User", recipient_email)
#     template = frappe.render_template('/templates/send_credentials_template.html', {
#         "first_name": user.first_name,
#         "last_name": user.last_name,
#         "email": recipient_email,
#         "password": password,         
#         "sent_by": sent_by
#     })
#     frappe.sendmail(
#         recipients=recipient_email,
#         cc=cc_email,
#         subject=subject,
#         message=template,
#         now=True,
#     )
#     return "Account credentials has been sent to your email."

@frappe.whitelist()
def trigger_send_credentials(user_email,password):
    user = frappe.get_doc("User",user_email)
    subject = "New Role : Qua Admin"
    message = f"Hi {user.first_name},<br><br>Please find below your Qua Admin credentials : <br><br>Email ID : {user_email} <br>Password : {password} <br><br>Regards,"
        
            
    # return (user_email,password)
    frappe.sendmail(
        recipients=user_email,
        subject=subject,
        message=message,
        sender='shrikarpatil1012@gmail.com',
        now=True
    )