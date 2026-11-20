window.BreadFast = window.BreadFast || {};
window.BreadFast.cart = new Map();
window.BreadFast.addToCart = function(id) {
  const cart = window.BreadFast.cart; cart.set(id, (cart.get(id) || 0) + 1); window.BreadFast.renderCart();
};
window.BreadFast.renderCart = function() {
  const items = window.BreadFast.menuItems, cart = window.BreadFast.cart;
  const container = document.getElementById("cart-items");
  const entries = [...cart.entries()];
  if (!entries.length) container.innerHTML = '<p class="muted">Your cart is empty.</p>';
  else container.innerHTML = entries.map(([id, quantity]) => {
    const item = items.find(entry => entry.id === id);
    return `<div class="cart-line"><div><strong>${window.BreadFast.escapeHtml(item.name)}</strong><small>${window.BreadFast.money(item.price)} each</small></div>
    <div class="quantity-control"><button type="button" data-action="minus" data-id="${id}" aria-label="Remove one">−</button><span>${quantity}</span><button type="button" data-action="plus" data-id="${id}" aria-label="Add one">+</button></div></div>`;
  }).join("");
  const total = entries.reduce((sum, [id, qty]) => sum + items.find(item => item.id === id).price * qty, 0);
  document.getElementById("cart-total").textContent = window.BreadFast.money(total);
  container.querySelectorAll("button[data-action]").forEach(button => button.addEventListener("click", () => {
    const id = Number(button.dataset.id), next = (cart.get(id) || 0) + (button.dataset.action === "plus" ? 1 : -1);
    if (next <= 0) cart.delete(id); else cart.set(id, next); window.BreadFast.renderCart();
  }));
};
