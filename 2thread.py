from threading import Thread

def do_work(start, end, result):
  sum = 0
  for i in range(start, end):
     sum += i
  result.append(sum)
  return

if __name__ == "__main__":
   START, END = 0, 20000000
   result = list()
   th1 = Thread(target=do_work, args=(START, END/2, result))
   th2 = Thread(target=do_work, args=(END/2, END, result))
   th1.start()
   th2.start()
   th1.join()
   th2.join()
   print "Result : ", sum(result)
