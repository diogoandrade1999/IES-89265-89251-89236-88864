import argparse
import random
import time
import pika
from datetime import datetime, date, timedelta
import pprint


users = {
		'Diogo': {'start': '2019-07-01', 'days_per_week': 1.5, 'age': 20, 'weight': 61},
		'André': {'start': '2008-11-01', 'days_per_week': 3, 'age': 40, 'weight': 83},
		'Gonçalo': {'start': '2019-10-01', 'days_per_week': 1, 'age': 20, 'weight': 67},
		'João': {'start': '2015-01-01', 'days_per_week': 2.5, 'age': 20, 'weight': 75},
		'Alberto': {'start': '2018-10-01', 'days_per_week': 4, 'age': 70, 'weight': 73}
		}

type_exercises = ['legs', 'cardio', 'back', 'biceps', 'chest', 'triceps', 'shoulders']

machines = {
			'legs': ['Horizontal seated leg press', 'Hanging leg raise', 'Leg extension machine', 'Seated leg curl'], 
			'back': ['Lat pulldown', 'Low-pulley cable bench'], 
			'biceps': ['Cable biceps bar'], 
			'triceps': ['Cable triceps bar', 'triceps pushdown'], 
			'chest': ['Chest press', 'Pec deck or chest flye'],
			'cardio': ['Rowing machine'],
			'shoulders': ['']
			}

heartbeat_age = {20: [100, 170], 30: [95, 162], 35: [93, 157], 40: [90, 153], 45: [88, 149],
				50: [85, 145], 55: [83, 140], 60: [80, 136], 65: [78, 132], 70: [75, 128]}

initial_weight = lambda p: p/2


def get_heartbeat_age(age):
	if age <= 20: return 20
	if age <= 30: return 30
	if age <= 35: return 35
	if age <= 40: return 40
	if age <= 45: return 45
	if age <= 50: return 50
	if age <= 55: return 55
	if age <= 60: return 60
	if age <= 65: return 65
	return 70

def random_date(start, end):
    days = random.randint(0, (end - start).days)
    hours = random.randint(9, 20)
    minutes = random.randint(0, 59)
    seconds = random.randint(0, 60)
    return start + timedelta(days=days, hours=hours, minutes=minutes, seconds=seconds)


def calc_weeks(start_date):
	actual_date = str(date.today())
	d1 = datetime.strptime(actual_date, "%Y-%m-%d")
	d2 = datetime.strptime(start_date, "%Y-%m-%d")
	if arg_time: d3 = random_date(d1, d1)
	else: d3 = random_date(d2, d1)
	weeks = (d3 - d2).days / 7
	return d3, weeks


def get_level(trainings):
	if trainings < 30: return 1
	if trainings < 90: return 2
	if trainings < 250: return 3
	if trainings < 500: return 4
	return 5


def choose_exercise(level, exercise):
	if level in [4, 5]: return exercise
	if exercise == 'legs': return type_exercises[random.randint(0,1)]
	if level == 3: return exercise
	if exercise == 'back': return type_exercises[random.randint(2,3)]
	if exercise == 'chest': return type_exercises[random.randint(4,5)]
	return exercise


def calc_weight(level):
	if level == 1: return 1.1
	if level == 2: return 1.3
	if level == 3: return 1.5
	if level == 4: return 1.6
	return 1.7


def reduction_weight(age):
	if age >= 40: return 0.15
	elif age >= 50: return 0.55
	elif age >= 70: return 0.75
	return 0.05


def generate(name):
	bad_choice = []
	dicts = []
	stats = users[name]
	date, weeks = calc_weeks(stats['start'])
	trainings = int(weeks * stats['days_per_week'])
	level = get_level(trainings)
	weight = round(initial_weight(stats['weight']) * (calc_weight(level) - reduction_weight(stats['age'])), 2)
	total_time = random.randint(45,75)
	while total_time > 0:
		exercises = []
		time = 0
		choose = type_exercises[random.randint(0,5)]
		type_exercise = choose_exercise(level, choose)
		machine = machines[type_exercise][random.randint(0,len(machines[type_exercise])-1)]
		if type_exercise != choose: bad_choice += [[name, choose, type_exercise]]
		for x in range(random.randint(1,3)):
			repetitions = random.randint(3,5)
			exercise = {'repetitions': repetitions, 'weight': weight}
			exercises.append(exercise)
			weight = round(initial_weight(stats['weight']) * (calc_weight(level) - (repetitions * reduction_weight(stats['age']))), 2)
			time += repetitions
		time += random.randint(1, time)
		total_time -= time
		heartbeat = heartbeat_age[get_heartbeat_age(stats['age'])]
		mydict = {
				'user': name,
				'date': date.strftime('%Y-%m-%d %H:%M:%S'),
				'type': type_exercise,
				'machine': machine,
				'exercises': exercises,
				'heartbeat': random.randint(heartbeat[0], heartbeat[1])
				}
		date += timedelta(minutes=time)
		dicts.append(mydict)
	return dicts, bad_choice


def main():
	for name in users:
		bad_choices = []
		if name == arg_name:
			for k in range(number):
				dicts, bad_choice = generate(name)
				pprint.pprint(dicts)
				bad_choices += [bad_choice]
				time.sleep(1)
				channel.basic_publish(exchange='',
									routing_key='population',
									body=str(dicts))
			if see: print(bad_choices)
			break


if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Generate data!')
	parser.add_argument('name', type=str, help='Name')
	parser.add_argument('-n', default=1, type=int)
	parser.add_argument('-s', nargs='?', const=True, default=False, type=bool)
	parser.add_argument('-t', nargs='?', const=True, default=False, type=bool)
	args = parser.parse_args()

	arg_name = args.name
	number = args.n
	see = args.s
	arg_time = args.t

	connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
	channel = connection.channel()

	main()

	connection.close()
