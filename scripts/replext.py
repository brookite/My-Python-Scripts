import builtins
import sys
import importlib.util
import os

if len(sys.argv) > 1:
    file = sys.argv[1]
    if os.path.exists(file):
        filename, ext = os.path.splitext(file)
        if os.path.splitext(file)[-1] == ".py":
            spec = importlib.util.spec_from_file_location(filename, file)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            for name in dir(module):
                if not name.startswith("__"):
                    globals()[name] = module.__getattribute__(name)


class _seq_operator:
    def __init__(self, action, stages, count):
        self.counter = count
        self.stages = stages
        self.action = action

    def __matmul__(self, arg):
        if self.counter - 1 > 0:
            return _seq_operator(self.action, self.stages + [arg], self.counter - 1)
        else:
            return self.action(self.stages + [arg])


map = _seq_operator(lambda args: list(builtins.map(args[0], args[1])), [], 2)
filter = _seq_operator(lambda args: list(builtins.filter(args[0], args[1])), [], 2)


def _call_logic(args):
    if len(args) == 2:
        return args[0](args[1])
    else:
        return args[0](*args[1:])


call = _seq_operator(_call_logic, [], 2)
