import typer

app = typer.Typer()

@app.command()
def hello(name: str):
    """
    Say hello to NAME
    """
    print(f"Hello {name}!")

@app.command()
def goodbye(name: str, formal: bool = False):
    """
    Say goodbye to NAME, optionally in a formal manner via the --formal flag
    """
    if formal:
        print(f"Goodbye, {name}!")
    else:
        print(f"Bye, {name}!")

if __name__ == "__main__":
    app()