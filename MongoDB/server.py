from flask import Flask, request, jsonify
from pymongo import MongoClient
import datetime

app = Flask(__name__)

client = MongoClient("localhost", 27017)
db = client['Rasp_Pico_W']
collection = db['radar_data']

print(client, db, collection)

@app.route('/api/dht', methods=['POST'])
def write_dht_data():
    try:
        data = request.get_json()
        print(f"Received Data: {data}")
        # if 'temperature' not in data or 'humidity' not in data:
        #     return jsonify({'error': 'Invalid data. Temperature and humidity are required.'}), 400
        
        # Create a document with the temperature, humidity, and timestamp
        timestamp = datetime.datetime.now().isoformat()
        # dht_document = {
        #     'timestamp': timestamp,
        #     'temperature': data['temperature'],
        #     'humidity': data['humidity']
        # }
        data["timestamp"] = timestamp
        
        result = collection.insert_one(data)
        
        return jsonify({
            'message': 'Data successfully inserted.',
            'document_id': str(result.inserted_id),
            'timestamp': timestamp
        }), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/dht', methods=['GET'])
def get_dht_data():
    try:
        # Fetch all documents from the collection
        dht_documents = list(collection.find({}, {'_id': 0}))  # Exclude the default MongoDB "_id" field
        
        if not dht_documents:
            return jsonify({'message': 'No data found'}), 404
        
        return jsonify(dht_documents), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    # Expose to all network interfaces for Raspberry Pi Pico W
    app.run(debug=True, host='0.0.0.0', port=5000)  

