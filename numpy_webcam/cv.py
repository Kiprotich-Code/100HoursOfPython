import cv2


def render_recv(resp):
    for d in resp.docs:
        cv2.imshow('output', d.tensor)


from jina import Client, Document

c = Client(host=server_address)
c.post(
    '/',
    Document.generator_from_webcam(
        tags={'user': 'han'}, show_window=False, height_width=(200, 300)
    ),
    on_done=render_recv,
    request_size=1,
)
