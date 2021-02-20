import sys
import unicodedata

loop_key = 1
series_nam = [1,3,5,6,7,8,9]
series_name_output = ['1000系','3000系','5000系','6000系','7000系','8000系','9000系']
car = [{1700,3700,5730,6700,6740,6720,6410,7700,7720,7800,7420,8700,8720,8730,9700,9730,9740},
       {1100,3100,5030,6030,6040,6020,6860,7000,7020,7200,7870,8000,8020,8030,9000,9030,9040},
       {1500,3500,5080,6080,6090,6070,7050,7070,7250,8050,8070,8080,9050,9080,9090},
       {1150,3150,5530,6530,6540,6520,7500,7520,7850,8500,8520,8530,9500,9530,9540},
       {1750,3750,5580,6580,6590,6570,7550,7570,8550,8570,8580,9550,9580,9590},
       {5130,6130,6140,6120,7100,7120,8100,8120,8130,9100,9130,9140},
       {5180,6180,6190,6170,7150,7170,8150,8170,8180,9150,9180,9190},
       {5230,6230,6240,6220,7200,7220,8200,8220,8230,9200,9230,9240},
       {5280,6280,6290,6270,7250,7270,8250,8270,8280,9250,9280,9290},
       {5780,6780,6790,6770,7750,7770,8750,8770,8780,9750,9780,9790}]
print('Keio vehicle number display program Ver.1.66')
print('Copyright ©︎2021 Chutoro Detteiu(@ctr_exe). All Rights Reserved.')
while True:
    if loop_key == 1:
        car_text = ""
        i = 0
        passing = False
        start = input("知りたい車番を入力してください。終了する場合にはexitと入力してくだささい:")
        input_type = str.isnumeric(start)
        if start ==  "exit":
            sys.exit()
        elif input_type == False:
            print('数字を入力してください')
            passing = True
        elif len(start) != 4:
            print('4桁の数値を入力してください')
            passing = True

        if passing:
            pass
        else:

            start_list = list(str(start))
            for i in range(0,len(series_nam)):
                if int(start_list[0]) == series_nam[i]:
                    series_seq = i
                else:
                    pass

            for a in range(0,2):
                del start_list[0]

            if start_list[0] == '0':
                pass
            else:
                del start_list[0]


            organi_nam = ''.join(start_list)

            type_nam = int(start) - int(organi_nam)

            for i in range(0,len(car)):
                if type_nam in car[i]:
                    car_text = str(i+1) + '両目'
                    break
                else:
                    if i == len(car) -1:
                        print('存在しない車番です')
                        passing = True
                        break

        if passing:
            pass
        else:
            organi_nam_full = int(start) - 50 #50は八王子方面車両の+50を引くため
            if list(str(organi_nam_full))[1] != list(start)[1]:
                organi_nam_full = int(start)
            else:
                pass

            print(series_name_output[series_seq] + str(organi_nam_full) + 'Fの' + car_text)
