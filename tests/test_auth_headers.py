import os
import sys
from unittest.mock import patch

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from digikey_mcp_server import _get_headers


def test_get_headers_uses_bearer_token():
    with patch("digikey_mcp_server._ensure_token", return_value="test_token"):
        headers = _get_headers()

    assert headers["Authorization"] == "Bearer test_token"
