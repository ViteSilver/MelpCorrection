# MelpCorrection
Improve the melp App

Test_back_end

Implement CRUD using Django and REST Framework with function views and decorators.

The Heroku link to review the API, this endpoint show all the elements and post new ones in a JSON format:

https://melpback.herokuapp.com/restaurant/

In this API implement a CRUD we have the following endpoints:

 https://melpback.herokuapp.com/restaurant/detail/id-value
 
 Example:
 
 https://melpback.herokuapp.com/restaurant/detail/851f799f-0852-439e-b9b2-df92c43e7672/

Endpoint to the second task, in this case only obtain the count, standar deviation and mean of the rating of all the restaurants in the area for the given data:
latitude, latitude coordinate
longitude, longitude coordinate
radius, the radius inside that we check the restaurants

https://melpback.herokuapp.com/restaurants/statistics?latitude=x&longitude=y&radius=z

Example: 

https://melptask.herokuapp.com/restaurant/statistics?latitude=19.44005705&longitude=-99.1270471&radius=1
