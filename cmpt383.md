#Author: Wei Yao
#301256560
#yaoweiy@sfu.ca
CMPT383 Fall 2020 Term Project
1) Idea/Goal :  
My grandfater once complained me about he can't view the Chinese TV weather broadcast now in Vancouver, So I decided to build a mini web app for him to view the weather of a list of cities where he attended the War between Japan and China in 1940's.

2) 
System language:  Go
Script language: Python Bash
#Python implemented the mian App features
#Go provides the struct of CityWeather, and the fetchWeather function to support the REST connector that python can call. Also, it control the calling of Bash's command and gathering the result from execution of Bash.
#Bash takes care of url requesting and adopting weather info from API.

3) Cross-lang Communication:
   a) Go creates a REST server and makes a request from python
   
   b) Run the Bash as an exec can capture the output back to Go

4) Instructions to run:
Enviornmnet: macOs Catalina Version 10.15.7  Docker version 19.03.13
Before you run the following commands make sure you are currently inside the dir of polygoltgigas
$ cd 18888-python
$ make image                       
$ cd ..
$ cd 18888-go
$ make image
$ cd ..
$ docker-compose up
Open the chrome and go to localhost:5000/index
The response speed is slow, it takes 4-5s to load the info from REST API :(

5) Features 
1. You can search a city's weather by entering the name of it and click the [Get Weather] button
2. You can click the Popular Cities to view a table showing all weather info of those cities where my grandfather went for the War
3. You can also view them sorted by Asc or Desc
4. The search bar in subpage is not working till this point
5. You can choose how many entries to show (10,25,50 or 100) when there are many rows.
6. The Previous and Next  buttons can work when put more than 10 cities into the popular city list in code.

Future Work
1. Fix bugs  of search in the sub-page
2. Imporve UI
3. Cut down the response time of actions
4. Add more useful features

