"""MAST dataset loading and inter-agent message extraction.

Input: MAD_full_dataset.json / MAD_human_labelled_dataset.json from HuggingFace (mcemri/MAD)
Output: Structured traces with inter-agent messages extracted per MAS framework
"""

import json
import re
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Optional


MAST_DATA_DIR = Path(__file__).parent.parent / "data" / "mast"

FAILURE_MODE_NAMES = {
    "1.1": "Poor task constraint compliance",
    "1.2": "Poor system prompt following",
    "1.3": "Step derailment",
    "1.4": "Erroneous action planning",
    "1.5": "Task interference",
    "2.1": "Conversation derailment",
    "2.2": "Miscommunication cascade",
    "2.3": "Redundant actions",
    "2.4": "Information withholding",
    "2.5": "Uninstructed actions",
    "2.6": "Poor task delegation",
    "3.1": "Premature termination",
    "3.2": "Absent verification",
    "3.3": "Faulty verification",
}


@dataclass
class Message:
    sender: str
    receiver: str
    content: str
    action: str = ""
    timestamp: str = ""
    metadata: dict = field(default_factory=dict)


@dataclass
class MastTrace:
    trace_id: int
    mas_name: str
    llm_name: str
    benchmark_name: str
    messages: list[Message]
    failure_modes: dict[str, int]
    raw_trajectory: str = ""

    def to_dict(self) -> dict:
        return {
            "trace_id": self.trace_id,
            "mas_name": self.mas_name,
            "llm_name": self.llm_name,
            "benchmark_name": self.benchmark_name,
            "messages": [asdict(m) for m in self.messages],
            "failure_modes": self.failure_modes,
        }


def _parse_metagpt_messages(trajectory: str) -> list[Message]:
    """Parse MetaGPT structured logs: FROM/TO/ACTION/CONTENT blocks and NEW MESSAGES blocks."""
    messages = []
    # Structured FROM/TO/ACTION/CONTENT format
    pattern = re.compile(
        r"\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\]\s+FROM:\s+(.+?)\s+TO:\s+(.+?)\n"
        r"ACTION:\s+(.+?)\n"
        r"CONTENT:\s*\n(.*?)(?=\n-{40,}|\Z)",
        re.DOTALL,
    )
    for m in pattern.finditer(trajectory):
        ts, sender, receiver, action, content = m.groups()
        receiver = receiver.strip().strip("{}'\"\u200b")
        messages.append(Message(
            sender=sender.strip(),
            receiver=receiver,
            content=content.strip(),
            action=action.strip(),
            timestamp=ts,
        ))

    # NEW MESSAGES blocks: [timestamp] NEW MESSAGES:\n\nAgentName:\ncontent...
    block_pat = re.compile(
        r"\[([\d\- :]+)\]\s+NEW MESSAGES:\s*\n\n(\w+):\s*\n(.*?)(?=\n-{40,}|\[[\d\- :]+\]|\Z)",
        re.DOTALL,
    )
    for m in block_pat.finditer(trajectory):
        ts, sender, content = m.groups()
        messages.append(Message(
            sender=sender.strip(),
            receiver="<all>",
            content=content.strip(),
            timestamp=ts.strip(),
        ))
    return messages


def _parse_chatdev_messages(trajectory: str) -> list[Message]:
    """Parse ChatDev phase-based conversation logs."""
    messages = []
    phase_pat = re.compile(
        r"\[[\d\- :]+\s+INFO\]\s+(.+?):\s+\*\*\[(.+?)\]\*\*\s*\n(.*?)(?=\n\[[\d\- :]+\s+INFO\]|\Z)",
        re.DOTALL,
    )
    for m in phase_pat.finditer(trajectory):
        sender, phase_tag, content = m.groups()
        messages.append(Message(
            sender=sender.strip(),
            receiver="<next>",
            content=content.strip()[:5000],
            metadata={"phase": phase_tag.strip()},
        ))
    return messages


def _parse_appworld_messages(trajectory: str) -> list[Message]:
    """Parse AppWorld supervisor-agent message exchange logs."""
    messages = []
    sup_pat = re.compile(
        r"Response from Supervisor Agent\s*\n(.*?)(?=\nCode Execution Output|\nEntering \w+ Agent|\Z)",
        re.DOTALL,
    )
    for m in sup_pat.finditer(trajectory):
        messages.append(Message(
            sender="Supervisor",
            receiver="<dispatch>",
            content=m.group(1).strip()[:5000],
        ))

    agent_pat = re.compile(
        r"(?:Message to|Response from)\s+(\w+)\s+Agent\s*\n\s*(.*?)(?=\n\s*(?:Message to|Response from)|Entering \w+ Agent|Response from Supervisor|\Z)",
        re.DOTALL,
    )
    for m in agent_pat.finditer(trajectory):
        agent_name = m.group(1).strip()
        content = m.group(2).strip()
        if "Message to" in m.group(0):
            messages.append(Message(sender="Supervisor", receiver=agent_name, content=content[:5000]))
        else:
            messages.append(Message(sender=agent_name, receiver="Supervisor", content=content[:5000]))
    return messages


