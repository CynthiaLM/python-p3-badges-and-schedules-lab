def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    badge_messages = [f"Hello, my name is {name}." for name in names]
    return badge_messages

def assign_rooms(names):
    room_assignments = []
    rooms = [f"Room {i}" for i in range(1, 8)]

    for i, name in enumerate(names):
        if i < len(rooms):
            room_assignment = f"Hello, {name}! You'll be assigned to {rooms[i]}!"
            room_assignments.append(room_assignment)

    return room_assignments


def printer(names):
    badge_messages = batch_badge_creator(names)
    room_assignments = assign_rooms(names)

    for badge in badge_messages:
        print(badge)

    for assignment in room_assignments:
        print(assignment)
