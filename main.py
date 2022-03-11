import typer
from PIL import Image
import os

def main():
    ON = True
    while ON:
        file_path = typer.prompt("Enter the file directory: ")
        im = Image.open(f"{file_path}")
        user_choice = typer.prompt("What would you like to do?\nPress '1' for Resizing\nPress '2' to change format")
        if int(user_choice) == 1:
            pixels = []
            for x in range(2):
                variable = typer.prompt("Please enter the resize values(first enter height then the width) in pixels: ")
                variable_int = int(variable)
                pixels.append(variable_int)
            resized_image = im.resize(tuple(pixels),0)
            end_path1 = typer.prompt("Where would you like to save the file?\n")
            resized_image.save(f"{end_path1}/resized image.jpeg")
        elif int(user_choice) == 2:
            format = input("Enter a format: ")
            end_path = typer.prompt("Where would you like to save the file?\n")
            im1 = im.save(f"{end_path}.{format}")
        on_off = input("Do you want to continue? Type 'Yes' or 'No'")
        if on_off.lower() == "no":
            ON = False


if __name__ == "__main__":
    typer.run(main)
