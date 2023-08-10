def tournament_winner(competitions, results):
    # Initiate an empty dictionary for the final scores
    # Loop through competitions and populate the final scores dictionary
    # Loop through the dictionary to pick out the tournament winner
    final_scores = {}
    for index in range(len(results)):
        competition = competitions[index]
        result = results[index]
        winning_team = competition[1] if result == 0 else competition[0]
        if winning_team not in final_scores:
            final_scores[winning_team] = 0
        final_scores[winning_team] += 3
    pass
