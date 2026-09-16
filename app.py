from openai import OpenAI
import os
from dotenv import load_dotenv
from flask import Flask, jsonify, render_template

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=OPENAI_API_KEY)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/generateimages/<prompt>')
def generate(prompt):
    print("prompt :", prompt)
    try:
        response = client.images.generate(
            model="gpt-image-2.5-flare",
            prompt=prompt,
            size="1024x1024",
            n=1
        )
        # model_dump() converts the SDK's response object into a plain
        # JSON-serializable dict so Flask's jsonify can handle it
        return jsonify(response.model_dump()), 200
    except Exception as e:
        print("error :", e)
        return jsonify({"error": str(e)}), 500
    
if __name__ == '__main__':
    app.run(debug=True)