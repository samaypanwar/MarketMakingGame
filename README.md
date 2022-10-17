### Instructions to Play the Game

* Get a deck of 52 shuffled cards
* When game init, give the player 1000$ and tell the rules of the game
* Ask player their confidence interval with a spread of 4 and their confidence level
* For each round in the game:
    * Draw 'n' number of cards &rarr; keep the true sum
    * Uniformly distribute a guess from 1 &rarr; max gain as a sell or buy transaction
    * With a certain probability p, carry out the proposed transaction if the user approves
    * then ask them their order size, their max loss and gain and expected gain
    * Finally reveal the true value of the transaction and ask the user to compute their pnl
    * compare the different values and tell the user if they are correct or not
    * ask if want to play another round