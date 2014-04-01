import cStringIO
from binascii import hexlify, unhexlify
from M2Crypto import EVP

def main():
    # From test_AES of:
    # http://svn.osafoundation.org/m2crypto/trunk/tests/test_evp.py

    enc = 1
    dec = 0
    test = {
        'KEY': '06a9214036b8a15b512e03d534120006',
        'IV':  '3dafba429d9eb430b422da802c9fac41',
        'PT':  'Single block msg',
        'CT':  'e353779c1079aeb82708942dbe77181a',
        }

    k=EVP.Cipher(alg='aes_128_cbc', key=unhexlify(test['KEY']), iv=unhexlify(test['IV']), op=enc)
    pbuf=cStringIO.StringIO(test['PT'])
    cbuf=cStringIO.StringIO()
    ciphertext = hexlify(cipher_filter(k, pbuf, cbuf))
    cipherpadding = ciphertext[len(test['PT']) * 2:]
    ciphertext = ciphertext[:len(test['PT']) * 2] # Remove the padding from the end
    pbuf.close()
    cbuf.close()
    assert ciphertext == test['CT']

    # decrypt
    j=EVP.Cipher(alg='aes_128_cbc', key=unhexlify(test['KEY']), iv=unhexlify(test['IV']), op=dec)
    pbuf=cStringIO.StringIO()
    cbuf=cStringIO.StringIO(unhexlify(test['CT'] + cipherpadding))
    plaintext=cipher_filter(j, cbuf, pbuf)
    pbuf.close()
    cbuf.close()
    assert plaintext == test['PT']

    # encrypt
    k=EVP.Cipher(alg='aes_128_cbc', key=unhexlify(test['KEY']), iv=unhexlify(test['IV']), op=enc, padding=False)
    pbuf=cStringIO.StringIO(test['PT'])
    cbuf=cStringIO.StringIO()
    ciphertext = hexlify(cipher_filter(k, pbuf, cbuf))
    pbuf.close()
    cbuf.close()
    assert ciphertext == test['CT']
    print(repr(ciphertext))

    # decrypt
    j=EVP.Cipher(alg='aes_128_cbc', key=unhexlify(test['KEY']), iv=unhexlify(test['IV']), op=dec, padding=False)
    pbuf=cStringIO.StringIO()
    cbuf=cStringIO.StringIO(unhexlify(test['CT']))
    plaintext=cipher_filter(j, cbuf, pbuf)
    pbuf.close()
    cbuf.close()
    assert plaintext == test['PT']

def cipher_filter(cipher, inf, outf):
    while 1:
        buf=inf.read()
        if not buf:
            break
        outf.write(cipher.update(buf))
    outf.write(cipher.final())
    return outf.getvalue()

if __name__ == '__main__':
    main()
