from Nba_stat_comparison import keys, create_dict,rank, read_dictionary
from tempfile import mktemp #so that we can create a filename that doesn't exist
from pytest import approx #so that we can get an approximate value 
import pytest # so that we can test all of our functions 

PLAYER_NAME_INDEX = 0
REBOUNDS_INDEX = 22
ASSISTS_INDEX = 23
POINTS_INDEX = 28

def test_keys():
    """
    this tests the keys function, and it ensures that the function takes a dictionary and returns a list that 
    contains all the keys in the dictionary
    """
    food_dict = {'pizza': 'peporoni', 'ice cream': 'chocolate','chicken nuggets':'Barboque Sauce'}
    car_dict = {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
    player_dict = {'height': 75, 'weight': 160, 'age': 23, 'position': 'PG'}
    assert keys(food_dict) == ['pizza','ice cream','chicken nuggets']
    assert keys(car_dict) == ['brand','model','year']
    assert keys(player_dict) == ['height','weight','age','position']

def test_create_dict():
    """
    this tests the create_dict function, and it ensures taht the function takes a compound dicitonary and returns
    a single-item dictionary, the value of the dictionary based on the index of the compound dictionary
    """
    players_dict = {'Stephen Curry': ['Stephen Curry',29.1,5.0,4.7], 'LeBron James': ['LeBron James',24.4,7.6,6.4],
                    'Kevin Durant': ['Kevin Durant',31.0,6.4,5.8], 'Joel Embiid': ['Joel Embiid',32.0,11.3,6.6],
                    'Jayson Tatum': ['Jayson Tatum',27.4,8.7,4.1], 'DeAaron Fox': ['DeAaron Fox',30.3,4.7,6.6]}
    
    assert create_dict(players_dict,1) == {'Stephen Curry': 29.1, 'LeBron James': 24.4, 'Kevin Durant': 31.0, 'Joel Embiid': 32.0, 'Jayson Tatum': 27.4, 'DeAaron Fox': 30.3}
    assert create_dict(players_dict,2) == {'Stephen Curry': 5.0, 'LeBron James': 7.6, 'Kevin Durant': 6.4, 'Joel Embiid': 11.3, 'Jayson Tatum': 8.7, 'DeAaron Fox': 4.7}
    assert create_dict(players_dict,3) == {'Stephen Curry': 4.7, 'LeBron James':6.4 , 'Kevin Durant': 5.8, 'Joel Embiid': 6.6, 'Jayson Tatum': 4.1, 'DeAaron Fox': 6.6}
    
def test_rank():
    """
    This tests the rank function, and it ensures that the function takes a dictionary and returns a new dictionary that contains
    the keys with the top 5 values. 
    """
    points_dict = {'Stephen Curry': 29.1, 'LeBron James': 24.4, 'Kevin Durant': 31.0, 'Joel Embiid': 32.0, 'Jayson Tatum': 27.4, 'DeAaron Fox': 30.3}
    rebounds_dict = {'Stephen Curry': 5.0, 'LeBron James': 7.6, 'Kevin Durant': 6.4, 'Joel Embiid': 11.3, 'Jayson Tatum': 8.7, 'DeAaron Fox': 4.7}
    assists_dict = {'Stephen Curry': 4.7, 'LeBron James':6.4 , 'Kevin Durant': 5.8, 'Joel Embiid': 6.6, 'Jayson Tatum': 4.1, 'DeAaron Fox': 6.6}

    assert rank(points_dict) == {'Joel Embiid': 32.0, 'Kevin Durant': 31.0, 'DeAaron Fox': 30.3, 'Stephen Curry': 29.1, 'Jayson Tatum': 27.4}
    assert rank(rebounds_dict) == {'Joel Embiid': 11.3, 'Jayson Tatum': 8.7, 'LeBron James': 7.6, 'Kevin Durant': 6.4, 'Stephen Curry': 5.0}
    assert rank(assists_dict) == {'Joel Embiid': 6.6, 'DeAaron Fox': 6.6, 'LeBron James': 6.4, 'Kevin Durant': 5.8, 'Stephen Curry': 4.7}

def test_read_dictionary():
    """
    this tests the read_dictionary function, and it ensures that it takes the csv file and converts it into a dictionary,
    with the player name or the first index as the key
    """
    filename = mktemp(dir=".", prefix="not", suffix=".csv")
    with pytest.raises(FileNotFoundError):
        read_dictionary(filename, PLAYER_NAME_INDEX)
        pytest.fail("read_dictionary function must use its filename parameter")

    filename =  ("nba-player-stats-2019.csv")
    players_dict = read_dictionary(filename, PLAYER_NAME_INDEX)

    assert isinstance(players_dict, dict), \
        "read_dictionary function must return a dictionary:" \
        f" expected a dictionary but found a {type(players_dict)}"
    
    check_player(players_dict, "Álex Abrines", ["Álex Abrines","SG",25,"OKC",31,2,19.0,1.8,5.1,.357,1.3,4.1,.323,0.5,1.0,.500,.487,0.4,0.4,.923,0.2,1.4,1.5,0.6,0.5,0.2,0.5,1.7,5.3])
    check_player(players_dict, "Quincy Acy", ["Quincy Acy","PF",28,"PHO",10,0,12.3,0.4,1.8,.222,0.2,1.5,.133,0.2,0.3,.667,.278,0.7,1.0,.700,0.3,2.2,2.5,0.8,0.1,0.4,0.4,2.4,1.7])
    check_player(players_dict, "Jaylen Adams", ["Jaylen Adams","PG",22,"ATL",34,1,12.6,1.1,3.2,.345,0.7,2.2,.338,0.4,1.1,.361,.459,0.2,0.3,.778,0.3,1.4,1.8,1.9,0.4,0.1,0.8,1.3,3.2])


def check_player(players_dict,player_name,expected_value):
    """
    this funtion ensures that the dictioanary created by the read_dictionary function contains the same values as the ones
    listed in the csv file that we're reading
    """
    assert player_name in players_dict
    actual_value = players_dict[player_name]

    exp_name = expected_value[PLAYER_NAME_INDEX]
    act_name = actual_value[PLAYER_NAME_INDEX]
    assert act_name == exp_name,\
        f"wrong name for product {player_name}: " \
        f"expected {exp_name} but found {act_name}"
    
    act_ppg = actual_value[POINTS_INDEX]
    if isinstance(act_ppg, str):
        act_ppg = float(act_ppg)
    exp_ppg = expected_value[POINTS_INDEX]
    assert act_ppg == approx(exp_ppg),\
        f"wrong name for product {player_name}: " \
        f"expected {exp_ppg} but found {act_apg}"
    
    
    act_apg = actual_value[ASSISTS_INDEX]
    if isinstance(act_apg, str):
        act_apg = float(act_apg)
    exp_apg = expected_value[ASSISTS_INDEX]
    assert act_apg == approx(exp_apg),\
        f"wrong name for product {player_name}: " \
        f"expected {exp_apg} but found {act_apg}"
    
    act_reb = actual_value[REBOUNDS_INDEX]
    if isinstance(act_reb, str):
        act_reb = float(act_reb)
    exp_reb = expected_value[REBOUNDS_INDEX]
    assert act_reb == approx(exp_reb),\
        f"wrong name for product {player_name}: " \
        f"expected {exp_reb} but found {act_reb}"
    
    

# call the main function of this program
# so that all the tests will be executed 
pytest.main(["-v", "--tb=line", "-rN", __file__])