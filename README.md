# Simple Bank Management System

## 1. Project Overview

This is a simple Python program for doing basic bank operations.

The program asks the user to enter a PIN. After successful login, the user can check their balance, deposit money, withdraw money, view transaction history, and check the number of transactions.

The starting balance is 5000.

## 2. Features

* PIN login
* Check balance
* Deposit money
* Withdraw money
* View transaction history
* View total transaction count
* Exit the program
* Checks for invalid amounts
* Checks for insufficient balance

## 3. Technologies and Tools Used

* Programming Language: Python
* Editor: Jupyter

### Python Concepts Used

* Variables
* if-elif-else
* while loop
* Lists
* input() and print()
* append()
* len()
* break
* Type conversion using int() and float()

## 4. Installation and Running

Open the Python file and run it.

The program will ask for a PIN.

Enter your PIN: 1234

The correct PIN used in this program is 1234.

## 5. Testing Instructions

The following tests can be performed to check the program.

### Test 1: Correct PIN

Enter:
1234

Expected result:
Login successful

### Test 2: Wrong PIN

Enter an incorrect PIN.

Expected result:
Wrong PIN

### Test 3: Deposit Money

Select option 2 and enter a positive amount.
Expected result:
Money deposited successfully

The balance should increase.

### Test 4: Withdraw Money

Select option 3 and enter an amount less than or equal to the balance.

Expected result:
Money withdrawn successfully

The balance should decrease.

### Test 5: Insufficient Balance

Try to withdraw more money than the current balance.

Expected result:
Invalid amount or insufficient balance

### Test 6: Transaction History

Select option 4.
Expected result:
The program displays the deposits and withdrawals made during the current run.

### Test 7: Transaction Count

Select option 5.
Expected result:
The program displays the total number of successful deposits and withdrawals.

## 6. Author
**Chaitanya Raghuvanshi**
