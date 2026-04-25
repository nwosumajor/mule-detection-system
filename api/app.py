from flask import Flask, request, jsonify
import tensorflow as tf
import joblib
import pandas as pd

app = Flask(__name__)

# 1. Load the trained model and scaler into memory at startup
try:
    model = tf.keras.models.load_model('mule_detection_model.keras')
    scaler = joblib.load('scaler.pkl')
    print("Model and Scaler loaded successfully.")
except Exception as e:
    print(f"Error loading assets: {e}")

@app.route('/predict-mule', methods=['POST'])
@app.route('/predict-mule', methods=['POST'])
def predict_fraud():
    try:
        data = request.get_json()
        
        # 1. Define the exact columns the model expects, in order
        expected_cols = [
            'amount', 'oldbalanceOrg', 'newbalanceOrig', 
            'oldbalanceDest', 'newbalanceDest', 
            'balance_diff_orig', 'balance_diff_dest', 
            'type_CASH_OUT', 'type_DEBIT', 'type_PAYMENT', 'type_TRANSFER'
        ]
        
        # 2. Create a clean dictionary, defaulting everything to 0
        clean_data = {col: 0 for col in expected_cols}
        
        # 3. Pull in the data from the JSON payload if it matches our list
        for key in expected_cols:
            if key in data:
                clean_data[key] = data[key]
                
        # 4. Convert to DataFrame (ignoring extra stuff like 'step')
        df = pd.DataFrame([clean_data], columns=expected_cols)
        
        # Scale and Predict
        scaled_features = scaler.transform(df)
        prediction_prob = model.predict(scaled_features)[0][0]
        
        is_mule = bool(prediction_prob > 0.80)
        
        return jsonify({
            'status': 'success',
            'mule_probability': float(prediction_prob),
            'flagged_as_fraud': is_mule
        }), 200
        
    except Exception as e:
        return jsonify({'error': str(e), 'status': 'failed'}), 400

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy', 'service': 'mule-detection-api'}), 200

if __name__ == '__main__':
    # Run the server on port 5000
    app.run(host='0.0.0.0', port=5000)
