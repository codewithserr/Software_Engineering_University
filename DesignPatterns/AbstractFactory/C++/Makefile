CC = g++
CFLAGS = -Wall -Wextra -std=c++11
TARGET = main
SRC = AbstractFactory.cpp

all: $(TARGET)

$(TARGET): $(SRC)
	$(CC) $(CFLAGS) -o $@ $^

clean:
	rm -f $(TARGET)