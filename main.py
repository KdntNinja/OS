class SimpleOS:
    def __init__(self):
        self.commands = {
            'echo': self.echo,
            'exit': self.exit
        }

    def echo(self, *args):
        print(' '.join(args))

    def exit(self, *args):
        exit()

    def run(self):
        while True:
            command = input('SimpleOS> ').split()
            if command[0] in self.commands:
                self.commands[command[0]](*command[1:])
            else:
                print(f'Unknown command: {command[0]}')


if __name__ == "__main__":
    os = SimpleOS()
    os.run()
