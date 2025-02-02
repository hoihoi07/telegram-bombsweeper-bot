from aiogram.utils.callback_data import CallbackData

cb_newgame = CallbackData("newgame", "size", "bombs", "as_separate")
cb_click = CallbackData("press", "game_id", "x", "y")
cb_switch_flag = CallbackData("flag", "game_id", "action", "x", "y")
cb_switch_mode = CallbackData("switchmode", "game_id", "new_mode")
cb_ignore = CallbackData("ignore", "x", "y")
