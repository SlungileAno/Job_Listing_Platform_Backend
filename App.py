from flask import Flask, request, jsonify 
from flask_cors import CORS 

app = Flask(__name__)
CORS(app)

jobs = []

@app.route('/jobs', methods=['GET', 'POST'])
def manage_jobs():
    if request.method == 'POST':
        job = request.get_json()
        jobs.append(job)
        return jsonify({"message": "Job added"}), 201
    return jsonify(jobs) 

@app.route('/jobs/<int:job_id>', methods=['GET'])
def get_job(job_id):
    if job_id >= len(jobs):
        return jsonify({"error": "Job not found"}), 404
    return jsonify(jobs[job_id])

if __name__ == '__main__':
    app.run(debug=True)
