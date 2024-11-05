from espn_api.football import League, helper


def create_team_overrides(league):
    team_map = {}
    for team in league.teams:
        team_map[team.team_id] = team

    week_1_data = {
        # Kev
        1: {
            "team": team_map[1],
            "wins": 1,
            "losses": 0,
            "ties": 0,
            "outcome": "W",
            "pf": 108.48,
            "pa": 74.76,
        },
        # Addy
        2: {
            "team": team_map[2],
            "wins": 0,
            "losses": 1,
            "ties": 0,
            "outcome": "L",
            "pf": 88.12,
            "pa": 126.32,
        },
        # Bran
        3: {
            "team": team_map[3],
            "wins": 1,
            "losses": 0,
            "ties": 0,
            "outcome": "W",
            "pf": 126.32,
            "pa": 88.12,
        },
        # KZ
        4: {
            "team": team_map[4],
            "wins": 1,
            "losses": 0,
            "ties": 0,
            "outcome": "W",
            "pf": 101,
            "pa": 50.24,
        },
        # Andy
        5: {
            "team": team_map[5],
            "wins": 0,
            "losses": 1,
            "ties": 0,
            "outcome": "L",
            "pf": 68.98,
            "pa": 108.98,
        },
        # Loc
        6: {
            "team": team_map[6],
            "wins": 1,
            "losses": 0,
            "ties": 0,
            "outcome": "W",
            "pf": 122.02,
            "pa": 92.56,
        },
        # Linsen
        7: {
            "team": team_map[7],
            "wins": 0,
            "losses": 1,
            "ties": 0,
            "outcome": "L",
            "pf": 82.16,
            "pa": 100.16,
        },
        # Dave
        8: {
            "team": team_map[8],
            "wins": 1,
            "losses": 0,
            "ties": 0,
            "outcome": "W",
            "pf": 100.16,
            "pa": 82.16,
        },
        # Wilbert
        9: {
            "team": team_map[9],
            "wins": 0,
            "losses": 1,
            "ties": 0,
            "outcome": "L",
            "pf": 74.76,
            "pa": 108.48,
        },
        # David
        10: {
            "team": team_map[10],
            "wins": 0,
            "losses": 1,
            "ties": 0,
            "outcome": "L",
            "pf": 92.56,
            "pa": 122.02,
        },
        # John
        11: {
            "team": team_map[11],
            "wins": 0,
            "losses": 1,
            "ties": 0,
            "outcome": "L",
            "pf": 50.24,
            "pa": 101,
        },
        # Chris Chan
        13: {
            "team": team_map[13],
            "wins": 1,
            "losses": 0,
            "ties": 0,
            ""
            "pf": 108.98,
            "pa": 68.98,
        },
    }

    return week_1_data


