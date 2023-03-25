from prime import prime_numbers

def test_prime_numbers():
    data = {
        (1,30):[2, 3, 5, 7, 11, 13, 17, 19, 23, 29],
        (10,1): [],
        (-1, 100):[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97],
        ("low","high"): [],
        (0,0):[],
        (2.25, 29.22):[3,5,7,11,13,17,19,23,29]
    }
    for i in data.keys():
        assert prime_numbers(i[0],i[1]) == data.get(i), f"Low = {i[0]}, High = {i[1]}, должно получиться на выходе: {data.get(i)}"
