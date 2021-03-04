from django.shortcuts import render, redirect
from .models import Calculation


def index(request):
    """Get logs and run calculations"""
    if request.method == 'GET':
        #get the last ten calculations
        calculations = Calculation.objects.order_by('-date_added')[:10][::-1]
        context = {'calculations': calculations}
        return render(request, 'logs/index.html', context)

    #Run a math operations
    if request.method == 'POST':
        answer = request.POST['input']
        try:
            result = eval(answer)
            #Save calculation in a log model
            new_calc = Calculation()
            new_calc.input = str(answer)
            new_calc.output = str(result)
            new_calc.save()
            #Retrive the last ten calculations
            calculations = Calculation.objects.order_by('-date_added')[:10][::-1]
            context = {'answer': answer, 'result': result, 'calculations': calculations}
            return render(request, 'logs/index.html', context)
        except:
            #Account for improper input
            error = 'Please check for errors in your input: '
            calculations = Calculation.objects.order_by('-date_added')[:10][::-1]
            context = {'error': error, 'answer': answer, 'calculations': calculations}
            return render(request, 'logs/index.html', context)


def delete_logs(request):
    """Remove all logs"""
    if request.method == 'POST':
        Calculation.objects.all().delete()
        return redirect('index')


