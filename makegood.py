#!/usr/bin/python3

import sys
import os
import arisu_data
import logger

def usage():
    print("""\
Usage: makegood.py <path> <result path>
""")

class MakeGood:
    def run(self, path, path_res):
        data = arisu_data.ArisuData()
        if not data.load(path, drop_loss_item=True):
            return 1

        with open(path_res, "w") as fw:
            fw.write("#date checker turbidity ph chlorine temperature conductivity\n")

            for aq in data.arisuqs:
                fw.write("{}, {}, {}, {}, {}, {}, {}\n".format(aq.dt, data.checker_names[aq.checkerid - 1],
                                                               aq.turbidity, aq.ph, aq.chlorine, aq.temperature,
                                                               aq.conductivity))
        return 0

if __name__ == "__main__":
    import makegood

    if len(sys.argv) < 3:
        usage()
        exit(1)

    logger.init("makegood")

    if not os.path.isfile(sys.argv[1]):
        logger.error("file not found: {}".format(sys.argv[1]))
        exit(1)
    if os.path.exists(sys.argv[2]):
        logger.error("result path already exist: {}".format(sys.argv[2]))
        exit(1)

    mg = makegood.MakeGood()
    exit(mg.run(sys.argv[1], sys.argv[2]))
