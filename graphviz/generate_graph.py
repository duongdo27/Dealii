def create_relation(main_project, sub_projects):
    result = ""
    for sub_project in sub_projects:
        result = result + '\t{} -> {} [label = ""];\n'.format(main_project, sub_project)
    return result


def generate_relation(inputfile):
    result = ""
    with open(inputfile) as f:
        lines = f.readlines()
        for line in lines:
            ls = line.strip('\n').split(',')

            main_project = ls[0]
            sub_projects = ls[1:]
            result += create_relation(main_project, sub_projects)
    return result


def write_to_dot_file(inputfile, outputfile):
    result = """digraph finite_state {
    rankdir=LR;
    node [shape = circle];\n"""
    result += generate_relation(inputfile)
    result += "}"
    output = open(outputfile, 'w')
    output.write(result)
    output.close()


write_to_dot_file("trees.csv", "grap2.dot")