from typing import List, Dict


# The smallest unit of deployment target. It is comprised of a single
# network port and its fair share of cores.
class HostNode:
    def __init__(self, dns: str, fastip: str, cores: List[int], rdma: str, config: str):
        """
        :param dns: DNS name of host
        :param fastip: IP address of the network port to listen on
        :param cores: List of core IDs to use
        :param rdma: Name of RDMA port to use, e.g. "mlx5_0"
        :param config: Hardware config of the server
        """
        self.dns = dns
        self.fastip = fastip
        self.cores = cores
        self.rdma = rdma
        self.config = config


host_nodes: List[HostNode] = [
    HostNode("ec2-52-36-150-160.us-west-2.compute.amazonaws.com", "172.31.11.30", [0,1], "mlx5_0", "A"),
    HostNode("ec2-52-36-150-160.us-west-2.compute.amazonaws.com", "172.31.11.30", [2,3], "mlx5_0", "A"),
    HostNode("ec2-52-36-150-160.us-west-2.compute.amazonaws.com", "172.31.11.30", [4], "mlx5_0", "A"),
    HostNode("ec2-52-36-150-160.us-west-2.compute.amazonaws.com", "172.31.11.30", [5], "mlx5_0", "A"),
    HostNode("ec2-52-36-150-160.us-west-2.compute.amazonaws.com", "172.31.11.30", [6], "mlx5_0", "A"),
    HostNode("ec2-52-36-150-160.us-west-2.compute.amazonaws.com", "172.31.11.30", [7], "mlx5_0", "A"),
    HostNode("ec2-52-36-150-160.us-west-2.compute.amazonaws.com", "172.31.11.30", [8], "mlx5_0", "A"),
    HostNode("ec2-52-36-150-160.us-west-2.compute.amazonaws.com", "172.31.11.30", [9], "mlx5_0", "A"),
    HostNode("ec2-52-36-150-160.us-west-2.compute.amazonaws.com", "172.31.11.30", [10], "mlx5_0", "A"),
    HostNode("ec2-52-36-150-160.us-west-2.compute.amazonaws.com", "172.31.11.30", [11], "mlx5_0", "A"),
    ]
port_bases: Dict[str, int] = {"cpo": 7000, "tso": 8000, "persist": 4000, "nodepool": 10000}
