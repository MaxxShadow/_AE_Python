import pytest
import soucet_s_posunem_ver3 
'''
@pytest.mark.parametrize("s, d, expected", [
    ([-1, -2, -3, -4, -5, -6, -7, -8], 1, [-1]),
    ([-1, -2, -3, -4, -5, -6, -7, -8], 8, [-1, -2, -3, -4, -5, -6, -7, -8]),
    ([-1, -2, -3, -4, -5, -6, -7, -8], 4, [-1, -2, -3, -4]),
    ([-1, -2, -3, -4, -5, -6, -7, -8], 5, [-1, -2, -3, -4, -5]),
    ([-1, -2, -3, -4, -5, -6, -7, -8], 6, [-1, -2, -3, -4, -5, -6])
])
def test_zkrat_seznam(s, d, expected):
     assert soucet_s_posunem_ver3.zkrat_seznam(s,d) == expected 


@pytest.mark.parametrize("s, p, expected",[
     ([-1, -2, -3, -4, -5, -6, -7, -8], 3, [-4, -5, -6, -7, -8, -1, -2, -3]),
])
def test_posun_seznam(s, p, expected):
     assert soucet_s_posunem_ver3.posun_seznam(s,p) == expected


@pytest.mark.parametrize("s, expected",[
     ([-1, -1, -1, -1, -1, -1, 3, 3], 0),
     ([-1, -2, -3, -4, -5, -6, -7, -8], -36)
])
def test_secti_seznam(s, expected):
     assert soucet_s_posunem_ver3.secti_seznam(s) == expected 
'''

'''
>> pytest -vv -rp
'''

@pytest.mark.parametrize("s1, s2, p, expected",[
     ([-1, -2, -3, -4, -5, -6, -7, -8]
	 ,[-1, -2, -3, -4, -5, -6, -7, -8]
	 , 3
	 , ([-1, -2, -3, -4, -5, -6, -7, -8],[-4, -5, -6, -7, -8, -1, -2, -3]))
])
def test_uprav_seznamy(s1, s2,p, expected):
     ss1,ss2 = soucet_s_posunem_ver3.uprav_seznamy(s1, s2,p)
     print(f"{ss1=} | {ss2=}")
     print(expected)
     assert soucet_s_posunem_ver3.uprav_seznamy(s1, s2,p) == expected 

     