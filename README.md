# FridgeBuddy
## 11.16.2020

## Overview
  This project is called FridgeBuddy[name subject to change]. This is for persons who own or share a fridge and want to keep track of what they have.
  
  This app is meant to help them keep track of what food products they have in their fridge and pantry. Additionally, it hopes to help reduce waste as an accurate record will reduce excess and ensure usage of all foods. 
  
  For a single user, the app allows them to keep a record of all items in their fridge and pantry. For shared households, a joint fridge will allow all members to update the record of items available in their shared fridge and pantry. A shopping list app will allow users to add and remove items accordingly. Recipe search and suggestions will also be available.

## Goals
  1. Users will be able to register or log in and log out. (P0)
  
  2. Users will be able to join or create a “Fridge”. (P0)
  
  3. Users will be able to add and remove items and quantities from their assigned fridge. (P0)
  
  4. Users will be able to create and edit Shopping Lists. (P1)
  
  5. Users will be able to create and update meal plans. (P1)
  
  6. (API) Users will be able to search recipes and suggestions. (P2)
  
  7. (API) Users will be able to search for ingredients to add to their Fridge and Shopping List. (P2)
  
  8. Message system between members of a fridge (P2.5)
  
  9. Cross integration between sections of the app. (P3)
  
     - Add items running low to the Shopping List.
  
     - Add bought items to Fridge.
  
     - Add items in the recipe to the Shopping List.
  
     - Search for recipes on the Meal Plan page, or pressing the (+) will redirect to the search page, and will redirect back after selection.
  
  10. Mobile version. Not just “mobile-friendly” (P3)

## Specifications
  The bulk of this project will be built in Python and Django. The reason for this selection is for ease of use, flexibility and familiarity. As it is technically a full stack project, Python/Django make the most sense.
  
  Presently, the front-end framework most likely to be SemanticUI, as it has flexibility and is more app focused. However, Bootstrap is also a strong contender due to ease of use and familiarity
  
  For the database, MySQL will be used. This is mainly due to the fact that much of this app truly relies on a table like structure as it is, and therefore would translate well to and from MySQL. MongoDB was looked at as an option, and remains on the table, but at the present is on the backburner
  
  The main API that will be used is spoonacular, a nutrition, recipe, and food API. The reason such an API will be used is that this app revolves entirely around food. Additionally, the API gives access to over 365, 000 recipes and 86, 000 food products which will help with ease of use.
  
  If we decide to host, we will most likely use AWS-EC2, mainly because it has more support and documentation at the moment.

## Related Links
  Python: https://www.python.org/
  
  Django: https://www.djangoproject.com/
  
  SemanticUI: https://semantic-ui.com/
  
  Bootstrap: https://getbootstrap.com/
  
  MySQL: https://www.mysql.com/
  
  MongoDB: https://www.mongodb.com/
  
  Spoonacular: https://spoonacular.com/food-api
  
  AWS: https://aws.amazon.com/

## Interactive Wireframe: 
  https://xd.adobe.com/view/554c3a37-643b-49a4-ac15-2ed6bb39fce9-001f/


## Sample Photos:
  ![Welcome](./READMEPics/Welcome.png "Welcome Page")
