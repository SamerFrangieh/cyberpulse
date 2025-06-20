from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from scanner.nmap_scan import run_nmap
from scanner.shodan_lookup import get_shodan_info
import os

app = Flask(__name__)

# Configure database (SQLite for now)
basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define a simple ScanResult model (optional - for future scan history)
class ScanResult(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    target = db.Column(db.String(100))
    nmap_result = db.Column(db.Text)
    shodan_result = db.Column(db.Text)

# Homepage with input
@app.route('/')
def index():
    return render_template('index.html')

# Handle scan request
@app.route('/scan', methods=['POST'])
def scan():
    target = request.form.get('target')
    if not target:
        return jsonify({'error': 'No target provided'}), 400

    try:
        # Run Nmap and Shodan scans
        nmap_data = run_nmap(target)
        shodan_data = get_shodan_info(target)

        # Optional: Save to database
        new_scan = ScanResult(
            target=target,
            nmap_result=str(nmap_data),
            shodan_result=str(shodan_data)
        )
        db.session.add(new_scan)
        db.session.commit()

        return jsonify({'nmap': nmap_data, 'shodan': shodan_data})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Create DB tables if they don't exist
    with app.app_context():
        db.create_all()

    app.run(debug=True)
