## User Story Title: Cleaner Accepts Job Bookings

### Priority 10 (high)

### Estimation: 1.5days
- Yunseo 1.5 days

### Description:
As a cleaner, I want to view pending bookings and accept a job, so that I can choose which cleaning tasks I will handle.

---

### Tasks:

1. Create a route `/cleaner/jobs` to display pending bookings – 0.25 day  
2. Add a query to fetch all bookings with status = "Pending" – 0.25 day  
3. Display booking details in a list or table with an “Accept” button – 0.25 day  
4. Create a route `/cleaner/accept/<booking_id>` to update status – 0.25 day  
5. Ensure only users with role `cleaner` can access these routes – 0.25 day  
6. Optional: Flash a success message after accepting – 0.1 day  
7. Optional: Refresh job list after accepting a booking – 0.15 day  

---

### Assumtions:
- Only cleaners can access the job list page  
- The list shows only pending bookings  
- Clicking "Accept" updates the status to "Accepted"  
- Booking is no longer listed once accepted  
- System flashes a message like "Booking accepted successfully"  
