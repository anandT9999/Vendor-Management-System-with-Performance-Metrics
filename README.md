# Vendor-Management-System-with-Performance-Metrics
Develop a Vendor Management System using Django and Django REST Framework. This system will handle vendor profiles, track purchase orders, and calculate vendor performance metrics.

## Backend Logic for Performance Metrics

### On-Time Delivery Rate
- **What it does**: Figures out how often orders arrive on time.
- **How it works**: When an order is marked as done, we check if it arrived by its due date. Then we see how many orders did and didn't make it on time, and calculate the percentage of on-time ones.

### Quality Rating Average
- **What it does**: Finds out how well vendors are rated for their orders.
- **How it works**: After each order is done, we add up all the ratings given to the vendor. Then we divide that total by the number of orders to get an average rating.

### Average Response Time
- **What it does**: Shows how quickly vendors respond to orders.
- **How it works**: When a vendor gets an order, we measure the time it takes them to say they got it. We do this for all orders, then find the average time it takes across all of them.

### Fulfilment Rate
- **What it does**: Tells us how often orders are completed without problems.
- **How it works**: Whenever an order changes status, we check if it was completed without any issues. Then we calculate the percentage of these problem-free orders out of all the orders sent to the vendor.

## API Endpoint Implementation

### Vendor Performance Endpoint (GET /api/vendors/{vendor_id}/performance)
- **Purpose**: Gets the performance numbers for a specific vendor.
- **Data Returned**: Includes how often they deliver on time, their average rating, how quickly they respond, and their success rate.

### Update Acknowledgment Endpoint
- **Purpose**: Lets vendors acknowledge they received an order.
- **Endpoint**: POST /api/purchase_orders/{po_id}/acknowledge
- **How it works**: When a vendor acknowledges they got an order, we update the system. This also helps in calculating how fast vendors usually respond.
