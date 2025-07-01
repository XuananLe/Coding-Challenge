BINARY_NAME := main
SRC := main.go

.PHONY: all build clean run

all: build

build:
	go build -o $(BINARY_NAME) $(SRC)

clean:
	go clean
	rm -f $(BINARY_NAME)

run: build
	./$(BINARY_NAME)
