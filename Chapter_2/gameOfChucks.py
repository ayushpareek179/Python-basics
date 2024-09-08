# Game of chucks

import random

# set base conditions for the game


def baseConditions():
    while True:
        userInpOvs = input("Enter a whole number for setting overs: ")
        if not userInpOvs.isdigit():  # is true only when string is positive
            print("Enter a positive number")
            continue
        userInpOvs = int(userInpOvs)
        break
    while True:
        userInpMaxRuns = input(
            "Enter the maximum possible runs in one shot (6 or 10): "
        )
        if not userInpMaxRuns.isdigit() or userInpMaxRuns not in ("6", "10"):
            print("Enter 6 or 10")
            continue
        userInpMaxRuns = int(userInpMaxRuns)
        break
    return (userInpOvs, userInpMaxRuns)


def baseConditionsHelper():
    global OVERS, VALID_SHOTS
    returnedTuple = (2, 6)
    if (
        input(
            "Press [Y] to define baseline conditions for the game (for advanced users only): "
        )
        == "Y"
    ):
        returnedTuple = baseConditions()
    OVERS = returnedTuple[0]
    VALID_SHOTS = list(map(str, list(range(1, returnedTuple[1] + 1))))


# display rules


def rulebook():
    if input("Press [H] to read rules: ") == "H":
        print(RULES)
    else:
        print("Experienced chap huh ;)")


# get game order


def toss():
    while True:
        player_call = input("Enter [H] for heads and [T] for tails: ")
        if player_call not in ["H", "T"]:
            print("Please enter a valid choice")
            continue
        toss = "H" if random.randint(1, 2) == 1 else "T"
        while player_call == toss:
            player_choice = input(
                "You have won the toss! Press [1] to bat and [0] to bowl: "
            )
            if player_choice not in ["0", "1"]:
                print("Please enter a valid choice")
                continue
            player_choice = int(player_choice)
            break
        else:
            print("You have lost the toss, the computer will take the call now")
            player_choice = random.randint(0, 1)
        break
    return player_choice


# function for user batting against computer


