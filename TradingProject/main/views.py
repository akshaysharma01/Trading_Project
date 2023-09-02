from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import csv
import json
import asyncio
from io import TextIOWrapper
from django.shortcuts import render, redirect
from django.conf import settings
from .models import Candle


# Create your views here.

def process_csv(request):
    if request.method == 'POST':
        # for uploaded CSV file from the form
        uploaded_file = request.FILES['csv_file']

        # to get timeframe
        timeframe = int(request.POST.get('timeframe', 1))

        # a list to store candle objects
        candles = []


        # Process the uploaded CSV file
        with uploaded_file.file as csv_file:
            csv_reader = csv.DictReader(TextIOWrapper(csv_file, encoding='utf-8'))
            for row in csv_reader:
                print(row)
                open_price = row.get('OPEN')  
                high_price = row.get('HIGH')  
                low_price = row.get('LOW')    
                close_price = row.get('CLOSE')  
                date = row.get('DATE')       

                print(f"Open: {open_price}, High: {high_price}, Low: {low_price}, Close: {close_price}, Date: {date}")


                # Now, here is Candle object with the extracted values
                candle = Candle(
                    open=open_price,
                    high=high_price,
                    low=low_price,
                    close=close_price,
                    date=date
                )
                candles.append(candle)

        # an async function for converting candles
        async def convert_candles(candles, timeframe):
            
            # Use asyncio.sleep() for simulation
            await asyncio.sleep(1) 
            return candles  

        # a new event loop
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        # Run the async code within the event loop
        converted_candles = loop.run_until_complete(convert_candles(candles, timeframe))

        # Close the event loop
        loop.close()

        # is JSON file and store the converted data
        json_data = [{'id': c.id, 'open': c.open, 'high': c.high, 'low': c.low, 'close': c.close, 'date': str(c.date)} for c in converted_candles]


        # generate a JSON response
        response_data = {'message': 'Processing complete.'}

        # HttpResponse with the option to download the JSON file
        response = HttpResponse(json.dumps(response_data), content_type='application/json')
        response['Content-Disposition'] = f'attachment; filename="converted_data.json"'

        # JSON data to the response
        response.write(json.dumps(json_data))

        return response

    return render(request, 'upload_form.html')  



