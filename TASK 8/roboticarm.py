import numpy as np
import math

class Arm:
    def __init__(self, link_lengths):
        self.link_lengths = link_lengths
        self.num_joints = len(link_lengths)
        self.joint_angles = np.zeros(self.num_joints)
        self.initial_position = np.zeros(self.num_joints)
        self.target_position = np.zeros(3)

    def set_initial_joint_positions(self, initial_joint_positions):
        self.initial_joint_positions = np.array(initial_joint_positions)

    def set_joint_angles(self, angles):
        self.initial_joint_angles = np.array(angles)

    def set_target_position(self, target):
        self.target_position = np.array(target)

    def is_reachable(self):
        distance_to_target = np.linalg.norm(self.target_position)
        if distance_to_target <= 46 and distance_to_target >= 15*math.sqrt(2):
            print("Target is reachable.")
            return True
        else:
            print("Target is not reachable.")
            return False


angle = input("Enter the three angles separated by a space (in radians):" )
angle_array = angle.split()
angles = [int(x) for x in angle_array]
arm = Arm([23, 15, 8])
arm.set_joint_angles(angles)
tposi = input("Enter the target coordinates separated by a space:")
posi_array = tposi.split()
posis = [int(x) for x in posi_array]
arm.set_target_position(posis)
arm.is_reachable()


