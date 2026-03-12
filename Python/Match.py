ch=int(input("Enter your choice \n1.Triangle 2.Circle 3.Square"))
match ch:
	case 1:
		b=float(input("Enter the base"))
		h=float(input("Enter the height"))
		print("Area=",(0.5*b*h))
	case 2:
	     r=float(input("Enter the radius"))	
	     print("Area=",(3.14*r*r))
	case 3:
	     b=float(input("Enter the length"))
	     print("Area=",(b*b))     
    case _:
    	 print("Invalid choice")