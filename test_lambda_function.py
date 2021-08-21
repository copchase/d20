import lambda_function

# Basic sanity test
def test_lambda_handler(mocker):
    request_mock = mocker.patch("lambda_function.requests.post")
    event = {
        "headers": {
            "Nightbot-Response-Url": "mock-url",
            "Nightbot-User": "name=copchase&displayName=copchase&provider=twitch&providerId=123&userLevel=owner",
            "Nightbot-Channel": "name=copchase&displayName=copchase&provider=twitch&providerId=123"
        }
    }

    lambda_function.lambda_handler(event, None)

    request_mock.assert_called_once()


def test_filter(monkeypatch, mocker):
    monkeypatch.setenv("FILTERED", "123")
    request_mock = mocker.patch("lambda_function.requests.post")
    mocker.patch("lambda_function.logger")
    event = {
        "headers": {
            "Nightbot-Response-Url": "mock-url",
            "Nightbot-User": "name=copchase&displayName=copchase&provider=twitch&providerId=123&userLevel=owner",
            "Nightbot-Channel": "name=copchase&displayName=copchase&provider=twitch&providerId=123"
        }
    }

    lambda_function.lambda_handler(event, None)

    request_mock.assert_not_called()
