
# Create your views here.
from django.shortcuts import render
import pickle

#model = pickle.load(open('C:\Users\Nithin\OneDrive\Desktop\DS E-E PRO\housePredModel\model.pkl', 'rb'))
model = pickle.load(open("C:\\Users\\Nithin\\OneDrive\\Desktop\\DS E-E PRO\\housePredModel\\model.pkl", 'rb'))

def home(request):
    return render(request, 'tempapp/index.html')

def predict(request):
    areaIncome = float(request.GET['arIncomeIn'])
    houseAge = float(request.GET['houseAgeIn'])
    noOfRooms = float(request.GET['noOfRoomsIn'])
    noOfBeds = float(request.GET['noBedRIn'])
    avgPopul = float(request.GET['populationIn'])
    prediction = model.predict([[areaIncome, houseAge, noOfRooms, noOfBeds, avgPopul]]) 
    dict1 = {
        'areaIncome': areaIncome,
        'houseAge': houseAge,
        'noOfRooms': noOfRooms,
        'noOfBeds': noOfBeds,
        'avgPopul': avgPopul,
        'predictVal': prediction[0]  # Assuming prediction is a single value, adjust accordingly
    }
    print(prediction)
    return render(request, 'tempapp/predicted.html', dict1)
