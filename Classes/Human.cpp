#include<iostream>
#include<bits/stdc++.h>
#include<Food.cpp>

using namespace std;

class Ayum{
    int health = 20;
    int age = 1;
    int sleep = 10;
    int hunger = 10;

    string eat(food food_item){
        this -> hunger += food_item.nutrition_value / 10;
        return "Ayum ate " + food_item.name + " " + "and Ayum's hunger level is " + to_string(this -> hunger) + " now. Thanks!";
    }
    
};