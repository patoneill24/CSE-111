from water_flow import water_column_height, pressure_loss_from_pipe, pressure_gain_from_water_height, pressure_loss_from_fittings, reynolds_number, pressure_loss_from_pipe_reduction, kPa_to_psi
#import all the function that we're going to be testing 

from pytest import approx
import pytest

def test_water_column_heihgt():
    """
    This tests the water_columnn_height function by calling it 4 times with different arguments
    """
    assert water_column_height(0,0) == 0
    assert water_column_height(0,10) == 7.5
    assert water_column_height(25,0) == 25
    assert water_column_height(48.3,12.8) == 57.9

def test_pressure_loss_from_pipe():
    """
    This tests the pressure_loss_from_pipe function by calling it 7 times with different arguments
    """
    assert pressure_loss_from_pipe(0.048692,0,0.018,1.75) == approx(0, abs = 0.001)
    assert pressure_loss_from_pipe(0.048692,200,0,1.75) == approx(0, abs= 0.001)
    assert pressure_loss_from_pipe(0.048692,200,0.018,0) == approx(0, abs = 0.001)
    assert pressure_loss_from_pipe(0.048692,200,0.018,1.75) == approx(-113.008, abs = 0.001)
    assert pressure_loss_from_pipe(0.048692,200,0.018,1.65) == approx(-100.462, abs = 0.001)
    assert pressure_loss_from_pipe(0.28687,1000,0.013,1.65) == approx(-61.576, abs = 0.001)
    assert pressure_loss_from_pipe(0.28687,1800.75,0.013,1.65) == approx(-110.884, abs = 0.001)

def test_pressure_gain_from_height():
    """
    This tests the pressure_gain_from_height function by calling it three times with different arguments
    """
    assert pressure_gain_from_water_height(0) == approx(0, abs = 0.001)
    assert pressure_gain_from_water_height(30.2) == approx(295.628, abs = 0.001)
    assert pressure_gain_from_water_height(50) == approx(489.450, abs = 0.001)

def test_pressure_loss_from_fittings():
    """
    This tests the test_pressure_loss_from_fittings function by calling it 5 times with different arguments
    """
    assert pressure_loss_from_fittings(0,3) == approx(0, abs = 0.001)
    assert pressure_loss_from_fittings(1.65,0) == approx(0, abs = 0.001)
    assert pressure_loss_from_fittings(1.65,2) == approx(-0.109, abs = 0.001)
    assert pressure_loss_from_fittings(1.75,2) == approx(-0.122, abs = 0.001)
    assert pressure_loss_from_fittings(1.75,5) == approx(-0.306, abs = 0.001)

def test_reynolds_number():
    """
    This tests the reynolds_number function by calling it 5 times with different arguments
    """
    assert reynolds_number(0.048692,0) == approx(0, abs= 1)
    assert reynolds_number(0.048692,1.65) == approx(80069, abs = 1)
    assert reynolds_number(0.048692,1.75) == approx(84922, abs = 1)
    assert reynolds_number(0.28687,1.65) == approx(471729, abs = 1)
    assert reynolds_number(0.28687,1.75) == approx(500318, abs = 1)

def test_pressure_lost_from_pipe_reduction():
    """
    This tests the pressure_lost_from_pipe_reduction function by calling it 3 times with differnet arguments
    """
    assert pressure_loss_from_pipe_reduction(0.28687,0,1,0.048692) == approx(0, abs = 0.001)
    assert pressure_loss_from_pipe_reduction(0.28687,1.65,471729,0.048692) == approx(-163.744, abs = 0.001)
    assert pressure_loss_from_pipe_reduction(0.28687,1.75,500318,0.048692) == approx(-184.182, abs = 0.001)

def test_kPa_to_psi():
    """
    This tests the kPA_to_psi function by calling it 4 times with differnt arguemtns 
    """
    assert kPa_to_psi(0) == approx(0, abs = 0.001)
    assert kPa_to_psi(2) == approx(0.290, abs = 0.001)
    assert kPa_to_psi(4) == approx(0.580, abs = 0.001)
    assert kPa_to_psi(10) == approx(1.450, abs = 0.001)


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])



