from mpi4py import MPI


def main():

    comm = MPI.COMM_WORLD
    size = comm.Get_size()
    rank = comm.Get_rank()

    if rank == 0:

        data = 1
    
    else:
        data = None

    data = comm.bcast(data, root=0)

    print("Data: ",data," on rank ",rank)

    if rank == 1:

        data = 2

    data = comm.bcast(data, root=1)

    print("Modified data: ",data," on rank ",rank)
    
if __name__ == '__main__':
    main()