from .. import app


@app.get("/boomerang")
def boomerang(number: int):
    # if number % 2 == 0:
    #     even_number = True
    # else:
    #     even_number = False

    is_even = bool
    is_even = True if number % 2 ==0 else False

    div_by_3 = bool
    div_by_3 = True if number % 3 ==0 else False

    multiply_list = []
    multiply_list = [(number * i) for i in range(1,6)]
    
    multiply_by_power = []
    multiply_by_power = [(number ** i) for i in range(1,6)]


    fibonacci = {}
    fibonacci.update({"1_number" : int(number)})
    fibonacci.update({"2_number" : int(number)*2})
    [fibonacci.update({f"{i+2}_number" : (fibonacci.get(f"{i}_number") + fibonacci.get(f"{i+1}_number"))}) for i in range(1,30)]
    fib_numbers = [fibonacci]


    return{"number" : number, "is_even?" : is_even, "divided_by_3?" : div_by_3, "multiplied_list" : multiply_list, "multiplied_by_power" : multiply_by_power, "fibonacci" : fib_numbers}