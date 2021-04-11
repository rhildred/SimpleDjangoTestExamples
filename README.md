||||
|---|---|---|
||MB215 Practice Final||
|Name:|||
|Student Number:|||

Please solve 7 of the following 10 problems with complete tests. Each solution is worth 10 marks. 
Create a django project with 1 app in it called `final`. Save all of your .py files to the `final` folder as in [the example final](https://github.com/rhildred/SimpleDjangoTestExamples). You can create a suitable django project by running:

1. `python3 -m django startproject final_exam`
2. open the final_exam folder in vscode
3. `python3 manage.py startapp final`

When your solutions are complete, please upload a .zip of that folder to the quiz tool.

#### 1. Canadian Federal tax is calculated using the following formula:

![Federal tax schedule1](http://res.cloudinary.com/salesucation-com-inc/image/upload/v1508437770/Schedule1.png "Federal tax schedule1")

Write a program that asks the user for their taxable income and displays the result from line 44.

```
Please enter your taxable income> 165000
Your tax on 165000.0 is 36166.479999999996
```

* Note: make sure that you have a test for non-numeric input

#### 2. Volume of a cylinder

Write a program to calculate the volume of a cylinder. The user enters in the diameter of the end of the circle, and the height in meters:

volume = pi * r ** 2 * height 

    Input the radius and height
    Output the radius and height as they were input
    Output the volume of the cylinder

*Note: You will need to test for non-numeric input as a test to fail case

##### Sample Output

```
radius >4
height >4
the volume is 201 cubic meters
```


#### 3. Vowels and Consonants

Write a program with a function that accepts a string as an argument and returns the number of vowels that the string contains. The application should have another function that accepts a string as an argument and returns the number of consonants that the string contains. The application should let the user enter a string and should display the number of vowels and the number of consonants it contains.

##### Sample Output

```
enter a string >The rain is raining over Spain
the string contains 11 vowels
the string contains 14 consonants
```

#### 4. Product Name and Price

Write a program that keeps product names and prices in a dictionary as key-value pairs.
The program should display a menu that lets the user look up a product’s price, add a new product name and price, change an
existing price, and delete an existing product name and price.
Add a method to list all of the product names and prices in the dictionary.

##### Sample Output

```
0 - Exit
1 - Look up
2 - Add
3 - Change
4 - Delete
5 - List
Enter your choice >2
Enter Name >bread
Enter Price >$1.99
{'bread': '$1.99'}
0 - Exit
1 - Look up
2 - Add
3 - Change
4 - Delete
5 - List
```

* Note: You will need to test the delete on a case where the key to be deleted doesn't exist.

#### 5. Cash Register

This exercise assumes that you have created the Item class from lab 7. Create a CashRegister class that can be used with the RetailItem class. The CashRegister class should be able to internally keep a list of RetailItem objects. The class should have the following methods:

* A method named purchase_item that accepts an Item object as an argument.
    Each time the purchase_item method is called, the RetailItem object that is passed as
    an argument should be added to the list.
* A method named get_total that returns the total price of all the Item objects stored in the CashRegister object’s internal list.
* A method named show_items that displays data about the RetailItem objects stored in the CashRegister object’s internal list.
* A method named clear that should clear the CashRegister object’s internal list.
* A method named add that allows the cashier to add a one of a kind item to the cash register
* A method named delete that allows the cashier to delete an item that is out of stock.

Demonstrate the CashRegister class in a program that allows the user to select several items for purchase. When the user is ready to check out, the program should display a list of all the items he or she has selected for purchase, as well as the total price.

##### Sample Output

```
Please Enter an item to purchase. Enter 0 to checkout, C to clear
1) Jacket, - 59.95
2) Designer Jeans - 34.95
3) Shirt - 24.95
a) Add an item
d) Delete an item
please enter an item no >f
Please enter an item number, C or 0
Please Enter an item to purchase. Enter 0 to checkout, C to clear
1) Jacket, - 59.95
2) Designer Jeans - 34.95
3) Shirt - 24.95
a) Add an item
d) Delete an item
please enter an item no >C
Items in Cart
Please Enter an item to purchase. Enter 0 to checkout, C to clear
1) Jacket, - 59.95
2) Designer Jeans - 34.95
3) Shirt - 24.95
a) Add an item
d) Delete an item
please enter an item no >2
Items in Cart
    2) Designer Jeans - 34.95
Please Enter an item to purchase. Enter 0 to checkout, C to clear
1) Jacket, - 59.95
2) Designer Jeans - 34.95
3) Shirt - 24.95
a) Add an item
d) Delete an item
please enter an item no >0
Items in Cart
    2) Designer Jeans - 34.95
total: 34.95
```

#### 6. Average calorie intake

Within a healthy, balanced diet, a man needs around 10,500kJ (2,500kcal) a day to maintain his weight. For a woman, that figure is around 8,400kJ (2,000kcal) a day.

Write a program that prompts the user to input the number of calories for 7 days and then prints the weekly average.

* Note: You will need a test case for a non-numeric value.

##### Sample Output

```
Enter your calories for day 1: 2490
Enter your calories for day 2: 2234
Enter your calories for day 3: 2768
Enter your calories for day 4: 2800
Enter your calories for day 5: 2900
Enter your calories for day 6: 2700
Enter your calories for day 7: 2200
Your average calories for 7 days was 2584.5714285714284
```

#### 7. Vowels, Consonants and word count

Write a program with a function that accepts a string as an argument and returns the number of vowels that the string contains. The application should have another function that accepts a string as an argument and returns the number of consonants that the string contains. A third function that is also required that looks counts the number of words in the sentence.

Hint Look for whitespace and punctuation

The application should let the user enter a string and should display the number of vowels, the number of consonants and the number of words that it contains.

```
enter a string >I am just a poor boy from a poor family. Spare me my life for this one atrocity.
the string contains 24 vowels
the string contains 38 consonants
the string contains 18 words
```

#### 8. Pig Latin

Write a program that accepts a sentence as input and converts each word to “Pig Latin.” In one version, to convert a word to Pig Latin you remove the letters up to the first vowel and place that letter at the end of the word. Then you append the string “ay” to the word. 
Here is an example:

English: I SLEPT MOST OF THE NIGHT

Pig Latin: IAY EPTSLAY OSTMAY OFAY ETHAY IGHTNAY

#### 9. ISO 3166 Country codes

Write a program that uses a dictionary to map 10 country names to their ISO 3166 2 letter code. Use an exception to make sure that if the country name isn't in the dictionary it returns a helpful error message.

* Note: You also need to have a test case for that exception

#### 10. Tossing a block

A child's block has a letter D on one face, the word thank-you on another, a picture of an apple on another, the numeral 6 on another, a car on another and a dog on the 6th face. Write a program that tosses that block and reports the side that is up when the block comes to a rest.

## (Partial) Solutions

The solutions are all in the [the example final](https://github.com/rhildred/SimpleDjangoTestExamples). You can run tests for the solutions by running `python manage.py test`. You can also run the answers to the in your terminal interactively using ctrl-f5 (or command f5 on mac) or in the debugger.