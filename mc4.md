# Mini Challenge 4
## Password Reset Overrides
### Acceptance Criteria
1. Override the password reset form template.
1.1. The password reset form template should allow users to specify their email address.
2. Override the password reset done template.
2.1. The password reset done template should inform users of email reception with instructions on resetting password.
3. Override the password reset confirm template.
3.1. The password reset confirm template should allow users to set a new password.
4. Override the password reset complete template.
4.1. The password resert complete template should inform users that they've succeeded in resetting their password.
5. All templates should match the look and feel of your web application.
6. Test

##  Note
Password Reset View templates:
```
template_name = "registration/password_reset_form.html"
subject_template_name = "registration/password_reset_subject.txt"
email_template_name = "registration/password_reset_email.html"
```
Password Reset Done template:
```
template_name = "registration/password_reset_done.html"
```
Password Reset Confirm template:
```
template_name = "registration/password_reset_confirm.html"
```
Password Reset Complete template:
```
template_name = "registration/password_reset_complete.html"
```