def playerBat(toss, target):

    print("Get ready to bat\n")
    print(
        "==================================================================================================="
    )

    balls = 6 * OVERS
    wickets = OVERS
    score = 0

    if toss == 0:
        print("Your target: " + str(target))

    while balls * wickets > 0:

        balls_left = (
            str((6 * OVERS - balls + 1) // 6) + "." + str((6 * OVERS - balls + 1) % 6)
        )

        while True:
            player_resp = input("Enter your run guess: ")
            if player_resp not in VALID_SHOTS:
                print(
                    "Invalid input, retry with a no. between 1 and %s" % VALID_SHOTS[-1]
                )
                continue
            player_resp = int(player_resp)
            break

        computer_resp = random.randint(1, int(VALID_SHOTS[-1]))

        print(
            "%s: You responded with [%s], Computer responded with [%s]"
            % (balls_left, player_resp, computer_resp)
        )

        # Condition for dismissal
        if player_resp == computer_resp:
            print("You lost a wicket!")
            wickets = wickets - 1
        else:
            score = score + player_resp

        balls = balls - 1

        # if player is batting second and has exceeded the target
        if toss == 0 and score > target:
            break

        # Over break prompted
        if balls != OVERS and balls % 6 == 0:
            print("")
            if balls == 6:
                print("1.0 over completed")
            else:
                print("%s overs completed" % (float(OVERS - balls / 6)))
            print("%s-%s in %s overs" % (score, OVERS - wickets, balls_left))
            if toss == 0:
                print("Runs needed for you to win: " + str(target - score))
            print("")

    print("Your final score: %s for loss of %s wickets\n" % (score, OVERS - wickets))
    print(
        "===================================================================================================\n"
    )

    return score


# function for computer batting against user


def computerBat(toss, target):

    print("Get ready to bowl\n")
    print(
        "==================================================================================================="
    )

    balls = 6 * OVERS
    wickets = OVERS
    score = 0

    if toss == 1:
        print("You have set the computer a target of %s runs" % target)

    while balls * wickets > 0:

        balls_left = (
            str((6 * OVERS - balls + 1) // 6) + "." + str((6 * OVERS - balls + 1) % 6)
        )

        computer_resp = random.randint(1, int(VALID_SHOTS[-1]))

        while True:
            player_resp = input("Enter your guess for computer's run: ")
            if player_resp not in VALID_SHOTS:
                print(
                    "Invalid input, retry with a no. between 1 and %s" % VALID_SHOTS[-1]
                )
                continue
            player_resp = int(player_resp)
            break

        print(
            "%s: Computer responded with [%s], You responded with [%s]"
            % (balls_left, computer_resp, player_resp)
        )

        # Condition for dismissal
        if player_resp == computer_resp:
            print("You won a wicket!")
            wickets = wickets - 1
        else:
            score = score + computer_resp

        balls = balls - 1

        # if computer is batting second and has exceeded the target
        if toss == 1 and score > target:
            break

        # Over break prompted
        if balls != OVERS and balls % 6 == 0:
            print("")
            if balls == 6:
                print("1.0 over completed")
            else:
                print("%s overs completed" % (float(OVERS - balls / 6)))
            print("%s-%s in %s overs" % (score, OVERS - wickets, balls_left))
            if toss == 1:
                print("Runs needed for the computer to win: " + str(target - score))
            print("")

    print(
        "Computer's final score: %s for loss of %s wickets\n" % (score, OVERS - wickets)
    )
    print(
        "===================================================================================================\n"
    )

    return score


# Main Code Section


def gameFunc():

    global RULES
    target = 0

    print("Welcome to the Game of Chucks!")
    print(
        "==================================================================================================="
    )
    baseConditionsHelper()

    RULES = """\nChucks is modeled after Cricket, albeit with many liberties

Player gets a turn to choose to bat and bowl, depending on whether they had called the toss correctly
* The 'Batter' guesses a number between 1 and %s
* If the 'Bowler' matches the guess, the Batter loses a wicket (total wickets - %s)
* Otherwise, the guess gets added to their runs scored

The Batter tries to maximize the runs scored while not losing wickets
* The Batter gets %s overs (%s chances - 1 Over = 6 Chances) to score
* If the Batter loses all their wickets, the innings ends prematurely

The roles are then reversed and the erstwhile Bowler now tries to score at least '1' more than the Batter's score

The player scoring the most runs 'Wins', the other player 'Loses'; if the scores are exactly equal, it's a 'Tie'
""" % (
        int(VALID_SHOTS[-1]),
        OVERS,
        OVERS,
        6 * OVERS,
    )

    rulebook()
    print(
        "===================================================================================================\n"
    )
    print("Let the ultimate showdon begin!\n")
    tossResult = toss()
    print(
        "\n===================================================================================================\n"
    )

    if tossResult == 1:
        playerScore = playerBat(tossResult, target)
        target = playerScore + 1
        computerScore = computerBat(tossResult, target)
    else:
        computerScore = computerBat(tossResult, target)
        target = computerScore + 1
        playerScore = playerBat(tossResult, target)

    if playerScore > computerScore:
        officialResult = "WIN"
        if tossResult == 0:
            print("Congratulations! You have successfully chased the target!")
        else:
            print("Congratulations! You have successfully defended your score!")
    elif playerScore == computerScore:
        officialResult = "TIE"
        print(
            "Wow, this was such a close match that neither the player nor the computer lost!"
        )
    else:
        officialResult = "LOSS"
        if tossResult == 0:
            print("Hard luck! The target was too high for you!")
        else:
            print("Hard luck! Your score could not stand against computer's blitz!")

    print(
        "\n===================================================================================================\n"
    )
    print("Final result: " + officialResult + "\n")
    print("Thanks for playing!")
    print(
        "\n===================================================================================================\n"
    )
    print("©ayushpareek179 2099")


# Calling the game

gameFunc()
