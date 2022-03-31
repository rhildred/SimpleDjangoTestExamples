||||
|---|---|---|
||MB215 Practice Final||
|Name:|||
|Student Number:|||

Please solve 4 of the following 7 problems with complete tests. Each solution is worth 10 marks. 
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


#### 4. Average marks

Write a program that prompts the user to input their mark on 7 labs, stores it in an array and calls a function to calculate the lab average. Your test harness can print the resulting average.

* Note: You will need a test case for a non-numeric value.

##### Sample Output

```
Enter your mark for lab 1: 7
Enter your mark for lab 2: 8
Enter your mark for lab 3: 8
Enter your mark for lab 4: 9
Enter your mark for lab 5: 8
Enter your mark for lab 6: 8
Enter your mark for lab 7: 9
Your average mark for 7 labs was 8.14
```

#### 5. Vowels, Consonants and word count

Write a program with a function that accepts a string as an argument and returns the number of vowels that the string contains. The application should have another function that accepts a string as an argument and returns the number of consonants that the string contains. A third function that is also required that looks counts the number of words in the sentence.

Hint Look for whitespace and punctuation

The application should let the user enter a string and should display the number of vowels, the number of consonants and the number of words that it contains.

```
enter a string >I am just a poor boy from a poor family. Spare me my life for this one atrocity.
the string contains 24 vowels
the string contains 38 consonants
the string contains 18 words
```

#### 6. Pig Latin

Write a program that accepts a sentence as input and converts each word to “Pig Latin.” In one version, to convert a word to Pig Latin you remove the letters up to the first vowel and place that letter at the end of the word. Then you append the string “ay” to the word. 
Here is an example:

English: I SLEPT MOST OF THE NIGHT

Pig Latin: IAY EPTSLAY OSTMAY OFAY ETHAY IGHTNAY

#### 7. ISO 3166 Country codes

Write a program that uses a dictionary to map 10 country names to their ISO 3166 2 letter code. Use an exception to make sure that if the country name isn't in the dictionary it returns a helpful error message.

* Note: You also need to have a test case for that exception

## (Partial) Solutions

The solutions are all in the [the example final](https://github.com/rhildred/SimpleDjangoTestExamples). You can run tests for the solutions by running `python manage.py test`. You can also run the answers to the in your terminal interactively using ctrl-f5 (or command f5 on mac) or in the debugger.
