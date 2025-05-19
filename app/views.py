from django.shortcuts import render

# Create your views here.
import json
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import os

LOGS_FILE_PATH = 'app/static/suspicious_logs.json'


# @csrf_exempt
# def save_suspicious_logs(request):
#     if request.method == 'POST':
#         logs = json.loads(request.body)
#         with open(LOGS_FILE_PATH, 'w') as f:
#             json.dump(logs, f)
#         return HttpResponse(status=200)
#     return HttpResponse(status=400)

# import json
# import os
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt

# LOGS_FILE_PATH = 'suspicious_detector/static/suspicious_logs.json'
@csrf_exempt
def save_suspicious_logs(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        
        # Ensure the directory and file exist
        os.makedirs(os.path.dirname(LOGS_FILE_PATH), exist_ok=True)
        if not os.path.exists(LOGS_FILE_PATH):
            with open(LOGS_FILE_PATH, 'w') as file:
                json.dump([], file)  # Initialize with an empty list
        
        try:
            # Append new log to the existing file content
            with open(LOGS_FILE_PATH, 'r+') as log_file:
                # Check if file is empty
                content = log_file.read()
                logs = json.loads(content) if content else []
                logs.extend(data)  # Append new data
                log_file.seek(0)   # Move to beginning of file to overwrite
                json.dump(logs, log_file)
                
            return JsonResponse({"status": "success", "message": "Log saved successfully."})
        except Exception as e:
            print("Error saving logs:", e)
            return JsonResponse({"status": "error", "message": str(e)})
    return JsonResponse({"status": "error", "message": "Invalid request"})


def get_suspicious_logs(request):
    if os.path.exists(LOGS_FILE_PATH):
        with open(LOGS_FILE_PATH, 'r') as f:
            logs = json.load(f)
        return JsonResponse(logs, safe=False)
    else:
        return JsonResponse([], safe=False)

# from django.shortcuts import render

def show_detector(request):
    return render(request, 'cloudcamera_ver2.html')

def show_report(request):
    return render(request, 'report.html')
