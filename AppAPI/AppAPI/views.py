from django.shortcuts import redirect,render
from django.http import HttpResponse

finalData = 0
def alspost(request):
    data = request.POST.get('data')
    global finalData
    finalData = data
    if int(data) == 1:
      data = "Food is being requested"
    elif int(data) == 2:
      data = "!!EMERGENCY!!"
    elif int(data) == 3:
      data = "Assisstance is being requested"
    print("\n\nThe Patient : \n")
    print(data)
    print("\n\n")
    return HttpResponse(status = 200)



def oldage(request):
  global finalData
  data = finalData
  print(data)
  if int(data) == 1:
    data = "Food is being requested"
    return render(request, 'AppAPI/Food.html', {})
  elif int(data) == 2:
    data = "!!EMERGENCY!!"
    return render(request, 'AppAPI/SOS.html', {})
  elif int(data) == 3:
    data = "Assisstance is being requested"
    return render(request, 'AppAPI/Assisstance.html', {})
  print("\n\nThe Patient : \n")
  print(data)
  print("\n\n")
  return render(request, 'AppAPI/index.html', {})