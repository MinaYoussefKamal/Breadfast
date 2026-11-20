const checkoutForm = document.getElementById("checkout-form");
const checkoutMessage = document.getElementById("checkout-message");

if (checkoutForm && checkoutMessage) {
  checkoutForm.addEventListener("submit", async event => {
    event.preventDefault();

    // Keep a direct reference before the async request. event.currentTarget
    // becomes null after the event handler yields to await.
    const formElement = event.currentTarget;
    const cart = window.BreadFast?.cart;

    if (!cart || cart.size === 0) {
      checkoutMessage.textContent = "Add at least one item before placing your order.";
      checkoutMessage.className = "message error";
      return;
    }

    const formData = new FormData(formElement);
    const payload = {
      student_name: String(formData.get("student_name") || "").trim(),
      pickup_time: formData.get("pickup_time"),
      pickup_place: formData.get("pickup_place"),
      items: [...cart.entries()].map(([id, quantity]) => ({ id: Number(id), quantity: Number(quantity) }))
    };

    const submitButton = formElement.querySelector('button[type="submit"]');
    if (submitButton) submitButton.disabled = true;
    checkoutMessage.textContent = "Submitting your order...";
    checkoutMessage.className = "message";

    try {
      const response = await fetch("/api/orders", {
        method: "POST",
        headers: { "Content-Type": "application/json", "Accept": "application/json" },
        body: JSON.stringify(payload)
      });

      const result = await response.json().catch(() => null);
      if (!response.ok) {
        throw new Error(result?.error || `Order could not be placed (HTTP ${response.status}).`);
      }
      if (!result || !result.order_id) {
        throw new Error("The server response was incomplete. Check the server terminal.");
      }

      checkoutMessage.textContent = `Order #${result.order_id} placed successfully. Total: ${window.BreadFast.money(result.total)}`;
      checkoutMessage.className = "message success";
      cart.clear();
      window.BreadFast.renderCart();
      formElement.reset();
    } catch (error) {
      checkoutMessage.textContent = error instanceof TypeError
        ? "Could not contact the server. Make sure the Flask server is running and open the site at http://127.0.0.1:5000."
        : (error.message || "Could not place order. Please try again.");
      checkoutMessage.className = "message error";
      console.error("BreadFast checkout failed:", error);
    } finally {
      if (submitButton) submitButton.disabled = false;
    }
  });
}
