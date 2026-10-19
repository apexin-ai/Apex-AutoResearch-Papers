from __future__ import annotations

import fcntl
import hashlib
import json
import os
import re
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


_ZERO_SHA256 = "0" * 64
_SHA256 = re.compile(r"[0-9a-f]{64}")


def _canonical_bytes(payload: dict[str, Any]) -> bytes:
    return json.dumps(
        payload,
        ensure_ascii=False,
        allow_nan=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")


class ExperimentRegistry:
    """Fact log plus a disposable materialized state summary.

    Historical campaigns retain their original unchained JSONL format.  New
    trust-sensitive controllers opt into ``hash_chain_v1``; those ledgers are
    canonical, hash chained, and bound to an atomically replaced head anchor.
    A reader auto-detects and verifies the strict format even when opened by
    legacy orchestration code.
    """

    def __init__(self, root: Path, *, integrity_mode: str = "legacy"):
        if integrity_mode not in {"legacy", "hash_chain_v1"}:
            raise ValueError("unsupported registry integrity mode")
        self.root = root.resolve()
        self.root.mkdir(parents=True, exist_ok=True)
        self.ledger_path = self.root / "ledger.jsonl"
        self.state_path = self.root / "state.json"
        self.lock_path = self.root / ".ledger.lock"
        self.head_path = self.root / "trusted-ledger-head.json"
        self.integrity_mode = integrity_mode

    def read_events(self) -> list[dict[str, Any]]:
        if not self.ledger_path.exists():
            if self.ledger_path.is_symlink() or (
                self.integrity_mode == "hash_chain_v1" and self.head_path.exists()
            ):
                raise ValueError("trusted registry ledger/head presence differs")
            return []
        if self.ledger_path.is_symlink() or not self.ledger_path.is_file():
            raise ValueError("registry ledger must be a regular file")
        try:
            lines = self.ledger_path.read_text(encoding="utf-8").splitlines()
        except UnicodeDecodeError as exc:
            raise ValueError("registry ledger is not UTF-8") from exc
        if any(not line.strip() for line in lines):
            raise ValueError("registry ledger contains an empty event")
        events: list[dict[str, Any]] = []
        for line in lines:
            try:
                event = json.loads(line)
            except json.JSONDecodeError as exc:
                raise ValueError("registry ledger contains invalid JSON") from exc
            if not isinstance(event, dict):
                raise ValueError("registry event must be an object")
            events.append(event)
        strict = bool(events and events[0].get("schema_version") == 2)
        if self.integrity_mode == "hash_chain_v1" and events and not strict:
            raise ValueError("trusted registry cannot adopt a legacy ledger")
        if strict:
            self._verify_strict_events(events, lines)
        return events

    def _verify_strict_events(
        self, events: list[dict[str, Any]], lines: list[str]
    ) -> None:
        expected_fields = {
            "schema_version",
            "sequence",
            "event_id",
            "event_type",
            "recorded_at",
            "prev_event_sha256",
            "payload",
            "event_sha256",
        }
        previous = _ZERO_SHA256
        event_ids: set[str] = set()
        for sequence, (event, line) in enumerate(zip(events, lines), start=1):
            if set(event) != expected_fields or event["schema_version"] != 2:
                raise ValueError("trusted registry event schema differs")
            if type(event["sequence"]) is not int or event["sequence"] != sequence:
                raise ValueError("trusted registry sequence is not contiguous")
            if (
                not isinstance(event["event_id"], str)
                or not event["event_id"]
                or event["event_id"] in event_ids
                or not isinstance(event["event_type"], str)
                or not event["event_type"]
                or not isinstance(event["payload"], dict)
            ):
                raise ValueError("trusted registry event identity differs")
            event_ids.add(event["event_id"])
            try:
                timestamp = datetime.fromisoformat(event["recorded_at"])
            except (TypeError, ValueError) as exc:
                raise ValueError("trusted registry timestamp is invalid") from exc
            if timestamp.tzinfo is None:
                raise ValueError("trusted registry timestamp lacks a timezone")
            if event["prev_event_sha256"] != previous:
                raise ValueError("trusted registry hash chain is broken")
            core = {key: value for key, value in event.items() if key != "event_sha256"}
            expected_sha = hashlib.sha256(_canonical_bytes(core)).hexdigest()
            if (
                not isinstance(event["event_sha256"], str)
                or _SHA256.fullmatch(event["event_sha256"]) is None
                or event["event_sha256"] != expected_sha
                or line.encode("utf-8") != _canonical_bytes(event)
            ):
                raise ValueError("trusted registry event hash/canonical form differs")
            previous = event["event_sha256"]
        if self.head_path.is_symlink() or not self.head_path.is_file():
            raise ValueError("trusted registry head anchor is missing")
        try:
            anchor = json.loads(self.head_path.read_text(encoding="utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError) as exc:
            raise ValueError("trusted registry head anchor is invalid") from exc
        if anchor != {
            "schema_version": 1,
            "event_count": len(events),
            "head_sha256": previous,
        }:
            raise ValueError("trusted registry head anchor differs")

    def append(
        self,
        event_type: str,
        payload: dict[str, Any],
        *,
        event_id: str,
    ) -> dict[str, Any]:
        if not event_type or not event_id:
            raise ValueError("event type and id are required")
        if self.lock_path.is_symlink():
            raise ValueError("registry lock cannot be a symlink")
        with self.lock_path.open("a+", encoding="utf-8") as lock:
            fcntl.flock(lock, fcntl.LOCK_EX)
            try:
                events = self.read_events()
                for event in events:
                    if event["event_id"] == event_id:
                        if (
                            event.get("event_type") == event_type
                            and event.get("payload") == payload
                        ):
                            return event
                        raise ValueError(
                            "event id is already bound to different registry content"
                        )
                if self.integrity_mode == "hash_chain_v1":
                    previous = events[-1]["event_sha256"] if events else _ZERO_SHA256
                    core = {
                        "schema_version": 2,
                        "sequence": len(events) + 1,
                        "event_id": event_id,
                        "event_type": event_type,
                        "recorded_at": datetime.now(timezone.utc).isoformat(),
                        "prev_event_sha256": previous,
                        "payload": payload,
                    }
                    event = {
                        **core,
                        "event_sha256": hashlib.sha256(
                            _canonical_bytes(core)
                        ).hexdigest(),
                    }
                    encoded = _canonical_bytes(event) + b"\n"
                    if self.ledger_path.is_symlink():
                        raise ValueError("registry ledger cannot be a symlink")
                    with self.ledger_path.open("ab") as ledger:
                        ledger.write(encoded)
                        ledger.flush()
                        os.fsync(ledger.fileno())
                    self._write_head(
                        event_count=len(events) + 1,
                        head_sha256=event["event_sha256"],
                    )
                else:
                    event = {
                        "event_id": event_id,
                        "event_type": event_type,
                        "recorded_at": datetime.now(timezone.utc).isoformat(),
                        "payload": payload,
                    }
                    encoded = json.dumps(event, ensure_ascii=False, sort_keys=True)
                    with self.ledger_path.open("a", encoding="utf-8") as ledger:
                        ledger.write(encoded + "\n")
                        ledger.flush()
                        os.fsync(ledger.fileno())
                events.append(event)
                self._write_state(events)
                return event
            finally:
                fcntl.flock(lock, fcntl.LOCK_UN)

    def _write_head(self, *, event_count: int, head_sha256: str) -> None:
        if self.head_path.is_symlink():
            raise ValueError("trusted registry head cannot be a symlink")
        content = _canonical_bytes(
            {
                "schema_version": 1,
                "event_count": event_count,
                "head_sha256": head_sha256,
            }
        ) + b"\n"
        fd, name = tempfile.mkstemp(dir=self.root, suffix=".head.tmp")
        try:
            with os.fdopen(fd, "wb") as handle:
                handle.write(content)
                handle.flush()
                os.fsync(handle.fileno())
            Path(name).replace(self.head_path)
        except Exception:
            Path(name).unlink(missing_ok=True)
            raise

    def _write_state(self, events: list[dict[str, Any]]) -> None:
        state = {
            "schema_version": 1,
            "event_count": len(events),
            "last_event": events[-1] if events else None,
            "updated_at": datetime.now(timezone.utc).isoformat(),
        }
        fd, name = tempfile.mkstemp(dir=self.root, suffix=".state.tmp")
        try:
            with os.fdopen(fd, "w", encoding="utf-8") as handle:
                json.dump(state, handle, ensure_ascii=False, indent=2, sort_keys=True)
                handle.write("\n")
                handle.flush()
                os.fsync(handle.fileno())
            Path(name).replace(self.state_path)
        except Exception:
            Path(name).unlink(missing_ok=True)
            raise
