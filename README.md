# styleru_py_week2
This is result of my work with SuperJob api:  
All of these scripts requires Python 3.x. and modules from requirements.txt   
Also there is full Eng interface.  
***
# 1. hello_api_superjob #
#### This is the first task, 
I made program wich search for programmers from Moscow and downloads 100 results of search into json file. 
You need to enter your api_key, wich you could get [here](https://api.superjob.ru/) after registration of your own app.  
#### example usage:    
    $python hello_api_superjob.py  
    Enter your api key :  
    3t543t34be4144d51bbaee6234f2w82bb    
    vacancies saved into vacancies.json 
  > Remember, that you must delete this data in couple of days, because superjob don't allow to save their data      
  
***
# 2. vacancies_treatment #
#### Second task,  
This program need path to json file from 1 task.  
Program copy only usefull information about downlowaded vacancies and put it into a new json file.
#### example usage:  
    $python vacancies_treatment.py  
    Enter path to DataBase:  
    vacancies.json
    vacancies saved into simple_vacancies.json
  
***
# 3. vacancies_explore #
#### Third task,
This program need path to json file from 2 task.  
Program count popularity of every languge for downloaded vacancions and averege earnings for each of them.  
Also it draws bar chart with this statistics and saves it in .png format.
#### example usage:  
    $python vacancies_explore.py  
    Enter path to DataBase:  
    simple_vacancies.json  
    here would be a bar chart  
    stats saved into statistics.png   
