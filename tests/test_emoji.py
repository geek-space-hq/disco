from discore.models import Emoji


def test_serialize():
    example_user_data = {
        "id": "41771983429993937",
        "name": "LUL",
        "roles": ["41771983429993000", "41771983429993111"],
        "user": {
            "username": "Luigi",
            "discriminator": "0002",
            "id": "96008815106887111",
            "avatar": "5500909a3274e1812beb4e8de6631111",
        },
        "require_colons": True,
        "managed": False,
        "animated": False,
    }

    assert Emoji.parse_obj(example_user_data)
