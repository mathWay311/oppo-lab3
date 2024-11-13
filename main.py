import math

class Figure:

    author: str
    density: float
    typestr = "none"

    def __init__(self, _density, _author):
        self.author =   _author
        self.density =  _density


    def get_mass(self):
        return None



class Sphere(Figure):

    radius: int
    typestr = "sphere"

    def __init__(self, _density, _author, _radius):
        self.radius = _radius
        super().__init__(_density, _author)

    def get_mass(self):
        return float(4/3 * math.pi * self.radius * self.radius * self.radius)



class Cuboid(Figure):

    a: int
    b: int
    c: int
    typestr = "cuboid"

    def __init__(self, _density, _author, _a, _b, _c):
        self.a = _a
        self.b = _b
        self.c = _c
        super().__init__(_density, _author)

    def get_mass(self):
        return float(self.density * self.a * self.b * self.c)



class Cylinder(Figure):

    r: int
    h: int
    typestr = "cylind"

    def __init__(self, _density, _author, _r, _h):
        self.r = _r
        self.h = _h
        super().__init__(_density, _author)

    def get_mass(self):
        return float(self.density * math.pi * self.r * 2 * self.h)



def print_add_invalid_syntax_warning():
    print("ERR! Invalid syntax. ADD syntax: ")
    print("ADD -t <type> -d <density> -a <author> [OPTIONAL: (-r <radius>) OR (-A <side_1> -B <side_2> -C <side_3>) OR (-r <radius> -h <height>)] ")


def print_invalid_syntax_warning():
    print("ERR! Invalid syntax.")


def print_rem_invalid_syntax_warning():
    print("ERR! Invalid syntax. REM syntax: ")
    print("REM ( OPTIONAL: -t [<type>] separated by ',') ( OPTIONAL: -d <density>[>/</=]<value>) ( OPTIONAL: -a [<author>] separated by ',') ( OPTIONAL: -m <density>[>/</=]<value>)")


def type_in_list(collection_elem, types: list):
    if collection_elem.typestr in types:
        return True
    return False


def auth_in_list(collection_elem, auths: list):
    if collection_elem.author in auths:
        return True
    return False

collection = []
collection.append(Cylinder(10, "mathway", 1, 2))
collection.append(Cuboid(12, "me", 1, 2, 3))
collection.append(Sphere(14, "mathway", 33))
collection.append(Cylinder(10, "mathway", 1, 2))
collection.append(Cuboid(12, "me", 1, 2, 3))
collection.append(Sphere(14, "mathway", 33))

