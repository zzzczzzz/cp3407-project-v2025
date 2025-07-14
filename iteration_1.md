# Actual iteration-1 board, (see chapters 3 and 4), add your start and end dates 

Checklist: 
1. github entry timestamps
2. User stories are correct: see p39

* Assumed Velocity: 0.6 
* Number of developers: 1
* Total estimated amount of work: 8 days -> 9.5 days as new user story is added

User stories or tasks (see chapter 4):
1. [User Registration & Login](user_stories/iteration1_users_registration.md), priority 10, 2 days

2. [Booking cleaner](user_stories/iteration1_book_a_cleaner.md), priority 10, 3 days

3. [View Upcoming Job](user_stories/iteration1_view_upcoming_job.md), priority 10, 2 days

4. [View Booking history](user_stories/iteration1_view_booking_history.md), priority 30, 1 day

5. New User story [Cleaner Accepts Booking](user_stories/iteration1_cleaner_accept_booking.md), priority 10, 1.5 days
   
To Do: tasks described for each user stories in their own user stories.md, and in readme.md


In progress:
* user registration - desigining login ui and register ui (Yunseo), 16th June started  
* user registration - Create user table/model in database - creating user table and using python built in program to create database (Yunseo), 20th June started  
* user registration - Implement registration form with validation - create a line for registration form with validaition (Yunseo), 22th June started  
* user registration - Implement login form and session logic - create a line for login form with validaition (Yunseo), 22th June started  
* user registration - hashing the credentials - hash the credentials to store securely (Yunseo), 22th June started  
* Test registration and login flow - testing of what are implemented, 24th june started  
* booking cleaner - design booking page ui (yunseo), 26th june started  
* booking cleaner - implementing booking model in the database (yunseo), 26th june started
* booking cleaner - date, time picking in html form, save the booking in sql, validation and comfirmation message on display 6th july started
* booking history - loading booking history of logged in customer, 9th july started
* cleaner accepts booking - creating route to display pending bookings, query to load pendings, create route to accepct their desired pending bookings, only cleaners can access cleaner dashboard, change the statu once accepted, and update the cleaner name in view bookings history for customer. 11th july started
* view upcomming jobs - load upcomming jobs from database, display bookings with date time and location 13th july started
* for all iterations, style the html file following the prototype desgin, and create automated testing 14th july started

  
Completed :
* user registration - desigining login ui and register ui (Yunseo), 16th June completed
* user registration - Create user table/model in database - creating user table and using python built in program to create database (Yunseo), 20th June completed  
* user registration - Implement registration form with validation - create a line for registration form with validaition (Yunseo), 22th June completed  
* user registration - Implement login form and session logic - create a line for login form with validaition (Yunseo), 22th June completed
* user registration - hashing the credentials - hash the credentials to store securely (Yunseo), 22th June started
Completed
* Test registration and login flow - testing of what are implemented, 24th june completed
* booking cleaner - design booking page ui, added in the iteration of booking (yunseo), 26th june completed
* booking cleaner - implementing booking model in the database (yunseo), 26th june completed
* booking cleaner - date, time picking in html form, save the booking in sql, validation and comfirmation message on display 7th july completed
* booking history - loading booking history of logged in customer, 10th july completed
* cleaner accepts booking - creating route to display pending bookings, query to load pendings, create route to accepct their desired pending bookings, only cleaners can access cleaner dashboard, change the statu once accepted, and update the cleaner name in view bookings history for customer. 13th july completed
* view upcomming jobs - load upcomming jobs from database, display bookings with date time and location 14th july completed

## Additional Implementation Details (Iteration 1)

The following features were implemented to support the user stories:

- **Login as Home Page**  
  users are redirected to the login page, ensuring a secure entry point.

- **Redirection After Login**  
  After successful authentication, users are redirected to the dashboard where they can access features such as booking and   logout.

- **Logout Functionality**  
  logout route was implemented to allow users to securely end their session. This clears their session data and redirects     them to login.

- **Navigation Links**  
  Pages such as login and registration include links to each other to improve user navigation.

- **Session Validation**
  without proper session id, proceeding to any other features in the web app is blocked.


### Burn Down for iteration-1 (see chapter 4):
Update this at least once per week
* 4 weeks left, 8 days of estimated amount of work 
* 3 weeks left, 7 days of estimated amount of work
* 1 weeks left, 4 days of estimated amount of work, 1.5days of worked added newly total 5.5 days left
* 0 weeks left, xx days
* Actual Velocity: ?? 
