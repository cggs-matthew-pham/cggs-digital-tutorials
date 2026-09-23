import gradio as gr

# Function to solve: X + num1 = num2
def algebra_add_to_x(num1, num2):
    # Return what x is
    return num2 - num1

# Call the function first and test without gradio
x_result = algebra_add_to_x(3,7)
print("x = " + str(x_result))

# Gradio wiring
interface = gr.Interface(
    inputs=[gr.Number(), gr.Number()],
    outputs=gr.Number(label="X:"),
    fn=algebra_add_to_x
)

# Launch the gradio interface
interface.launch()