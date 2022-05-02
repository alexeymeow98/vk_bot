from typing import Optional
from dataclasses import dataclass, field

@dataclass
class UserState:
    scenario_name: str
    step_name: str
    context: Optional[dict] = field(default_factory=dict)
