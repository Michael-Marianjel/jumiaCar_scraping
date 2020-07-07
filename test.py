from multiprocessing.dummy import Pool as ThreadPool

def kgs(link):
  print(link)

car_urls =['kgs', 'wg', 'erh', 'rtj', 'tyk', 'il', 'ui;', 'io', 'op', 'op']
def main():
  pool = ThreadPool(10)
  pool.map(kgs, car_urls)

  # close the pool and wait for the work to finish
  pool.close()
  pool.join()
main()

