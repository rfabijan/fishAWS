from operations import get_avg, get_avg_total
from S3Client import S3
import CSV as CSV


def run():
    client1 = S3("fish-market.csv")
    client2 = S3("fish-market-tues.csv")
    client3 = S3("fish-market-mon.csv")

    file1 = get_avg(CSV.get_csv(client1.get_object_body()))
    file2 = get_avg(CSV.get_csv(client2.get_object_body()))
    file3 = get_avg(CSV.get_csv(client3.get_object_body()))

    Robert = get_avg_total(file1, file2, file3)

    str_buffer = CSV.save_csv_file(Robert)
    CSV.put_object(str_buffer, client1, Robert)



