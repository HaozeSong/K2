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
    HostNode("ec2-35-84-195-137.us-west-2.compute.amazonaws.com", "172.31.58.29", [0,1,2,3], "mlx5_0", "A"),
    HostNode("ec2-35-84-195-137.us-west-2.compute.amazonaws.com", "172.31.58.29", [4,5], "mlx5_0", "A"),
    HostNode("ec2-35-84-195-137.us-west-2.compute.amazonaws.com", "172.31.58.29", [6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25], "mlx5_0", "A"),
    HostNode("ec2-35-84-195-137.us-west-2.compute.amazonaws.com", "172.31.58.29", [26], "mlx5_0", "A"),
    HostNode("ec2-35-84-195-137.us-west-2.compute.amazonaws.com", "172.31.58.29", [27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46], "mlx5_0", "A"),
    ]
port_bases: Dict[str, int] = {"cpo": 7000, "tso": 8000, "persist": 4000, "nodepool": 10000}
