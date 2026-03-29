import time
from os import path
from sys import argv

def isint(string):
    try:
        int(string)
        return True
    except:
        return False
    
def rect(string):
    lines = string.split('\n')
    width = max(len(line) for line in lines)
    return '\n'.join(line.ljust(width, ' ') for line in lines)


def stueued(code: str, speed: int =10): 
    lines = rect(code).split('\n')
    pointer = [0, 0]
    pointervel = [1, 0]
    stack = []
    queue = []
    while True:
        time.sleep(1/speed)
        try:
            cell = lines[pointer[1]][pointer[0]]
            if cell == '>':
                pointervel = [1, 0]
            elif cell == '<':
                pointervel = [-1, 0]
            elif cell == 'v':
                pointervel = [0, 1]
            elif cell == '^':
                pointervel = [0, -1]
            elif cell == '#':
                stack.append(0)
            elif cell.isdigit():
                num = stack.pop()*10
                num += int(cell)
                stack.append(num)
            elif cell == ':':
                stack.append(stack[-1])
            elif cell == '!':
                print(chr(stack.pop()), end='')
            elif cell == '?':
                print(stack[-1], end='')
                stack.pop()
            elif cell == '$':
                inp = input()
                if not inp:
                    stack.append(0)
                else:
                    stack.append(ord(inp))
            elif cell == '@':
                inp = input()
                if isint(inp):
                    stack.append(int(inp))
                else:
                    stack.append(0)
            elif cell == 'X':
                if stack.pop() == 0:
                    pointer[0] += pointervel[0]
                    pointer[1] += pointervel[1]
            elif cell == '+':
                b = stack.pop()
                a = stack.pop()
                stack.append(a + b)
            elif cell == '-':
                b = stack.pop()
                a = stack.pop()
                stack.append(a - b)
            elif cell == '*':
                b = stack.pop()
                a = stack.pop()
                stack.append(a * b)
            elif cell == '/':
                b = stack.pop()
                a = stack.pop()
                stack.append(a // b)
            elif cell == '%':
                b = stack.pop()
                a = stack.pop()
                stack.append(a % b)
            elif cell == '~':
                stack.pop()
            elif cell == '.':
                queue.append(stack.pop())
            elif cell == ',':
                stack.append(queue.pop(0))
            pointer[0] += pointervel[0]
            pointer[1] += pointervel[1]
            #print(stack, queue, pointer)
        except Exception as e:
            print(e)
            break

if __name__ == '__main__':
    if len(argv) > 1:
        if path.exists(argv[1]):
            with open(argv[1], 'r') as f:
                stueued(f.read())
