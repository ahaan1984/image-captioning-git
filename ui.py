import gradio as gr
from PIL import Image

processor = AutoProcessor.from_pretrained(saved_folder_path)
model = AutoModelForCausalLM.from_pretrained(saved_folder_path)


def generate_caption(image):
    image = Image.fromarray(image)
    inputs = tokenizer(image, return_tensors="pt")
    inputs = processor(images=image, return_tensors="pt").to(device)
    pixel_values = inputs.pixel_values

    generated_ids = model.generate(pixel_values=pixel_values, max_length=50)
    generated_caption = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]

    return generated_caption

# Define the Gradio interface
interface = gr.Interface(
    fn=generate_caption,
    inputs=gr.Image(),
    outputs=gr.Textbox(),
    live=True
)

interface.launch()