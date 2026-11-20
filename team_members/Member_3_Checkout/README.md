# Member 3 Checkout

Owns checkout form submission and order confirmation. Jira: SCRUM-12 (Select Pickup Time Slot and Place Order). Sends POST /api/orders; backend validation and saving are in app.py owned by Member 5.

## Your assigned files
- `static/js/checkout.js`

## Team rule
Do not edit another member’s owned files without coordinating first. Test your part in the complete BreadFast project before opening a pull request.


**Checkout fix:** The form element is saved before the asynchronous request, so the success handler can safely reset the form. The main project uses the same corrected checkout script.
