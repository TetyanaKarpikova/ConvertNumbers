from django.shortcuts import render
from django.http import HttpResponse
from .forms import IntForm


def index(request):
    if request.method == "POST":
        user_form = IntForm(request.POST)
        if user_form.is_valid():
            input_date = user_form.cleaned_data["input_date"]

            try:
                output_date = arab_to_roman(input_date)
            except Exception as e:
                output_date = roman_to_arab(input_date)

            return render(request, "index.html", {"form": user_form, "answer": output_date})

        else:
            return HttpResponse("Invalid data")

    else:
        user_form = IntForm()
        return render(request, "index.html", {"form": user_form})


CONV_TABLE = ((1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
              (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
              (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I'))


def arab_to_roman(number):
    number = int(number)
    if number <= 0: return ''
    res = ''
    for arab, roman in CONV_TABLE:
        while number >= arab:
            res += roman
            number -= arab

    return res


def roman_to_arab(str_rom):
    str_rom = str_rom.upper()
    res = 0
    for arab, roman in CONV_TABLE:
        while str_rom.startswith(roman):
            res += arab
            str_rom = str_rom[len(roman):]
    return res


