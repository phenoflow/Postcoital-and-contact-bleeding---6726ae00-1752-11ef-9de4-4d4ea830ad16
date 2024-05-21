# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2024.

import sys, csv, re

codes = [{"code":"K587.00","system":"readv2"},{"code":"1581.00","system":"readv2"},{"code":"K59B.00","system":"readv2"},{"code":"K597.00","system":"readv2"},{"code":"K59A.00","system":"readv2"},{"code":"1941.0","system":"readv2"},{"code":"12426.0","system":"readv2"},{"code":"47026.0","system":"readv2"},{"code":"46997.0","system":"readv2"},{"code":"6301.0","system":"readv2"},{"code":"N93.0","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('postcoital-and-contact-bleeding-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["postcoital-and-contact-bleeding---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["postcoital-and-contact-bleeding---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["postcoital-and-contact-bleeding---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
