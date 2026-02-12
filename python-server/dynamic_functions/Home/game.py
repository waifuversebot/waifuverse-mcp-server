import atlantis
import logging
import os

logger = logging.getLogger("mcp_server")

@public
@game
async def game():
    """
    Main game function - initializes WaifuVerse session
    """

    await atlantis.client_command("/silent on")

    # get user id
    user_id = atlantis.get_caller()
    logger.info(f"Game started for user: {user_id}")

    owner_id = atlantis.get_owner()
    await atlantis.client_log(f"Owner ID: {owner_id}")

    await atlantis.client_command("/chat set " + owner_id + "*mochi")

    # set background
    await atlantis.client_command("/silent off")
    image_path = os.path.join(os.path.dirname(__file__), "background.jpg")

    await atlantis.set_background(image_path)

    # send Mochi face image
    mochi_path = os.path.join(os.path.dirname(__file__), "mochi_face.jpg")
    await atlantis.client_image(mochi_path)

    await atlantis.client_log(f"Welcome to WaifuVerse, {user_id}! Mochi is here to help, nya~!")

