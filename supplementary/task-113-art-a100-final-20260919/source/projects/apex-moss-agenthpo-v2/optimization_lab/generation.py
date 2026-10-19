from __future__ import annotations

import ast
import hashlib
import json
import os
import re
import tempfile
from dataclasses import dataclass, field
from pathlib import Path, PurePosixPath
from typing import Any, Protocol

from optimization_lab.feedback import FeedbackCard


class InvalidCandidate(ValueError):
    pass


@dataclass(frozen=True)
class GenerationResult:
    raw_response: str
    api_cost_usd: float = 0.0
    provider: str = "unknown"
    usage: dict[str, int] = field(default_factory=dict)
    audit_log_path: str = ""

    def __post_init__(self) -> None:
        if self.api_cost_usd < 0:
            raise ValueError("generation API cost cannot be negative")
        if any(value < 0 for value in self.usage.values()):
            raise ValueError("generation usage cannot be negative")


class CandidateGenerator(Protocol):
    def estimated_api_cost_usd(self) -> float:
        """Return a hard-cap reservation made before the model call."""

    def generate(self, prompt: str, *, model: str) -> GenerationResult:
        """Generate one raw response for the frozen prompt and model."""


class FakeGenerator:
    """Deterministic no-network generator used by controller contract tests."""

    def __init__(self, response: str, *, api_cost_usd: float = 0.0):
        if api_cost_usd < 0:
            raise ValueError("generation API cost cannot be negative")
        self.response = response
        self.api_cost_usd = api_cost_usd
        self.calls: list[dict[str, str]] = []

    def estimated_api_cost_usd(self) -> float:
        return self.api_cost_usd

    def generate(self, prompt: str, *, model: str) -> GenerationResult:
        self.calls.append({"prompt": prompt, "model": model})
        return GenerationResult(
            raw_response=self.response,
            api_cost_usd=self.api_cost_usd,
            provider="fake",
        )


@dataclass(frozen=True)
class GeneratedCandidate:
    raw_response: str
    code: str
    sha256: str

    @classmethod
    def from_response(cls, response: str) -> "GeneratedCandidate":
        blocks = re.findall(r"```([^\n]*)\n(.*?)```", response, flags=re.DOTALL)
        if len(blocks) != 1:
            raise InvalidCandidate("response must contain exactly one fenced code block")
        language, code = blocks[0]
        if language.strip().lower() not in {"", "python", "py"}:
            raise InvalidCandidate("the candidate code block must be Python")
        code = code.strip() + "\n"
        try:
            tree = ast.parse(code)
        except SyntaxError as exc:
            raise InvalidCandidate(f"candidate syntax error: {exc.msg}") from exc
        model_classes = [
            node
            for node in ast.walk(tree)
            if isinstance(node, ast.ClassDef) and node.name == "ModelNew"
        ]
        if len(model_classes) != 1:
            raise InvalidCandidate("candidate must define exactly one ModelNew class")
        return cls(
            raw_response=response,
            code=code,
            sha256=hashlib.sha256(code.encode()).hexdigest(),
        )


@dataclass(frozen=True)
class GenerationRequest:
    task_id: str
    lane_id: str
    harness_text: str
    task_card: str
    reference_source: str
    feedback_history: tuple[FeedbackCard, ...] = ()
    previous_candidate: str | None = None
    best_candidate_id: str | None = None
    best_candidate: str | None = None

    def __post_init__(self) -> None:
        if not all(
            (self.task_id, self.lane_id, self.harness_text, self.task_card, self.reference_source)
        ):
            raise ValueError("generation request fields cannot be empty")
        if any(card.task_id != self.task_id for card in self.feedback_history):
            raise ValueError("feedback task does not match generation task")

    def to_prompt(self) -> str:
        feedback = [self._public_feedback(card) for card in self.feedback_history]
        previous = self.previous_candidate or "（这是第一轮，没有上一候选）"
        best = self.best_candidate or "（尚无正确的历史最好候选）"
        return f"""你正在执行一套冻结的 KernelBench Harness。严格按 Harness 工作流行动，
只输出一个包含完整候选的 Python 代码块。不要输出第二个代码块。

## Harness
{self.harness_text}

## 任务卡
{self.task_card}

## 固定参考实现
```text
{self.reference_source}
```

## 本 lane 上一候选
```text
{previous}
```

## 本 lane 历史最好候选（{self.best_candidate_id or '无'}）
```text
{best}
```

## 本 lane 的短反馈卡
{json.dumps(feedback, ensure_ascii=False, indent=2)}

不得读取或推断私有评分日志、其他 lane 的历史、评分器实现或未提供的输入。"""

    @staticmethod
    def _public_feedback(card: FeedbackCard) -> dict[str, Any]:
        return {
            "candidate_id": card.candidate_id,
            "outcome": card.outcome,
            "stage_reached": card.stage_reached,
            "compiled": card.compiled,
            "correct": card.correct,
            "speedup_vs_eager": card.speedup_vs_eager,
            "error_summary": _sanitize_private_paths(card.error_summary)[:800],
            "next_action": card.next_action,
        }


