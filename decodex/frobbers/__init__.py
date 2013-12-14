from decodex.stream import Stream
import importlib


ACTIVE_FROBBERS = [
    "decodex.frobbers.basic.base10",
    "decodex.frobbers.basic.base16",
]


def iter_frobbers():
    for decoder in ACTIVE_FROBBERS:
        module, function_ = decoder.rsplit(".", 1)
        mod = importlib.import_module(module)
        yield getattr(mod, function_)


def iter_streams(input_):
    null = Stream(input_, 'string')
    null.frobber = 'raw'
    yield null

    for frobber in iter_frobbers():
        yield frobber(null)
