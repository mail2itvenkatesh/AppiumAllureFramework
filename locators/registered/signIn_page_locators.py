class SignInPageLocators(object):
    sign_in_page_title = ('id', "com.hsp.clinicalX:id/title_text_view")
    sign_in_back_arrow_navigation = ('id', "com.hsp.clinicalX:id/back_imageview")
    not_registered_create_account_text = ('id', "com.hsp.clinicalX:id/create_account_text_view")
    username_label = ('id', "com.hsp.clinicalX:id/txt_username")
    username_input_field = ('id', "com.hsp.clinicalX:id/edt_uname")
    forgot_username_text_link = ('id', "com.hsp.clinicalX:id/txt_forusername")
    password_label = ('id', "com.hsp.clinicalX:id/txt_passwrd")
    password_input_field = ('id', "com.hsp.clinicalX:id/edt_pss")
    forgot_password_text_link = ('id', "com.hsp.clinicalX:id/txt_forgetpass")
    sign_in_button = ('id', "com.hsp.clinicalX:id/btn_singin_sign")
    cancel_button = ('id', "") # Have to add id and logic to validate

class SignInPageLocatorsStaticText(object):
    not_registered_create_account = "Not registered yet? Create an account."
    username_label_text = "Username"
    forgot_username_link_text = "Forgot your username?"
    password_label_text = "Password"
    forgot_password_link_text = "Forgot your password?"
    sign_in_button_text = "Sign In"
    cancel_button_text = "Cancel"
