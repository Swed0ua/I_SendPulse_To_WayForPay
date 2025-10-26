from flask import Flask, json, request, jsonify
from config.config import SP_REST_API_ID, SP_REST_API_SECRET, SP_TOKEN_STORAGE, SP_ADDRESSBOOK_ID
from service.SendPulseClient.api import SendPulseManager

def create_app():
    app = Flask(__name__)

    sendpulse_manager = SendPulseManager(
        SP_REST_API_ID,
        SP_REST_API_SECRET,
        SP_TOKEN_STORAGE
    )

    @app.route('/proccessInvoice', methods=['POST'])
    def proccessInvoice():
        if request.is_json:
            data = request.get_json()
        else:
            if len(request.form) == 1:
                raw = next(iter(request.form.keys()))
                try:
                    data = json.loads(raw)
                except Exception:
                    return jsonify({'error': 'Malformed JSON in form data'}), 400
            else:
                return jsonify({'error': 'Invalid form data'}), 400

        print("Received data:", data)

        user_email = data.get("email")
        user_phone = data.get("phone")

        if user_email:
            contact = {
                "email": user_email,
                "variables": {
                    "phone": user_phone
                }
            }

            response = sendpulse_manager.add_contacts(SP_ADDRESSBOOK_ID, [contact])

            return jsonify({
                'status': 'success',
                'sendpulse_response': response
            }), 200
        else:   
            return jsonify({'error': 'Email is required'}), 200

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5060, debug=True)