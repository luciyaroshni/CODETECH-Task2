from django.shortcuts import render
from django.http import HttpResponse
import requests
import base64

def upload_file_view(request):
    if request.method == 'POST' and request.FILES.get('file'):
        file = request.FILES['file']
        
        # Encode file content to base64
        encoded_file_data = base64.b64encode(file.read()).decode('utf-8')
        
        url = 'https://767s1ecok5.execute-api.ap-south-1.amazonaws.com/dev/upload'
        headers = {
            'Content-Type': 'application/octet-stream',
            'file-name': file.name
        }
        
        # Send the base64 encoded file data
        response = requests.post(url, data=encoded_file_data, headers=headers)
        
        if response.status_code == 200:
            return HttpResponse('File uploaded successfully!')
        else:
            return HttpResponse(f'File upload failed! Status code: {response.status_code}', status=response.status_code)
    return render(request, 'FileHandler1.html')
