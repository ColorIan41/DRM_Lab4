import do_relations as dr
import copy

#    b1 b2 b3 b4 b5
# a1 [ 0 1 0 0 1           R = {(a1,b2),(a1,b5),(a2,b4),(a3,b4),(a4,b5),(a5,b1),(a5,b2)}
# a2  0 0 0 1 0
# a3  0 0 0 1 0
# a4  0 0 0 0 1
# a5  1 1 0 0 0 ]

R = [[0, 1, 0, 0, 1],
     [0, 0, 0, 1, 0],
     [0, 0, 0, 1, 0],
     [0, 0, 0, 0, 1],
     [1, 1, 0, 0, 0]]

if dr.is_reflexive(R) and dr.is_symmetric(R) and dr.is_transitive(R):
    print(R, "є відношенням еквівалентності")
else:
    print(R, "\nReflective: ", dr.is_reflexive(R), "\nSymmetric: ", dr.is_symmetric(R), "\nTransivity: ",
          dr.is_transitive(R), "\nВідношення не є еквівалентним\n")

if dr.is_reflexive(R) and dr.is_antisymmetric(R) and dr.is_transitive(R):
    print(R, "є відношенням часткового порядку")
else:
    print(R, "\nReflective: ", dr.is_reflexive(R), "\nAntiSymmetric: ", dr.is_symmetric(R), "\nTransivity: ",
          dr.is_transitive(R), "\nВідношення не є частковим порядком\n")

if dr.is_irreflexive(R) and dr.is_transitive(R):
    print(R, "є відношенням строгого порядку")
else:
    print(R, "\nReflective: ", dr.is_reflexive(R), "\nTransivity: ", dr.is_transitive(R),
          "\nВідношення не є строгим порядком\n")

if not dr.is_reflexive(R):
    ref = copy.deepcopy(R)
    print(dr.make_reflective(ref), " - рефлексивне замикання")
if not dr.is_symmetric(R):
    sym = copy.deepcopy(R)
    print(dr.make_symmetric(sym), " - симетричне замикання")
if not dr.is_transitive(R):
    tr = copy.deepcopy(R)
    print(dr.make_transitive(tr), " - транзитивне замикання")
power2 = copy.deepcopy(R)
power3 = copy.deepcopy(R)
print("\nДругий степінь відношення: ", dr.power(power2, 2))
print("Третій степінь відношення: ", dr.power(power3, 3))
