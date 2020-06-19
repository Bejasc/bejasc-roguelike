import tcod as libtcod
from enum import Enum
from game_states import GameStates


class InputModes(Enum):
    """Gives the ability to switch between a simpler keypad binding vs the tutorials own vim keys

    Args:
        Enum ([InputModes]): [The type of input system to use]
    """

    INPUT_VIM = 1
    INPUT_NUMPAD = 2


def handle_keys(key, game_state, input_mode):
    if game_state == GameStates.PLAYERS_TURN:
        return handle_player_turn_keys(key, input_mode)
    elif game_state == GameStates.PLAYER_DEAD:
        return handle_player_dead_keys(key)
    elif game_state in (GameStates.SHOW_INVENTORY, GameStates.DROP_INVENTORY):
        return handle_inventory_keys(key)

    return {}


def handle_player_turn_keys(key, input_mode):
    key_char = chr(key.c)

    if input_mode == InputModes.INPUT_VIM:
        if key.vk == libtcod.KEY_UP or key_char == "k":
            return {"move": (0, -1)}
        elif key.vk == libtcod.KEY_DOWN or key_char == "j":
            return {"move": (0, 1)}
        elif key.vk == libtcod.KEY_LEFT or key_char == "h":
            return {"move": (-1, 0)}
        elif key.vk == libtcod.KEY_RIGHT or key_char == "l":
            return {"move": (1, 0)}
        elif key_char == "y":
            return {"move": (-1, -1)}
        elif key_char == "u":
            return {"move": (1, -1)}
        elif key_char == "b":
            return {"move": (-1, 1)}
        elif key_char == "n":
            return {"move": (1, 1)}
    elif input_mode == InputModes.INPUT_NUMPAD:
        # Intend to fix this up later
        if key.vk == libtcod.KEY_UP or key_char == "k":
            return {"move": (0, -1)}
        elif key.vk == libtcod.KEY_DOWN or key_char == "j":
            return {"move": (0, 1)}
        elif key.vk == libtcod.KEY_LEFT or key_char == "h":
            return {"move": (-1, 0)}
        elif key.vk == libtcod.KEY_RIGHT or key_char == "l":
            return {"move": (1, 0)}
        elif key_char == "y":
            return {"move": (-1, -1)}
        elif key_char == "u":
            return {"move": (1, -1)}
        elif key_char == "b":
            return {"move": (-1, 1)}
        elif key_char == "n":
            return {"move": (1, 1)}

    if key_char == "g":
        return {"pickup": True}

    elif key_char == "i":
        return {"show_inventory": True}

    elif key_char == "d":
        return {"drop_inventory": True}

    return handle_generic_keys(key)


def handle_player_dead_keys(key):
    key_char = chr(key.c)

    if key_char == "i":
        return {"show_inventory": True}

    return handle_generic_keys(key)


def handle_inventory_keys(key):
    index = key.c - ord("a")

    if index >= 0:
        return {"inventory_index": index}

    return handle_generic_keys(key)


def handle_generic_keys(key):

    if key.vk == libtcod.KEY_ENTER and key.lalt:
        # Alt+Enter: toggle full screen
        return {"fullscreen": True}
    elif key.vk == libtcod.KEY_ESCAPE:
        # Exit the menu
        return {"exit": True}

    return {}
