import yaml
import os


def yaml_to_header(yaml_path, header_path):
    with open(yaml_path) as f:
        data = yaml.safe_load(f)

    with open(header_path, 'w') as f:
        f.write("#ifndef INST_DATA_H\n#define INST_DATA_H\n\n")
        f.write("// Auto-generated from YAML\n")
        f.write("typedef struct {\n")
        f.write("    const char* name;\n")
        f.write("    const char* long_name;\n")
        f.write("    const char* description;\n")
        f.write("    const char* match;\n")
        f.write("    const char* xs1_loc;\n")
        f.write("    const char* xs2_loc;\n")
        f.write("    const char* xd_loc;\n")
        f.write("    const char* access_s;\n")
        f.write("    const char* access_u;\n")
        f.write("    const char* access_vs;\n")
        f.write("    const char* access_vu;\n")
        f.write("} InstData;\n\n")

        f.write("static InstData inst = {\n")
        f.write(f'    "{data["name"]}",\n')
        f.write(f'    "{data["long_name"]}",\n')
        desc = data["description"].strip().replace("\n", " ").replace('"', '\"')
        f.write(f'    "{desc}",\n')
        f.write(f'    "{data["encoding"]["match"]}",\n')

        vars = {v["name"]: v["location"] for v in data["encoding"]["variables"]}
        f.write(f'    "{vars.get("xs1", "")}",\n')
        f.write(f'    "{vars.get("xs2", "")}",\n')
        f.write(f'    "{vars.get("xd", "")}",\n')

        access = data.get("access", {})
        f.write(f'    "{access.get("s", "")}",\n')
        f.write(f'    "{access.get("u", "")}",\n')
        f.write(f'    "{access.get("vs", "")}",\n')
        f.write(f'    "{access.get("vu", "")}"\n')
        f.write("};\n\n")
        f.write("#endif // INST_DATA_H\n")

def main():
    yaml_to_header("input/add.yaml", "output/inst_data.h")

if __name__ == "__main__":
    main()

