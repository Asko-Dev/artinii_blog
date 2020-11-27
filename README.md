<h2>Django Blog app with User Registration</h2>

- User Registration/ Login/ Logout/ Password reset
- User Profile created on registration
- User Profile Update (including pictures)
- User Create and Update/Delete a Blog post
- User Create a competition submission (Form submit)
- User Display "My Artinii" tab to see User posts and Competition submissions
- Blog with posts
    - See all posts from all users
    - Click on a User name to see all their posts
    - Click on a post for detail view (if owner -> Update/Delete)
    - Pagination on the posts embedded
- Competition Submission
    - List of submitted inquiries
    - Submit a form with a new inquiry
    - One submission per user
    - File submission (Motivational letter)
- About page, Landing page, Contact details
- Frontend done with bootstrapping

<h2>DEPLOYED TO HEROKU (Using AWS S3 Bucket for storage)</h2>

<b>ROOT URL: https://artiniiapp.herokuapp.com/

URL endpoints:</b>
- /
- /register/                                       
- /login/                                        
- /logout/                                           
- /password-reset/                                               
- /profile/   
- /about/    
- /submitted-movies/                                  
- /amateur_competition/                                     
- /amateur_competition/pk/                         
- /blog/   
- /post/new/                              
- /post/<int:pk>/  
- /post/<int:pk>/update
- /post/<int:pk>/delete
- /my-artinii/
