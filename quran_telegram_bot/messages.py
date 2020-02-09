from jinja2 import Environment, FileSystemLoader, select_autoescape

from quran_telegram_bot.settings import TEMPLATE_PATH

# Loading Jinja2 environment
env = Environment(
    loader=FileSystemLoader(TEMPLATE_PATH),
    autoescape=select_autoescape(['html', 'xml'])
)


def render_message(template_name: str, *args, **kwargs):
    """render_message_template Render a message via Jinja2 template
    
    :param template_name: Jija2 template name
    :type template_name: str
    """
    template = env.get_template(template_name)
    return template.render(*args, **kwargs)
