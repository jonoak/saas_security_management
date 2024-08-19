from flask import Flask, jsonify, request
from apscheduler.schedulers.background import BackgroundScheduler
import logging
from modules.api_integration import APIIntegration
from modules.data_storage import DataStorage
from modules.analysis_compliance import AnalysisCompliance
from modules.visualization_reporting import VisualizationReporting
from modules.monitoring_alerts import MonitoringAlerts

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

# Initialize Modules
api_integration = APIIntegration()
data_storage = DataStorage()
analysis_compliance = AnalysisCompliance()
visualization_reporting = VisualizationReporting()
monitoring_alerts = MonitoringAlerts()

# Scheduler for data collection
scheduler = BackgroundScheduler()
scheduler.add_job(api_integration.collect_data, 'interval', hours=1)
scheduler.start()

@app.route('/api/login', methods=['POST'])
def login():
    # User authentication would be handled here
    return jsonify({"message": "Login successful"})

@app.route('/api/dashboard', methods=['GET'])
def dashboard_view():
    data = visualization_reporting.get_dashboard_data()
    return jsonify(data)

@app.route('/api/analysis', methods=['GET'])
def analysis_view():
    data = analysis_compliance.get_analysis_data()
    return jsonify(data)

@app.route('/api/reports', methods=['GET'])
def reports_view():
    data = visualization_reporting.get_report_data()
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)