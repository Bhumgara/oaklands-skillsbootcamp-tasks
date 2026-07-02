# Login Page Design
## Case
Create a Google login page

## Instructions
- Create two user stories
- Split into different tasks
- Create a data pipeline/data flow
- Make kanban board

## User Stories
### User Story 1
As a user, I want to be able to reset my password so that if I forget my password or lose access to my account I can reset the details used to login in order to regain access to my account.

### User Story 2
As a security expert, I want passwords to be hashed so that if hackers manage to access the database, they still may not login to accounts without the proper password.

## Task Breakdown
### User Story 1: Reset password
 - Create lost account hyperlink
 - Design email input field
 - Create 'submit password reset request' button
 - Write function to send email with new hyperlink to reset password
 - Connect inputs to the function
 - Connect reset password hyperlink to specific account using randomised access code
 - Design new password input field
 - Create 'submit password' button
 - Write function to accept new password and associate it with user

### User Story 2: Password Hashing
 - Design password input field on signup page
 - Create 'sign up' button
 - Write hashing function to hash password
 - Write function to accept new hashed password and associate it with user
 - Design password input field on login page
 - Create 'login' button
 - Write function to compare hashed password to stored hash
 - Write function to accept and approve login

## Data Pipelines
### General Login
 - User enters one of the options email or phone or username
 - User enteres the password
 - If matching according to the DB, then they go to account
 - If they fail to match an error message is printed

### User Story 1: Reset password
 - User can enter email to entry form
 - Backend releases reset link direct to the email
 - User checks email and opens link
 - From link they may enter a new password

### User Story 2: Password Hashing - Sign up
 - User enters password into login form
 - Backend accepts password entry
 - Hashing function acts on password
 - Hashed password is associated with the account in the DB

### User Story 2: Password Hashing - Login
 - User enters password into login form
 - Backend accepts password entry
 - Hashing function acts on password
 - Hashed password is checked against database
 - If the two hashes match, then the password is accepted
 - If the two hashes don't match, then the password is rejected
 - Signal is sent back to login page
 - User is either able to access account or presented with an error message

## Kanban Board (hypothetical)

+----------------------------------+  +----------------------------------+  +----------------------------------+
|  To Do                           |  |  In Progress                     |  |  Done                            |
+----------------------------------+  +----------------------------------+  +----------------------------------+
| Connect inputs to the function   |  | Write function to send email     |  | Create lost account hyperlink    |
+----------------------------------+  | with new hyperlink to reset      |  +----------------------------------+
| Connect reset password hyperlink |  | password                         |  | Design email input field         |
| to specific account using        |  +----------------------------------+  +----------------------------------+
| randomised access code           |  | Design new password input field  |  | Create 'submit password reset    |
+----------------------------------+  +----------------------------------+  | request' button                  |
| Create 'submit password' button  |  | Write hashing function to hash   |  +----------------------------------+
+----------------------------------+  | password                         |  | Design password input field on   |
| Write function to accept new     |  +----------------------------------+  | signup page                      |
| password and associate it with   |  | Write function to accept and     |  +----------------------------------+
| user                             |  | approve login                    |  | Create 'sign up' button          |
+----------------------------------+  +----------------------------------+  +----------------------------------+
| Write function to accept new     |                                        | Design password input field on   |
| hashed password and associate it |                                        | login page                       |
| with user                        |                                        +----------------------------------+
+----------------------------------+                                        | Create 'login' button            |
| Write function to compare hashed |                                        +----------------------------------+
| password to stored hash          |                                                                            
+----------------------------------+                                                                            