mon=str(input('enter the month'))
date=int(input('enter the date'))
if mon=='jan' and date==1:
	print('new years day')
elif mon=='july' and date==1:
	print('canada day')
elif mon=='dec' and date==25:
	print('christmas day')
else:
	print('no fixed holiday on entered date')
