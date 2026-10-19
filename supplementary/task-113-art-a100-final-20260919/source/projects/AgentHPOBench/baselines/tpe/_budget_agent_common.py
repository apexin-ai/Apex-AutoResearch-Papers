#!/usr/bin/env python3
from __future__ import annotations

import gc
import ast
import json
import math
import os
import re
import shutil
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(os.environ.get("AUTOREP_ROOT", "."))
FORMAL_ROOT = ROOT / "baselines/tpe"
RESULTS_BASE = Path(os.environ.get("AUTOREP_AGENT_RESULTS_BASE", str(ROOT / "results/formal_agent/qwen3_32b")))
MODEL_PATH = Path(os.environ.get("QWEN3_MODEL", "models/Qwen/Qwen3-32B"))
AGENT_LABEL = os.environ.get("AUTOREP_AGENT_LABEL", "QwenLocal")
RESULT_FILE_AGENT_NAME = "QwenLocal"
_AGENT_CACHE: dict[tuple[str, str, str, str, str, str], Any] = {}


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def load_json(path: Path) -> Any:
    return json.loads(path.read_text())


def dump_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")


def run_cmd(cmd: list[str], cwd: Path, env: dict[str, str], log_path: Path, append: bool = False) -> float:
    log_path.parent.mkdir(parents=True, exist_ok=True)
    started = time.time()
    mode = "ab" if append else "wb"
    with log_path.open(mode) as log:
        if append:
            log.write(b"\n")
        log.write(("COMMAND: " + " ".join(cmd) + "\n").encode())
        log.flush()
        proc = subprocess.run(cmd, cwd=str(cwd), env=env, stdout=log, stderr=subprocess.STDOUT)
    if proc.returncode != 0:
        tail = log_path.read_text(errors="replace")[-8000:]
        print(tail, flush=True)
        raise RuntimeError(f"command failed rc={proc.returncode}: {' '.join(cmd)}")
    return round(time.time() - started, 3)


def run_shell(script: str, cwd: Path, env: dict[str, str], log_path: Path, append: bool = False) -> float:
    return run_cmd(["bash", "-lc", script], cwd=cwd, env=env, log_path=log_path, append=append)


def nearest(value: Any, choices: list[Any]) -> Any:
    if not choices:
        return value
    if isinstance(choices[0], bool):
        if isinstance(value, str):
            return value.strip().lower() in {"1", "true", "yes", "on"}
        return bool(value)
    if isinstance(choices[0], str):
        candidate = str(value).strip()
        lower_map = {str(item).lower(): item for item in choices}
        return lower_map.get(candidate.lower(), choices[0])
    try:
        number = float(value)
        return min(choices, key=lambda item: abs(float(item) - number))
    except Exception:
        return choices[0]


def clamp_config(
    proposed: dict[str, Any],
    base: dict[str, Any],
    search_space: dict[str, list[Any]],
    aliases: dict[str, str] | None = None,
) -> dict[str, Any]:
    aliases = aliases or {}
    merged = dict(base)
    for key, value in (proposed or {}).items():
        mapped = aliases.get(str(key), str(key))
        if mapped in merged:
            merged[mapped] = value
    clamped: dict[str, Any] = {}
    for key, value in merged.items():
        if key in search_space:
            selected = nearest(value, search_space[key])
        else:
            selected = value
        if isinstance(base.get(key), int) and not isinstance(base.get(key), bool):
            selected = int(selected)
        elif isinstance(base.get(key), float):
            selected = float(selected)
        elif isinstance(base.get(key), bool):
            selected = bool(selected)
        clamped[key] = selected
    return clamped


def cleanup_torch() -> None:
    gc.collect()
    try:
        import torch

        if torch.cuda.is_available():
            torch.cuda.empty_cache()
            try:
                torch.cuda.ipc_collect()
            except Exception:
                pass
    except Exception:
        pass
    gc.collect()


