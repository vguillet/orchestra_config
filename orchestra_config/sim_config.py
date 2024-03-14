
ALLOCATION_METHOD = "CBAA w. intercession"

DEBUG = False

# ----------------- SIMULATION MODE -----------------
# >>>>>>>>>> RUN MODES DEFINITION
SIM = 0
OPERATIONAL = 1
# >>>>>>>>>>

RUN_MODE = OPERATIONAL

# ----------------- NODE CONFIGURATION -----------------
FLEET_MSG_UPDATE_TIMER = 0.1


# ----------------- SIMULATION CONFIGURATION -----------------
NO_TASK = 0
ACTION_1 = 1
ACTION_2 = 2

# TODO: Cleanup
env_size = 9

goto_task_count = 20
no_task_task_count = 6
action_1_task_count = 7     # action_1 task     (even goal ids)
action_2_task_count = 7     # action_2 tasks    (odd goal ids)

initial_tasks_announcement = 5

# goto_task_count = 100
# no_task_task_count = 30
# action_1_task_count = 35     # action_1 task     (even goal ids)
# action_2_task_count = 35     # action_2 tasks    (odd goal ids)
#
# initial_tasks_announcement = 15

EVEN = 0
RANDOM = 1

release_spread = EVEN
release_ration = EVEN

release_max_epoch = 100

assert goto_task_count == (no_task_task_count + action_1_task_count + action_2_task_count)

# agent_lst = ["Turtle_1", "Turtle_2", "Turtle_3", "Turtle_4", "Turtle_5", "Turtle_6", "Turtle_7", "Turtle_8", "Turtle_9", "Turtle_10"]
agent_lst = ["Turtle_1", "Turtle_2", "Turtle_3", "Turtle_4"]
# agent_lst = ["Turtle_1", "Turtle_2"]


skillsets = {
    "Operator": [],
    # "Operator": ["GOTO", "ACTION_1"],
    "Turtle_1": ["GOTO", "ACTION_1"],
    "Turtle_2": ["GOTO", "ACTION_1"],
    "Turtle_3": ["GOTO", "ACTION_2"],
    "Turtle_4": ["GOTO", "ACTION_2"],
}

# skillsets = {
#     "Operator": [],
#     # "Operator": ["GOTO", "ACTION_1"],
#     "Turtle_1": ["GOTO", "ACTION_1"],
#     "Turtle_2": ["GOTO", "ACTION_1"],
#     "Turtle_3": ["GOTO", "ACTION_1"],
#     "Turtle_4": ["GOTO", "ACTION_1"],
#     "Turtle_5": ["GOTO", "ACTION_1"],
#     "Turtle_6": ["GOTO", "ACTION_2"],
#     "Turtle_7": ["GOTO", "ACTION_2"],
#     "Turtle_8": ["GOTO", "ACTION_2"],
#     "Turtle_9": ["GOTO", "ACTION_2"],
#     "Turtle_10": ["GOTO", "ACTION_2"]
# }

bid_function = {
    # "Operator": "anticipated_action_task_interceding_agent",
    # "Operator": "graph_weighted_manhattan_distance_bid",
    "Turtle_1": "graph_weighted_manhattan_distance_bid",
    "Turtle_2": "graph_weighted_manhattan_distance_bid",
    "Turtle_3": "graph_weighted_manhattan_distance_bid",
    "Turtle_4": "graph_weighted_manhattan_distance_bid",
    # "Turtle_5": "graph_weighted_manhattan_distance_bid",
    # "Turtle_6": "graph_weighted_manhattan_distance_bid",
    # "Turtle_7": "graph_weighted_manhattan_distance_bid",
    # "Turtle_8": "graph_weighted_manhattan_distance_bid",
    # "Turtle_9": "graph_weighted_manhattan_distance_bid",
    # "Turtle_10": "graph_weighted_manhattan_distance_bid"
}


# class SimConfig:
#     def __init__(self):
#         self.robot_count


