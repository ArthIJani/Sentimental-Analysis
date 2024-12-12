# Sentiment Analysis Web App

A simple and modern sentiment analysis web app built with **Django** and styled using **Tailwind CSS**. Users can sign up, log in, and analyze text for sentiment. The app features a frosted glass effect for a sleek, modern interface.

---

## Features

- **User Authentication**: Sign up, log in, and log out functionality.
- **Sentiment Analysis**: Users can enter text (e.g., reviews, tweets) and get the sentiment analysis result (Positive, Negative, or Neutral).
- **History**: Users can view their sentiment analysis history.
- **Glass Effect**: The login and signup pages feature a stylish frosted glass effect using Tailwind CSS.
- **Responsive Design**: Optimized for both desktop and mobile devices.

---

## Technologies Used

- **Django**: Python web framework for building the backend.
- **Tailwind CSS**: Utility-first CSS framework for creating modern, responsive designs.
- **SQLite**: Default database used for storing user data and sentiment analysis history.
- **TextBlob**: A Python library used for sentiment analysis.

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/sentiment-analysis-web-app.git
cd sentiment-analysis-web-app
```
### 2. Set Up a Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
### 3. Install Dependencies

Install the required Python packages using pip:

```bash
pip install -r requirements.txt
```
### 4. Set Up the Database

Run Django migrations to set up the database:

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a Superuser (for Admin Access)

If you want to access the Django admin panel, create a superuser:

```bash
python manage.py createsuperuser
```

Follow the prompts to create your admin user.

### 6. Start the Development Server

Run the development server:

```bash
python manage.py runserver
```

Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser to access the application.

### Usage

1. **Sign Up**: Go to the `/accounts/signup/` page to create a new account.
2. **Login**: After signing up, log in with your credentials on the `/accounts/login/` page.
3. **Sentiment Analysis**: Once logged in, enter text into the provided form, and click “Analyze Sentiment” to receive the sentiment result.
4. **History**: View your previous sentiment analyses in the history section.

### Customization

You can customize the app by:
- Modifying the TextBlob sentiment analysis logic in the `analyze_sentiment` function.
- Updating the frontend templates in the `templates` directory.
- Adjusting the URL routes in the `urls.py` file.

### Contributing

1. Fork this repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Make your changes and commit (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Open a pull request.

### License

This project is licensed under the MIT License - see the `LICENSE` file for details.

### Acknowledgements

- Django: Web framework used for the backend.
- Tailwind CSS: Provides a modern, responsive design.
- TextBlob: Used for sentiment analysis.
- FontAwesome: For icons (if used in the project).

