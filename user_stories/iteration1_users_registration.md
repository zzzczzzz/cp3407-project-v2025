# User Story Title: User Registration & Login

This story covers allowing customers to register and log in to the platform so they can manage their cleaning bookings.

---

## Priority: 10 (High)
This is a high-priority task required to enable access control and personalization. Without login, customers cannot book or manage services.

---

## Estimation: 2 days
- Yunseo: 2 days  

---

## Assumptions:
- Users will use email + password
- Password must be stored securely
- No social login required for now

---

## Description:
**Description 1**: As a customer, I want to register and log in so that I can manage my cleaning bookings.  
**Description 1**: The system must allow new users to sign up and existing users to log in to access the MyClean dashboard. Validation must be included.

---

## Tasks:

1. Design login and registration UI – 0.5 day  
2. Create user table/model in database – 0.5 day  
3. Implement registration form with validation – 0.5 day  
4. Implement login form and session logic – 0.5 day  
5. Secure password storage (hashing) – 0.25 day  
6. Test registration and login flow – 0.25 day  

---

## UI Design:
![Registration UI](ui/register.png)
![Login UI](ui/sign_in.png)




---

## Completed: task 1, task 2, taks 3, task 4, task 5, task 6
test completed, all message indicating the statue, register succeed, existing email, fill in all fileds are correctly displayed
the credentials are stored in database, was able to view it using sql database program, password is stored in hash
in login test, using the right credential redirects to dashboard page, when trying login using unexisting credential
refreshes the login page and displays meessage saying wrong credential
completed 24th june
