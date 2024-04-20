def main():
    print("""This program is an implementation of the Rosenberg
Self-Esteem Scale. This program will show you ten
statements that you could possibly apply to yourself.
Please rate how much you agree with each of the
statements by responding with one of these four letters:

D means you strongly disagree with the statement.
d means you disagree with the statement.
a means you agree with the statement.
A means you strongly agree with the statement.""")
    scores = []
    print('1. I feel that I am a person of worth, at least on an equal plane with others.')
    scores.append(positive_question('   Enter D, d, a, or A:  '))
    print('2. I feel that I have a number of good qualities.')
    scores.append(positive_question('   Enter D, d, a, or A:  '))
    print('3. All in all, I am inclined to feel that I am a failure.')
    scores.append(negative_question('   Enter D, d, a, or A:  '))
    print('4. I am able to do things as well as most other people.')
    scores.append(positive_question('   Enter D, d, a, or A:  '))
    print('5. I feel I do not have much to be proud of.')
    scores.append(negative_question('   Enter D, d, a, or A:  '))
    print('6. I take a positive attitude toward myself.')
    scores.append(positive_question('   Enter D, d, a, or A:  '))
    print('7. On the whole, I am satisfied with myself.')
    scores.append(positive_question('   Enter D, d, a, or A:  '))
    print('8. I wish I could have more respect for myself.')
    scores.append(negative_question('   Enter D, d, a, or A:  '))
    print('9. I certainly feel useless at times.')
    scores.append(negative_question('   Enter D, d, a, or A:  '))
    print('10. At times I think I am no good at all.')
    scores.append(negative_question('   Enter D, d, a, or A:  '))
    total_score = 0
    for score in scores:
        total_score += score
    print(f'Your score is: {total_score}')
    print('A score below 15 may indicate problematic low self-esteem.')


    

def positive_question(question):
    letter = ''
    while letter != 'A' or letter != 'a' or letter != 'd' or letter != 'D':
        letter = input(question)
        if letter == 'A':
            score = 3
            break
        elif letter == 'a':
            score = 2
            break
        elif letter == 'd':
            score = 1
            break
        elif letter == 'D':
            score = 0
            break
        print('Not a valid option!')
    return score

def negative_question(question):
    letter = ''
    while letter != 'A' or letter != 'a' or letter != 'd' or letter != 'D':
        letter = input(question)
        if letter == 'A':
            score = 0
            break
        elif letter == 'a':
            score = 1
            break
        elif letter == 'd':
            score = 2
            break
        elif letter == 'D':
            score = 3
            break
        print('Not a valid option!')
    return score


main()