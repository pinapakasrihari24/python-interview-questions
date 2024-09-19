from pyspark.sql import SparkSession


def main():
    spark = SparkSession \
        .builder \
        .appName("seat_id") \
        .getOrCreate()

    data = [
        (1, "Abbot"),
        (2, "Doris"),
        (3, "Emerson"),
        (4, "Green"),
        (5, "Jeames")
    ]

    # Define the schema (column names)
    columns = ["id", "student"]

    # Create the DataFrame
    df = spark.createDataFrame(data, columns)

    # Show the DataFrame
    df.show()

    seat_swap = spark.sql("""
    SELECT
    id,
    CASE
        WHEN id % 2 = 1 AND id < (SELECT MAX(id) FROM students) THEN (SELECT student FROM students WHERE id = s.id + 1)
        WHEN id % 2 = 0 THEN (SELECT student FROM students WHERE id = s.id - 1)
        ELSE student
    END AS student
FROM students s
ORDER BY id;
    """)
    seat_swap.show()

if __name__ == '__main__':
    main()