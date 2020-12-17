import time


class Timer:

	def __init__(self, function):
		self.function = function

	def __call__(self, num_runs, *args, **kwargs):
		avg_time = 0
		for _ in range(num_runs):
			t0 = time.time()

			self.function(*args, **kwargs)

			t1 = time.time()
			avg_time += (t1 - t0)
		avg_time /= num_runs
		print("Выполнение заняло %.5f секунд" % avg_time)   


@Timer
def f():
	for j in range(1000000):
		pass


if __name__ == '__main__':
	num = input("Enter num: ")
	
	while num!="quit":

		f(int(num))

		num = input("Enter num: ")  