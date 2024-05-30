import reflex as rx
from langchain_community.llms import Ollama

llm = Ollama(model="phi3:3.8b")


class State(rx.State):
    prompt = ""

    

# def index() -> rx.Component:
#     """
#         Your Index Page
#     """
#     return rx.Component(
#         rx.vstack(
#             rx.heading("DALL-E", font_size="1.5em"),
#             rx.input(
#                 placeholder="Enter a prompt..",
#                 on_blur=State.set_prompt,
#                 width="25em",
#             ),
#         ),
#         width='100%',
#         height='100vh'
#     )


def index():
    return rx.center(
        rx.vstack(
            rx.heading("DALL-E", font_size="1.5em"),
            rx.input(
                placeholder="Enter a prompt..",
                on_blur=State.set_prompt,
                width="25em",
            ),
            # rx.button("Generate Image", on_click=State.get_image, width="25em"),
            # rx.cond(
            #     State.processing,
            #     rx.chakra.circular_progress(is_indeterminate=True),
            #     rx.cond(
            #         State.complete,
            #         rx.image(src=State.image_url, width="20em"),
            #     ),
            # ),
            # align="center",
        ),
        width="100%",
        height="100vh",
    )

app = rx.App()
app.add_page(index, title="Reflex:Phi-3")