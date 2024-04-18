def main():
    # Reading the input_queues file.
    input_file = open("input_queue.txt", "r")
    input_data = input_file.read()
    input_file.close()

    # Input packets as string list.
    input_packets = input_data.split("\n")

    # Queues from input packets, P=Priority, S=Standard, E=Economy.
    p_queue = []
    s_queue = []
    e_queue = []

    for packet in input_packets:
        if packet[0] == "P":
            p_queue.append(packet)
        elif packet[0] == "S":
            s_queue.append(packet)
        elif packet[0] == "E":
            e_queue.append(packet)
        else:
            print(f"'{packet}' is an abnormal packet!")

    print(f"P: {p_queue}\nS: {s_queue}\nE: {e_queue}")


if __name__ == '__main__':
    main()
