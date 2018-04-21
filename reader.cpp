#include <iostream>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>

int main()
{
	int pipefifo, returnval;
	char buffer[3] = {0,0,0};

	while (buffer[0] != 0x30)
	{
		pipefifo = open("/tmp/myfifo", O_RDONLY);
		if (pipefifo == -1)
		{
			std::cout << "Error, cannot open fifo" << std::endl;
			return 1;
		}

		returnval = read(pipefifo, buffer, sizeof(buffer));
		returnval = read(pipefifo, buffer, sizeof(buffer));
		fflush(stdin);

		std::cout << "Printing value..." << std::endl;
		std::cout << buffer[0] << std::endl;
	}


	close(pipefifo);

	return 0;
}