def input_to_float(message: str = "", msgIsTip: bool = False) -> float:
    if msgIsTip:
        msg_tip = " (integer)"
    else:
        msg_tip = ""

    while True:
        try:
            return float(input(message + msg_tip + ": "))

        except ValueError:
            print("[Error]: It's not an float!")