class CandidateArchive:
    """Append-only model output archive scoped to exactly one baseline or lineage."""

    def __init__(self, artifact_root: Path, history_scope: str):
        root = artifact_root.resolve()
        scope = PurePosixPath(history_scope)
        if scope.is_absolute() or not scope.parts or ".." in scope.parts:
            raise ValueError("history scope must be a safe relative path")
        self.root = root
        self.scope_root = (root / Path(*scope.parts)).resolve()
        if not self.scope_root.is_relative_to(root):
            raise ValueError("history scope escapes artifact root")

    def store(
        self,
        candidate_id: str,
        candidate: GeneratedCandidate,
    ) -> dict[str, str]:
        if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._-]{0,127}", candidate_id):
            raise ValueError("candidate id must be a safe, single path component")
        candidate_path = self.scope_root / "candidates" / f"{candidate_id}.py"
        raw_path = self.scope_root / "raw_responses" / f"{candidate_id}.txt"
        metadata_path = self.scope_root / "metadata" / f"{candidate_id}.json"
        result = {
            "candidate_path": str(candidate_path),
            "raw_response_path": str(raw_path),
            "metadata_path": str(metadata_path),
        }
        if metadata_path.exists():
            metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
            if metadata.get("candidate_sha256") != candidate.sha256:
                raise ValueError("candidate id is already bound to different content")
            if not candidate_path.is_file() or not raw_path.is_file():
                raise ValueError("candidate archive is incomplete")
            if hashlib.sha256(candidate_path.read_bytes()).hexdigest() != candidate.sha256:
                raise ValueError("archived candidate content no longer matches metadata")
            return result

        _write_atomic(candidate_path, candidate.code)
        _write_atomic(raw_path, candidate.raw_response)
        metadata = {
            "schema_version": 1,
            "candidate_id": candidate_id,
            "candidate_sha256": candidate.sha256,
            **result,
        }
        _write_atomic(
            metadata_path,
            json.dumps(metadata, ensure_ascii=False, indent=2) + "\n",
        )
        return result

    def store_rejected(
        self,
        candidate_id: str,
        raw_response: str,
        error: str,
    ) -> dict[str, str]:
        """Archive invalid model output without making it an executable candidate."""
        _validate_candidate_id(candidate_id)
        raw_path = self.scope_root / "raw_responses" / f"{candidate_id}.txt"
        metadata_path = self.scope_root / "metadata" / f"{candidate_id}.json"
        result = {
            "raw_response_path": str(raw_path),
            "metadata_path": str(metadata_path),
        }
        response_sha = hashlib.sha256(raw_response.encode()).hexdigest()
        if metadata_path.exists():
            metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
            if (
                metadata.get("status") != "rejected"
                or metadata.get("raw_response_sha256") != response_sha
            ):
                raise ValueError("candidate id is already bound to different content")
            if not raw_path.is_file():
                raise ValueError("rejected candidate archive is incomplete")
            return result
        _write_atomic(raw_path, raw_response)
        _write_atomic(
            metadata_path,
            json.dumps(
                {
                    "schema_version": 1,
                    "candidate_id": candidate_id,
                    "status": "rejected",
                    "raw_response_sha256": response_sha,
                    "error": error,
                    **result,
                },
                ensure_ascii=False,
                indent=2,
            )
            + "\n",
        )
        return result


def _sanitize_private_paths(text: str) -> str:
    return re.sub(
        r"(?<![A-Za-z0-9])/(?:[^\s:|]+/)*[^\s:|]+",
        "<private-path>",
        text,
    )


def _validate_candidate_id(candidate_id: str) -> None:
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._-]{0,127}", candidate_id):
        raise ValueError("candidate id must be a safe, single path component")


def _write_atomic(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, name = tempfile.mkstemp(dir=path.parent, suffix=".archive.tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            handle.write(content)
            handle.flush()
            os.fsync(handle.fileno())
        Path(name).replace(path)
    except Exception:
        Path(name).unlink(missing_ok=True)
        raise
