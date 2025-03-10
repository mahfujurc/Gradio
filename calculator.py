##import gradio as gr

# Calculator logic inside the same file
##def calculator(a, b, operation):
   ## if operation == "Add":
     ##   return a + b
   ## elif operation == "Subtract":
      ##  return a - b
##  elif operation == "Multiply":
       ## return a * b
   ## elif operation == "Divide":
      ##  if b == 0:
         ##   return "Error: Division by zero"
      ##  return a / b

# Create a Gradio interface (Gradio will automatically generate the GUI)
## interface = gr.Interface(
     ## fn=calculator,  # Function to link the calculator logic
   ## inputs=[  # Define inputs - automatically generated in the GUI
     ##   gr.Number(label="Enter first number"), 
    ##    gr.Number(label="Enter second number"), 
     ##   gr.Dropdown(["Add", "Subtract", "Multiply", "Divide"], label="Select Operation")
 ##   ],
  ##  outputs="text",  # This will display the result in text format
   ## live=True  # Makes the interface live to show results as you type
##)

# Launch the interface (this will generate a live GUI and provide a link)
##interface.launch(share=True)





















import gradio as gr

# Calculator logic inside the same file
def calculator(a, b, operation):
    if operation == "Add":
        return f"The result is: {a + b}"
    elif operation == "Subtract":
        return f"The result is: {a - b}"
    elif operation == "Multiply":
        return f"The result is: {a * b}"
    elif operation == "Divide":
        if b == 0:
            return "Error: Division by zero"
        return f"The result is: {a / b}"

# Create a more interactive and structured Gradio interface
interface = gr.Interface(
    fn=calculator,  # Function to link the calculator logic
    inputs=[  # Define inputs
        gr.Number(label="Enter first number", precision=2),  # Number 1
        gr.Number(label="Enter second number", precision=2),  # Number 2
        gr.Dropdown(
            choices=["Add", "Subtract", "Multiply", "Divide"], 
            label="Select Operation", 
            type="index"
        ),  # Operation dropdown
    ],
    outputs="text",  # Display the result in text format
    live=True,  # Makes the interface live to show results as you type
    layout="vertical",  # Align elements vertically
    theme="compact",  # More compact and elegant theme
    title="Interactive Calculator",  # Adding a title
    description="A simple interactive calculator for basic arithmetic operations (Add, Subtract, Multiply, Divide).",
    examples=[  # Optional: adding examples for quick access
        [5, 3, "Add"],
        [10, 2, "Multiply"],
        [20, 4, "Divide"],
    ]
)

# Launch the interface with a public shareable link
interface.launch(share=True)
