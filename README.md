# Streamify – OTT Platform Clone
Streamify is a full-stack web application that replicates the core features of an OTT (Over-The-Top) streaming platform. It is built using Django for backend development and Bootstrap for frontend styling.

### Tech Stack
- Backend: Django Framework
  Handles:
    - User authentication (Signup / Login)
    - Database operations (storing user info, movies, series)
    - Routing HTML pages based on user requests
    - Displaying the right content dynamically
    - Integration with the frontend

- Frontend: Bootstrap
    - Used for designing clean, responsive, and interactive web pages.

#### Key Features
Below are the main features available on Streamify:
- Start Page
    First page the user sees, whether logged in or not. It displays a preview of all available content along with Sign Up and Log In buttons at the top right.
- Sign Up
    New users can register by providing basic details and a password. After successful registration, users are redirected to the login page.
- Log In
    Registered users can log in with their credentials. On successful login, users are redirected to the home page.
- Home Page (Visible only after login)
    Shows various sections like:
      - Most Watched Movies
      - Most Watched Series
      - New Releases
    Navigation bar includes links to Dashboard, Profile, Genre, My List, Movies, Series, Search, and Popular content.
- Profile Page
    Users can view and update the details they provided during sign-up.
- Genre Page
    Shows a list of movies/series filtered by genre: Romance, Comedy, Action, Horror, Thriller, etc.
- My List
    A personalized space for users to add movies/series they want to watch later.
- Movies Page
    Shows only movies (filtered by genre).
- Series Page
    Similar to the movies page but displays only TV series.
