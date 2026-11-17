# Cafeteria Pre-Order App - User Stories Backlog

## Epic 1: Menu & Availability
### US1: View Menu and Item Availability
- **As a** student,
- **I want** to browse the daily cafeteria menu with real-time availability status,
- **So that** I can see which items are available and avoid ordering sold-out items.
- **Acceptance Criteria:** Menu lists items categorized by type; sold-out items are grayed out.
- **MVP:** Yes | **Points:** 3

### US2: Manage Daily Menu Items (Manager)
- **As a** cafeteria manager,
- **I want** to add, edit, or remove food items and prices so the catalog is accurate,
- **So that** menu details stay up-to-date.
- **Acceptance Criteria:** Manager can update item names, descriptions, and prices in EGP.
- **MVP:** Yes | **Points:** 3

### US3: Hide Sold-Out Items Automatically
- **As a** kitchen staff member,
- **I want** to mark an item as out-of-stock when supplies run out,
- **So that** students cannot select unavailable items in their cart.
- **Acceptance Criteria:** Toggling availability instantly removes it from the active student menu view.
- **MVP:** Yes | **Points:** 2

### US4 (Stretch): Highlight Daily Specials
- **As a** student,
- **I want** to view daily specials highlighted on the menu,
- **So that** I can easily spot today's featured meals.
- **Acceptance Criteria:** Specials appear with a special badge at the top of the menu list.
- **MVP:** No (Stretch) | **Points:** 2

---

## Epic 2: Cart & Checkout
### US5: Add Items to Cart
- **As a** student,
- **I want** to add multiple food items and quantities to my shopping cart,
- **So that** I can review my complete meal before placing an order.
- **Acceptance Criteria:** Cart displays itemized list, total price in EGP, and allows quantity changes.
- **MVP:** Yes | **Points:** 3

### US6: Select Pickup Time Slot and Place Order
- **As a** student,
- **I want** to choose an available pickup time slot (e.g., 10:40 AM) at checkout,
- **So that** my food is freshly prepared right when my lecture ends.
- **Acceptance Criteria:** System enforces slot capacity limits; payment defaults to cash on pickup[cite: 5].
- **MVP:** Yes | **Points:** 5

### US7: Validate Slot Capacity Limits (Key Rule)
- **As a** system,
- **I want** to reject order attempts for a specific time slot once it hits maximum capacity ($N$ orders)[cite: 5],
- **So that** the kitchen staff is never overwhelmed.
- **Acceptance Criteria:** If capacity is full, the slot is disabled and user is prompted to choose another.
- **MVP:** Yes | **Points:** 5

### US8 (Stretch): Apply Loyalty Points Discount
- **As a** student,
- **I want** to apply loyalty points for a discount at checkout,
- **So that** I save money based on my past purchases.
- **Acceptance Criteria:** Loyalty points balance deducts correctly from the total EGP amount.
- **MVP:** No (Stretch) | **Points:** 5

---

## Epic 3: Kitchen Workflow Board
### US9: View Incoming Orders Queue
- **As a** kitchen staff member,
- **I want** to view a live board of incoming orders categorized by pickup times,
- **So that** I know what food needs to be prepared first.
- **Acceptance Criteria:** Orders show student name, items, quantities, and target pickup time slot.
- **MVP:** Yes | **Points:** 3

### US10: Update Order Status Progression
- **As a** kitchen staff member,
- **I want** to move orders through the Kanban lifecycle (`ordered` $\rightarrow$ `preparing` $\rightarrow$ `ready`)[cite: 5],
- **So that** progress is tracked accurately.
- **Acceptance Criteria:** Status updates reflect instantly on the system board.
- **MVP:** Yes | **Points:** 3

### US11: Mark Order as Collected
- **As a** kitchen staff member,
- **I want** to mark an order as `collected` once the student picks it up,
- **So that** completed orders leave the active kitchen workflow queue.
- **Acceptance Criteria:** Order moves to historical records and drops off the active preparation board.
- **MVP:** Yes | **Points:** 2

### US12 (Stretch): View Busy-Slot Statistics
- **As a** manager,
- **I want** to view busy-slot statistics and peak hours,
- **So that** I can plan kitchen staffing more effectively.
- **Acceptance Criteria:** Dashboard displays a chart showing order volume per time slot.
- **MVP:** No (Stretch) | **Points:** 5

---

## Epic 4: Student Order Status & History
### US13: Track Live Order Status
- **As a** student,
- **I want** to view a dedicated order-status page showing my current order state[cite: 5],
- **So that** I know when to walk down to the cafeteria.
- **Acceptance Criteria:** Page displays real-time status updates (`Ordered`, `Preparing`, `Ready`).
- **MVP:** Yes | **Points:** 3

### US14: View Order History
- **As a** student,
- **I want** to view a list of my past orders and pickup times,
- **So that** I can easily re-order my favorite meals.
- **Acceptance Criteria:** History page archives completed and collected orders.
- **MVP:** Yes | **Points:** 2

### US15: Cancel Pending Order
- **As a** student,
- **I want** to cancel my order before the kitchen starts preparing it,
- **So that** I am not charged or wasting food if my schedule changes.
- **Acceptance Criteria:** Cancellation is only allowed while status is `ordered`.
- **MVP:** Yes | **Points:** 3

### US16 (Stretch): Order Status Notifications
- **As a** student,
- **I want** to receive push/email reminders when my order status changes to ready,
- **So that** I don't forget to pick it up.
- **Acceptance Criteria:** System triggers an alert notification upon status change to ready.
- **MVP:** No (Stretch) | **Points:** 3
