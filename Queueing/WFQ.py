def main():
    # Reading the input_queues file.
    input_file = open("input_queue.txt", "r")
    input_data = input_file.read()
    input_file.close()
    # Input file data as string list.
    input_packets = input_data.split("\n")

    # Queues from input packets, P=Priority, S=Standard, E=Economy.
    p_queue = []
    s_queue = []
    e_queue = []

    # Append each item to proper queue with first letter.
    for packet in input_packets:
        if packet[0] == "P":
            p_queue.append(packet)
        elif packet[0] == "S":
            s_queue.append(packet)
        elif packet[0] == "E":
            e_queue.append(packet)
        else:
            print(f"'{packet}' has no weight!")

    # Initial weighted fair queue.
    wfq = []

    # Loop over each queue, appending 3 priority, 2 standard, and 1 economy to the weighted fair queue.
    # Repeat until all queues are empty.
    while len(p_queue) > 0 or len(s_queue) > 0 or len(e_queue) > 0:
        if len(p_queue) > 0:
            for i in range(3):
                if len(p_queue) > 0:
                    wfq.append(p_queue.pop(0))
        if len(s_queue) > 0:
            for i in range(2):
                if len(s_queue) > 0:
                    wfq.append(s_queue.pop(0))
        if len(e_queue) > 0:
            if len(e_queue) > 0:
                wfq.append(e_queue.pop(0))

    # Final weighted fair queue.
    print(f"WFQ: {wfq}")


if __name__ == '__main__':
    main()
