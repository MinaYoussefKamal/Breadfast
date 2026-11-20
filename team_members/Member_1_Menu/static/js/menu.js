window.BreadFast = window.BreadFast || {};
window.BreadFast.menuItems = [];
const money = value => `EGP ${Number(value).toFixed(2)}`;
function escapeHtml(value) {
  return String(value).replace(/[&<>"']/g, char => ({"&":"&amp;", "<":"&lt;", ">":"&gt;", '"':"&quot;", "'":"&#39;"}[char]));
}
async function loadMenu() {
  const response = await fetch("/api/menu");
  if (!response.ok) throw new Error("Menu request failed");
  window.BreadFast.menuItems = await response.json();
  const grid = document.getElementById("menu-grid");
  grid.innerHTML = window.BreadFast.menuItems.map(item => `
    <article class="food-card"><div class="food-art">${item.emoji}</div><div class="food-info">
    <div class="food-title"><h3>${escapeHtml(item.name)}</h3><strong>${money(item.price)}</strong></div>
    <p>${escapeHtml(item.description)}</p>
    ${item.available ? `<button class="button button-primary add-button" data-id="${item.id}">Add to cart</button>` : `<span class="unavailable">Currently unavailable</span>`}
    </div></article>`).join("");
  grid.querySelectorAll(".add-button").forEach(button => button.addEventListener("click", () => window.BreadFast.addToCart(Number(button.dataset.id))));
}
window.BreadFast.escapeHtml = escapeHtml;
window.BreadFast.money = money;
loadMenu().catch(() => { document.getElementById("menu-grid").textContent = "Could not load the menu. Please refresh."; });
