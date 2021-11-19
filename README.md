## _Smart Elevators, Offline algorithm_

- Created by : Michael Agarkov and Goel Didi

## Literature Research

- https://www.geeksforgeeks.org/smart-elevator-pro-geek-cup/
- https://www.youtube.com/watch?v=siqiJAJWUVg&ab_channel=ThinkSoftware
- https://www.bjmc.lu.lv/fileadmin/user_upload/lu_portal/projekti/bjmc/Contents/8_4_12_Robal.pdf

## Off-line Algorithm formulation
We will define this algorithm for a general number of elevators when we already have all the calls in advance(source, destination and time of the call) and the starting place of all the elevators, we will go over all the possibilities of assigning an elevator to a call by calculating the time it will take for each elevator to get to the source call and then to its destination, finally returning the minimum time it will take for an elevator to perform the whole operation.

# UML
![image](https://user-images.githubusercontent.com/88629415/142693208-a8c9ac7b-b1fd-4801-95a7-f44ba8cca8d8.png)

# run locally

Open cmd in your folder - you can do it by click on the folder path on the top window and type cmd.
Type Ex1.py 'json building path' "csv calls path' 'csv output path'. Example: Ex1.py .\Ex1_Buildings\B5.json .\Ex1_Calls\Calls_a.csv out.csv .
You can see the file has been created and changed column F in the excel. (Elevator column).


![image](https://user-images.githubusercontent.com/88629415/142696903-9a59ce54-4eb5-4651-b341-807ecc614d96.png)
