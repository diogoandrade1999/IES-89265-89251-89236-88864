import argparse
import random
from datetime import datetime, date


users = {
		'Diogo': {'start': '2019-07-01', 'days_per_week': 1.5, 'age': 20, 'weight': 61},
		'André': {'start': '2008-11-01', 'days_per_week': 3, 'age': 40, 'weight': 83},
		'Gonçalo': {'start': '2019-10-01', 'days_per_week': 1, 'age': 20, 'weight': 67},
		'João': {'start': '2015-01-01', 'days_per_week': 2.5, 'age': 20, 'weight': 75}
		}

type_exercises = ['legs', 'cardio', 'back', 'biceps', 'chest', 'triceps']

machines = {
			'legs': ['Horizontal seated leg press', 'Hanging leg raise', 'Leg extension machine', 'Seated leg curl'], 
			'back': ['Lat pulldown', 'Low-pulley cable bench'], 
			'biceps': ['Cable biceps bar'], 
			'triceps': ['Cable triceps bar', 'triceps pushdown'], 
			'chest': ['Chest press', 'Pec deck or chest flye'],
			'cardio': ['Rowing machine'],
			}


initial_weight = lambda p: p/2


def calc_weeks(start_date):
	actual_date = str(date.today())
	d1 = datetime.strptime(actual_date, "%Y-%m-%d")
	d2 = datetime.strptime(start_date, "%Y-%m-%d")
	return (d1 - d2).days / 7


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
	trainings = int(calc_weeks(stats['start']) * stats['days_per_week'])
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
			exercise = {'repetitions': repetitions, 'Weight': weight}
			exercises.append(exercise)
			weight = round(initial_weight(stats['weight']) * (calc_weight(level) - (repetitions * reduction_weight(stats['age']))), 2)
			time += repetitions
		time += random.randint(1, time)
		total_time -= time
		mydict = {
				'name': name,
				'date': str(date.today()),
				'time': time,
				'type': type_exercise,
				'machine': machine,
				'exercises' : exercises
				}
		dicts.append(mydict)
	return dicts, bad_choice


def main():
	for name in users:
		for k in range(number):
			dicts, bad_choice = generate(name)
			print(dicts)
		if see: print(bad_choice)


if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Generate data!')
	parser.add_argument('-n', default=1, type=int)
	parser.add_argument('-s', nargs='?', const=True, default=False, type=bool)
	args = parser.parse_args()

	number = args.n
	see = args.s

	main()