def _parse_ag2_messages(trajectory: str) -> list[Message]:
    """Parse AG2 (AutoGen) traces — YAML-like indented content/role/name blocks."""
    messages = []
    if "trajectory:" not in trajectory:
        return messages
    traj_section = trajectory.split("trajectory:", 1)[1]

    # Split into message blocks by looking for content: fields
    block_pat = re.compile(
        r"^\s+content:\s*\n(.*?)(?=^\s+content:|\Z)",
        re.DOTALL | re.MULTILINE,
    )
    role_pat = re.compile(r"^\s+role:\s*(\w+)", re.MULTILINE)
    name_pat = re.compile(r"^\s+name:\s*(\w+)", re.MULTILINE)

    # Find all content blocks with their surrounding role/name
    parts = re.split(r"(?=^\s+content:)", traj_section, flags=re.MULTILINE)
    for part in parts:
        content_m = re.match(r"^\s+content:\s*\n?(.*)", part, re.DOTALL)
        if not content_m:
            continue
        remaining = content_m.group(1)
        # Split content from metadata — role/name appear after content at same indent
        meta_split = re.split(r"\n\s+role:", remaining, maxsplit=1)
        content_text = meta_split[0].strip()
        role = "assistant"
        name = ""
        if len(meta_split) > 1:
            role_m = re.search(r"(\w+)", meta_split[1])
            if role_m:
                role = role_m.group(1)
            name_m = re.search(r"name:\s*(\w+)", meta_split[1])
            if name_m:
                name = name_m.group(1)
        sender = name if name else role
        messages.append(Message(
            sender=sender,
            receiver="<next>",
            content=content_text[:5000],
            metadata={"role": role, "name": name} if name else {"role": role},
        ))
    return messages


def _parse_generic_messages(trajectory: str) -> list[Message]:
    """Fallback parser for Magentic/HyperAgent/OpenManus — extract conversation turns."""
    messages = []
    turn_pat = re.compile(
        r"(?:^|\n)(?:INFO|DEBUG)?\s*\[?[\d\- :.]*\]?\s*(?:\|\s*\w+\s*\|)?\s*(.+?)(?:says|:)\s*(.*?)(?=\n(?:INFO|DEBUG)?\s*\[|\Z)",
        re.DOTALL,
    )
    for m in turn_pat.finditer(trajectory[:50000]):
        sender, content = m.groups()
        if len(content.strip()) > 10:
            messages.append(Message(
                sender=sender.strip()[:100],
                receiver="<unknown>",
                content=content.strip()[:5000],
            ))
    return messages


PARSERS = {
    "MetaGPT": _parse_metagpt_messages,
    "ChatDev": _parse_chatdev_messages,
    "AppWorld": _parse_appworld_messages,
    "AG2": _parse_ag2_messages,
}


def parse_trace_messages(entry: dict) -> list[Message]:
    """Route to the appropriate parser based on MAS framework name."""
    mas_name = entry["mas_name"]
    trace_data = entry.get("trace", "")
    if isinstance(trace_data, dict):
        trajectory = trace_data.get("trajectory", "")
    else:
        trajectory = trace_data

    parser = PARSERS.get(mas_name, _parse_generic_messages)
    return parser(trajectory)


def load_mast_full(
    path: Optional[str] = None,
    mas_filter: Optional[list[str]] = None,
) -> list[MastTrace]:
    """Load MAD_full_dataset.json and parse into structured MastTrace objects."""
    if path is None:
        path = str(MAST_DATA_DIR / "MAD_full_dataset.json")
    with open(path) as f:
        raw = json.load(f)

    traces = []
    for entry in raw:
        if mas_filter and entry["mas_name"] not in mas_filter:
            continue
        messages = parse_trace_messages(entry)
        traces.append(MastTrace(
            trace_id=entry["trace_id"],
            mas_name=entry["mas_name"],
            llm_name=entry.get("llm_name", ""),
            benchmark_name=entry["benchmark_name"],
            messages=messages,
            failure_modes=entry.get("mast_annotation", {}),
        ))
    return traces


def load_mast_human_labelled(
    path: Optional[str] = None,
) -> list[MastTrace]:
    """Load MAD_human_labelled_dataset.json."""
    if path is None:
        path = str(MAST_DATA_DIR / "MAD_human_labelled_dataset.json")
    with open(path) as f:
        raw = json.load(f)

    traces = []
    for entry in raw:
        messages = parse_trace_messages(entry)
        annotations = entry.get("annotations", [])
        failure_modes = {}
        for ann in annotations:
            fm_name = ann.get("failure mode", "")
            code_match = re.match(r"(\d+\.\d+)", fm_name)
            if code_match:
                code = code_match.group(1)
                votes = sum(1 for k in ["annotator_1", "annotator_2", "annotator_3"]
                            if ann.get(k, False))
                failure_modes[code] = 1 if votes >= 2 else 0

        traces.append(MastTrace(
            trace_id=entry["trace_id"],
            mas_name=entry["mas_name"],
            llm_name=entry.get("llm_name", ""),
            benchmark_name=entry["benchmark_name"],
            messages=messages,
            failure_modes=failure_modes,
        ))
    return traces


def get_inter_agent_messages(trace: MastTrace) -> list[Message]:
    """Filter to only inter-agent messages (exclude human/system)."""
    exclude_senders = {"Human", "human", "system", "System", "user"}
    return [m for m in trace.messages if m.sender not in exclude_senders]


def trace_summary(trace: MastTrace) -> dict:
    """Quick summary stats for a trace."""
    msgs = trace.messages
    inter = get_inter_agent_messages(trace)
    active_failures = [
        f"{code}: {FAILURE_MODE_NAMES.get(code, code)}"
        for code, val in trace.failure_modes.items() if val == 1
    ]
    return {
        "trace_id": trace.trace_id,
        "mas_name": trace.mas_name,
        "llm_name": trace.llm_name,
        "benchmark": trace.benchmark_name,
        "total_messages": len(msgs),
        "inter_agent_messages": len(inter),
        "unique_senders": list({m.sender for m in msgs}),
        "failure_modes": active_failures,
    }
