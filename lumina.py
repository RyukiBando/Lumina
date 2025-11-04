import gradio as gr
import numpy as np
from PIL import Image

def rgb_to_ycbcr(image):
    arr = np.array(image).astype(np.float32)
    R, G, B = arr[..., 0], arr[..., 1], arr[..., 2]
    Y  = 0.299 * R + 0.587 * G + 0.114 * B
    Cb = 128 - 0.168736 * R - 0.331264 * G + 0.5 * B
    Cr = 128 + 0.5 * R - 0.418688 * G - 0.081312 * B
    return np.stack((Y, Cb, Cr), axis=-1)

def ycbcr_to_rgb(ycbcr):
    Y, Cb, Cr = ycbcr[..., 0], ycbcr[..., 1], ycbcr[..., 2]
    R = Y + 1.402 * (Cr - 128)
    G = Y - 0.344136 * (Cb - 128) - 0.714136 * (Cr - 128)
    B = Y + 1.772 * (Cb - 128)
    rgb = np.stack((R, G, B), axis=-1)
    rgb = np.clip(rgb, 0, 255).astype(np.uint8)
    return rgb

def process_image(image, brilho):
    if image is None:
        return None, None
    image = image.convert("RGB")
    ycbcr = rgb_to_ycbcr(image)

    # Ajuste de brilho (canal Y)
    ycbcr[..., 0] = np.clip(ycbcr[..., 0] * brilho, 0, 255)

    reconstructed = ycbcr_to_rgb(ycbcr)
    reconstructed_img = Image.fromarray(reconstructed)
    return image, reconstructed_img

title = "✨ lumina"
description = (
    "Transforme uma imagem em YCbCr e reconverta para RGB, "
    "comparando lado a lado com a original. "
    "Use o controle de brilho (canal Y) para visualizar o efeito da conversão."
)

demo = gr.Interface(
    fn=process_image,
    inputs=[
        gr.Image(type="pil", label="Selecione ou solte uma imagem"),
        gr.Slider(0.5, 1.5, 1.0, step=0.05, label="Brilho (canal Y)")
    ],
    outputs=[
        gr.Image(label="Original"),
        gr.Image(label="Processada (YCbCr → RGB)")
    ],
    title=title,
    description=description,
    allow_flagging="never",
)

if __name__ == "__main__":
    demo.launch(share=True)