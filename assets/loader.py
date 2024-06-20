loader_ready = True

try:
    from time import sleep
except ImportError:
    loader_ready = False


loader_list1 = ["⠻", "⠽", "⠾", "⠷", "⠯", "⠟"]
loader_list2 = ["/", "-", "\\", "|"]


def load_anim(load_type: int, time: float) -> str:
    """Loader function, this function takes an integer and float as input
    and returns strings from a list in an animated form to simulate a
    loading animation."""
    if load_type == 1:
        for x in range(1, time + 1):
            for i in loader_list1:
                sleep(0.1)
                if x == time:
                    print(end="")
                    break
                else:
                    print("Loading " + i, end="\r")
    elif load_type == 2:
        for x in range(1, time + 1):
            for i in loader_list2:
                sleep(0.1)
                if x == time:
                    print(end="")
                    break
                else:
                    print(i, end="\r")
    else:
        print("Invalid argument!")

