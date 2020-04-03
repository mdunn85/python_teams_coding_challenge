

# Function to get all the teams a person is assigned to
# Returns a list of Person objects
def exercise1(person, person_list):
    return_list = []
    # iterate through person_list to see if the object is a team
    for _person in person_list:
        # if the person object is a team and person is a member of that team add to return list
        if _person.is_team and person in _person.members:
            return_list.append(_person)
    return return_list


# Function to get all the teams a person is assigned to
# when tested exercise1 function with data2 ['The A-Team']. modified exercise1 function to the following
# Returns a list of Person objects
def exercise2(person, person_list):
    return_list = []
    # iterate through person_list to see if they are a team
    for team in person_list:
        if team.is_team:
            # if the person is in the team members add them to the return array
            if person in team.members:
                return_list.append(team)
            else:
                # iterate through members to see if they are a team
                for member in team.members:
                    # if the member of a team is a team and the person exists in that team members
                    # add them to the return array
                    if member.is_team and person in member.members:
                        return_list.append(team)
    return return_list


# Function to get all the members from a team
def get_members(team):
    return_list = []
    # iterate through team members and add them to the return list
    for member in team.members:
        # if member is a team iterate through that team to get its members
        if member.is_team:
            for _member in member.members:
                return_list.append(_member)
        else:
            return_list.append(member)
    return return_list


'''
 task 4 returned ['Alice', 'Bob', 'Carlos', 'Charlie', 'Eve', 'The B-Team'] so previous version of get_members function
 is incorrect. Testing get_members_v2 with Data3 caused an infinite loop which is fixed in get_members_v3
'''


# Function to get all the members from a team including teams of teams
def get_members_v2(team):
    # get non team members from team
    members = list(member for member in team.members if not member.is_team)
    # get teams from team members
    teams = list(team for team in team.members if team.is_team)
    # iterate through teams list and get non team members
    if len(teams) > 0:
        for _team in teams:
            # add members to members list
            members = members + get_members_v2(_team)
    return members


def get_members_v3(team):
    # get members of the team
    team_members = get_team_members(team)
    # add current team to processed teams list
    processed_team_names = [team.displayname]
    # get teams from the current team members
    not_processed_teams = get_teams_from_member_list(team, processed_team_names)
    # process not_processed_teams list
    while len(not_processed_teams) > 0:
        for not_processed_team in not_processed_teams:
            if not_processed_team.displayname not in processed_team_names:
                new_members = get_team_members(not_processed_team)
                # add new members to the members list
                team_members = team_members + new_members
                # add team to processed team list
                processed_team_names.append(not_processed_team.displayname)
                # remove team from not processed list
                not_processed_teams.remove(not_processed_team)
                # add new non processed teams to not processed list
                not_processed_teams = not_processed_teams + get_teams_from_member_list(not_processed_team,
                                                                                       processed_team_names)
    return team_members


# Function to get only non teams from a team members
def get_team_members(team):
    return list(member for member in team.members if not member.is_team)


# Function to get teams from a team members
def get_teams_from_member_list(team, processed_team_names):
    return list(team for team in team.members if team.is_team and team.displayname not in processed_team_names)
