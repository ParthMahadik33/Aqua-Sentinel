from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__, 
            template_folder='templates',
            static_folder='static',
            static_url_path='/static')

# Enable static file serving with cache control
@app.after_request
def set_cache_control(response):
    response.headers['Cache-Control'] = 'public, max-age=3600'
    return response

@app.route('/')
def index():
    """Serve the main homepage"""
    return render_template('index.html')

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({'status': 'healthy', 'message': 'AquaSentinel is running'}), 200

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return render_template('index.html'), 200

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    # Run the app in debug mode for development
    # Set debug=False and use a production server for production
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )
