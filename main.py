import typer

from cli.encrypter.keygen import generate_key_pair

app = typer.Typer()


@app.command()
def user_input():
    private_key_pem, public_key_pem = generate_key_pair()
    print("private_key_pem =", private_key_pem)
    print("public_key_pem =", public_key_pem)
    name = typer.prompt("What's your name?")
    typer.echo(f"Hello {name}")
    recipient_ip = typer.prompt("What's the IP address of the recipient?")
    typer.echo(f"Recipient IP: {recipient_ip}")
    recipient_public_key_path = typer.prompt("What's the path to the recipient's public key?")
    typer.echo(f"Recipient Public Key Path: {recipient_public_key_path}")


if __name__ == "__main__":
    typer.run(user_input)
