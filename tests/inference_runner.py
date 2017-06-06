from frontend.pre_analysis import PreAnalyzer
from frontend.stmt_inferrer import *
import frontend.z3_types as z3_types
import ast

r = open("tests/inference/test.py")
t = ast.parse(r.read())

analyzer = PreAnalyzer(t)


config = analyzer.get_all_configurations()
solver = z3_types.TypesSolver(config)

context = Context()
for stmt in t.body:
    infer(stmt, context, solver)

solver.push()
check = solver.check(solver.assertions_vars)

if check == z3_types.unsat:
    print("Check: unsat")
    print([solver.assertions_errors[x] for x in solver.unsat_core()])
else:
    solver.optimize.check()
    model = solver.optimize.model()
    for v in sorted(context.types_map):
        z3_t = context.types_map[v]
        print("{}: {}".format(v, model[z3_t]))