def decide_config(
    *,
    task_name: str,
    current_config: dict[str, Any],
    search_space: dict[str, list[Any]],
    training_log: str,
    metrics_history: list[Any] | None = None,
    budget_remaining: int = 1,
    total_budget: int = 1,
    decision_number: int = 0,
    aliases: dict[str, str] | None = None,
) -> dict[str, Any]:
    """Run the local open-source agent once and return a clamped decision record."""
    sys.path.insert(0, str(ROOT))
    deps = ROOT / ".python_deps"
    if deps.exists():
        sys.path.insert(0, str(deps))
    started = time.time()
    raw_config: dict[str, Any] = {}
    reasoning = "Fallback: keep current configuration."
    confidence = 0.5
    metadata: dict[str, Any] = {"fallback": True}
    agent_stats: dict[str, Any] = {
        "name": AGENT_LABEL,
        "model_name": str(MODEL_PATH),
        "total_decisions": 0,
    }

    backend = str(os.environ.get("AUTOREP_AGENT_BACKEND", "")).strip().lower()
    if backend in {"random", "random_search", "tpe", "tpe_search", "bayesian", "bayesopt", "bayesian_optimization"}:
        import random

        seed = os.environ.get("AUTOREP_RANDOM_SEED", os.environ.get("AUTOREP_TPE_SEED", "0"))
        state = json.dumps(current_config, sort_keys=True, default=str)
        rng = random.Random(f"{seed}:{task_name}:{decision_number}:{state}")
        if backend in {"random", "random_search", "tpe", "tpe_search", "bayesian", "bayesopt", "bayesian_optimization"}:
            from tpe_backend import propose_tpe_config
            raw_config = propose_tpe_config(task_name=task_name, current_config=current_config, search_space=search_space, history=metrics_history or [], training_log=training_log, seed=seed, decision_number=decision_number)
            backend_name = "tpe_search"
            reasoning = "TPE baseline selected a configuration from the allowed discrete intervention space using observed trials."
        else:
            raw_config = {key: rng.choice(list(values)) for key, values in search_space.items() if values}
            backend_name = "random_search"
            reasoning = "Random-search baseline sampled uniformly from the allowed intervention space."
        new_config = clamp_config(raw_config, current_config, search_space, aliases=aliases)
        return {
            "task_name": task_name,
            "new_config": new_config,
            "raw_new_config": raw_config,
            "reasoning": reasoning,
            "confidence": 0.0,
            "metadata": {"backend": backend_name, "seed": seed, "decision_seconds": round(time.time() - started, 3)},
            "agent_stats": {"name": AGENT_LABEL, "model_name": backend_name, "total_decisions": 1},
        }

    def _extract_json_config(text: str) -> dict[str, Any]:
        start = text.find("{")
        if start < 0:
            raise ValueError("missing JSON object")
        depth = 0
        end = -1
        for idx, ch in enumerate(text[start:], start=start):
            if ch == "{":
                depth += 1
            elif ch == "}":
                depth -= 1
                if depth == 0:
                    end = idx + 1
                    break
        if end < 0:
            raise ValueError("unterminated JSON object")
        block = text[start:end]
        try:
            parsed = json.loads(block)
        except json.JSONDecodeError:
            parsed = ast.literal_eval(block)
        if not isinstance(parsed, dict):
            raise ValueError("JSON config is not a dict")
        if isinstance(parsed.get("new_config"), dict):
            parsed = parsed["new_config"]
        return parsed

    api_requested = False
    try:
        from agenthpobench.agents.api_decision_client import api_backend_enabled, call_decision_api

        api_requested = api_backend_enabled()
        if api_requested:
            prompt = "\n".join(
                [
                    f"Task: choose the next hyperparameter config for {task_name}.",
                    "Return exactly one JSON object containing only proposed hyperparameter keys and values.",
                    f"Current config: {json.dumps(current_config, sort_keys=True)}",
                    f"Search space: {json.dumps(search_space, sort_keys=True)}",
                    f"Budget remaining: {budget_remaining} of {total_budget}.",
                    "Training history:",
                    str(training_log)[-6000:],
                ]
            )
            response = call_decision_api(
                prompt,
                temperature=float(os.environ.get("AUTOREP_API_TEMPERATURE", "0")),
                max_tokens=int(os.environ.get("AUTOREP_API_MAX_TOKENS", os.environ.get("AUTOREP_AGENT_MAX_NEW_TOKENS", "384"))),
            )
            try:
                raw_config = _extract_json_config(response.text)
                reasoning = response.text[:2000]
                confidence = 0.7
                metadata = {"api_backend": True, "api": response.metadata}
            except Exception as exc:  # noqa: BLE001
                raw_config = {}
                reasoning = f"API response did not contain a parseable config; keeping current config. Error: {exc!r}"
                confidence = 0.0
                metadata = {"api_backend": True, "api_parse_fallback": True, "api": response.metadata, "raw_text": response.text[:1000]}
            new_config = clamp_config(raw_config, current_config, search_space, aliases=aliases)
            return {
                "task_name": task_name,
                "new_config": new_config,
                "raw_new_config": raw_config,
                "reasoning": reasoning,
                "confidence": confidence,
                "metadata": metadata | {"decision_seconds": round(time.time() - started, 3)},
                "agent_stats": {"name": AGENT_LABEL, "model_name": os.environ.get("AUTOREP_API_MODEL", "api-model"), "total_decisions": 1},
            }
    except Exception:
        if api_requested or str(os.environ.get("AUTOREP_AGENT_BACKEND", "")).strip().lower() in {"api", "openai", "openai-compatible", "anthropic", "glm", "claude_code", "claude-code", "codex", "codex_cli", "codex-cli"}:
            raise
    cache_enabled = os.environ.get("AUTOREP_KEEP_AGENT_LOADED", "0").strip().lower() in {
        "1",
        "true",
        "yes",
        "on",
    }
    agent = None
    try:
        from agenthpobench.agents.open_source.qwen_agent import QwenAgent
        from agenthpobench.core.agent_base import DecisionContext

        temperature = float(os.environ.get("AUTOREP_AGENT_TEMPERATURE", "0.1"))
        max_new_tokens = int(os.environ.get("AUTOREP_AGENT_MAX_NEW_TOKENS", "256"))
        torch_dtype = os.environ.get("AUTOREP_AGENT_TORCH_DTYPE", "bfloat16")
        use_chat_template = os.environ.get("AUTOREP_USE_CHAT_TEMPLATE", "0").lower() in {"1", "true", "yes", "on"}
        cache_key = (
            str(MODEL_PATH),
            str(temperature),
            str(max_new_tokens),
            torch_dtype,
            str(use_chat_template),
            os.environ.get("AUTOREP_API_PROVIDER", ""),
        )
        agent = _AGENT_CACHE.get(cache_key) if cache_enabled else None
        if agent is None:
            agent = QwenAgent(
                model_path=str(MODEL_PATH),
                temperature=temperature,
                max_new_tokens=max_new_tokens,
                torch_dtype=torch_dtype,
                use_chat_template=use_chat_template,
            )
            if cache_enabled:
                _AGENT_CACHE[cache_key] = agent
        else:
            agent.temperature = temperature
            agent.max_new_tokens = max_new_tokens
        # The shared QwenAgent prompt is intentionally generic and some models
        # emit aliases or irrelevant fields such as "learning_rate". Keep the
        # raw proposal, then task scripts clamp/filter it against their own
        # search spaces instead of falling back before aliases can be applied.
        agent.validate_decision = lambda _decision, _space: (True, None)
        ctx = DecisionContext(
            training_log=training_log,
            current_config=current_config,
            metrics_history=metrics_history or [],
            budget_remaining=budget_remaining,
            total_budget=total_budget,
            search_space=search_space,
            epoch=total_budget - budget_remaining,
            decision_number=decision_number,
        )
        decision = agent.decide(ctx)
        raw_config = dict(decision.new_config)
        reasoning = decision.reasoning
        confidence = float(decision.confidence)
        metadata = dict(decision.metadata)
        agent_stats = agent.get_stats()
        agent_stats["name"] = AGENT_LABEL
    except Exception as exc:
        metadata = {"fallback": True, "error": repr(exc)}
    finally:
        if not cache_enabled:
            if agent is not None:
                del agent
            cleanup_torch()
    new_config = clamp_config(raw_config, current_config, search_space, aliases=aliases)
    return {
        "task_name": task_name,
        "new_config": new_config,
        "raw_new_config": raw_config,
        "reasoning": reasoning,
        "confidence": confidence,
        "metadata": metadata | {"decision_seconds": round(time.time() - started, 3)},
        "agent_stats": agent_stats,
    }


def result_root(dirname: str) -> Path:
    return RESULTS_BASE / dirname


def copy_result_alias(src: Path, alias_dirname: str | None) -> None:
    if not alias_dirname:
        return
    alias_root = RESULTS_BASE / alias_dirname
    alias_root.mkdir(parents=True, exist_ok=True)
    dst = alias_root / src.name
    if dst.resolve() != src.resolve():
        shutil.copy2(src, dst)


def load_manifest_record(record_id: str) -> dict[str, Any]:
    path = ROOT / "results/formal_baselines/budget_protocol/scoreable_benchmark_manifest_20260505.json"
    if not path.exists():
        return {}
    payload = load_json(path)
    for item in payload.get("records", []):
        if item.get("id") == record_id:
            return item
    return {}


def maybe_dry_run(payload: dict[str, Any]) -> None:
    if os.environ.get("AUTOREP_DRY_RUN", "0") == "1":
        print(json.dumps(payload, indent=2, sort_keys=True))
        raise SystemExit(0)
