from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from transformers import PegasusForConditionalGeneration, PegasusTokenizer

app = Flask(__name__)
CORS(app)

# Load Pegasus model and tokenizer
model_name = "google/pegasus-xsum"
tokenizer = PegasusTokenizer.from_pretrained(model_name)
model = PegasusForConditionalGeneration.from_pretrained(model_name)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize_text():
    try:
        data = request.get_json()
        input_text = data.get("text", "")

        if not input_text:
            return jsonify({"error": "No text provided"}), 400

        inputs = tokenizer(input_text, return_tensors="pt", truncation=True, max_length=512)
        summary_ids = model.generate(**inputs, max_length=250, min_length=50, length_penalty=2.0, num_beams=4)
        summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

        return jsonify({"summary": summary})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
