#include <stdio.h>
#include "output/inst_data.h"

int main() {
    FILE* f = fopen("output/regenerated.yaml", "w");
    if (!f) {
        perror("Could not open file");
        return 1;
    }

    fprintf(f, "name: %s\n", inst.name);
    fprintf(f, "long_name: %s\n", inst.long_name);
    fprintf(f, "description: \"%s\"\n", inst.description);
    fprintf(f, "encoding:\n");
    fprintf(f, "  match: %s\n", inst.match);
    fprintf(f, "  variables:\n");
    fprintf(f, "    - name: xs1\n      location: %s\n", inst.xs1_loc);
    fprintf(f, "    - name: xs2\n      location: %s\n", inst.xs2_loc);
    fprintf(f, "    - name: xd\n      location: %s\n", inst.xd_loc);
    fprintf(f, "access:\n");
    fprintf(f, "  s: %s\n", inst.access_s);
    fprintf(f, "  u: %s\n", inst.access_u);
    fprintf(f, "  vs: %s\n", inst.access_vs);
    fprintf(f, "  vu: %s\n", inst.access_vu);

    fclose(f);
    return 0;
}
