from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


# Create your views here.
def contest(request, id):
    content= """
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
          <br><br>
        You may assume that each input would have exactly one solution, and you may not use the same element twice.
        <br><br>
        You can return the answer in any order.
        <br><br>
        Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
        <br><br>
      You may assume that each input would have exactly one solution, and you may not use the same element twice.
      <br><br>
      You can return the answer in any order.
      <br><br>
    """
    return render(request, 'Contest/index.html', {'id': id, 'content': content})

