## TURTLE RACE GAME
Two turtles race to the finish line. 
Players can press a key to make their turtle move forward, and the first to reach the finish line wins!

### Features
✅ Two-player game using keyboard controls
✅ Randomized speed for some excitement
✅ Display winner message when a turtle reaches the finish line

### Enhancements
🔹 Countdown Timer (3-2-1-GO! 🎬)
🔹 Speed Boost Power-Up (Golden Circle) ⚡
🔹 Animated Winner Celebration (Flashing Turtle) 🎆
🔹 Game Closes After Win 🏁

### Advanced features
✅ Obstacle Turtles 🐢 (Slow down the players)
✅ More Power-Ups (Super Boost, Teleport!)
✅ AI Opponent (A bot turtle that moves automatically)
✅ Lap-based Racing (Multiple laps before winning)
### Pseudo Code
START GAME

1. SET UP SCREEN
   - Create a game window with a title "Turtle Race Game"
   - Set the background color to light green

2. DRAW RACE TRACK
   - Draw a rectangular track using lines
   - Draw a finish line at the end of the track

3. CREATE TURTLE PLAYERS
   - Create Player 1 (Blue Turtle) and position it at the starting line
   - Create Player 2 (Red Turtle) and position it at the starting line

4. CREATE POWER-UP (Speed Boost)
   - Place a power-up (golden circle) at a random position on the track

5. SHOW COUNTDOWN BEFORE RACE STARTS
   - Display "3", wait 1 second
   - Display "2", wait 1 second
   - Display "1", wait 1 second
   - Display "GO!", wait 0.5 seconds
   - Clear the countdown message

6. DEFINE PLAYER MOVEMENT
   - When Player 1 presses "W", move Player 1 forward by a random small distance
   - When Player 2 presses "O", move Player 2 forward by a random small distance

7. CHECK FOR POWER-UP
   - If a player touches the power-up, move that player forward by an extra boost
   - Remove the power-up after it has been collected

8. CHECK FOR WINNER
   - If any player's x-position reaches or crosses the finish line:
     - Display "{Player Color} Turtle Wins!"
     - Run a celebration animation (turtle blinks between colors)
     - End the game

9. WAIT FOR PLAYER INPUT (Loop Until a Winner is Found)
   - Listen for key presses to move the turtles
   - Repeat until one turtle wins

END GAME
