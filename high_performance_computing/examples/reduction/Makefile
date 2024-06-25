CC=gcc
LINKER=gcc

EXECUTABLE=approx_pi

DEPS=util_random.h Makefile

OBJS=util_random.o approx_pi.o

OPT_FLAGS=-O0

CFLAGS=-I. -std=c99 -Wall -fopenmp $(OPT_FLAGS)

LDFLAGS=-fopenmp -lm $(OPT_FLAGS)
all: $(EXECUTABLE)

# meaning of symbols below:
# `%.c` is a placeholder/wildcard for any file name that ends with .c
# `$@`  stands for the left-hand side of the colon ":"
# `$<`  stands for the first item on the right-hand side of the colon ":"
# `$^`  stands for all items on the right-hand side of the colon ":"

# rule for all ".o" (object) files
# note: one object file is created from each .c file
%.o: %.c $(DEPS)
	$(CC) -o $@ $< -c $(CFLAGS)

# rule `$@`: $^`
$(EXECUTABLE): $(OBJS)
	$(LINKER) -o $@ $^ $(LDFLAGS)

# clean up compiled files
clean:
	rm -f $(EXECUTABLE) *.o

