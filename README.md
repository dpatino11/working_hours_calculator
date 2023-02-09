# working_hours_calculator

![Tests](https://github.com/dpatino11/working_hours_calculator/actions/workflows/pytest.yaml/badge.svg)

# Working hours calculator

This is a working repository for the solution of the programming problem for the company ACME, this solution is written in Python and it takes an input file and calculates the payment, then returns a file with the details and prints the full payments in terminal


## Exercise 
Exercise

The company ACME offers their employees the flexibility to work the hours they want. They will pay for the hours worked based on the day of the week and time of day, according to the following table:

Monday - Friday

00:01 - 09:00 25 USD

09:01 - 18:00 15 USD

18:01 - 00:00 20 USD

Saturday and Sunday

00:01 - 09:00 30 USD

09:01 - 18:00 20 USD

18:01 - 00:00 25 USD

The goal of this exercise is to calculate the total that the company has to pay an employee, based on the hours they worked and the times during which they worked. The following abbreviations will be used for entering data:

MO: Monday

TU: Tuesday

WE: Wednesday

TH: Thursday

FR: Friday

SA: Saturday

SU: Sunday

Input: the name of an employee and the schedule they worked, indicating the time and hours. This should be a .txt file with at least five sets of data. You can include the data from our two examples below.

Output: indicate how much the employee has to be paid

For example:

Case 1:

INPUT

RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00

OUTPUT:

The amount to pay RENE is: 215 USD

Case 2:

INPUT

ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00

OUTPUT:

The amount to pay ASTRID is: 85 USD

Once you have finished the exercise, please upload the solution to GitHub and send us the link. Don’t forget to include a README.md file. Your README should include an overview of your solution, an explanation of your architecture, an explanation of your approach and methodology and instructions on how to run the program locally.


## Getting Started

The solution to this problem was solved in Python 3.9 and used an additional python library for the creation of the unit test

### Requirements
- Python 3.9
- Pytest, use the package manager [pip](https://pip.pypa.io/en/stable/) to install pytest

```bash
pip install pytest
```
## APP Configuration
The app configuration and the inputs for the calculations are in the configuration class, if a change in the input parameters make sure to change the dictionary in the class.
## Usage
### Main script run
for running the program open the project directory and run the following command
```bash
python src <input>
```
- make sure that the input file for the code is in the input root folder

### test run

for running the program open the project directory and run the following command
```bash
pytest
```
## Response
The details for the calculation of the payments are created in the output root folder, also the payments for each person on the input are displayed on the terminal


