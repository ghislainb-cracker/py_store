# ==============================
# IMPORT REQUIRED LIBRARIES
# ==============================


# Import NBA API endpoint that provides
# today's NBA scoreboard information
#
# This library handles communication with
# NBA servers and returns structured data
from nba_api.stats.endpoints import scoreboardv3



# Import datetime because we can use it
# to automatically get today's date
from datetime import datetime





# ==============================
# SCOREBOARD FETCHING FUNCTION
# ==============================

# Function responsible for:
#
# 1. Getting NBA games for a specific date
# 2. Extracting game information
# 3. Displaying results
def get_scoreboard():



    # Get today's date dynamically
    #
    # The format required by NBA API:
    # MM/DD/YYYY
    #
    # Example:
    # 01/15/2026
    #
    # Current code uses a fixed date for testing
    #
    # Replace this with:
    #
    # today = datetime.today().strftime("%m/%d/%Y")
    #
    # when building a live version
    today = "01/15/2026"





    # Send a request to the NBA API
    #
    # The API returns scoreboard information
    # for all games played on this date
    scoreboard = scoreboardv3.ScoreboardV3(
        game_date=today
    )



    # Convert the API response into a Python dictionary
    #
    # The returned data is similar to JSON:
    #
    # {
    #    "scoreboard": {
    #          "games": [...]
    #    }
    # }
    data = scoreboard.get_dict()





    # Navigate through the nested dictionary
    # to access the list of games
    #
    # Extract:
    #
    # scoreboard
    #       ↓
    # games
    games = data["scoreboard"]["games"]





    # Check whether any games exist
    #
    # Some dates have no NBA games scheduled
    if not games:

        print(
            "No games today."
        )

        return





    # ==============================
    # DISPLAY GAME INFORMATION
    # ==============================


    # Loop through every game returned by the API
    #
    # Example:
    #
    # Game 1:
    # Lakers vs Warriors
    #
    # Game 2:
    # Celtics vs Heat
    for game in games:



        # Extract home team information
        #
        # Contains:
        # - team name
        # - abbreviation
        # - score
        home = game["homeTeam"]



        # Extract away team information
        away = game["awayTeam"]





        # Create visual separation between games
        print(
            "-------------------------------"
        )



        # Display matchup information
        #
        # Example:
        #
        # Lakers (LAL)
        # vs
        # Warriors (GSW)
        print(
            f"{away['teamName']} "
            f"({away['teamTricode']}) "
            f"vs "
            f"{home['teamName']} "
            f"({home['teamTricode']})"
        )



        # Display current score
        #
        # Away team score comes first
        # Home team score comes second
        print(
            f"Score: "
            f"{away['score']} - {home['score']}"
        )



        # Display current game status
        #
        # Examples:
        #
        # "Final"
        # "Q3 05:32"
        # "Scheduled"
        print(
            f"Status: {game['gameStatusText']}"
        )





# ==============================
# PROGRAM ENTRY POINT
# ==============================


# Execute the scoreboard function
get_scoreboard()