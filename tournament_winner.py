def tournament_winner(competitions, results):
    final_scores = {}
    for index in range(len(results)):
        competition = competitions[index]
        result = results[index]
        winning_team = competition[1] if result == 0 else competition[0]
        if winning_team not in final_scores:
            final_scores[winning_team] = 0
        final_scores[winning_team] += 3

    highest_score = 0
    winner = None
    for team in final_scores:
        if winner is None or final_scores[team] > highest_score:
            winner = team
            highest_score = final_scores[team]

    return winner
