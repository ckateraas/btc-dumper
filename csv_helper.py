def write_to_csv(address_iterator, output_file_path):
    csv_rows = ['address,amount_satoshi,last_height']
    with open(output_file_path, 'w') as file:
        counter = 0
        for address, sat_val, block_height in address_iterator:
            if sat_val == 0:
                continue
            csv_rows.append(
                address + ',' + str(sat_val) + ',' + str(block_height)
            )
            counter += 1
            if counter == 1000:
                file.write('\n'.join(csv_rows) + '\n')
                csv_rows = []
                counter = 0
        if counter > 0:
            file.write('\n'.join(csv_rows) + '\n')
        file.write('\n')
