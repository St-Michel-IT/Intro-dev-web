import sqlite3


class Customer:
    """
    Customer class containing all the method to interact with the customer table
    """

    def __init__(self, path=":memory:") -> None:
        """
        Connect to in memory database by default, or to a database file if
        specified.
        """
        self.con = sqlite3.connect(path)

    def create_table(self) -> None:
        """
        Create the customer table if not exists
        """
        self.con.execute(
            """
            CREATE TABLE IF NOT EXISTS customer (
                id INT PRIMARY KEY NOT NULL,
                email TEXT NOT NULL
            )
            """
        )

    def insert(self, customer_id: int, email: str) -> None:
        """
        Insert a new customer in the table.

           :param customer_id: The customer id as an int
           :param email: The customer email as a string
        """
        self.con.execute(
            """
            INSERT INTO customer (
                id,
                email
            ) VALUES (
                ?, ?
            )""",
            (customer_id, email),
        )
        self.con.commit()

    def get(self, customer_id: int) -> str:
        """
        Get the email of a customer by its id.

           :param customer_id: The customer id as an int
           :return: The customer email as a string
        """
        cursor = self.con.execute(
            """
            SELECT email
            FROM customer
            WHERE id = ?
            """,
            (customer_id,),
        )
        return cursor.fetchone()[0]

    def delete(self, customer_id: int) -> None:
        """
        Delete a customer by its id.

           :param customer_id: The customer id as an int
        """
        self.con.execute(
            """
            DELETE FROM customer
            WHERE id = ?
            """,
            (customer_id,),
        )
        self.con.commit()

    def customers(self) -> list:
        """
        Get the list of all customers.

           :return: The list of all customers
        """
        cursor = self.con.execute(
            """
            SELECT id, email
            FROM customer
            """
        )
        return cursor.fetchall()
