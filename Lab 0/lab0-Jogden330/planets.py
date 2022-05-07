def weight_on_planets():
   weigh = float(input("What do you weigh on earth? \n"))
   print('On Mars you would weigh',  weigh * 0.38, 'pounds.\nOn Jupiter you would weigh', weigh * 2.34, 'pounds.')
   
if __name__ == '__main__':
   weight_on_planets()