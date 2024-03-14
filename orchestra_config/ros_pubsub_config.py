
# ------------------------------------ Topics Config ------------------------------------
# ------ SIMULATOR
topic_simulator_signals = "/simulator/simulator_signals"

# ------ SIM
topic_environment = "/sim/environment"
topic_epoch = "/sim/epoch"
topic_fleet_msgs_filtered = "/sim/fleet/fleet_msgs_filtered"
topic_sim_events_instructions = "/sim/events_instructions"

# ------ FLEET
topic_fleet_msgs = "/fleet/fleet_msgs"
topic_tasks = "/fleet/tasks"
topic_goals = "/fleet/goals"

topic_bids = "/fleet/bids"
topic_allocations = "/fleet/allocations"

# ------ AGENT
topic_pose = "/data/pose"


# ------------------------------------ QoS Profile ------------------------------------
from rclpy.qos import QoSProfile, QoSReliabilityPolicy, QoSHistoryPolicy

qos_simulator_signals = QoSProfile(
    reliability=QoSReliabilityPolicy.RELIABLE,
    history=QoSHistoryPolicy.KEEP_ALL,
)

qos_env = QoSProfile(
    reliability=QoSReliabilityPolicy.BEST_EFFORT,
    history=QoSHistoryPolicy.KEEP_LAST,
    depth=1
)

qos_fleet_msgs = QoSProfile(
    reliability=QoSReliabilityPolicy.RELIABLE,
    history=QoSHistoryPolicy.KEEP_ALL
)

# qos_fleet_msgs = QoSProfile(
#     reliability=QoSReliabilityPolicy.BEST_EFFORT,
#     history=QoSHistoryPolicy.KEEP_LAST,
#     depth=1
# )

qos_tasks = QoSProfile(
    reliability=QoSReliabilityPolicy.RELIABLE,
    history=QoSHistoryPolicy.KEEP_ALL,
)

qos_pose = QoSProfile(
    reliability=QoSReliabilityPolicy.BEST_EFFORT,
    history=QoSHistoryPolicy.KEEP_LAST,
    depth=1
)

qos_intercession = QoSProfile(
    reliability=QoSReliabilityPolicy.RELIABLE,
    history=QoSHistoryPolicy.KEEP_ALL,
)

qos_goal = QoSProfile(
    reliability=QoSReliabilityPolicy.RELIABLE,
    history=QoSHistoryPolicy.KEEP_ALL,
)

qos_sim_epoch = QoSProfile(
    reliability=QoSReliabilityPolicy.RELIABLE,
    history=QoSHistoryPolicy.KEEP_ALL,
)

qos_sim_events_instructions = QoSProfile(
    reliability=QoSReliabilityPolicy.RELIABLE,
    history=QoSHistoryPolicy.KEEP_ALL,
)


class ros_pubsub_config:
    def __init__(self):
        # ------------------------------------ Topics Config ------------------------------------
        # ------ SIMULATOR
        self.topic_simulator_signals = "/simulator/simulator_signals"

        # ------ SIM
        self.topic_environment = "/sim/environment"
        self.topic_epoch = "/sim/epoch"
        self.topic_fleet_msgs_filtered = "/sim/fleet/fleet_msgs_filtered"
        self.topic_sim_events_instructions = "/sim/events_instructions"

        # ------ FLEET
        self.topic_fleet_msgs = "/fleet/fleet_msgs"
        self.topic_tasks = "/fleet/tasks"
        self.topic_goals = "/fleet/goals"

        self.topic_bids = "/fleet/bids"
        self.topic_allocations = "/fleet/allocations"

        # ------ AGENT
        self.topic_pose = "/data/pose"

        # ------------------------------------ QoS Profile ------------------------------------
        from rclpy.qos import QoSProfile, QoSReliabilityPolicy, QoSHistoryPolicy

        self.qos_simulator_signals = QoSProfile(
            reliability=QoSReliabilityPolicy.RELIABLE,
            history=QoSHistoryPolicy.KEEP_ALL,
        )

        self.qos_env = QoSProfile(
            reliability=QoSReliabilityPolicy.BEST_EFFORT,
            history=QoSHistoryPolicy.KEEP_LAST,
            depth=1
        )

        self.qos_fleet_msgs = QoSProfile(
            reliability=QoSReliabilityPolicy.RELIABLE,
            history=QoSHistoryPolicy.KEEP_ALL
        )

        # self.qos_fleet_msgs = QoSProfile(
        #     reliability=QoSReliabilityPolicy.BEST_EFFORT,
        #     history=QoSHistoryPolicy.KEEP_LAST,
        #     depth=1
        # )

        self.qos_tasks = QoSProfile(
            reliability=QoSReliabilityPolicy.RELIABLE,
            history=QoSHistoryPolicy.KEEP_ALL,
        )

        self.qos_pose = QoSProfile(
            reliability=QoSReliabilityPolicy.BEST_EFFORT,
            history=QoSHistoryPolicy.KEEP_LAST,
            depth=1
        )

        self.qos_intercession = QoSProfile(
            reliability=QoSReliabilityPolicy.RELIABLE,
            history=QoSHistoryPolicy.KEEP_ALL,
        )

        self.qos_goal = QoSProfile(
            reliability=QoSReliabilityPolicy.RELIABLE,
            history=QoSHistoryPolicy.KEEP_ALL,
        )

        self.qos_sim_epoch = QoSProfile(
            reliability=QoSReliabilityPolicy.RELIABLE,
            history=QoSHistoryPolicy.KEEP_ALL,
        )