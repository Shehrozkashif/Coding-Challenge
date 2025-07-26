#ifndef INST_DATA_H
#define INST_DATA_H

// Auto-generated from YAML
typedef struct {
    const char* name;
    const char* long_name;
    const char* description;
    const char* match;
    const char* xs1_loc;
    const char* xs2_loc;
    const char* xd_loc;
    const char* access_s;
    const char* access_u;
    const char* access_vs;
    const char* access_vu;
} InstData;

static InstData inst = {
    "add",
    "Integer add",
    "Add the value in xs1 to xs2, and store the result in xd. Any overflow is thrown away.",
    "0000000----------000-----0110011",
    "19-15",
    "24-20",
    "11-7",
    "always",
    "always",
    "always",
    "always"
};

#endif // INST_DATA_H
