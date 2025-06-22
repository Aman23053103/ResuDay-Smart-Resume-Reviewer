from flask import Flask, render_template, request, jsonify
import fitz  # PyMuPDF
import google.generativeai as genai

# Configure Gemini API
genai.configure(api_key="YOUR API KEY")
model = genai.GenerativeModel("gemini-1.5-flash")

app = Flask(__name__)

def extract_text_from_pdf(file_stream):
    doc = fitz.open(stream=file_stream.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/evaluate", methods=["POST"])
def evaluate_resume():
    resume_file = request.files["resume"]
    job_desc = request.form["job_description"]
    resume_text = extract_text_from_pdf(resume_file)

    prompt = f"""
You are a professional career coach.

Evaluate this resume for the following job description.
Provide:
- A score out of 10
- Key strengths
- Suggestions to improve

Resume:
{resume_text}

Job Description:
{job_desc}
    """

    response = model.generate_content(prompt)
    return jsonify({"result": response.text})

if __name__ == "__main__":
    app.run(debug=True)
