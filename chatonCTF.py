#!/usr/bin/env python3
# coding utf8

import re
import pwn
import binwalk
from gmpy2 import iroot

def rsaSmalle(c,e,n):
    """recover ciphered message from small e exponant"""
    m = iroot(c,e)
    if (m[0]**e) % n == c:
        m = INTtoASCII(str(m[0]))
        return m
    else:
        return None

def INTtoASCII(string):
    """Convert an Integer to hex string then his ASCII representation"""
    string = int(string)
    string = hex(string)[2:]
    return bytes.fromhex(string).decode("utf-8")


def ReverseString(string):  # {{{
    """Reverse a string"""
    reversed = string[::-1]
    return reversed
    # }}}


def FlagFinder(cible, flag):  # {{{
    """Search for a string by his regex representation"""
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
    """Extract data from target with binwalk"""
    pwn.info("Extraction en cours de {}".format(cible))
    binwalk.scan(cible, signature=True, extract=True)
    # }}}


def binScan(cible):  # {{{
    """Scan data from target with binwalk"""
    pwn.info("Scan en cours de {}".format(cible))
    binwalk.scan(cible, signature=True, extract=False)
    # }}}


def rsaFindN(p, q):  # {{{
    """Compute N from p and q"""
    n = int(p) * int(q)
    return n
    # }}}


def rsaFindpq(n, x):  # {{{
    """Find p or q when you have N and p or q"""
    solution = int(n) // int(x)
    return solution
    # }}}


def rsaFindPhi(p, q):  # {{{
    """Compute Phi(n) from p and q"""
    solution = (int(p) - 1) * (int(q) - 1)
    return solution
    # }}}


def rsaFindDfromPhi(phi, e):  # {{{
    """Compute D from Phi(n) and modulus e"""
    d = pow(int(e), -1, int(phi))
    return d
    # }}}


def rsaFindDfromPQ(p, q, e):  # {{{
    """Compute D from p, q and modulus e"""
    phi = rsaFindPhi(int(p), int(q))
    d = pow(int(e), -1, phi)
    return d
    # }}}


def rsaCipherMessage(m, e, n):  # {{{
    """Compute ciphered message from cleartext, modulus and N"""
    c = pow(int(m), int(e), int(n))
    return c
    # }}}


def rsaUncipherMessage(c, d, n):  # {{{
    """Compute cleartext message from ciphered text, D and N"""
    m = pow(int(c), int(d), int(n))
    return m
    # }}}


def rsaSignMessage(m, d, n):  # {{{
    """Compute signature from message, D and N"""
    s = pow(int(m), int(d), int(n))
    return s
    # }}}


if __name__ == "__main__":
    pwn.warn("Ceci est à utiliser en tant que module")
