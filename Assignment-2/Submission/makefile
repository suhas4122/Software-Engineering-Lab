CC = g++ -std=c++11

bms: book.o novel.o play.o main.o
	$(CC) book.o novel.o play.o main.o -o bms

book.o: book.cc
	$(CC) -c book.cc

novel.o: novel.cc 
	$(CC) -c novel.cc

play.o: play.cc
	$(CC) -c play.cc

main.o: main.cc
	$(CC) -c main.cc

clean: 
	rm *.o bms