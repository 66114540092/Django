from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# คำถามตัวอย่าง
example_question = {
    "id": 1,
    "text": "ประเทศไทยมีกี่จังหวัด",
    "choices": [50, 68, 72, 77]
}

@csrf_exempt
def get_question(request):
    if request.method == "GET":
        return JsonResponse(example_question)
    else:
        return JsonResponse({"error": "Method not allowed"}, status=405)

@csrf_exempt
def create_question(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            return JsonResponse(data)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
    else:
        return JsonResponse({"error": "Method not allowed"}, status=405)
