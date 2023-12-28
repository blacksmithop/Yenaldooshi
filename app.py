import gradio as gr
import os
from utils.wolvesville import Wolvesville

wolf = Wolvesville()


with gr.Blocks() as roleTab:
    gr.Markdown("# Roles")
    roles = wolf.getRoles()
    with gr.Row():
        for role in roles[:5]:  # slow loading
            with gr.Group():
                gr.Image(
                    role.image.url,
                    scale=0.025,
                )
                gr.Markdown(
                    f"**Name**: {role.name}\n\n**Team**: {role.team}\n\n**Aura**: {role.aura}\n\n{role.description}"
                )


with gr.Blocks() as otherTab:
    gr.Markdown("# Emojis")
    emojis = wolf.getEmojis()
    with gr.Row():
        for emoji in emojis[:5]:  # slow loading
            with gr.Group():
                gr.Image(
                    emoji.urlPreview,
                    scale=0.025,
                )
                gr.Markdown(
                    f"**Name**: {emoji.name}\n\n**Rarity**: {emoji.rarity}\n\n**Event**: {emoji.event}"
                )

demo = gr.TabbedInterface([roleTab, otherTab], ["Roles", "Other"])

demo.launch()

if __name__ == "__main__":
    demo.launch()
