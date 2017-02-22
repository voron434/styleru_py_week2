# styleru_py_week2
This is result of my work with SuperJob api:  
All of these scripts requires Python 3.x.  
Also there is full Eng interface.  
***
# 1. hello_api_superjob #
#### This is the first task, 
I made program wich searchers for programmers from Moscow and downloads 100 results of search into .json file. 
You need to enter your api_key, wich you could get [here](https://api.superjob.ru/) after registration of your own app.  
#### example of code process:    
  *python hello_api_superjob.py*  
  ***Enter your api key :***  
  *64be4144d51bbaee6234f2w82bb*    
  ***Process finished with exit code 0***  
  > Remember, that you must delete this in couple of days, because TMDB don't allow to save their data      
  
***
# 2. vacancies_treatment #
#### Second task,  
For this program need path to json file from 1 task.  
Program copy only usefull information about downlowaded vacancies  
#### example of code process:  
  *python vacancies_treatment.py*  
  ***Enter path to DataBase::***  
  *vacancies.json*   
  ***Process finished with exit code 0***  
  
***
# 3. vacancies_explore #
#### Third task,
For this program need path to json file from 2 task.
Program count needless of every languge for downloaded vacancions and averege earnings for each of them.  
Also it draws bar chart with this statistics.
#### example of code process:  
  *python vacancies_explore.py*  
  ***Enter path to DataBase:***  
  *simple_vacancies.json*  
  **bar chart**  
  ***Process finished with exit code 0***    
