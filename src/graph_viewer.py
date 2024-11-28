#!/usr/bin/env python3

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Graph Viewer
# @raycast.mode fullOutput

# Optional parameters:
# @raycast.icon 🤖
# @raycast.packageName graph viewer

# Documentation:
# @raycast.description View a compressed graph
# @raycast.author Sam

import pyperclip
import zlib
import base64
import pydot
from PIL import Image
import io

def decompress_clipboard_content():
    try:
        input_data = pyperclip.paste()
        if not input_data:
            print("Clipboard is empty or does not contain valid text.")
            return
        decoded_data = base64.b64decode(input_data)
        decompressed_data = zlib.decompress(decoded_data)
        return decompressed_data.decode("utf-8")

    except Exception as e:
        print(f"Clipboard content is not a valid graph")
        return None

def display_graph():
    graph_text = decompress_clipboard_content()
    graph = pydot.graph_from_dot_data(graph_text)[0]
    png_data = graph.create_png()
    image = Image.open(io.BytesIO(png_data))
    image.show()

if __name__ == '__main__':
    display_graph()

