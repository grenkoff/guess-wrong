# Project `guess-wrong`

A web application designed to help users learn foreign words through a fun and engaging quiz game. The game identifies the words users are unfamiliar with and helps them improve their vocabulary over time.

## Features

- **Interactive Quiz Game**: Test your knowledge of foreign words and track your progress.
- **Personalized Learning**: The system identifies and highlights words the user does not know.
- **User-friendly Interface**: Powered by Bootstrap for a modern and responsive design.
- **RESTful API**: Built with Django Rest Framework (DRF) for seamless integration and scalability.

## Technologies Used

- **Backend**: Python, Django, Django Rest Framework (DRF)
- **Frontend**: Bootstrap
- **Database**: PostgreSQL
- **Deployment**: Railway.app

## Installation

### Prerequisites

- Python 3.10 or later
- PostgreSQL
- Railway account (optional, for deployment)

### Steps

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/grenkoff/guess-wrong.git
   cd guess-wrong
   ```

2. **Set Up Virtual Environment**:

   ```bash
   python -m venv .venv
   source .venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**:
   Create a `.env` file in the project root with the following variables:

   ```env
   SECRET_KEY=your_secret_key
   DEBUG=True
   DATABASE_URL=postgres://user:password@localhost:5432/yourdatabase
   ```

5. **Apply Migrations**:

   ```bash
   python manage.py migrate
   ```

6. **Run the Server**:

   ```bash
   python manage.py runserver
   ```

   The application will be available at `http://127.0.0.1:8000`.

## Deployment

### Railway.app Deployment

1. **Sign Up/Log In**:
   Create an account or log in to [Railway.app](https://railway.app).

2. **Create a New Project**:

   - Link your GitHub repository.
   - Add environment variables in the Railway dashboard (e.g., `SECRET_KEY`, `DATABASE_URL`).

3. **Deploy**:
   Railway will automatically build and deploy your project.

## Usage

- Visit the homepage to start the quiz.
- Answer the questions to test your vocabulary.
- View your progress and focus on improving the words you struggle with.

## Contributing

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-name
   ```
3. Make your changes and commit them:
   ```bash
   git commit -m "Add feature-name"
   ```
4. Push the changes:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Django](https://www.djangoproject.com/)
- [Bootstrap](https://getbootstrap.com/)
- [Railway](https://railway.app/)
- [PostgreSQL](https://www.postgresql.org/)