while True:
    print(">>> ", end="")
    cmd = input()

    args = cmd.split(" ")

    if args[0] == "PRINT":
        print("Printing objects from collection...")
        print("TYPESTR\t\tDENSITY\t\tAUTHOR\t\tMASS")
        for obj in collection:
            print(obj.typestr, end="\t\t")
            print(obj.density, end="\t\t")
            print(obj.author, end="\t\t")
            print(obj.get_mass(), end="\n")

    elif args[0] == "ADD":
        try:
            print("Adding...")
            if len(args) < 7:
                print_add_invalid_syntax_warning()
                continue

            if args[1] != "-t":
                print_add_invalid_syntax_warning()
                continue

            if args[2] not in ["none", "sphere", "cuboid", "cylind"]:
                print("ERR! Invalid type. ADD types: ")
                print("'none', 'sphere', 'cuboid', 'cylind' ")
                continue
            typestr = args[2]

            if args[3] != "-d":
                print_add_invalid_syntax_warning()
                continue

            try:
                density = float(args[4])
            except:
                print("ERR! Invalid density. Density should be of type FLOAT (e.g 123.456)")
                continue

            if args[5] != "-a":
                print_add_invalid_syntax_warning()
            author = args[6]


            if typestr == "none":
                new_obj = Figure(density, author)
                collection.append(new_obj)
                continue

            if typestr == "sphere":
                if len(args) < 8:
                    print_add_invalid_syntax_warning()
                    continue

                if args[7] != "-r":
                    print_add_invalid_syntax_warning()
                    continue
                try:
                    radius = int(args[8])
                except:
                    print("ERR! Invalid radius. Radius should be of type INT (e.g 100500)")
                    continue

                new_obj = Sphere(density, author, radius)
                collection.append(new_obj)
                continue

            if typestr == "cuboid":
                if args[7] != "-A":
                    print_add_invalid_syntax_warning()
                    continue
                try:
                    a = int(args[8])
                except:
                    print("ERR! Invalid side length. Should be of type INT (e.g 100500)")
                    continue

                if args[9] != "-B":
                    print_add_invalid_syntax_warning()
                    continue
                try:
                    b = int(args[10])
                except:
                    print("ERR! Invalid side length. Should be of type INT (e.g 100500)")
                    continue

                if args[11] != "-C":
                    print_add_invalid_syntax_warning()
                    continue
                try:
                    c = int(args[12])
                except:
                    print("ERR! Invalid side length. Should be of type INT (e.g 100500)")
                    continue

                new_obj = Cuboid(density, author, a, b, c)
                collection.append(new_obj)
                continue

            if typestr == "cylind":
                if args[7] != "-r":
                    print_add_invalid_syntax_warning()
                    continue
                try:
                    r = int(args[8])
                except:
                    print("ERR! Invalid radius. Should be of type INT (e.g 100500)")
                    continue

                if args[9] != "-h":
                    print_add_invalid_syntax_warning()
                    continue
                try:
                    h = int(args[10])
                except:
                    print("ERR! Invalid height. Should be of type INT (e.g 100500)")
                    continue

                new_obj = Cylinder(density, author, r, h)
                collection.append(new_obj)
                continue

        except:
            print_add_invalid_syntax_warning()
            continue

    elif args[0] == "REM":
        if (not "-t" in args) and (not "-d" in args) and (not "-a" in args) and (not "-m" in args):
            print_rem_invalid_syntax_warning()
            continue

        items_to_delete = []
        if "-t" in args:
            index = args.index("-t")
            regexp = args[index + 1]
            types = regexp.split(",")

            for item in collection:
                if type_in_list(item, types):
                    if not item in items_to_delete:
                        items_to_delete.append(item)

        if "-d" in args:
            index = args.index("-d")
            regexp = args[index + 1]
            operator = args[index + 1][0]
            density = int(args[index + 1][1:])

            if operator == ">":
                for item in collection:
                    if item.density > density:
                        if not item in items_to_delete:
                            items_to_delete.append(item)
            if operator == "<":
                for item in collection:
                    if item.density < density:
                        if not item in items_to_delete:
                            items_to_delete.append(item)
            if operator == "=":
                for item in collection:
                    if item.density == density:
                        if not item in items_to_delete:
                            items_to_delete.append(item)

        if "-a" in args:
            index = args.index("-a")
            regexp = args[index + 1]
            types = regexp.split(",")

            for item in collection:
                if auth_in_list(item, types):
                    if not item in items_to_delete:
                        items_to_delete.append(item)

        if "-m" in args:
            index = args.index("-m")
            regexp = args[index + 1]
            operator = args[index + 1][0]
            mass = int(args[index + 1][1:])

            if operator == ">":
                for item in collection:
                    if item.get_mass() > mass:
                        if not item in items_to_delete:
                            items_to_delete.append(item)
            if operator == "<":
                for item in collection:
                    if item.get_mass() < mass:
                        if not item in items_to_delete:
                            items_to_delete.append(item)
            if operator == "=":
                for item in collection:
                    if item.get_mass() == mass:
                        if not item in items_to_delete:
                            items_to_delete.append(item)


        for item in items_to_delete:
            collection.remove(item)

        print("Success")


    else:
        print(">>> Invalid command. Try again")



