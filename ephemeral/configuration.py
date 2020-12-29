from typing import Iterable
from typing import Optional

import pluggy

QUICK_PORTS = [
    1,
    3,
    7,
    9,
    13,
    17,
    19,
    21,
    22,
    23,
    25,
    26,
    37,
    53,
    79,
    80,
    81,
    82,
    88,
    100,
    106,
    110,
    111,
    113,
    119,
    135,
    139,
    143,
    144,
    179,
    199,
    254,
    255,
    280,
    311,
    389,
    427,
    443,
    444,
    445,
    464,
    465,
    465,
    497,
    513,
    514,
    515,
    543,
    544,
    548,
    554,
    587,
    593,
    625,
    631,
    636,
    646,
    787,
    808,
    873,
    902,
    990,
    993,
    995,
    1000,
    1022,
    1024,
    1025,
    1026,
    1027,
    1028,
    1029,
    1030,
    1031,
    1032,
    1033,
    1035,
    1036,
    1037,
    1038,
    1039,
    1040,
    1041,
    1044,
    1048,
    1049,
    1050,
    1053,
    1054,
    1056,
    1058,
    1059,
    1064,
    1065,
    1066,
    1069,
    1071,
    1074,
    1080,
    1110,
    1234,
    1337,
    1338,
    1433,
    1494,
    1521,
    1720,
    1723,
    1755,
    1761,
    1801,
    1900,
    1935,
    1998,
    2000,
    2001,
    2001,
    2003,
    2005,
    2049,
    2103,
    2105,
    2107,
    2121,
    2161,
    2301,
    2383,
    2401,
    2601,
    2717,
    2869,
    2967,
    3000,
    3001,
    3128,
    3268,
    3306,
    3389,
    3689,
    3690,
    3703,
    3986,
    4000,
    4001,
    4045,
    4899,
    5000,
    5001,
    5003,
    5009,
    5050,
    5051,
    5060,
    5101,
    5120,
    5190,
    5357,
    5432,
    5555,
    5631,
    5666,
    5800,
    5900,
    5901,
    6000,
    6001,
    6002,
    6004,
    6112,
    6646,
    6666,
    7000,
    7070,
    7937,
    7938,
    8000,
    8002,
    8008,
    8009,
    8010,
    8031,
    8080,
    8081,
    8443,
    8888,
    9000,
    9001,
    9090,
    9100,
    9102,
    9999,
    10000,
    10001,
    10010,
    32768,
    32771,
    49152,
    49153,
    49154,
    49155,
    49156,
    49157,
    50000,
]


class Configuration:
    def __init__(
        self,
        verbose: bool,
        target: str,
        port_range: Optional[Iterable[int]],
        quick: bool,
        random: bool,
        thread_count: bool,
        plugin_manager: pluggy.PluginManager,
        write_vulnerable: bool,
    ) -> None:
        self.verbose = verbose
        self.target = target
        self.port_range = port_range or range(2 ** 16) if not quick else QUICK_PORTS
        self.quick = quick
        self.random = random
        self.thread_count = thread_count
        self.plugin_manager = plugin_manager
        self.write_vulnerable = write_vulnerable
