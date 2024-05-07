## Toothpick Pattern Simulation: Python Program
This project involves creating a Python program to visualize the "Toothpick Sequence," a fascinating geometric pattern on a 1000x1000 pixel canvas. The program includes two main Python files: Toothpick.py and Sketch.py, along with a descriptive README to guide users on how to run the program and understand its functionality.

### Project Structure
Toothpick.py - This module defines the Toothpick class, which encapsulates properties and behaviors of a toothpick in the canvas. Each toothpick is either vertical or horizontal and is represented as a line segment. The class includes methods to display the toothpick on the canvas and to calculate potential new toothpicks at each end.
Sketch.py - This script is the main executable for the program. It uses the graphics.py package for drawing the toothpick pattern on the canvas. It reads the number of iterations from the command line, initializes the canvas, and iteratively adds new toothpicks according to the rules of the toothpick sequence. It also prints the number of toothpicks added in each iteration and the cumulative count.
Toothpick Class
Attributes:
Direction (vertical or horizontal)
Location (x, y coordinates)
Length of the toothpick (fixed to 63 pixels)
Methods:
show(): Displays the toothpick on the canvas.
toothpickToAddA(): Returns a new Toothpick at one end if possible.
toothpickToAddB(): Returns a new Toothpick at the other end if possible.
Running the Program
To run the program, navigate to the directory containing Sketch.py and execute:

python3 Sketch.py <number_of_iterations>
Replace <number_of_iterations> with the desired number of iterations to visualize the toothpick pattern development.

### Output
The program outputs the details of toothpick additions for each iteration directly in the console and updates the canvas with the current state of the toothpick sequence.

Requirements
Python 3.x
graphics.py (a simple object-oriented graphics library)
Example Output
Upon running the command python3 Sketch.py 12, you will see output similar to the following in your terminal, along with a graphical window showing the toothpick pattern:


Iteration #0: #Toothpicks added in this iteration: 1, Total #toothpicks: 1
...
Iteration #12: #Toothpicks added in this iteration: 16, Total #toothpicks: 95
### Conclusion
This program provides a visual and interactive way to explore the mathematical properties of the toothpick sequence. It serves as an excellent educational tool for those interested in geometric patterns and sequences in mathematics.

