#include "rclcpp/rclcpp.hpp"
#include "ackermann_msgs/msg/ackermann_drive_stamped.hpp"

class RelayNode : public rclcpp::Node
{
public:
    RelayNode() : Node("relay")
    {
        drive_relay_publisher_ = this->create_publisher<ackermann_msgs::msg::AckermannDriveStamped>("drive_delay", 10);
        drive_subscriber_ = this->create_subscription<ackermann_msgs::msg::AckermannDriveStamped>(
            "drive", 10, std::bind(&RelayNode::callback, this, std::placeholders::_1));
        RCLCPP_INFO(this->get_logger(), "Relay has been started");
    }

private:
    void callback(const ackermann_msgs::msg::AckermannDriveStamped::SharedPtr msg)
    {
        v_relay_ = msg->drive.speed;
        d_relay_ = msg->drive.steering_angle;
        auto msg_delay = ackermann_msgs::msg::AckermannDriveStamped();
        msg_delay.drive.speed = v_relay_ * 3;
        msg_delay.drive.steering_angle = d_relay_ * 3;
        drive_relay_publisher_->publish(msg_delay);
    }

    float v_relay_;
    float d_relay_;
    rclcpp::Publisher<ackermann_msgs::msg::AckermannDriveStamped>::SharedPtr drive_relay_publisher_;
    rclcpp::Subscription<ackermann_msgs::msg::AckermannDriveStamped>::SharedPtr drive_subscriber_;
};

int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);
    auto node = std::make_shared<RelayNode>();
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}