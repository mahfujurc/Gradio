import gradio as gr

# Calculator logic inside the same file
def calculator(a, b, operation):
    if operation == "Add":
        return a + b
    elif operation == "Subtract":
        return a - b
    elif operation == "Multiply":
        return a * b
    elif operation == "Divide":
        if b == 0:
            return "Error: Division by zero"
        return a / b

# Create a Gradio interface (Gradio will automatically generate the GUI)
interface = gr.Interface(
    fn=calculator,  # Function to link the calculator logic
    inputs=[  # Define inputs - automatically generated in the GUI
        gr.Number(label="Enter first number"), 
        gr.Number(label="Enter second number"), 
        gr.Dropdown(["Add", "Subtract", "Multiply", "Divide"], label="Select Operation")
    ],
    outputs="text",  # This will display the result in text format
    live=True  # Makes the interface live to show results as you type
)

# Launch the interface (this will generate a live GUI and provide a link)
interface.launch(share=True)
