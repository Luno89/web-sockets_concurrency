import websocket
from nose.tools import *
from mock import MagicMock
import producer


def setup():
    print("")


def teardown():
    print("")


def test_basic():
    assert True

def makes_data():
    web_socket = websocket.WebSocket()
    web_socket.send = MagicMock()

    # producer.produce(100)

    web_socket.send.assert_called_once_with(1)
