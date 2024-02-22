#● The conversions you need to support are: temp (F <-> C),
#speed (MPH <-> KPH), weight (kg <-> stone <-> lbs).
#● use the input function to ask for 2 pieces of information: the
#type of conversion, source value.


type=str(input("please chose conversions from the following, you need to type exactly like hot it looks in this text: temp(F->C) temp(C->F) weight(KG->STONE) weight(STONE->KG) weight(STONE->LBS) weight(LBS->STONE) speed(MPH->KPH) speed(KPH->MPH)"))

match type:
    case "temp(F->C)":
        fheit=int(input("Enter the temperature in Fahrenheit: "))
        cels=(fheit-32)*5/9
        print(f'The temprature in celsuis is: {cels} C')
    case "temp(C->F)":
        cels=int(input("Enter a temperature in celsuis: "))
        fheit=(cels*9/5)+32
        print(f'The temperature in ferhenheit is {fheit} F')
    case "weight(KG->STONE)":
        kg=int(input("Enter a weight in kg: "))
        print(f'the weigh in stone is: {kg*0.157}')
    case "weight(STONE->KG)":
        stone=int(input("Enter a weight in stone: "))
        print(f'The weight in KG is: {stone*6.350}')
    case "weight(STONE->LBS)":
        stone=int(input("Enter a weight in stone: "))
        print(f'The weight in LBS(pounds) is: {stone*14}')
    case "weight(LBS->STONE)":
        lbs=int(input("Enter a weight in pounds(lbs): "))
        print(f'The weight in stone is: {lbs/14}')
    case "speed(MPH->KPH)":
        mph=int(input("Enter the speed in MPH: "))
        print(f'The speed in KPH IS: {mph*1.60}')
    case "speed(KPH->MPH)":
        kph=int(input("Enter the speed in KPH: "))
        print(f'The speed in MPH IS: {kph/1.60}')
    case _:
        input('Wrong input, Please try again!!')
