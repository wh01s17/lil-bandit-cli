# mi_cli/main.py
import typer

app = typer.Typer()


@app.command()
def hola(nombre: str):
    print(f"Hola {nombre}")


def main():
    app()


if __name__ == "__main__":
    main()
