"""Module providing a function printing python version."""

from src.models.history_model import HistoryModel
from src.models.user_model import UserModel


def test_history_delete(app_test):
    """Function printing python version."""

    # Usuário de exemplo
    user_data = {"name": "Stephan", "level": "admin", "token": "123456"}
    user = UserModel(user_data)
    user.save()

    # Históricos de exemplo
    history_data = [
        {
            "text-to-translate": "I like to run",
            "translate-from": "en",
            "translate-to": "pt",
        },
        {
            "text-to-translate": "What do you like to eat",
            "translate-from": "en",
            "translate-to": "pt",
        },
    ]
    for history_info in history_data:
        HistoryModel(history_info).save()

    # Encontra o histórico que desejamos excluir
    history_to_delete = HistoryModel.find_one(
        {"text-to-translate": "What do you like to eat"}
    )

    # Encontra o usuário para autenticação
    user_to_authenticate = UserModel.find_one({"name": "Stephan"})

    # Exclui o histórico
    app_test.delete(
        f"/admin/history/{history_to_delete.data['_id']}",
        headers={
            "Authorization": user_to_authenticate.data["token"],
            "User": user_to_authenticate.data["name"],
        },
    )
