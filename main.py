from colorist import ColorRGB
from typing import IO
from os import get_terminal_size
from argparse import ArgumentParser, FileType

def parseColor(colors: str) -> list:
	color = colors.split(",")
	colors = []
	for c in color:
		colors.append(ColorRGB(int(c.split(" ")[0]), int(c.split(" ")[1]), int(c.split(" ")[2])))
	return colors

def fileReader(file: IO) -> tuple:
	length = file.readline().strip()
	if length.isdigit():
		length = int(length)
	else:
		raise ValueError("Invalid input: first line is not an integer")
	values = file.readline().strip()
	if len(values.split(",")) != length:
		raise ValueError("Illegal input: Potentially corrupted data")
	return values
	
def printScreen(colors: list) -> None:
	colors = parseColor(colors)
	cbreaks = 0
	columns, rows = get_terminal_size()
	for i in colors:
		if cbreaks == columns:
			print()
			cbreaks = 0
		print(f"{i}█", end="")
		cbreaks += 1


def main() -> None:
	parser = ArgumentParser()
	parser.add_argument("--print-screen", "-ps", action="store_true", help="Print a .rgb file to the terminal")
	parser.add_argument("file", type=FileType('r'), help="File to read")
	args = parser.parse_args()
	if args.print_screen:
		colors = fileReader(args.file)
		printScreen(colors)



if __name__ == "__main__":
    main()