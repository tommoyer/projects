import pprint

pp = pprint.PrettyPrinter()


def config(state):
    pp.pprint(state)
    print(f'Called config for plain_text notes')
