from dataclasses import dataclass


@dataclass(frozen=True, repr=True, eq=True)
class ScanResult:
    port: int
    is_open: bool
