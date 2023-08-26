from PyQt5.QtCore import pyqtSignal


class Emitter:
    my_signal = pyqtSignal(str)

    def emit_event(self):
        self.my_signal.emit("Hello from emitter!")


emitter = Emitter()


class Receiver:
    def __init__(self):
        super().__init__()
        emitter.my_signal.connect(self.handle_event)

    def handle_event(self, message):
        print("Signal received:", message)
