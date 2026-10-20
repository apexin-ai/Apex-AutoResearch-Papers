"""DTD shared data structures and utility functions.

Defines TraceEvent, TraceSegment, ScoredSegment dataclasses used across all modules.
Provides serialization helpers and token estimation.
"""
from __future__ import annotations

import json
from dataclasses import dataclass, field, asdict
from typing import Any, Dict, List, Optional


@dataclass
class TraceEvent:
    event_type: str  # "call", "return", "line", "exception"
    function_name: str
    filename: str
    lineno: int
    locals_snapshot: dict
    call_depth: int
    timestamp: float
    return_value: Any = None
    exception_info: Optional[tuple] = None  # (type, value, traceback_str)


@dataclass
class TraceSegment:
    segment_type: str  # "call_subtree", "loop_iteration", "exception_chain", "basic_block", "line_window"
    events: List[TraceEvent]
    start_idx: int
    end_idx: int
    metadata: dict
    token_estimate: int = 0

    def __post_init__(self):
        if self.token_estimate == 0:
            self.token_estimate = estimate_tokens(str(self.events))


@dataclass
class ScoredSegment:
    segment: TraceSegment
    label: str  # "keep" or "drop"
    confidence: float
    reasoning: str


def estimate_tokens(text: str) -> int:
    return len(text) // 4


def serialize_event(event: TraceEvent) -> dict:
    d = {
        "event_type": event.event_type,
        "function_name": event.function_name,
        "filename": event.filename,
        "lineno": event.lineno,
        "locals_snapshot": _safe_serialize(event.locals_snapshot),
        "call_depth": event.call_depth,
        "timestamp": event.timestamp,
    }
    if event.return_value is not None:
        d["return_value"] = repr(event.return_value)
    if event.exception_info is not None:
        d["exception_info"] = {
            "type": str(event.exception_info[0]),
            "value": str(event.exception_info[1]),
            "traceback": event.exception_info[2] if len(event.exception_info) > 2 else "",
        }
    return d


def serialize_segment(segment: TraceSegment) -> dict:
    return {
        "segment_type": segment.segment_type,
        "start_idx": segment.start_idx,
        "end_idx": segment.end_idx,
        "metadata": segment.metadata,
        "token_estimate": segment.token_estimate,
        "events": [serialize_event(e) for e in segment.events],
    }


def _safe_serialize(obj: Any, max_depth: int = 3) -> Any:
    if max_depth <= 0:
        return repr(obj)
    if isinstance(obj, dict):
        return {str(k): _safe_serialize(v, max_depth - 1) for k, v in list(obj.items())[:50]}
    if isinstance(obj, (list, tuple)):
        truncated = list(obj[:100])
        return [_safe_serialize(v, max_depth - 1) for v in truncated]
    if isinstance(obj, str):
        return obj[:500]
    if isinstance(obj, (int, float, bool, type(None))):
        return obj
    return repr(obj)[:200]
