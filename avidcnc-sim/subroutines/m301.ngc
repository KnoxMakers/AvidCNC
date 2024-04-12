#!/usr/bin/python
import sys

def update_tool_table(tool_number, new_pocket_number):
    filename = '/home/avidcnc/avidcnc-sim/tool.tbl'
    updated_lines = []
    with open(filename, 'r') as file:
        for line in file:
            parts = line.split()
            if parts and parts[0].startswith(f'T{tool_number}' + ' '*3):
                parts[1] = f'P{new_pocket_number}'
                line = ' '.join(parts) + '\n'
            updated_lines.append(line)

    with open(filename, 'w') as file:
        for line in updated_lines:
            file.write(line)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 update_tool_table.py <tool_number> <new_pocket_number>")
        sys.exit(1)

    tool_number = int(sys.argv[1])
    new_pocket_number = int(sys.argv[2])

    update_tool_table(tool_number, new_pocket_number)
