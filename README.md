# health-analytics
This is for an assignment that serves as  a primer for HHA 504 / 507.

## Variables
I created three different variables with assigned values. The first is a number value, which I called number_value. I assigned 10 to it, which is also an integer. Next, I made a string variable called string_variable. Strings need to be contained in quotes, so I assigned "string" to it. Next I created a list. Lists use the [] brackets, and can contain a string, number, variable or other lists. I then created a dictionary that would contain 3 key:value pairs, while also containing another list and a then a nested dictionary. The family members were the list within the dictionary. Then, I created a nested dictionary, meaning a dictionary within a dictionary. I called this nested dictionary health, which contained the variables for weight, height, and blood pressure. 

## Function
The function I created is a simple calculator for if a party needs to pay a gratuity fee based on number of people that sat in a restaurant. There seems to be a mandatory gratuity fee if the party has 4 guests or greater. If the amount of guests is 4 or greater, there is a 20% gratuity fee. If the guest number is less than 4, then there is not a gratuity fee. My function has two inputs: people, and bill. It will take the bill and multiply it by the gratuity and add it to the bill again, calculating the total cost. 

## Output expectations
The expected outcome for inputting 4 as the people, and the bill to be 100 will be 120. Since 4 is greater than or equal to 4, the bill will be multiplied by 0.20, and then added to the bill again. This will result the total cost to be 120. 

The expected outcome for inputting 3 as the people, and the bill to be 50 will be 50. Since 3 is less than 4, the bill will be multipled by 0, and then added to the bill again. This will result the total cost to be 50. 