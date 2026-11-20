const ordersList = document.getElementById("orders-list");

function escapeHtml(value) {
  return String(value).replace(/[&<>"']/g, char => ({
    "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;"
  }[char]));
}

async function loadOrders() {
  const response = await fetch("/api/orders");
  const orders = await response.json();
  if (!orders.length) {
    ordersList.innerHTML = '<div class="empty-state">No orders yet. New student orders will appear here.</div>';
    return;
  }
  ordersList.innerHTML = orders.map(order => `
    <article class="order-card">
      <div class="order-top">
        <div><span class="order-number">ORDER #${order.id}</span><h3>${escapeHtml(order.student_name)}</h3></div>
        <span class="status status-${order.status.toLowerCase()}">${escapeHtml(order.status)}</span>
      </div>
      <ul>${order.items.map(item =>
        `<li>${escapeHtml(item.item_name)} × ${item.quantity} <span>${(item.unit_price * item.quantity).toFixed(2)} EGP</span></li>`
      ).join("")}</ul>
      <div class="order-details">
        <span>Pickup: ${escapeHtml(order.pickup_time)}</span>
        <span>Place: ${escapeHtml(order.pickup_place)}</span>
        <strong>Total: ${Number(order.total).toFixed(2)} EGP</strong>
      </div>
      <div class="order-actions">
        <label for="status-${order.id}">Update status</label>
        <select id="status-${order.id}" data-order-id="${order.id}">
          ${["Preparing", "Ready", "Completed"].map(status =>
            `<option value="${status}" ${order.status === status ? "selected" : ""}>${status}</option>`
          ).join("")}
        </select>
        <button class="button button-primary update-status" data-id="${order.id}">Save</button>
      </div>
    </article>`).join("");

  ordersList.querySelectorAll(".update-status").forEach(button => {
    button.addEventListener("click", async () => {
      const id = button.dataset.id;
      const status = document.getElementById(`status-${id}`).value;
      const result = await fetch(`/api/orders/${id}/status`, {
        method: "PATCH",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({status})
      });
      if (result.ok) loadOrders();
      else alert("Could not update this order.");
    });
  });
}

document.getElementById("refresh-orders").addEventListener("click", loadOrders);
loadOrders();
