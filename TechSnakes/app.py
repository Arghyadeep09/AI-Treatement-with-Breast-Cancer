from flask import Flask, render_template, request, jsonify, redirect, url_for, session, flash
import pickle
import numpy as np
from flask_sqlalchemy import SQLAlchemy
import bcrypt
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for session management

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)

# Define the User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

    def check_password(self, password):
        # Ensure both password and stored password are in the same format (bytes)
        if isinstance(self.password, str):
            stored_password = self.password.encode('utf-8')
        else:
            stored_password = self.password
        return bcrypt.checkpw(password.encode('utf-8'), stored_password)

# Create the database tables if they don't exist
with app.app_context():
    db.create_all()

@app.route('/user')
def user():
    return render_template('user.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        # Check if email already exists
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash('Email is already registered. Please use a different email.', 'error')
            return redirect(url_for('register'))

        # If email does not exist, create a new user
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        new_user = User(name=name, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash('Registration successful! Please log in.', 'success')
        return redirect('/user')
    
    return render_template('reuser.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email).first()

        if user and user.check_password(password):
            session['email'] = user.email
            return redirect(request.args.get('next') or '/')
        else:
            flash('Invalid email or password. Please try again.', 'error')
            return redirect(url_for('user'))

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('email', None)
    flash('You have been logged out.', 'info')
    return redirect('/')


# Load the trained model and scaler
with open('scaler.pkl', 'rb') as scaler_file:
    scaler = pickle.load(scaler_file)

with open('model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/recommandations')
def recommandations():
    if 'email' not in session:
        return redirect(url_for('user', next=request.url))
    return render_template('recommandations.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/predictor')
def predictor():
    if 'email' not in session:
        return redirect(url_for('user', next=request.url))
    return render_template('predictor.html')

@app.route('/howitworks')
def howitworks():
    return render_template('howitworks.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extracting form data
        area_worst = float(request.form['area_worst'])
        concave_points_worst = float(request.form['concave_points_worst'])
        concave_points_mean = float(request.form['concave_points_mean'])
        radius_worst = float(request.form['radius_worst'])
        perimeter_worst = float(request.form['perimeter_worst'])

        # Preparing the features for prediction
        features = np.array([[area_worst, concave_points_worst, concave_points_mean, radius_worst, perimeter_worst]])
        scaled_features = scaler.transform(features)

        # Making a prediction
        prediction = model.predict(scaled_features)
        prediction_proba = model.predict_proba(scaled_features)[0]

        # Prepare the response data
        response_data = {
            'prediction': 'Cancer' if prediction[0] == 1 else 'No Cancer',
            'benign_percentage': round(prediction_proba[0] * 100, 2),
            'malignant_percentage': round(prediction_proba[1] * 100, 2)
        }

        return jsonify(response_data)
    except Exception as e:
        return jsonify({'error': str(e)})
    
# Your email credentials
SENDER_EMAIL = 'tumortrust@gmail.com'
SENDER_PASSWORD = 'esbv hrxp kuti zhlm'

def send_email(recipient_email):
    try:
        # Create the email message
        message_body = """
        Dear valued subscriber,

        We are thrilled to welcome you to the TumorTrace community! By subscribing, you've taken a vital step toward staying informed about groundbreaking innovations in breast cancer research, personalized treatment options, and much more.

        Your trust means the world to us, and we are dedicated to providing you with the most relevant and insightful updates from the field of cancer care.

        Stay tuned for exciting developments, expert insights, and ways we can continue to support you. Together, we are making strides towards a healthier future.

        Warm regards,
        The TumorTrace Team
        """

        message = MIMEText(message_body)
        message['Subject'] = "Welcome to TumorTrace – Subscription Confirmation"
        # message = MIMEText("Thank you for subscribing to Tumor Trust!")
        # message['Subject'] = "Subscription Confirmation"
        message['From'] = SENDER_EMAIL
        message['To'] = recipient_email

        # Send the email
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, recipient_email, message.as_string())
        server.quit()

        return True
    except Exception as e:
        print(f"Failed to send email: {e}")
        return False

@app.route('/subscribe', methods=['POST'])
def subscribe():
    data = request.get_json()
    recipient_email = data.get('email')

    # Validate email input
    if not recipient_email:
        return jsonify({'error': 'Email is required'}), 400

    # Send email to the recipient
    if send_email(recipient_email):
        return jsonify({'success': True}), 200
    else:
        return jsonify({'error': 'Failed to send email'}), 500
if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Create database tables if they don't exist
    app.run(host='0.0.0.0',port=8080)
