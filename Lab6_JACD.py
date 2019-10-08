import json
import random


def person_stats(number_people):
    for x in range(0, number_people+1):
        x += 1
        # ///// This first section of code creates random values for each attribute and adds it to a dictionary \\\\\
        # If you want to play around with it, simply uncomment the code between the hashtag lines, and then comment out
        # the code between the @ lines
        #####################################################################
        # person_dict = {'Person': {'Number': x, 'Score': 0, '10 Year Risk': 0}}
        #
        # # Randomly decides the age of the person
        # age = round(random.uniform(20, 79))
        # person_dict['Person']['Age'] = age
        #
        # # Randomly decided whether the person is male or female
        # male_female = round(random.uniform(0, 1))
        # if male_female == 1:
        #     person_dict['Person']['Sex'] = 'Male'
        # else:
        #     person_dict['Person']['Sex'] = 'Female'
        #
        # # Randomly decides their Cholesterol level
        # cholesterol = round(random.uniform(160, 280))
        # person_dict['Person']['Cholesterol Level'] = cholesterol
        #
        # # Randomly decides whether or not the person is a smoker
        # smoker_nonsmoker = round(random.uniform(0, 1))
        # if smoker_nonsmoker == 1:
        #     person_dict['Person']['Smoker?'] = 'Smoker'
        # else:
        #     person_dict['Person']['Smoker?'] = 'Nonsmoker'
        #
        # # Randomly decides the HDL level of the person
        # hdl = round(random.uniform(60, 40))
        # person_dict['Person']['HDL'] = hdl
        #
        # # Randomly decides the Systolic Blood Pressure of a person
        # systolic_bp = round(random.uniform(120, 160))
        # person_dict['Person']['Systolic BP'] = systolic_bp
        #
        # # Randomly decides whether or not the person has been treated
        # treated_untreated = round(random.uniform(0, 1))
        # if treated_untreated == 1:
        #     person_dict['Person']['Treated?'] = 'Treated'
        # else:
        #     person_dict['Person']['Treated?'] = 'Untreated'
        ####################################################################
        # \\\\\ End of attribute randomizer /////

        # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        # First, to ask for input from the user
        sex = input("What is the sex of the person? Please enter Male or Female: ")
        age = int(input("What is the age of the person:  "))
        cholesterol = int(input("What is the cholesterol level of the person: "))
        smoker = input("Is the person a Smoker or a Nonsmoker: ")
        hdl = int(input("What is the person's HDL level: "))
        systolic_bp = int(input("What is the person's Systolic Blood Pressure: "))
        treated = input("Finally, is the person Treated or Untreated: ")

        # Next, initialize the person_dict dictionary
        person_dict = {'Person': {'Number': x, 'Score': 0, '10 Year Risk': 0}}


        # Next, to update the dictionary values
        person_dict['Person']['Age'] = age
        person_dict['Person']['Sex'] = sex
        person_dict['Person']['Cholesterol Level'] = cholesterol
        person_dict['Person']['Smoker?'] = smoker
        person_dict['Person']['HDL'] = hdl
        person_dict['Person']['Systolic BP'] = systolic_bp
        person_dict['Person']['Treated?'] = treated
        # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


        total_score = 0

        # First section is for Males
        if person_dict['Person']['Sex'] == 'Male':
            # This section of code will determine their point score base on age
            if 20 <= person_dict['Person']['Age'] <= 34:
                total_score += -9
            elif 35 <= person_dict['Person']['Age'] <= 39:
                total_score += -4
            elif 40 <= person_dict['Person']['Age'] <= 44:
                total_score += 0
            elif 45 <= person_dict['Person']['Age'] <= 49:
                total_score += 3
            elif 50 <= person_dict['Person']['Age'] <= 54:
                total_score += 6
            elif 55 <= person_dict['Person']['Age'] <= 59:
                total_score += 8
            elif 60 <= person_dict['Person']['Age'] <= 64:
                total_score += 10
            elif 65 <= person_dict['Person']['Age'] <= 69:
                total_score += 11
            elif 70 <= person_dict['Person']['Age'] <= 74:
                total_score += 12
            elif 75 <= person_dict['Person']['Age'] <= 79:
                total_score += 13

            # Next, we'll determine their point score based on Cholesterol level and age
            if person_dict['Person']['Cholesterol Level'] < 160:
                total_score += 0
            if 160 < person_dict['Person']['Cholesterol Level'] <= 199:
                if 20 <= person_dict['Person']['Age'] <= 39:
                    total_score -= 4
                elif 40 <= person_dict['Person']['Age'] <= 49:
                    total_score -= 3
                elif 50 <= person_dict['Person']['Age'] <= 59:
                    total_score += 2
                elif 60 <= person_dict['Person']['Age'] <= 69:
                    total_score += 1
                elif 70 <= person_dict['Person']['Age'] <= 79:
                    total_score += 0
            elif 200 < person_dict['Person']['Cholesterol Level'] <= 239:
                if 20 <= person_dict['Person']['Age'] <= 39:
                    total_score -= 7
                elif 40 <= person_dict['Person']['Age'] <= 49:
                    total_score -= 5
                elif 50 <= person_dict['Person']['Age'] <= 59:
                    total_score += 3
                elif 60 <= person_dict['Person']['Age'] <= 69:
                    total_score += 1
                elif 70 <= person_dict['Person']['Age'] <= 79:
                    total_score += 0
            elif 240 < person_dict['Person']['Cholesterol Level'] <= 279:
                if 20 <= person_dict['Person']['Age'] <= 39:
                    total_score -= 9
                elif 40 <= person_dict['Person']['Age'] <= 49:
                    total_score -= 6
                elif 50 <= person_dict['Person']['Age'] <= 59:
                    total_score += 4
                elif 60 <= person_dict['Person']['Age'] <= 69:
                    total_score += 2
                elif 70 <= person_dict['Person']['Age'] <= 79:
                    total_score += 1
            elif person_dict['Person']['Cholesterol Level'] > 280:
                if 20 <= person_dict['Person']['Age'] <= 39:
                    total_score -= 11
                elif 40 <= person_dict['Person']['Age'] <= 49:
                    total_score -= 8
                elif 50 <= person_dict['Person']['Age'] <= 59:
                    total_score += 5
                elif 60 <= person_dict['Person']['Age'] <= 69:
                    total_score += 3
                elif 70 <= person_dict['Person']['Age'] <= 79:
                    total_score += 1

            # Next, we'll determine their point score based on whether or not they have smoked and their age
            if person_dict['Person']['Smoker?'] == 'Smoker':
                if 20 <= person_dict['Person']['Age'] <= 39:
                    total_score -= 8
                elif 40 <= person_dict['Person']['Age'] <= 49:
                    total_score -= 5
                elif 50 <= person_dict['Person']['Age'] <= 59:
                    total_score += 3
                elif 60 <= person_dict['Person']['Age'] <= 69:
                    total_score += 1
                elif 70 <= person_dict['Person']['Age'] <= 79:
                    total_score += 1
            if person_dict['Person']['Smoker?'] == 'Nonsmoker':
                total_score += 0

            # Next, we'll determine their point score based on their HDL level
            if person_dict['Person']['HDL'] >= 60:
                total_score += -1
            elif 50 < person_dict['Person']['HDL'] < 59:
                total_score += 0
            elif 40 < person_dict['Person']['HDL'] < 49:
                total_score += 1
            elif person_dict['Person']['HDL'] < 40:
                total_score += 2

            # And finally, we'll determine their score based on their Systolic Bp and whether or not they have been
            # treated
            if person_dict['Person']['Treated?'] == 'Treated':
                if person_dict['Person']['Systolic BP'] < 120:
                    total_score += 0
                if 120 <= person_dict['Person']['Systolic BP'] <= 129:
                    total_score += 1
                if 130 <= person_dict['Person']['Systolic BP'] <= 139:
                    total_score += 2
                if 140 <= person_dict['Person']['Systolic BP'] <= 149:
                    total_score += 2
                if 150 <= person_dict['Person']['Systolic BP'] <= 159:
                    total_score += 3
            if person_dict['Person']['Treated?'] == 'Untreated':
                if person_dict['Person']['Systolic BP'] < 120:
                    total_score += 0
                if 120 <= person_dict['Person']['Systolic BP'] <= 129:
                    total_score += 0
                if 130 <= person_dict['Person']['Systolic BP'] <= 139:
                    total_score += 1
                if 140 <= person_dict['Person']['Systolic BP'] <= 149:
                    total_score += 1
                if 150 <= person_dict['Person']['Systolic BP'] <= 159:
                    total_score += 2

            # Next, we'll determine the 10 Year Risk percentage based on their total score
            if person_dict['Person']['Score'] < 0:
                person_dict['Person']['10 Year Risk'] = '<1%'
            elif person_dict['Person']['Score'] == 0:
                person_dict['Person']['10 Year Risk'] = '1%'
            elif person_dict['Person']['Score'] == 1:
                person_dict['Person']['10 Year Risk'] = '1%'
            elif person_dict['Person']['Score'] == 2:
                person_dict['Person']['10 Year Risk'] = '1%'
            elif person_dict['Person']['Score'] == 3:
                person_dict['Person']['10 Year Risk'] = '1%'
            elif person_dict['Person']['Score'] == 4:
                person_dict['Person']['10 Year Risk'] = '1%'
            elif person_dict['Person']['Score'] == 5:
                person_dict['Person']['10 Year Risk'] = '2%'
            elif person_dict['Person']['Score'] == 6:
                person_dict['Person']['10 Year Risk'] = '2%'
            elif person_dict['Person']['Score'] == 7:
                person_dict['Person']['10 Year Risk'] = '3%'
            elif person_dict['Person']['Score'] == 8:
                person_dict['Person']['10 Year Risk'] = '4%'
            elif person_dict['Person']['Score'] == 9:
                person_dict['Person']['10 Year Risk'] = '5%'
            elif person_dict['Person']['Score'] == 10:
                person_dict['Person']['10 Year Risk'] = '6%'
            elif person_dict['Person']['Score'] == 11:
                person_dict['Person']['10 Year Risk'] = '8%'
            elif person_dict['Person']['Score'] == 12:
                person_dict['Person']['10 Year Risk'] = '10%'
            elif person_dict['Person']['Score'] == 13:
                person_dict['Person']['10 Year Risk'] = '12%'
            elif person_dict['Person']['Score'] == 14:
                person_dict['Person']['10 Year Risk'] = '16%'
            elif person_dict['Person']['Score'] == 15:
                person_dict['Person']['10 Year Risk'] = '20'
            elif person_dict['Person']['Score'] == 16:
                person_dict['Person']['10 Year Risk'] = '25%'
            elif person_dict['Person']['Score'] >= 17:
                person_dict['Person']['10 Year Risk'] = '30%'

            person_dict['Person']['Score'] += total_score

        # Second section is for Females
        if person_dict['Person']['Sex'] == 'Female':
            # This section of code will determine their point score base on age
            if 20 <= person_dict['Person']['Age'] <= 34:
                total_score += -7
            elif 35 <= person_dict['Person']['Age'] <= 39:
                total_score += -3
            elif 40 <= person_dict['Person']['Age'] <= 44:
                total_score += 0
            elif 45 <= person_dict['Person']['Age'] <= 49:
                total_score += 3
            elif 50 <= person_dict['Person']['Age'] <= 54:
                total_score += 6
            elif 55 <= person_dict['Person']['Age'] <= 59:
                total_score += 8
            elif 60 <= person_dict['Person']['Age'] <= 64:
                total_score += 10
            elif 65 <= person_dict['Person']['Age'] <= 69:
                total_score += 12
            elif 70 <= person_dict['Person']['Age'] <= 74:
                total_score += 14
            elif 75 <= person_dict['Person']['Age'] <= 79:
                total_score += 16

            # Next, we'll determine their point score based on Cholesterol level and age
            if person_dict['Person']['Cholesterol Level'] < 160:
                total_score += 0
            if 160 < person_dict['Person']['Cholesterol Level'] <= 199:
                if 20 <= person_dict['Person']['Age'] <= 39:
                    total_score -= 4
                elif 40 <= person_dict['Person']['Age'] <= 49:
                    total_score -= 3
                elif 50 <= person_dict['Person']['Age'] <= 59:
                    total_score += 2
                elif 60 <= person_dict['Person']['Age'] <= 69:
                    total_score += 1
                elif 70 <= person_dict['Person']['Age'] <= 79:
                    total_score += 1
            elif 200 < person_dict['Person']['Cholesterol Level'] <= 239:
                if 20 <= person_dict['Person']['Age'] <= 39:
                    total_score -= 8
                elif 40 <= person_dict['Person']['Age'] <= 49:
                    total_score -= 6
                elif 50 <= person_dict['Person']['Age'] <= 59:
                    total_score += 4
                elif 60 <= person_dict['Person']['Age'] <= 69:
                    total_score += 2
                elif 70 <= person_dict['Person']['Age'] <= 79:
                    total_score += 1
            elif 240 < person_dict['Person']['Cholesterol Level'] <= 279:
                if 20 <= person_dict['Person']['Age'] <= 39:
                    total_score -= 11
                elif 40 <= person_dict['Person']['Age'] <= 49:
                    total_score -= 8
                elif 50 <= person_dict['Person']['Age'] <= 59:
                    total_score += 5
                elif 60 <= person_dict['Person']['Age'] <= 69:
                    total_score += 3
                elif 70 <= person_dict['Person']['Age'] <= 79:
                    total_score += 2
            elif person_dict['Person']['Cholesterol Level'] > 280:
                if 20 <= person_dict['Person']['Age'] <= 39:
                    total_score -= 13
                elif 40 <= person_dict['Person']['Age'] <= 49:
                    total_score -= 10
                elif 50 <= person_dict['Person']['Age'] <= 59:
                    total_score += 7
                elif 60 <= person_dict['Person']['Age'] <= 69:
                    total_score += 4
                elif 70 <= person_dict['Person']['Age'] <= 79:
                    total_score += 2

            # Next, we'll determine their point score based on whether or not they have smoked and their age
            if person_dict['Person']['Smoker?'] == 'Smoker':
                if 20 <= person_dict['Person']['Age'] <= 39:
                    total_score -= 9
                elif 40 <= person_dict['Person']['Age'] <= 49:
                    total_score -= 7
                elif 50 <= person_dict['Person']['Age'] <= 59:
                    total_score += 4
                elif 60 <= person_dict['Person']['Age'] <= 69:
                    total_score += 2
                elif 70 <= person_dict['Person']['Age'] <= 79:
                    total_score += 1
            if person_dict['Person']['Smoker?'] == 'Nonsmoker':
                total_score += 0

            # Next, we'll determine their point score based on their HDL level
            if person_dict['Person']['HDL'] >= 60:
                total_score += -1
            elif 50 < person_dict['Person']['HDL'] < 59:
                total_score += 0
            elif 40 < person_dict['Person']['HDL'] < 49:
                total_score += 1
            elif person_dict['Person']['HDL'] < 40:
                total_score += 2

            # And finally, we'll determine their score based on their Systolic Bp and whether or not they have been
            # treated
            if person_dict['Person']['Treated?'] == 'Treated':
                if person_dict['Person']['Systolic BP'] < 120:
                    total_score += 0
                if 120 <= person_dict['Person']['Systolic BP'] <= 129:
                    total_score += 3
                if 130 <= person_dict['Person']['Systolic BP'] <= 139:
                    total_score += 5
                if 140 <= person_dict['Person']['Systolic BP'] <= 149:
                    total_score += 6
                if 150 <= person_dict['Person']['Systolic BP'] <= 159:
                    total_score += 6
            if person_dict['Person']['Treated?'] == 'Untreated':
                if person_dict['Person']['Systolic BP'] < 120:
                    total_score += 0
                if 120 <= person_dict['Person']['Systolic BP'] <= 129:
                    total_score += 1
                if 130 <= person_dict['Person']['Systolic BP'] <= 139:
                    total_score += 2
                if 140 <= person_dict['Person']['Systolic BP'] <= 149:
                    total_score += 3
                if 150 <= person_dict['Person']['Systolic BP'] <= 159:
                    total_score += 4

            # Next, we'll determine the 10 Year Risk percentage based on their total score
            if person_dict['Person']['Score'] < 9:
                person_dict['Person']['10 Year Risk'] = '<1%'
            elif person_dict['Person']['Score'] == 9:
                person_dict['Person']['10 Year Risk'] = '1%'
            elif person_dict['Person']['Score'] == 10:
                person_dict['Person']['10 Year Risk'] = '1%'
            elif person_dict['Person']['Score'] == 11:
                person_dict['Person']['10 Year Risk'] = '1%'
            elif person_dict['Person']['Score'] == 12:
                person_dict['Person']['10 Year Risk'] = '1%'
            elif person_dict['Person']['Score'] == 13:
                person_dict['Person']['10 Year Risk'] = '2%'
            elif person_dict['Person']['Score'] == 14:
                person_dict['Person']['10 Year Risk'] = '2%'
            elif person_dict['Person']['Score'] == 15:
                person_dict['Person']['10 Year Risk'] = '3%'
            elif person_dict['Person']['Score'] == 16:
                person_dict['Person']['10 Year Risk'] = '4%'
            elif person_dict['Person']['Score'] == 17:
                person_dict['Person']['10 Year Risk'] = '5%'
            elif person_dict['Person']['Score'] == 18:
                person_dict['Person']['10 Year Risk'] = '6%'
            elif person_dict['Person']['Score'] == 19:
                person_dict['Person']['10 Year Risk'] = '8%'
            elif person_dict['Person']['Score'] == 20:
                person_dict['Person']['10 Year Risk'] = '11%'
            elif person_dict['Person']['Score'] == 21:
                person_dict['Person']['10 Year Risk'] = '14%'
            elif person_dict['Person']['Score'] == 22:
                person_dict['Person']['10 Year Risk'] = '17%'
            elif person_dict['Person']['Score'] == 23:
                person_dict['Person']['10 Year Risk'] = '22%'
            elif person_dict['Person']['Score'] == 24:
                person_dict['Person']['10 Year Risk'] = '27'
            elif person_dict['Person']['Score'] == 25:
                person_dict['Person']['10 Year Risk'] = '30%'

            person_dict['Person']['Score'] += total_score

        print(json.dumps(person_dict, sort_keys=False, indent=0))
        person_dict.update({'Person': x + 1})

person_stats(10)