def pretty_print_to_html(data, output_file="teams_data.html"):
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Men Bowl XIV Standings</title>
        <style>
            body {
                font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
                background-color: #f5f5f5;
                color: #333;
                margin: 0;
                padding: 0;
            }
            h1 {
                text-align: center;
                color: #D50A0A;  /* ESPN red color */
                margin-top: 20px;
                font-size: 36px;
                font-weight: bold;
            }
            table {
                width: 80%;
                margin: 30px auto;
                border-collapse: collapse;
                background-color: white;
                border: 1px solid #ccc;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            }
            th {
                background-color: #D50A0A; /* ESPN red color */
                color: white;
                padding: 15px;
                font-size: 14px;
                text-align: left;
            }
            td {
                padding: 12px 15px;
                font-size: 16px;
                border-bottom: 1px solid #ddd;
            }
            tr:nth-child(even) {
                background-color: #f9f9f9;
            }
            tr:hover {
                background-color: #f1f1f1;
            }
            tr:last-child td {
                border-bottom: none;
            }
            .highlight {
                font-weight: bold;
                color: #D50A0A;
            }
        </style>
    </head>
    <body>
        <h1>Men Bowl XIV Standings</h1>
        <table>
            <tr>
                <th></th>
                <th>Owner (Team Name)</th>
                <th>W</th>
                <th>L</th>
                <th>T</th>
                <th>%</th>
                <th>PF</th>
                <th>PA</th>
                <th>Waiver</th>
            </tr>
    """

    # Adding data rows to the HTML table
    index = 0
    for team_data in data:
        # Assuming `metadata` is a `Team` object
        team_name = str(team_data['metadata'].team_name)
        owner_name = str(team_data['metadata'].owners[0]["firstName"]
                         ) + " " + team_data['metadata'].owners[0]["lastName"]
        wins = team_data['wins']
        losses = team_data['losses']
        ties = team_data['ties']
        points_for = round(team_data['points_for'], 2)
        points_against = round(team_data['points_against'], 2)
        win_pct = "{:.3f}".format(team_data['win_pct'])
        waiver_rank = team_data['metadata'].waiver_rank

        html_content += f"""
            <tr>
                <td>{index + 1}</td>
                <td>{owner_name} ({team_name})</td>
                <td>{wins}</td>
                <td>{losses}</td>
                <td>{ties}</td>
                <td>{win_pct}</td>
                <td>{points_for}</td>
                <td>{points_against}</td>
                <td>{waiver_rank}</td>
            </tr>
        """
        index += 1

    html_content += """
        </table>
    </body>
    </html>
    """

    # Write the HTML content to a file
    with open(output_file, "w") as file:
        file.write(html_content)

    print(f"Data has been pretty printed to {output_file}")


def print_standings(standings):
    print("Standings:")

    for team in standings:
        print(
            f"[ {team['metadata'].team_id} ] - {team['metadata'].owners[0]['firstName']} {team['metadata'].owners[0]['lastName']}: {team['wins']}-{team['losses']}-{team['ties']} | {round(team['points_for'], 2)} - {round(team['points_against'], 2)} | {team['metadata'].waiver_rank}")


def sort_by_win_pct(team_data_list):
    """Take a list of team standings data and sort it using the TOTAL_POINTS_SCORED tiebreaker"""
    return sorted(team_data_list, key=lambda x: x["win_pct"], reverse=True)


def sort_by_points_for(team_data_list):
    """Take a list of team standings data and sort it using the TOTAL_POINTS_SCORED tiebreaker"""
    return sorted(team_data_list, key=lambda x: x["points_for"], reverse=True)


if __name__ == '__main__':
    # hydrate data into league object
    league = League(league_id=721759, year=2024, fetch_league=True)

    standings = league.standings_weekly(league.currentMatchupPeriod)

    team_overrides = create_team_overrides(league)

    tiebreaker_hierarchy = [
        (helper.sort_by_win_pct, "win_pct"), (helper.sort_by_points_for, "points_for")]

    list_of_team_data = []
    print("Standings: ", standings[0].__dict__)
    for team in standings:
        if team.team_id in team_overrides:
            team_data = {}

            team_data["metadata"] = team

            # wins
            team_data["wins"] = team.wins + \
                team_overrides[team.team_id]["wins"]
            team_data["losses"] = team.losses + \
                team_overrides[team.team_id]["losses"]
            team_data["ties"] = team.ties + \
                team_overrides[team.team_id]["ties"]
            team_data["points_against"] = team.points_against + \
                team_overrides[team.team_id]["pa"]
            team_data["points_for"] = team.points_for + \
                team_overrides[team.team_id]["pf"]
            team_data["win_pct"] = team_data["wins"] / \
                (team_data["wins"] + team_data["losses"] + team_data["ties"])
            list_of_team_data.append(team_data)

    # Then sort the rest of the teams
    sorted_team_data = helper.sort_team_data_list(
        list_of_team_data, tiebreaker_hierarchy
    )

    print("Sorted team data: ", sorted_team_data)

    print_standings(sorted_team_data)

    pretty_print_to_html(sorted_team_data, "team_data.html")
