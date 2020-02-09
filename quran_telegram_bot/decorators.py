from functools import wraps


def send_action(action):
    """Sends `action` while processing func command."""

    def decorator(func):
        @wraps(func)
        def command_func(bot, update, *args, **kwargs):
            bot.send_chat_action(chat_id=update.message.chat_id, action=action)
            return func(bot, update,  *args, **kwargs)
        return command_func

    return decorator
