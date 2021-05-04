"""
Contains the NoC and other util classes
"""

class Configuration:
    """
    Config of NoC
    """
    def __init__(self, x_dim = 3, y_dim = 3, vcs = 4, buffer_depth = 10, flits_per_packet = 10):
        self.x_dim = x_dim
        self.y_dim = y_dim
        self.vcs = vcs
        self.buffer_depth = buffer_depth
        self.flits_per_packet = flits_per_packet
        self.simulation_time = 10000
        self.bit_width = 32
        self.benchmark = "synthetic"
        self.report_buffers_of_routers_with_id = [2, 3, 4]
        self.buffer_depth_type = "single"
        self.routing = "XYZ"
        self.clock_delay = 1

    def __repr__(self):
        return "Configuration()"

    def __str__(self):
        return "2-D mesh of size "+str(self.x_dim)+"x"+str(self.y_dim)
