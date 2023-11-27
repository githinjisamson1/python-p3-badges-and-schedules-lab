def badge_maker(name):
    return f"Hello, my name is {name}."

# !call badge_maker for each element


def batch_badge_creator(names):
    badgeMessagesLc = [badge_maker(item) for item in names]

    return badgeMessagesLc


def assign_rooms(names):
    # !initialize roomAssignments
    roomAssignments = []

    # !for each item assign then append to roomAssignments
    # !room => currentindex + 1
    for item in names:
        assignment = f"Hello, {item}! You'll be assigned to room {names.index(item) + 1}!"

        roomAssignments.append(assignment)

    return roomAssignments


# print(assign_rooms(["Arel", "Carol", "c", "z", "v", "f"]))

def printer(names):
    # !batch_badge_creator()
    badgeMessages = batch_badge_creator(names)

    for item in badgeMessages:
        print(item)

    # !assign_rooms()
    roomAssignments = assign_rooms(names)

    for item in roomAssignments:
        print(item)


# printer(["Arel", "Carol"])

# TODO: rewrite using ternary expressions
