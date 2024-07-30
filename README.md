## Area Calculator 📐

This Python script is a simple command-line tool for calculating the area of various geometric shapes. The user is presented with a menu to choose the type of shape they want to calculate the area for. 

### Features:
- **Triangle**: Calculates the area using the formula \( \text{Area} = \frac{1}{2} \times \text{base} \times \text{height} \).
- **Rectangle**: Calculates the area using the formula \( \text{Area} = \text{length} \times \text{width} \).
- **Square**: Calculates the area using the formula \( \text{Area} = \text{side}^2 \).
- **Circle**: Calculates the area using the formula \( \text{Area} = \pi \times \text{radius}^2 \), where \( \pi \) is approximated as 3.14.
- **Quit**: Exits the program.

### How to Use:
1. Run the script.
2. Select the shape type by entering the corresponding number:
   - 1 for Triangle
   - 2 for Rectangle
   - 3 for Square
   - 4 for Circle
   - 5 to Quit
3. Follow the prompts to enter the required dimensions.
4. The program will display the calculated area or exit based on your selection.

### Example:
```
================== 
 Area Calculator 📐 
 ================== 
 1) Triangle 
 2) Rectangle 
 3) Square 
 4) Circle 
 5) Quit
```
If the user selects option `1` and inputs `10` for the side, the script will compute and display:
```
Area is 100
```

If an invalid option is entered, the script will notify the user with "Sorry wrong input!"

### Notes:
- Ensure to input positive integer values for dimensions.
- The circle area calculation uses a simplified value for π (3.14).

Feel free to modify and expand the code to suit additional needs or improve accuracy, especially for the circle area calculation.
