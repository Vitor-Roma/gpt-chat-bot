from main import openai_chat_message
from unittest.mock import patch, MagicMock


@patch("openai.resources.chat.completions.Completions.create")
def test_call_open_ai(mock_create_completion):
    message = 'teste123, meu telefone é: 15 151515-151515'
    mock = MagicMock()
    mock.message.choices = [MagicMock()]
    mock.message.choices[0].message = MagicMock()
    mock.choices[0].message.content = message
    mock_create_completion.return_value = mock

    response = openai_chat_message(message)

    assert response == message
