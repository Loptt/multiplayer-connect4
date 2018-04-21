#include <iostream>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>

int main(int argc, char* args[])
{
    int pipefifo, returnval;
    char buffer[2];

    for (int i = 0; i < 2; ++i)
    {
        buffer[i] = args[1][i];
    }

    returnval = mkfifo("/tmp/myfifo", 0666);

    pipefifo = open("/tmp/myfifo", O_WRONLY);
    if (pipefifo == -1)
    {
        std::cout << "Error, cannot open fifo" << std::endl;
        return 1;
    }

    write(pipefifo, buffer, sizeof(buffer));

    close(pipefifo);

    return 0;
    
}