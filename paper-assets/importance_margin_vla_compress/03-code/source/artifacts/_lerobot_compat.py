"""Compatibility shim for lerobot 0.5.x API changes.

lerobot 0.5.x moved from lerobot.common.{policies,datasets} to
lerobot.{policies,datasets}. The policies __init__ has a groot dataclass
bug on Python 3.12, so we stub it out before importing smolvla.
"""
import sys
import types

def _patch_lerobot_policies():
    key = "lerobot.policies"
    if key not in sys.modules or isinstance(sys.modules[key], types.ModuleType):
        try:
            import lerobot.policies
        except (TypeError, ImportError):
            import lerobot
            stub = types.ModuleType(key)
            stub.__path__ = [p + "/policies" for p in lerobot.__path__]
            stub.__package__ = key
            sys.modules[key] = stub

            smolvla_key = "lerobot.policies.smolvla"
            if smolvla_key not in sys.modules:
                smolvla_stub = types.ModuleType(smolvla_key)
                smolvla_stub.__path__ = [p + "/smolvla" for sp in stub.__path__ for p in [sp]]
                smolvla_stub.__package__ = smolvla_key
                sys.modules[smolvla_key] = smolvla_stub

_patch_lerobot_policies()

from lerobot.policies.smolvla.configuration_smolvla import SmolVLAConfig
from lerobot.policies.smolvla.modeling_smolvla import SmolVLAPolicy
from lerobot.datasets import LeRobotDataset
