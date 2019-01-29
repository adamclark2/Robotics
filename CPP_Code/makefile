
CC=g++

# Windows users may want to install PUTTY & use pscp
SCP=scp

build:
	$(CC) -o RemoteControl.o src/Main.cpp

clean:
	rm RemoteControl.o

help:
	@cat makeHelp.txt

run: build
	./RemoteControl.o

copy-code: 
	$(SCP) -r ./ robot@ev3dev.local:code

	