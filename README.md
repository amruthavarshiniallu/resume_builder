# AI Resume Builder — n8n + Streamlit

Paste Job Description + LaTeX → hits your n8n webhook → returns Google Drive PDF link.

## Local Run
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Deploy to Streamlit Cloud

1. Push this folder to a GitHub repo
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Sign in with GitHub → **New app**
4. Select repo → branch `main` → file `app.py`
5. Click **Deploy**

No extra packages needed — only `streamlit` and `requests`.

## n8n Setup

Make sure your n8n webhook node:
- Is set to **POST** method
- Receives JSON body with keys: `job_description` and `latex_code`
- The **Respond to Webhook** node at the end returns JSON with your Google Drive link

Expected response format from n8n:
```json
{ "drive_link": "https://drive.google.com/file/d/..." }
```
If your key name is different (e.g. `link`, `url`, `pdf_link`), the app tries all common names automatically.
# resume_builder
