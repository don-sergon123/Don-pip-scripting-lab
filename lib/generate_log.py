from datetime import datetime
import os


def generate_log(log_data=None):
    if log_data is None or len(log_data) == 0:
        raise ValueError("log_data cannot be empty or None")

    date_str = datetime.now().strftime("%Y%m%d")
    filename = f"log_{date_str}.txt"

    with open(filename, "w") as file:
        for entry in log_data:
            file.write(f"{entry}\n")

    print(f"Log written to {filename}")

    return filename


if __name__ == "__main__":
    sample_data = ["User logged in", "User updated profile", "Report exported"]
    generate_log(sample_data)
