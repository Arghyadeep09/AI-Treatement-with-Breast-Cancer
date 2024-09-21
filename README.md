
</head>
<body>
    <div class="container">
        <h1>🩺 Breast Cancer Prediction System</h1>
        <img src="https://i.ibb.co/HXRZfyM/Screenshot-2024-09-21-153131.png" alt="Breast Cancer Detection">
        <h2>Overview</h2>
        <p class="animated">Welcome to the <b>Breast Cancer Prediction System</b>, a comprehensive web application that predicts whether a tumor is <b>Malignant</b> or <b>Benign</b> based on user input. This system uses advanced machine learning algorithms and presents results interactively through visual representations like <b>Pie Charts</b> and a user-friendly interface.</p>
        <h3>Malignant vs. Benign Prediction (%)</h3>
        <img src="https://i.ibb.co/XSxpdbF/Screenshot-2024-09-21-153659.png" alt="Malignant vs Benign Pie Chart" />
          <!-- Chatbot section -->
        <h2>🤖 MammoMate - AI Chatbot</h2>
        <p class="animated">Introducing <b>MammoMate</b>, your AI-powered assistant to answer all breast cancer-related questions. MammoMate is designed to provide you with helpful information, clarify doubts, and offer guidance through personalized interactions.</p>
        <img src="https://i.ibb.co/sqWDFtM/Screenshot-2024-09-21-160537.png" height=450 alt="MammoMate Chatbot">
      <!-- YouTube video section -->
        <h2>📽️ How Does This Work?</h2>
        <p class="animated">Watch the video below to see how this breast cancer prediction system works.</p>
          Video Link:(https://youtu.be/EyUxRbKOjsU)
        <h2>✨ Key Features</h2>
        <ul>
            <li>Frontend: Home Page, About Page, Predictor Page, Registration Page, Login Page, Recommendation Page, Subscription for Newsletters (via Email)</li>
            <li>Backend: Flask for seamless web service operations, integration of machine learning models for real-time prediction</li>
            <li>Chatbot: <b>MammoMate</b>, the AI-powered chatbot for breast cancer-related queries</li>
        </ul>
        <h2>🖼️ Page Previews</h2>
        <table>
            <tr>
                <th>Home Page</th>
                <th>About Page</th>
                <th>Predictor Page</th>
                <th>Recommandains</th> 
                <th>Log In interface</th>
            </tr>
            <tr>
                <td><img src="https://i.ibb.co/Qn36v7P/Screenshot-2024-09-21-153953.png" alt="Home Page"></td>
                <td><img src="https://i.ibb.co/SKR01Zk/Screenshot-2024-09-21-154705.png" alt="About Page"></td>
                <td><img src="https://i.ibb.co/rypKnZk/Screenshot-358.png" alt="Screenshot-358" alt="Predictor Page"></td>
                <td><img src="https://i.ibb.co/b2NNNhm/Screenshot-2024-09-21-155036.png" alt="Recommandains"></td>
               <td><img src="https://i.ibb.co/MSRY3ps/Screenshot-2024-09-21-154215.png" alt="user"></td>
            </tr>
        </table>
        <h2>💻 Frontend Tech Stack</h2>
        <ul>
            <li>HTML5/CSS3/JavaScript</li>
            <li>Bootstrap for responsiveness</li>
            <li>GSAP & Locomotive Scroll for smooth animations</li>
            <li>Chart.js for visualizing prediction results</li>
        </ul>
        <p>Each page of the website offers a clean, stylish, and responsive design:</p>
        <ul>
            <li><b>Home Page:</b> The homepage introduces the application with seamless animations and navigations.</li>
            <li><b>About Page:</b> Information about breast cancer and its early detection methods.</li>
            <li><b>Predictor Page:</b> An interactive user input form for prediction with live result visualization.</li>
            <li><b>MammoMate:</b> The chatbot provides interactive AI-based responses to breast cancer-related queries.</li>
            <li><b>Registration/Login:</b> Users can register and log in for personalized experience.</li>
            <li><b>Subscription Section:</b> Users who subscribe receive periodic newsletters via email about the latest in breast cancer research and treatment.</li>
        </ul>
        <h2>🔥 Backend Tech Stack</h2>
        <ul>
            <li>Flask Framework for backend logic</li>
            <li>Jinja Templating Engine for rendering dynamic content</li>
            <li>Machine Learning Algorithms for real-time prediction</li>
            <li>REST API for handling prediction requests</li>
        </ul>
        <h3>Backend Flow:</h3>
        <ul>
            <li>Flask receives user input from the predictor page.</li>
            <li>The machine learning model processes the input and calculates a prediction score.</li>
            <li>The result is dynamically rendered as 'Cancer' or 'No Cancer' along with a percentage-based pie chart showing Malignant vs Benign predictions.</li>
        </ul>
        <h2>📊 Data Science & Machine Learning</h2>
        <ul>
            <li>Python3 for backend data handling</li>
            <li>Pandas & NumPy for data manipulation</li>
            <li>scikit-learn & TensorFlow for machine learning model creation</li>
            <li>Matplotlib for backend visualizations</li>
        </ul>
        <p>The model was trained on historical breast cancer datasets to predict malignant or benign outcomes based on medical parameters such as Area Worst, Concave Points Worst, Radius Worst, and more. Predictions are served via Flask, and the result is displayed in a pie chart showing the percentage distribution of Malignant vs Benign predictions.</p>
        <h2>🛠️ Tech Stack Summary</h2>
        <table>
            <tr>
                <th>Frontend</th>
                <th>Backend</th>
                <th>Data Science</th>
            </tr>
            <tr>
                <td>HTML5, CSS3, JS, Bootstrap</td>
                <td>Flask, Python</td>
                <td>Pandas, NumPy</td>
            </tr>
            <tr>
                <td>GSAP, Locomotive Scroll</td>
                <td>Jinja Templating</td>
                <td>scikit-learn, TensorFlow</td>
            </tr>
            <tr>
                <td>Chart.js for Data Viz</td>
                <td>REST API, Flask-Mail</td>
                <td>Keras</td>
            </tr>
        </table>
        <h2>📬 Email Subscription System</h2>
        <p>If users subscribe by entering their email address on the homepage:</p>
        <ul>
            <li>They will receive a confirmation email.</li>
            <li>Periodic newsletters will be sent regarding updates in breast cancer research and treatment options.</li>
            <img src="https://i.ibb.co/0JHKbkj/Screenshot-2024-09-21-162044.png" alt="Email Subscription">
        </ul>
        <h2>🚀 How to Run the Project</h2>
        <ol>
            <li>Clone the repository:
                <pre><code>git clone https://github.com/your-repo-name.git</code></pre>
            </li>
            <li>Set up the environment and install dependencies:
                <pre><code>pip install -r requirements.txt</code></pre>
            </li>
            <li>Run the Flask application:
                <pre><code>python app.py</code></pre>
            </li>
            <li>Access the application at:
                <pre><code>
Mobile: http://107.22.25.169:8080/
Desktop : http://ec2-107-22-25-169.compute-1.amazonaws.com:8080/
</code></pre>
            </li>
          <li>Deploy on AWS Cloud (EC2 Instance):
    <pre><code>
    1. Launch an EC2 instance:
       - Choose ubuntu 22.02 LTS AMI (HVM), SSD Volume Type.
       - Select an instance type (t2.micro for free tier).
       - Configure security group to allow HTTP (port 80) and SSH (port 22).
    2. Connect to your EC2 instance using SSH:
       ssh -i your-key.pem ec2-user@<your-ec2-public-ip>
    3. Install necessary packages:
       sudo yum update -y
       sudo yum install python3-pip git -y
    4. Clone your project repository:
       git clone <your-repo-url>
       cd <your-project-directory>
    5. Install required Python libraries:
       pip3 install -r requirements.txt
    6. Run the Flask application:
       python3 app.py
    7. Configure EC2 security group to allow traffic on port 5000 (if running Flask on default port).
    8. Access your application via:
       http://<your-ec2-public-ip>:5000
    </code></pre>
        </ol>
        <h2>🧑‍💻 Contributing</h2>
        <p>We welcome contributions from the community. If you'd like to improve or add new features, feel free to fork the repo and submit a pull request.</p>
        <h2>📜 License</h2>
        <p>This project is licensed under the MIT License - see the LICENSE file for details.</p>
    </div>
    <div class="footer">
        © 2024 Breast Cancer Prediction System
    </div>
</body>
</html>
