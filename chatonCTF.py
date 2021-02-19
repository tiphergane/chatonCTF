#!/usr/bin/env python3
# coding utf8

import re
import pwn
import binwalk


def ReverseString(string):  # {{{
    reversed = string[::-1]
    return reversed


# }}}


def FlagFinder(cible, flag):  # {{{
    regex = flag
    file = cible
    t = pwn.read(file)
    c = re.findall(regex, str(t))
    if not c:
        pwn.warn("Flag non trouvé")
    else:
        for a in c:
            pwn.success("Yeah !!!! flag found: {result}\n".format(result=a))
            pwn.warn("flag is now copied in flag.txt")
            pwn.write("flag.txt", a)


# }}}


def binExtract(cible):  # {{{
    pwn.info("Extraction en cours de {}".format(cible))
    binwalk.scan(cible, signature=True, extract=True)
    # }}}


def binScan(cible):  # {{{
    pwn.info("Scan en cours de {}".format(cible))
    binwalk.scan(cible, signature=True, extract=False)


# }}}


def rsaFindN(p, q):  # {{{
    n = int(p) * int(q)
    return n


# }}}


def rsaFindpq(n, x):  # {{{
    solution = int(n) // int(x)
    return solution


# }}}


def rsaFindPhi(p, q):  # {{{
    solution = (int(p) - 1) * (int(q) - 1)
    return solution


# }}}


def rsaFindD(phi, e):  # {{{
    d = pow(int(e), -1, int(phi))
    return d


# }}}


if __name__ == "__main__":
    pwn.warn("Ceci est à utiliser en tant que module")
else:
    pwn.warn("Module chargé")
