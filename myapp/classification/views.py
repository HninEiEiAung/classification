# myapp/views.py

from django.http import JsonResponse
from .utils import classify_text

def predict(request):

    print("this is predict view")

    if request.method == 'GET':
        text = request.GET.get('text')
        if text:
            prediction = classify_text(text)
            print(f"Prediction: {prediction}")  # Debug print to see the structure of the prediction
            # Ensure the prediction is a list or dict
            if isinstance(prediction, list):
                return JsonResponse({'predictions': prediction}, safe=False)  # Wrap in a dictionary
            else:
                return JsonResponse(prediction, safe=False)
        else:
            return JsonResponse({'error': 'No text provided'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)
