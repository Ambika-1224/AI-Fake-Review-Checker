from google import genai
from config import GEMINI_API_KEY
from google.genai import types

client = genai.Client(api_key=GEMINI_API_KEY)

def analyze_review(review):

    prompt = f"""
You are an expert Fake Review Detection AI.

Analyze the following product review carefully.

Review:
{review}

Provide your answer ONLY in the following format:

 Verdict: Genuine or Fake

 Confidence: XX%

 Sentiment: Positive / Negative / Neutral

 Reason:
Write only 2 short lines.

Return each field on a new line.

Example:

Verdict: Genuine

Confidence: 85%

Sentiment: Positive

Reason:
Line 1
Line 2

Do not write any extra text.
"""
    models = [
        "gemini-2.5-flash",
        "gemini-2.0-flash"
    ]

    for model in models:
        try:
            response = client.models.generate_content(
                model=model,
                contents=prompt
            )

            return response.text

        except Exception as e:
            return str(e)

    return """
⚠️ AI service is temporarily unavailable.

Please try again after a few minutes.
"""
def analyze_review_image(image_path):

    prompt = """
You are an expert Fake Review Detection AI.

Read the product review from the uploaded image.

Provide ONLY this format:

Verdict: Genuine or Fake

Confidence: XX%

Sentiment: Positive / Negative / Neutral

Reason:
Write only 2 short lines.

Return each field on a new line.

Example:

Verdict: Genuine

Confidence: 85%

Sentiment: Positive

Reason:
Line 1
Line 2
"""

    models = [
        "gemini-2.5-flash",
        "gemini-2.0-flash"
    ]

    try:
        uploaded = client.files.upload(file=image_path)
        print(uploaded)

        for model in models:
            try:
                response = client.models.generate_content(
                    model=model,
                    contents=[prompt, uploaded]
                )

                return response.text

            except Exception:
                continue

    except Exception as e:
        import traceback
        traceback.print_exc()
        return str(e)

    return """
⚠️ AI service is temporarily unavailable.

Please try again after a few minutes.
"""