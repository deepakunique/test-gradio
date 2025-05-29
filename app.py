import gradio as gr

def greet(name):
    return f"Hello Hworld, {name}!"

gr.Interface(fn=greet, inputs="text", outputs="text").launch()
