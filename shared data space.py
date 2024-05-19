# import multiprocessing 

#problem


# y = 8
# def f (x):
#     global y 
#     y = x +5
#     print("y in p1 1 :{}".format(y))
# if __name__=='__main__':
#     x = 2 
#     p1 = multiprocessing.Process(target=f,args=(x,))
#     p1.start()
#     p1.join()
#     print("y in main :{}".format(y))

#print('###################################################################################')

##solution


# def f (x,y):
#     y.value=(x+2)
#     print("y in p1 1 :{}".format(y.value))
# if __name__=='__main__':
#     x =2 
#     y = multiprocessing.Value('i',3)
#     p1 = multiprocessing.Process(target=f,args=(x,y))
#     p1.start()
#     p1.join()
#     print("y in main :{}".format(y.value))