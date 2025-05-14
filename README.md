# Airbnb Reservations

A Django-based web application for a travel booking platform, allowing users to explore, book, and review properties (hotels, restaurants, and places), manage profiles, and engage with blog content. The platform provides a user-friendly interface for travelers to discover destinations, make reservations, and share feedback, with features like property filtering, user authentication, and a blog section for tips and articles.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features

This project includes the following features:

- **User Authentication**:
  - Sign up, log in, and log out functionality.
  - Password reset and change options.
  - User profile management with image upload, phone number, and address.

- **Property Management**:
  - Browse properties (hotels, restaurants, places) with filtering by name, description, category, and place.
  - Detailed property views with images, descriptions, availability checks, and average ratings.
  - Book properties with a form for selecting dates, guests, and children.
  - Users can view their reservations and listings.
  - Property review system for users to rate and provide feedback.

- **Blog Section**:
  - View blog posts with categories, tags, and search functionality.
  - Detailed post views with Disqus comments integration.
  - Filter posts by category or tag.

- **About Page**:
  - Displays information about the platform's mission, goals, and activities.
  - FAQ section with collapsible answers.

- **Search and Filtering**:
  - Home page search by property name and place.
  - Category and place-based filtering for properties.
  - Blog search by title or description.

- **Responsive Design**:
  - Built with Bootstrap 4 for a mobile-friendly interface.
  - Includes Owl Carousel for image sliders and AOS for animations.

- **Admin Panel**:
  - Django admin interface for managing properties, users, blog posts, and settings.
  - Integration with Django Summernote for rich text editing.

- **Footer and Settings**:
  - Dynamic footer with site name, description, social media links, and contact information.
  - Configurable settings via the `Settings` model.

## Technologies Used

- **Backend**:
  - Django 5.2
  - Python 3.12
  - SQLite (default database, can be configured for others)

- **Frontend**:
  - Bootstrap 4
  - jQuery
  - Owl Carousel
  - AOS (Animate on Scroll)
  - Font Awesome and Ionicons

- **Additional Libraries**:
  - `django-taggit` for tagging blog posts
  - `django-summernote` for rich text editing
  - `django-filters` for property filtering
  - Disqus for blog comments

- **Static and Media**:
  - Static files for CSS, JavaScript, and images
  - Media files for user-uploaded content (profile images, property images, etc.)

## Installation

Follow these steps to set up the project locally:

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Virtualenv (recommended)
- Git

### Steps
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Mohammed-Aljazzar/Airbnb-Reservations.git
   cd Airbnb-Reservations
   ```
   
2. Create a Virtual Environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
   
4. Install Dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   Note: If requirements.txt is not provided, install the following packages:
    ```bash
   pip install django django-taggit django-summernote django-filters bootstrap4
   ```
  
6. Apply Migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

8. Create a Superuser (for admin access):
   ```bash
   python manage.py createsuperuser
   ```

10. Collect Static Files:
    ```bash
    python manage.py collectstatic
    ```
    
12. Run the Development Server:
    ```bash
    python manage.py runserver
    ```

## Usage

- **Home Page:** Explore featured destinations, search for properties, and browse categories.
- **Property Listing:** Filter properties by name, description, category, or place. Click on a property to view details and book.
- **User Profile:** Sign up or log in to manage your profile, view reservations, and list your properties.
- **Blog:** Read articles, filter by category or tag, and leave comments using Disqus.
- **About Page:** Learn about the platform and view FAQs.
- **Admin Panel:** Manage users, properties, blog posts, and site settings.
   
## Configuration
### Environment Variables

Update project/settings.py for production:
- Set DEBUG = False.
- Configure ALLOWED_HOSTS.
- Replace SECRET_KEY with a secure value.
- Configure a production database (e.g., PostgreSQL).

### Media Files
Ensure the MEDIA_ROOT directory exists and is writable:
  ``` bash
  MEDIA_URL = '/media/'
  MEDIA_ROOT = BASE_DIR / 'media'
  ```

### Disqus Integration
For blog comments, configure Disqus in post_detail.html:
- Update disqus_config with your Disqus shortname and site URL.
  
### Static Files
For production, use a storage backend like WhiteNoise or a CDN:
  ```bash
  # In settings.py
  STATIC_ROOT = os.path.join(BASE_DIR, 'static', 'staticroot')
  STATICFILES_DIRS = [BASE_DIR / "static"]
  ```

## Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch (git checkout -b feature/your-feature).
3. Make your changes and commit (git commit -m "Add your feature").
4. Push to the branch (git push origin feature/your-feature).
5. Open a Pull Request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contact
For questions or feedback, please contact:
- Author: Mohammed Aljazzar
- Email: m.i.aljazzar19@gmail.com
