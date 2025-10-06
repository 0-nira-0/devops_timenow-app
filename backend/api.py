from datetime import datetime

def handler(request):
    now = datetime.now()
    return now.strftime("%H:%M:%S")
