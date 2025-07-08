from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse, HttpResponseNotFound
from StudentApp.serializers import StudentSerializer
from StudentApp.models import Student

@csrf_exempt
def studentApi(request, id=0):
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"message": "Added Successfully"}, status=201)
        return JsonResponse({"error": "Failed to Add"}, status=400)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        try:
            student = Student.objects.get(id=id)
        except Student.DoesNotExist:
            return HttpResponseNotFound("Student not found")

        serializer = StudentSerializer(student, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"message": "Updated Successfully"})
        return JsonResponse({"error": "Failed to Update"}, status=400)

    elif request.method == 'DELETE':
        try:
            student = Student.objects.get(id=id)
        except Student.DoesNotExist:
            return HttpResponseNotFound("Student not found")

        student.delete()
        return JsonResponse({"message": "Deleted Successfully"})