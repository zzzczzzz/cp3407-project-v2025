# User Story Title: Online Payment
Priority: 20 (Medium)
Estimation: 3 days
Yunseo: 3 days

# Description:
**As a customer, I want to pay securely online so that I can complete the booking process easily.**

# Tasks:
- Research and select a payment provider (e.g. Stripe, PayPal) – 0.5 day

- Integrate payment API in Flask backend – 1.0 day

- Add “Proceed to Payment” button on booking confirmation page – 0.25 day

- Create route /payment to handle payment process – 0.5 day

- Update booking status to “Paid” upon success – 0.25 day

- Flash success/failure messages accordingly – 0.25 day

- Add validation and security checks – 0.25 day


# Assupmtions:
- Customer must be logged in to access payment

- Payment is optional only for bookings not yet paid

- Backend securely handles transaction confirmation
