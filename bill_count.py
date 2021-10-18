

def bill_count(amount):
	bills = [10,5,2,1]

	count = 0
	
	bills_count = dict()


	if amount<1:
		return 0

	for bill in bills:
		count = 0
		count += amount // bill
		amount = amount%bill
		bills_count[bill] = count
		if amount==0:
			break

	return bills_count






def main():
	amount = int(input("Enter amount: "))
	print(bill_count(amount))
	
if __name__ == '__main__':
	main()