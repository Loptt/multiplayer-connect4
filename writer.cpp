#include <iostream>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>

int main(int argc, char* args[])
{
    int pipefifo, returnval;
    char buffer[1];

    returnval = mkfifo("/tmp/myfifo", 0666);

    for (int i = 0; i < 1; ++i)
    {
        buffer[i] = args[1][i];
    }

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