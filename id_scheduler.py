import schedule 
import time
import math

from itertools import cycle


def id_list_generator(start,end):

	account_ids = []

	for i in range(start,end):

		account_ids.append(i)

	return account_ids


def get_load_spreaded(ids_to_spread,schedule_minutes): 

	"""
	Inputs type: 
		ids_to_spreat = list
		schedule_minutes = int
	Output type: iterator 
	
	Constraints:
		schedule_minutes >= 15
	"""

	account_ids_to_return = []

	# Creates the minimal size of the spread to divide 
	# id list in order to match schedule minutes
	spread = math.ceil(len(ids_to_spread)/schedule_minutes)

	# Creates a matrix with the spreads
	for i in range(0,len(ids_to_spread),spread):

		account_ids_to_return.append(ids_to_spread[i:i+spread])
	
	# cycle creates an iterator that can be looped infinitely
	return cycle(account_ids_to_return)


def get_account_ids_to_run(account_ids_to_return):

	print(next(account_ids_to_return))


if __name__ == '__main__':

	id_list = id_list_generator(1000,2000)

	# Insert scheduling time in minutes
	schedule_time = 15

	# combine every(0).minutes and time.sleep(60) for scheduling a te top of the minute
	schedule.every(0).minutes.do(get_account_ids_to_run, get_load_spreaded(id_list,schedule_time))


	while True:

		schedule.run_pending()
		time.sleep(60)

