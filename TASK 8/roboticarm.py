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
            print("Yes, Target is reachable.")
            return True
        else:
            print("No, Target is not reachable.")
            return False
        
def convert_to_coordinates(angles):
    x1 = 23 * math.sin(angles[0])
    y1 = 23 * math.cos(angles[0])
    x2 = x1 + 15 * math.sin(angles[0] + angles[1])
    y2 = y1 + 15 * math.cos(angles[0] + angles[1])
    x3 = x1 + x2 + 8 * math.sin(angles[0] + angles[1] + angles[2])
    y3 = y1 + y2 + 8 * math.cos(angles[0] + angles[1] + angles[2])
    print("The joint coordinates are:")
    print(x1,y1,"0")
    print(x2,y2,"0")
    print(x2,y3,"0")



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
convert_to_coordinates(angles)



