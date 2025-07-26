all:
	gcc parse.c -o parse

clean:
	rm -f parse
	rm -f output/regenerated.yaml
