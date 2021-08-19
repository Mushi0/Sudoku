# Sudoku

Integer programming models for solving and generating Sudoku puzzles

----------------------

## Solving Sudoku Puzzles

### Sudoku_IP.mos

The basic integer programming model S1 for solving Sudoku puzzles. 

### Sudoku_IP_rc.mos

The model improved by removing redundant constraints. 

### Sudoku_IP_rv.mos

The model improved by removing redundant variables and corresponding constraints. 

### Sudoku_IP_rc_rv.mos

The model improved by removing both redundant constraints and variables. 

-----------------------

## Generating Sudoku Puzzles

### Generator_pattern.mos

Generate different Sudoku patterns for 9x9 and 16x16 Sudoku. 

### Generator_pattern_2.mos

Another approach for generating different 9x9 Sudoku patterns. 

### Generator_obj.mos

Model used to choose the best objective function for 25x25 Sudoku. 

### Generator_grids_25.mos

Generate Sudoku grids for 25x25 Sudoku. 

### Generator.mos

Randomly remove values from cells and create Sudoku puzzles. 

### Pattern_25x25.mos

Check how many different patterns do the grids generated have. 

-----------------------

## Uniqueness Checking

### Sudoku_IP_UniqCheck.mos

Check whether a puzzle is uniquely solvable. 

------------------------

## Utile Python Scripts

### Counting.py

Count the average number of clues. 

### Minimum17.py

Collect 17-clue Sudoku puzzles from the website. 

### Minimum17_to_excel.py

Transform the 17-clue puzzles to excel for people to solve.  
