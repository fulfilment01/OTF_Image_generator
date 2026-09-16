# OTF — Image Studio
A minimal image generation platform. Type a prompt, get a frame back.
Built with Flask and OpenAI's `gpt-image-2.5-flare` model.
## Tech Stack
- **Backend** — Flask (Python), OpenAI Python SDK
- **Model** — `gpt-image-2.5-flare`
- **Frontend** — Single `index.html` template (Tailwind CSS, vanilla JS)
- **Config** — `python-dotenv` for environment variables
## Project Structure
```
.
├── app.py              # Flask app: serves the page + /generateimages endpoint
├── .env                # OPENAI_API_KEY=your_key_here  (not committed)
└── templates/
    └── index.html      # The entire frontend
```
## Setup
1. **Install dependencies**
   ```bash
   pip install flask openai python-dotenv
   ```
2. **Add your API key**
   Create a `.env` file in the project root:
   ```
   OPENAI_API_KEY=sk-...
   ```
3. **Run the server**
   ```bash
   python app.py
   ```
4. **Open the studio** at `http://localhost:5000`
## Usage
Type a prompt and press **Enter** (or **⌘/Ctrl + Enter**) to generate.
Each run renders one 256×256 image. Results can be downloaded as PNG, and
your generation history is stored locally in the browser (localStorage) —
up to 18 recent frames.
## API
| Endpoint | Method | Description |
|---|---|---|
| `/` | GET | Renders the studio page |
| `/generateimages/<prompt>` | GET | Generates one image, returns the OpenAI response as JSON |
Example:
```bash
curl http://localhost:5000/generateimages/a%20lighthouse%20at%20dawn
```
## Notes
- Prompts containing `/` are sanitized by the frontend — Flask's default path
  converter can't match slashes.
- The backend converts the OpenAI SDK response with `model_dump()` before
  returning it, since Flask's `jsonify` can't serialize SDK objects directly.
- Image payload is handled as either `b64_json` or `url`, depending on what
  the model returns.
```