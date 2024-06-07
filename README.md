# car-destroyer
The car destroyer game is a simple game, it requires two players to play. The objective of the game is for the person who is playing the rock to destroy the car and the person playing the car is to avoid the rock at all times. The car destroyer game has two characters, a rock and a car. The rock uses the keys A, D, and S, A is to move to the left, D is to move the right, and the S key is to move down. The car uses the left and right arrow keys, the left arrow is to move to the left and the right arrow is to move to the right.

Here are some screenshots of the game itself:



<img width="596" alt="Screenshot 2024-06-06 at 10 32 45 PM" src="https://github.com/prudenalaysia/car-destroyer/assets/150814058/769bd725-aef5-49cd-ad08-d0afcb5a0fe2">

<img width="594" alt="Screenshot 2024-06-06 at 10 32 52 PM" src="https://github.com/prudenalaysia/car-destroyer/assets/150814058/7c0ec404-7ca9-43c8-9c4b-818570243d37">

<img width="603" alt="Screenshot 2024-06-06 at 10 32 57 PM" src="https://github.com/prudenalaysia/car-destroyer/assets/150814058/52396243-67b6-4440-a879-63d2fa499101">

<img width="603" alt="Screenshot 2024-06-06 at 10 33 01 PM" src="https://github.com/prudenalaysia/car-destroyer/assets/150814058/d997da56-68ca-4ce5-b462-317c6fa786dd">



All of the graphics I drew myself, however I used the font and audio from a pygame tutorial, where he had uploaded his code onto github where I was able to access the font and audio. I also had inspriation from him and another youtubers video to help me code this project. This is the link to their videos: 
Audio and Font guy - https://www.youtube.com/watch?v=AY9MnQ4x3zk
Other guy that helped with the process of my code - https://www.youtube.com/watch?v=GMBqjxcKogA

Overview of the code - 

Any variables with _surf in it means the surface, any variables with _rect next to it means the rectangle of the object which yuou can manipulate and effect, for example if you wanted the game to end when to objects collided you would use their rects to determine what part would be touching, same goes for when you are using the mouse for buttons.

The code consists of alot of variables and 11 functions. The reset_game function resets the game when the rock and the car collide returning the players back to the main menu. The main_menu function is the main_menu itself, it consits of the buttons used fo the main menu and the input. So when the desert, daytime, or night time button is pushed it will go to those settings where the players can then play the game. The back function is a function used for the back button, the back button is used so that if the player chose the wrong setting that they want to be in they can easily go back to the main menu and choose a setting they'd rather be in. The display_score function displays the score for players to see how long they've been in the game, the longer the car player has survived the higher the score will go up. The rock_animation function is used to animate the rock as its falling or moving. The directiions function is used for when the players press the keys, so if a player presses the S key when plauing the rock, they are going to go down, by going down their y position increases as they continue to press the S key. The same rule applies for the left arrow, right arrow, D key, and the A key, except if you go to the left your x positon will decrease, and if you go to the right your x position will increase. The desert, daytime, and nightime functions are all the same, they have the same outputs, inputs, etc. except they all have different backgrounds. The desert, daytime, and nightime functions is what makes the game the game, it shows the score, the car, the rock, and it shows the back button where the player can travel from setting to menu as much as they want. The run function is so that the game can run, and when it runs it will always go to the main_menu function and when the car and rock collide it will also direct you to the main menu instead of the game shutting down.


