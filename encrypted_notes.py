import click
import os
from crypto_utils import encrypt_note, decrypt_note

NOTES_FILE = "notes.enc"

def get_password(prompt="Enter password: "):
    """Get password input using simple input method."""
    return input(prompt)

@click.group()
def cli():
    """Encrypted Notes CLI App"""
    pass

@cli.command()
def write():
    """Write a new encrypted note."""
    note = click.prompt("Enter your note")
    password = get_password("Enter a password to encrypt the note: ")
    encrypted = encrypt_note(note, password)
    with open(NOTES_FILE, "ab") as f:
        f.write(len(encrypted).to_bytes(4, 'big'))
        f.write(encrypted)
    click.echo("Note saved and encrypted.")

@cli.command()
def read():
    """Read and decrypt notes."""
    password = get_password("Enter your password to decrypt notes: ")
    if not os.path.exists(NOTES_FILE):
        click.echo("No notes found.")
        return
    with open(NOTES_FILE, "rb") as f:
        notes = []
        while True:
            len_bytes = f.read(4)
            if not len_bytes:
                break
            note_len = int.from_bytes(len_bytes, 'big')
            encrypted = f.read(note_len)
            try:
                note = decrypt_note(encrypted, password)
                notes.append(note)
            except Exception:
                notes.append("[Decryption failed: wrong password or corrupted note]")
    click.echo("\n--- Your Notes ---")
    for i, note in enumerate(notes, 1):
        click.echo(f"{i}. {note}")

if __name__ == "__main__":
    cli() 