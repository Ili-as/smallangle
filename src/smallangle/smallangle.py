import click
import numpy as np
from numpy import pi
import pandas as pd

@click.group()
def cmd_group():
    pass

@cmd_group.command()
@click.option(
    "-n",
    "--number",
    default = 10,
    help = "Number of values between 0 and 2 pi",
    show_default=True,
    type = int
)
def sin(number):
    """Gives the sin between 0 and 2 pi in #n steps

    Args:
        number (int): "Number of values between 0 and 2 pi"
    """    
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "sin (x)": np.sin(x)})
    print(df)

@cmd_group.command()
@click.option(
    "-n",
    "--number",
    default = 10,
    help = "Number of values between 0 and 2 pi",
    show_default=True,
    type = int
)
def tan(number):
    """Gives the tan between 0 and 2 pi in #n steps

    Args:
        number (int): "Number of values between 0 and 2 pi"
    """    
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "tan (x)": np.tan(x)})
    print(df)


if __name__ == "__main__":
    cmd_group