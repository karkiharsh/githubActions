from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        data = request.json  # Get the JSON payload from GitHub
        print("Received webhook event:", data)
        return jsonify({"message": "Webhook received!"}), 200

if __name__ == '__main__':
    app.run(port=5000, debug=True)

