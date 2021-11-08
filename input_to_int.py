def input_to_int(message: str = "", msgIsTip: bool = False) -> int:
    if msgIsTip:
        msg_tip = " (integer)"
    else:
        msg_tip = ""

    while True:
        try:
            return int(input(message + msg_tip + ": "))

        except ValueError:
            print("[Error]: It's not an integer!")
