from django.http import HttpResponse
from django.shortcuts import render
import datetime
import os

def generate_tables(request):
    # Scenario a: Print tables from 3 to 20 directly
    response = "Multiplication tables from 3 to 20:\n"
    for i in range(3, 21):
        for j in range(1, 11):
            response += f"{i} * {j} = {i*j}\n"
        response += "\n"

    return HttpResponse(response)
