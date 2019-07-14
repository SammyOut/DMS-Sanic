from asyncio import get_event_loop

from app import create_app
from models import init_db

if __name__ == '__main__':
    get_event_loop().run_until_complete(init_db())
    app = create_app()

    app.run()
