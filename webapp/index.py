from app import app, server

from routes import render_page_content

from layout.sidebar.sidebar_callbacks import toggle_collapse, toggle_classname

from environment.settings import APP_HOST, APP_PORT, APP_DEBUG, DEV_TOOLS_PROPS_CHECK


if __name__ == "__main__":
    app.run_server(
        host='127.0.0.1',
        port='8050',
        debug=True,
        dev_tools_props_check=True
    )