import gradio as gr

def small_sentiment(text):
    text = text.lower()
    if "good" in text or "happy" in text or "love" in text:
        return "Positive 😊"
    elif "bad" in text or "sad" in text or "hate" in text:
        return "Negative 😢"
    else:
        return "Neutral 😐"

demo = gr.Interface(
    fn=small_sentiment, 
    inputs=gr.Textbox(lines=2, placeholder="Enter your sentence here..."), 
    outputs="text",
    title="Very Small AI Sentiment Model",
    description="Type any text and get a simple sentiment result!"
)

demo.launch()
