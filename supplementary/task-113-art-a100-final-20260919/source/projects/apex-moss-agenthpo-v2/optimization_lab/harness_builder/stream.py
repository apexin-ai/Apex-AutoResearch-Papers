from __future__ import annotations

import re
from dataclasses import dataclass

from .schema import PilotManifest


ARMS = ("A", "B0", "B*", "B-online")
_SHA256 = re.compile(r"[0-9a-f]{64}")


@dataclass(frozen=True)
class StreamItem:
    stream_index: int
    block_index: int
    suite: str
    task_id: str
    arm_order: tuple[str, ...]

    @property
    def instance_id(self) -> str:
        return f"{self.suite}:{self.task_id}"

    def to_dict(self) -> dict[str, object]:
        return {
            "stream_index": self.stream_index,
            "block_index": self.block_index,
            "suite": self.suite,
            "task_id": self.task_id,
            "instance_id": self.instance_id,
            "arm_order": list(self.arm_order),
        }


def _rotate(values: tuple[str, ...], offset: int) -> tuple[str, ...]:
    pivot = offset % len(values)
    return values[pivot:] + values[:pivot]


def build_stream(manifest: PilotManifest) -> tuple[StreamItem, ...]:
    if len(manifest.benchmarks) != 3:
        raise ValueError("prequential stream requires exactly three benchmark suites")
    suite_order = tuple(pool.suite for pool in manifest.benchmarks)
    ranked = {
        pool.suite: tuple(
            sorted(
                (candidate for candidate in pool.candidates if candidate.eligible),
                key=lambda candidate: candidate.selection_digest,
            )
        )
        for pool in manifest.benchmarks
    }
    if any(len(candidates) != 8 for candidates in ranked.values()):
        raise ValueError("each benchmark suite must contribute exactly eight instances")

    items: list[StreamItem] = []
    for block_index in range(8):
        for suite in _rotate(suite_order, block_index):
            candidate = ranked[suite][block_index]
            stream_index = len(items)
            items.append(
                StreamItem(
                    stream_index=stream_index,
                    block_index=block_index,
                    suite=suite,
                    task_id=candidate.task_id,
                    arm_order=_rotate(ARMS, stream_index),
                )
            )
    return tuple(items)


class PrequentialState:
    """In-memory reducer for the test-first, learn-after-seal transition gate."""

    def __init__(
        self,
        stream: tuple[StreamItem, ...],
        *,
        initial_checkpoint_sha256: str,
    ) -> None:
        if not stream:
            raise ValueError("prequential stream cannot be empty")
        if not _SHA256.fullmatch(initial_checkpoint_sha256):
            raise ValueError("initial online checkpoint must be content addressed")
        self._stream = stream
        self._cursor = 0
        self._sealed_arms: set[str] = set()
        self._instance_sealed = False
        self.online_checkpoint_sha256 = initial_checkpoint_sha256

    @property
    def current(self) -> StreamItem:
        if self._cursor >= len(self._stream):
            raise StopIteration("prequential stream is complete")
        return self._stream[self._cursor]

    @property
    def ready_for_distillation(self) -> bool:
        return self._instance_sealed

    def seal_arm(self, arm: str) -> None:
        if self._instance_sealed:
            raise ValueError("distillation must finish before the next arm can start")
        if arm not in ARMS:
            raise ValueError("unknown experiment arm")
        if arm in self._sealed_arms:
            raise ValueError("arm is already sealed for the current instance")
        self._sealed_arms.add(arm)

    def seal_instance(self) -> None:
        if self._instance_sealed:
            raise ValueError("current instance is already sealed")
        if self._sealed_arms != set(ARMS):
            raise ValueError("all arms must be sealed before the instance")
        self._instance_sealed = True

    def apply_distillation(self, new_checkpoint_sha256: str) -> None:
        if not self._instance_sealed:
            raise ValueError("current instance must be sealed before distillation")
        if not _SHA256.fullmatch(new_checkpoint_sha256):
            raise ValueError("distilled checkpoint must be content addressed")
        self.online_checkpoint_sha256 = new_checkpoint_sha256
        self._cursor += 1
        self._sealed_arms.clear()
        self._instance_sealed = False
