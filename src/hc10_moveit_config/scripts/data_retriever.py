#!/usr/bin/env python3

import rospy
import sensor_msgs.point_cloud2 as pc2
from sensor_msgs.msg import PointCloud2
import std_msgs.msg

class Talker():
    def __init__(self):
        rospy.init_node("pointcloud_saver")
        rospy.Subscriber('/camera/depth/points', PointCloud2, self.points_callback)

        self.publisher = rospy.Publisher("/object_cloud", PointCloud2, queue_size=100)
        self.object = []

    def points_callback(self, msg):
        points = pc2.read_points(msg, field_names=("x","y","z"))

        with open("object.txt","w") as f:
            for p in points:
                #TODO: transformer les points en repère monde en fonction de la pos et de la rot
                point = [p[0],p[1],p[2]]
                

                # print("Point added")
                self.object.append([p[0],p[1],p[2]])
                f.write(f"{p[0]} {p[1]} {p[2]}\n")

        header = std_msgs.msg.Header()
        header.stamp = rospy.Time.now()
        header.frame_id = "base_link"

        cloud = pc2.create_cloud_xyz32(header, self.object)
        
        self.publisher.publish(cloud)
        print(cloud)

if __name__ == '__main__':
    node = Talker()

    try:
        rospy.spin()
    except KeyboardInterrupt:
        node.get_logger().info("Shutdown requested, stopping node...")