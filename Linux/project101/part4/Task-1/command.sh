#!/bin/bash

sed -i "s/ec2-private_ip/$(grep PrivateIpAddress info.json | head -n1 | cut -d'"' -f4)/g" terraform.tf


# hocanın çözümü

# ip=$(cat info.json | grep -m1 PrivateIpAddress | cut -d":" -f2 | cut -d'"' -f2)
#sudo sed -i "s/ec2-private_ip/$ip/" terraform.tf