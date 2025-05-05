def share_pizza(slices, friends):
    slices_each = slices / friends
    print(f"{slices_each} slices each")
    
if __name__ == "__main__":
    slices = 12
    bears = 1
    foxes = 2
    badgers = -3
    share_pizza(slices, bears + foxes + badgers)