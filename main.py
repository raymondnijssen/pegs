from pegboard import PegBoard
import time
from random import randrange

t0 = time.time()

pr = 100
attempts = 0
high_score = 32


for a in range(10000000):
    pb = PegBoard()
    pb.doMove(3,1,3,3)
    #print(pb)
    while True:
        mvs = pb.getAllMoves()
        #print(mvs)

        if len(mvs) == 0:
            np = pb.getNumPegs()
            if np == 1:
                print(pb)
            high_score = min(high_score, np)
            break

        mv = mvs[randrange(len(mvs))]
        pb.doMove(mv[0],mv[1],mv[2],mv[3])

    attempts += 1

    if attempts % 10000 == 0:
        t = time.time() - t0
        print('games: {}, hi: {}, time: {}'.format(attempts, high_score, t))

        if high_score == 1:
            break

#print(len(pb.moves))
print(time.time() - t0)
