players_red_cards = input().split()
team_A = 11
team_B = 11

terminated = False
for el in players_red_cards:
    if el[0] == "A":
        team_A -=1
    else:
        team_B -=1

    if team_A < 7 or team_B < 7:
        terminated = True
        print(f"Team A - {team_A}; Team B - {team_B}")
        print("Game was terminated")
        break

if not terminated:
    print(f"Team A - {team_A}; Team B - {team_B}")