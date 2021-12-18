PROGRAM = Program
MODULES = modules
# Compile options. Το -I<dir> λέει στον compiler να αναζητήσει εκεί include files
CFLAGS = -Wall -no-pie -fPIE -g -I$(INCLUDE)

# Αρχεία .o
OBJS = $(PROGRAM)/csp.py $(MODULES)/search.py $(MODULES)/utils.py


# the executable program
EXEC = csp

$(EXEC):
	python $(OBJS)

# clean:
# rm -rf __pycache__

run: $(EXEC)
	./$(EXEC)
