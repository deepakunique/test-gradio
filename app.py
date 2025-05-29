import gradio as gr

def greet(name):
    return f"Thank you for deploying, {name}!"

gr.Interface(fn=greet, inputs="text", outputs="text").launch()
