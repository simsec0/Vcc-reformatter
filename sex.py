from logging import exception

def main():
    while True:
        try:
            original = open("vccs.txt","r")
            ong = original.readline().split("|")
            with open("vccs.txt","r") as fin:
                data = fin.read().splitlines(True)
            with open("vccs.txt","w") as fout:
                fout.writelines(data[1:])
            fin.close()
            fout.close()
            original.close()
            long = ong[0]
            twocharexp = ong[1]
            fourcharexp = ong[2]
            mainsecexpr = fourcharexp[2:4]
            threeletter = ong[3]
            final = long+":"+twocharexp+mainsecexpr+":"+threeletter
            ssdd = open("outfile.txt","a")
            ssdd.write(final)
            ssdd.close()
            print("Reformatted -> "+final)
        except IndexError:
            print("No more VCCs to format")
            break

main()