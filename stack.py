class Stack:

    def __init__(self, *args) -> None:
        self.stack = list(*args)

    def isEmpty(self) -> bool:
        if not self.stack:
            return True
        return False

    def push(self, value) -> None:
        self.stack.insert(0, value)

    def peek(self):
        return self.stack[0]

    def size(self) -> int:
        return len(self.stack)

    def pop(self):
        self.stack.pop(0)
        if self.isEmpty:
            return self.stack[0]


def pop_from_2_stacks(stack_1, stack_2):
    stack_1.pop()
    stack_2.pop()


def couple_value(peek_1, peek_2):
    if peek_1 == '(' and peek_2 == ')':
        return True
    elif peek_1 == '[' and peek_2 == ']':
        return True
    elif peek_1 == '{' and peek_2 == '}':
        return True
    return False


def checking(orig, temp):
    temp.push(orig.peek())
    p_temp = temp.peek()
    orig.pop()
    if orig.isEmpty():
        p_orig = orig.peek()
    else:
        if not temp.isEmpty():
            print('Сбалансированно')
            exit()
        else:
            print('Несбалансированно')
            exit()
    if couple_value(p_temp, p_orig):
        pop_from_2_stacks(temp, orig)
    return orig, temp


def is_ok(orig, temp):
    sum_of_sizes = orig.size() + temp.size()
    if sum_of_sizes == 0:
        print('Сбалансированно')
        return False
    if (sum_of_sizes % 2) != 0:
        print('Несбалансированно')
        return False
    return True

if __name__=='__main__':
    brackets_line = '[([])((([[[]]])))]{()}'
    temp_stack = Stack()
    orig_stack = Stack(list(brackets_line))

    while is_ok(orig_stack, temp_stack):
        orig_stack, temp_stack = checking(orig_stack, temp_stack)
