for z in range(0, len(self.symbol)):
                for xe in file_open.readlines():
                    dec.append(xe)
                    y = ''.join(dec).split()
                    print(''.join(dec).split(), 'DEC')
                    op = []
                    for e in y:
                        opa = [txt_dec[i:i+n] for i in range(0, len(txt_dec), n)]
                        print(opa, 'OPA')
                        p = []
                        for g in opa:

                            if e == g[z]:
                                p.append(self.symbol[z])

                                str_d = ''.join(p).split()
                                print(''.join(str_d))