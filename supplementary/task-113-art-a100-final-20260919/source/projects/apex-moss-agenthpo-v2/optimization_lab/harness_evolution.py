from __future__ import annotations

import hashlib
import json
import os
import re
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from optimization_lab.feedback import FeedbackCard
from optimization_lab.generation import _sanitize_private_paths


class InvalidHarness(ValueError):
    pass


@dataclass(frozen=True)
class HarnessVersion:
    version_id: str
    text: str
    sha256: str
    parent_version_id: str | None

    @classmethod
    def from_text(
        cls,
        version_id: str,
        text: str,
        *,
        parent_version_id: str | None,
    ) -> "HarnessVersion":
        if not re.fullmatch(r"v\d{3}", version_id):
            raise InvalidHarness("Harness version must use vNNN format")
        if parent_version_id is not None and not re.fullmatch(
            r"v\d{3}", parent_version_id
        ):
            raise InvalidHarness("Harness parent version must use vNNN format")
        normalized = text.strip() + "\n"
        if len(normalized) < 100:
            raise InvalidHarness("Harness response is too short to be a complete workflow")
        if len(normalized) > 20_000:
            raise InvalidHarness("Harness response exceeds the frozen context limit")
        if "\x00" in normalized:
            raise InvalidHarness("Harness response contains a NUL byte")
        if re.search(r"(?<![A-Za-z0-9])/(?:[^\s:|]+/)+[^\s:|]+", normalized):
            raise InvalidHarness("Harness response must not contain absolute paths")
        return cls(
            version_id=version_id,
            text=normalized,
            sha256=hashlib.sha256(normalized.encode()).hexdigest(),
            parent_version_id=parent_version_id,
        )


@dataclass(frozen=True)
class HarnessEvolutionRequest:
    task_id: str
    lineage_id: str
    target_version_id: str
    current_harness: HarnessVersion
    task_card: str
    feedback_history: tuple[FeedbackCard, ...]
    best_candidate_id: str | None
    best_speedup: float | None

    def to_prompt(self) -> str:
        feedback = [
            {
                "candidate_id": card.candidate_id,
                "outcome": card.outcome,
                "compiled": card.compiled,
                "correct": card.correct,
                "speedup_vs_eager": card.speedup_vs_eager,
                "error_summary": _sanitize_private_paths(card.error_summary)[:800],
                "next_action": _sanitize_private_paths(card.next_action)[:800],
            }
            for card in self.feedback_history
        ]
        best = {
            "candidate_id": self.best_candidate_id,
            "speedup_vs_eager": self.best_speedup,
        }
        return f"""你是任务专用 Harness 优化器，不是 Kernel 做题模型。
只为当前任务、当前谱系提出下一版完整 Harness，输出纯 Markdown 正文。

允许修改：提示结构、信息顺序、失败处理、任务记忆、历史最好比较和时间分配。
必须冻结：底层模型、官方评分方法、候选合同、GPU 类型、总预算和八轮上限。
不得读取、猜测或命名私有评分日志、其他谱系、其他任务、评分器实现或未提供的输入；
不得要求跳过正确性、伪造计时、修改 benchmark 或更换模型。

## 身份
- task_id: {self.task_id}
- lineage_id: {self.lineage_id}
- target_version: {self.target_version_id}

## 任务卡
{self.task_card}

## 当前 Harness（{self.current_harness.version_id}）
{self.current_harness.text}

## 仅本谱系的短反馈
{json.dumps(feedback, ensure_ascii=False, indent=2)}

## 本谱系历史最好
{json.dumps(best, ensure_ascii=False)}

输出一份可直接替换当前版本的完整 Harness，不要解释修改过程，不要输出代码围栏或第二份版本。
"""


class HarnessArchive:
    """Immutable Harness versions and raw optimizer responses for one lineage."""

    def __init__(self, scope_root: Path):
        self.scope_root = scope_root.resolve()

    def store_seed(self, text: str, *, expected_sha256: str) -> HarnessVersion:
        version = HarnessVersion.from_text("v001", text, parent_version_id=None)
        if version.sha256 != expected_sha256:
            raise ValueError("P2 seed Harness no longer matches the campaign plan")
        return self._store(version, raw_response=text, metadata_extra={"source": "seed"})

    def store_generated(
        self,
        version: HarnessVersion,
        *,
        raw_response: str,
        prompt_sha256: str,
    ) -> HarnessVersion:
        return self._store(
            version,
            raw_response=raw_response,
            metadata_extra={"source": "optimizer", "prompt_sha256": prompt_sha256},
        )

    def load(self, version_id: str) -> HarnessVersion:
        metadata_path = self.scope_root / "harness_metadata" / f"{version_id}.json"
        if not metadata_path.is_file():
            raise ValueError(f"Harness version is not archived: {version_id}")
        metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
        harness_path = self.scope_root / "harnesses" / f"{version_id}.md"
        if not harness_path.is_file():
            raise ValueError("Harness archive is incomplete")
        text = harness_path.read_text(encoding="utf-8")
        version = HarnessVersion.from_text(
            version_id,
            text,
            parent_version_id=metadata.get("parent_version_id"),
        )
        if version.sha256 != metadata.get("harness_sha256"):
            raise ValueError("archived Harness content changed")
        return version

    def _store(
        self,
        version: HarnessVersion,
        *,
        raw_response: str,
        metadata_extra: dict[str, Any],
    ) -> HarnessVersion:
        harness_path = self.scope_root / "harnesses" / f"{version.version_id}.md"
        raw_path = (
            self.scope_root
            / "raw_harness_responses"
            / f"{version.version_id}.txt"
        )
        metadata_path = (
            self.scope_root
            / "harness_metadata"
            / f"{version.version_id}.json"
        )
        if metadata_path.exists():
            existing = self.load(version.version_id)
            if existing != version:
                raise ValueError("Harness version id is bound to different content")
            return existing
        _write_atomic(harness_path, version.text)
        _write_atomic(raw_path, raw_response)
        _write_atomic(
            metadata_path,
            json.dumps(
                {
                    "schema_version": 1,
                    "version_id": version.version_id,
                    "parent_version_id": version.parent_version_id,
                    "harness_sha256": version.sha256,
                    "harness_path": str(harness_path),
                    "raw_response_path": str(raw_path),
                    **metadata_extra,
                },
                ensure_ascii=False,
                indent=2,
                sort_keys=True,
            )
            + "\n",
        )
        return version


def _write_atomic(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, name = tempfile.mkstemp(dir=path.parent, suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            handle.write(content)
            handle.flush()
            os.fsync(handle.fileno())
        Path(name).replace(path)
    except Exception:
        Path(name).unlink(missing_ok=True)
        raise
