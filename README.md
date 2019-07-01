# asciilines

copyright (c) 2019 Evan DePosit

This program takes a .tvg file as an argument whose first line is the dimensions of the canvas to be built. The program constructs a matrix according to the specified dimensions with a '.' at each position.  Each line after the first in the file is interpreted as line to render.  the first character in the line is the character that will replace the '.' when rendered.  The next two characters in the line specify at which row and column the rendering should begin respectively.  the following character is either a 'v' or an 'h'.  If it is a 'v', the line rendered is vertical.  If it is a 'h', the lined rendered is horizontal. The last number character on the line specifies the length of the rendered line. 

## Build and Run

`python3 asciilines.py <file.tvg>`

To run test file:

`python3 asciilines.py tests/test1.tvg`

The program was built using Python 3.7.3.  Using python 2.7.10 will result in errors at the print statements.  

## License

This program is licensed under the "MIT License".  Please
see the file `LICENSE` in the source distribution of this
software for license terms.
