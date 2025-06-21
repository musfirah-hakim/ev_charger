from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Temporary in-memory status variable
CURRENT_STATUS = "Idle"

def charger_control(request):
    return render(request, 'evfrontend/charger_control.html')

def charger_status(request):
    # Returns the current status (GET)
    return JsonResponse({'status': CURRENT_STATUS})

@csrf_exempt
def update_status(request):
    global CURRENT_STATUS
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            CURRENT_STATUS = data.get('status', CURRENT_STATUS)
            return JsonResponse({'message': 'Status updated successfully', 'status': CURRENT_STATUS})
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=405)
