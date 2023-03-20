import Side

Bags = [10,10,10]
username = Side.BeginGame()

while True:
    Bags,LastTurn = Side.HumanTurn(username,Bags)
    GameState = Side.CheckGameState(Bags)
    if(GameState==False):
        Side.EndGame(LastTurn,username)
        break
    Side.ShowBags(Bags)
    Bags,LastTurn = Side.DiceTurn(Bags)
    Side.ShowBags(Bags)
    GameState = Side.CheckGameState(Bags)
    if(GameState==False):
        Side.EndGame(LastTurn,username)
        break