"""Local Transformers agent for AgentHPOBench open-weight evaluations.

The implementation is model-family neutral and supports compatible causal language
model checkpoints, including Qwen, Gemma, Llama, DeepSeek, and Phi.
"""

from __future__ import annotations

import ast
import json
import os
import re
import sys
import time
from importlib import import_module
from pathlib import Path
from typing import Any, Dict, Optional


def _env_flag(name: str, legacy_name: str | None = None) -> bool:
    """Read a boolean environment flag with an optional compatibility alias."""
    value = os.environ.get(name)
    if value is None and legacy_name is not None:
        value = os.environ.get(legacy_name)
    return str(value or "0").strip().lower() in {"1", "true", "yes", "on"}


from agenthpobench.core.agent_base import Agent, DecisionContext, AgentDecision, InvalidDecisionError
from agenthpobench.agents.api_decision_client import api_backend_enabled, api_model_name, call_decision_api


_root_override = os.environ.get("AUTOREP_ROOT")
if _root_override:
    _REPO_ROOT = Path(_root_override).expanduser().resolve()
else:
    _REPO_ROOT = next(
        parent
        for parent in Path(__file__).resolve().parents
        if (parent / "agenthpobench").is_dir() and (parent / "configs").is_dir()
    )
_VENDORED_DEPS = _REPO_ROOT / ".python_deps"
if _VENDORED_DEPS.exists():
    sys.path.insert(0, str(_VENDORED_DEPS))

torch: Any = None
AutoModelForCausalLM: Any = None
AutoTokenizer: Any = None


def _load_local_dependencies() -> None:
    """Load heavyweight optional dependencies only for local inference."""
    global torch, AutoModelForCausalLM, AutoTokenizer
    if all(
        dependency is not None
        for dependency in (torch, AutoModelForCausalLM, AutoTokenizer)
    ):
        return
    try:
        torch = import_module("torch")
        transformers = import_module("transformers")
    except ModuleNotFoundError as exc:
        raise ImportError(
            "Local open-weight inference requires the optional dependencies. "
            "Install them with `pip install -e '.[local]'`."
        ) from exc
    AutoModelForCausalLM = transformers.AutoModelForCausalLM
    AutoTokenizer = transformers.AutoTokenizer


class LocalTransformersAgent(Agent):
    """Agent backed by a local Hugging Face Transformers checkpoint."""

    def __init__(
        self,
        model_path: str,
        temperature: float = 0.1,
        max_new_tokens: int = 256,
        device_map: str = "auto",
        torch_dtype: str = "bfloat16",
        trust_remote_code: bool = True,
        use_chat_template: bool = False,
        **kwargs,
    ):
        super().__init__(
            name=os.environ.get("AUTOREP_AGENT_LABEL", "LocalTransformers"),
            model_name=model_path,
            temperature=temperature,
            max_new_tokens=max_new_tokens,
            device_map=device_map,
            torch_dtype=torch_dtype,
            **kwargs,
        )

        if api_backend_enabled():
            self.api_backend = True
            self.model_path = str(model_path)
            self.api_model = api_model_name(str(model_path))
            self.name = os.environ.get("AUTOREP_AGENT_LABEL", "API")
            self.model_name = self.api_model
            self.temperature = float(os.environ.get("AUTOREP_API_TEMPERATURE", str(temperature)))
            self.max_new_tokens = int(os.environ.get("AUTOREP_API_MAX_TOKENS", str(max_new_tokens)))
            self.device_map = device_map
            self.trust_remote_code = bool(trust_remote_code)
            self.use_chat_template = False
            self.tokenizer = None
            self.model = None
            self._last_api_metadata = None
            return

        _load_local_dependencies()
        self.api_backend = False
        self._last_api_metadata = None
        self._response_prefix = ""
        self.model_path = str(Path(model_path).resolve())
        if not Path(self.model_path).exists():
            raise ValueError(f"Local model path does not exist: {self.model_path}")

        self.temperature = float(temperature)
        self.max_new_tokens = int(max_new_tokens)
        self.device_map = device_map
        self.trust_remote_code = bool(trust_remote_code)
        env_chat_template = os.environ.get("AUTOREP_USE_CHAT_TEMPLATE")
        if env_chat_template is not None:
            use_chat_template = env_chat_template.strip().lower() in {"1", "true", "yes", "on"}
        self.use_chat_template = bool(use_chat_template)

        dtype = self._resolve_dtype(torch_dtype)
        model_kwargs = {
            "device_map": self.device_map,
            "trust_remote_code": self.trust_remote_code,
            "local_files_only": True,
            "low_cpu_mem_usage": True,
        }
        if dtype is not None:
            model_kwargs["torch_dtype"] = dtype
        attn_implementation = os.environ.get("AUTOREP_ATTN_IMPLEMENTATION", "eager").strip()
        if attn_implementation:
            model_kwargs["attn_implementation"] = attn_implementation

        self.tokenizer = AutoTokenizer.from_pretrained(
            self.model_path,
            trust_remote_code=self.trust_remote_code,
            local_files_only=True,
        )
        self.model = AutoModelForCausalLM.from_pretrained(
            self.model_path,
            **model_kwargs,
        )
        if self.tokenizer.pad_token_id is None:
            self.tokenizer.pad_token_id = self.tokenizer.eos_token_id

    def decide(self, context: DecisionContext) -> AgentDecision:
        prompt = self._build_prompt(context)
        start_time = time.time()

        response_text = ""
        try:
            response_text = self._generate(prompt)
            decision = self._parse_response(response_text, context)
            decision.metadata.update(
                {
                    "model_path": self.model_path,
                    "api_backend": bool(getattr(self, "api_backend", False)),
                    "api_model": getattr(self, "api_model", None),
                    "api": getattr(self, "_last_api_metadata", None),
                    "generation_seconds": round(time.time() - start_time, 3),
                }
            )
            return decision
        except Exception as exc:
            backend = "API" if getattr(self, "api_backend", False) else "Local Transformers"
            print(f"{backend} inference error: {exc}")
            decision = self._fallback_decision(context, error=str(exc))
            decision.metadata.update(
                {
                    "api_backend": bool(getattr(self, "api_backend", False)),
                    "api_model": getattr(self, "api_model", None),
                    "api": getattr(self, "_last_api_metadata", None),
                    "raw_response": response_text[:4000],
                    "generation_seconds": round(time.time() - start_time, 3),
                }
            )
            if not getattr(self, "api_backend", False):
                self.model = None
                self.tokenizer = None
                import gc
                gc.collect()
                torch.cuda.empty_cache()
            return decision

    def _resolve_dtype(self, torch_dtype: str):
        if not torch_dtype:
            return None
        value = str(torch_dtype).strip().lower()
        if value == "auto":
            if torch.cuda.is_available():
                return torch.bfloat16
            return None
        return getattr(torch, value, None)

    @staticmethod
    def _resolve_metric_direction(context: DecisionContext) -> tuple[str, str]:
        """Return the optimization verb and reader-facing metric direction."""
        explicit = str(getattr(context, "metric_direction", "") or "").strip().lower()
        lower_aliases = {
            "lower",
            "lower_is_better",
            "lower is better",
            "minimize",
            "minimise",
        }
        higher_aliases = {
            "higher",
            "higher_is_better",
            "higher is better",
            "maximize",
            "maximise",
        }
        if explicit in lower_aliases:
            return "minimize", "lower is better"
        if explicit in higher_aliases:
            return "maximize", "higher is better"

        log_text = str(context.training_log or "").lower()
        candidates = []
        for marker in ("lower is better", "lower_is_better"):
            position = log_text.find(marker)
            if position >= 0:
                candidates.append((position, "minimize", "lower is better"))
        for marker in ("higher is better", "higher_is_better"):
            position = log_text.find(marker)
            if position >= 0:
                candidates.append((position, "maximize", "higher is better"))
        if candidates:
            _, objective, direction = min(candidates, key=lambda item: item[0])
            return objective, direction

        raise ValueError(
            "Metric direction is required. Set DecisionContext.metric_direction "
            "to higher_is_better or lower_is_better."
        )

    def _build_prompt(self, context: DecisionContext) -> str:
        optimization_goal, metric_direction = self._resolve_metric_direction(context)
        return f"""You are an expert machine learning researcher helping optimize hyperparameters for model training.

## Task
Optimize hyperparameters to {optimization_goal} the target metric within the remaining budget.
- Metric Direction: {metric_direction}

## Current Training Progress
- Current Epoch: {context.epoch}
- Budget Remaining: {context.budget_remaining} epochs (out of {context.total_budget} total)
- Decision Number: {context.decision_number + 1}

## Recent Training Logs
```
{context.training_log}
```

## Current Hyperparameters
```
{self._format_config(context.current_config)}
```

## Hyperparameter Search Space
{self._format_search_space(context.search_space)}

## Instructions
- Be conservative unless the run is clearly plateauing or unstable.
- Only return values inside the search space.
- If training is improving normally, keeping the current config is acceptable.
- Output plain text only. Do not use markdown code fences, XML tags, or extra sections.
- Follow the exact headers below.

## Response Format
REASONING: <short explanation>
NEW_CONFIG: {{"learning_rate": 0.05, "batch_size": 128, "optimizer": "sgd"}}
CONFIDENCE: 0.8
"""

    def _render_prompt(self, prompt: str) -> str:
        self._response_prefix = ""
        if self.use_chat_template and hasattr(self.tokenizer, "apply_chat_template"):
            messages = [{"role": "user", "content": prompt}]
            try:
                rendered = self.tokenizer.apply_chat_template(
                    messages,
                    tokenize=False,
                    add_generation_prompt=True,
                )
                no_think = _env_flag(
                    "AUTOREP_LOCAL_MODEL_NO_THINK",
                    legacy_name="AUTOREP_QWEN_NO_THINK",
                )
                # DeepSeek-R1-Distill templates always prefill an open thinking
                # block and ignore enable_thinking=False. Close that block and
                # prefill the JSON object so generation starts with config fields.
                if no_think and rendered.rstrip().endswith("<think>"):
                    self._response_prefix = "NEW_CONFIG: {"
                    return rendered.rstrip() + "\n</think>\n\n" + self._response_prefix
                force_prefix = os.environ.get(
                    "AUTOREP_FORCE_CONFIG_PREFIX", "0"
                ).strip().lower() in {"1", "true", "yes", "on"}
                if force_prefix:
                    self._response_prefix = "NEW_CONFIG: {"
                    return rendered.rstrip() + "\n" + self._response_prefix
                return rendered
            except Exception:
                pass
        force_prefix = os.environ.get("AUTOREP_FORCE_CONFIG_PREFIX", "0").strip().lower() in {"1", "true", "yes", "on"}
        if force_prefix:
            self._response_prefix = "NEW_CONFIG: {"
            return prompt.rstrip() + chr(10) + self._response_prefix
        return prompt

    def _generate(self, prompt: str) -> str:
        if getattr(self, "api_backend", False):
            response = call_decision_api(prompt, temperature=self.temperature, max_tokens=self.max_new_tokens)
            self._last_api_metadata = response.metadata
            return response.text.strip()

        if _env_flag(
            "AUTOREP_LOCAL_MODEL_NO_THINK",
            legacy_name="AUTOREP_QWEN_NO_THINK",
        ):
            prompt = prompt + "\n/no_think\nDo not output thinking. Start immediately with REASONING."
        rendered_prompt = self._render_prompt(prompt)
        inputs = self.tokenizer(rendered_prompt, return_tensors="pt")
        try:
            device = getattr(self.model, "device", None)
            if device is not None:
                inputs = {k: v.to(device) for k, v in inputs.items()}
        except Exception:
            pass

        do_sample = self.temperature > 0
        generation_kwargs = {
            "max_new_tokens": self.max_new_tokens,
            "do_sample": do_sample,
            "pad_token_id": self.tokenizer.pad_token_id,
            "eos_token_id": self.tokenizer.eos_token_id,
        }
        if do_sample:
            generation_kwargs["temperature"] = max(self.temperature, 1e-5)
        else:
            generation_kwargs["temperature"] = None
            generation_kwargs["top_p"] = None
            generation_kwargs["top_k"] = None

        with torch.no_grad():
            outputs = self.model.generate(
                **inputs,
                **generation_kwargs,
            )
        input_len = inputs["input_ids"].shape[1]
        generated = outputs[0][input_len:]
        generated_text = self.tokenizer.decode(
            generated, skip_special_tokens=True
        ).strip()
        return (self._response_prefix + generated_text).strip()

    def _strip_code_fences(self, text: str) -> str:
        text = text.strip()
        if text.startswith("```"):
            lines = text.splitlines()
            if lines and lines[0].startswith("```"):
                lines = lines[1:]
            if lines and lines[-1].strip() == "```":
                lines = lines[:-1]
            text = "\n".join(lines).strip()
        return text

    def _extract_json_block(self, text: str, anchor: str = "NEW_CONFIG:") -> str:
        text = self._strip_code_fences(text)
        anchor_pos = text.find(anchor)
        if anchor_pos == -1:
            anchor_pos = 0
        brace_start = text.find("{", anchor_pos)
        if brace_start == -1:
            raise ValueError("Missing JSON object in model response")

        depth = 0
        for idx in range(brace_start, len(text)):
            ch = text[idx]
            if ch == "{":
                depth += 1
            elif ch == "}":
                depth -= 1
                if depth == 0:
                    return text[brace_start : idx + 1]
        raise ValueError("Unterminated JSON object in model response")

    def _loads_config_block(self, block: str) -> dict[str, Any]:
        normalized = block.translate(
            str.maketrans(
                {
                    "\u201c": '"',
                    "\u201d": '"',
                    "\u2018": "'",
                    "\u2019": "'",
                    "\uff1a": ":",
                    "\uff0c": ",",
                }
            )
        )
        try:
            return json.loads(normalized)
        except json.JSONDecodeError:
            normalized = re.sub(r"\bTrue\b", "true", normalized)
            normalized = re.sub(r"\bFalse\b", "false", normalized)
            normalized = re.sub(r"\bNone\b", "null", normalized)
            try:
                return json.loads(normalized)
            except json.JSONDecodeError:
                # Some local models emit JSON-like mappings with unquoted
                # identifier keys or enum values. Normalize only those tokens;
                # the resulting values are still validated against the task
                # search space before execution.
                relaxed = re.sub(
                    r'([{,]\s*)([A-Za-z_][A-Za-z0-9_.-]*)(\s*:)',
                    r'\1"\2"\3',
                    normalized,
                )

                def quote_bare_value(match: re.Match[str]) -> str:
                    prefix, value, suffix = match.groups()
                    if value in {"true", "false", "null"}:
                        return match.group(0)
                    return f'{prefix}"{value}"{suffix}'

                relaxed = re.sub(
                    r'(:\s*)([A-Za-z_][A-Za-z0-9_./:+-]*)(\s*[,}])',
                    quote_bare_value,
                    relaxed,
                )
                relaxed = re.sub(r",\s*}", "}", relaxed)
                try:
                    return json.loads(relaxed)
                except json.JSONDecodeError:
                    parsed = ast.literal_eval(relaxed)
                    if not isinstance(parsed, dict):
                        raise ValueError("configuration block is not a dict")
                    return parsed

    def _parse_response(self, response: str, context: DecisionContext) -> AgentDecision:
        try:
            response = self._strip_code_fences(response)
            raw_new_config = self._loads_config_block(self._extract_json_block(response))
            allowed_keys = set(context.search_space.keys())
            ignored_unknown = sorted(k for k in raw_new_config if k not in allowed_keys)
            filtered = {k: v for k, v in raw_new_config.items() if k in allowed_keys}
            # Keep the current valid settings for omitted keys; extra model-suggested
            # fields should not force a fallback when the core decision is usable.
            new_config = {k: v for k, v in context.current_config.items() if k in allowed_keys}
            new_config.update(filtered)

            config_start = response.find("NEW_CONFIG:")
            brace_start = response.find("{")
            reasoning_start = response.find("REASONING:")

            if reasoning_start != -1:
                reasoning_content_start = reasoning_start + len("REASONING:")
                end_candidates = [
                    pos
                    for marker in ("NEW_CONFIG:", "CONFIDENCE:")
                    if (pos := response.find(marker, reasoning_content_start)) != -1
                ]
                reasoning_end = min(end_candidates) if end_candidates else len(response)
                reasoning = response[reasoning_content_start:reasoning_end].strip()
            else:
                reasoning_end = config_start if config_start != -1 else brace_start
                if reasoning_end == -1:
                    reasoning_end = len(response)
                reasoning = response[:reasoning_end].strip()

            reasoning = reasoning.replace("<think>", "").replace("</think>", "").strip()
            if not reasoning:
                reasoning = "Local model decision"

            confidence = 0.7
            match = re.search(r"CONFIDENCE:\s*([0-9]*\.?[0-9]+)", response)
            if match:
                confidence = float(match.group(1))
            confidence = max(0.0, min(1.0, confidence))

            is_valid, error_msg = self.validate_decision(new_config, context.search_space)
            if not is_valid:
                raise InvalidDecisionError(f"Invalid config: {error_msg}")

            return AgentDecision(
                new_config=new_config,
                reasoning=reasoning,
                confidence=confidence,
                metadata={"raw_response": response, "raw_new_config": raw_new_config, "ignored_unknown_parameters": ignored_unknown},
            )
        except Exception as exc:
            raise InvalidDecisionError(f"Failed to parse local model response: {exc}") from exc

    def _fallback_decision(
        self,
        context: DecisionContext,
        error: Optional[str] = None,
    ) -> AgentDecision:
        metrics_history = context.metrics_history
        new_config = context.current_config.copy()

        if len(metrics_history) >= 2:
            def metric_value(entry: Any) -> Optional[float]:
                value = entry[1] if isinstance(entry, (list, tuple)) and len(entry) > 1 else entry
                if isinstance(value, dict):
                    value = value.get("accuracy")
                try:
                    return float(value)
                except (TypeError, ValueError):
                    return None

            current_acc = metric_value(metrics_history[-1])
            previous_acc = metric_value(metrics_history[-2])
            if (
                current_acc is not None
                and previous_acc is not None
                and current_acc <= previous_acc
                and "learning_rate" in new_config
            ):
                new_config["learning_rate"] = max(new_config["learning_rate"] * 0.5, 1e-6)
                return AgentDecision(
                    new_config=new_config,
                    reasoning="Fallback: plateau detected, halving learning rate.",
                    confidence=0.55,
                    metadata={"fallback": True, "error": error},
                )

        return AgentDecision(
            new_config=new_config,
            reasoning="Fallback: keeping current configuration.",
            confidence=0.5,
            metadata={"fallback": True, "error": error},
        )

    def _format_config(self, config: Dict[str, Any]) -> str:
        return "\n".join(f"  {k}: {v}" for k, v in config.items())

    def _format_search_space(self, search_space: Dict[str, Any]) -> str:
        lines = []
        for param, spec in search_space.items():
            if isinstance(spec, list):
                lines.append(f"- {param}: {spec}")
            elif isinstance(spec, dict) and "min" in spec and "max" in spec:
                scale = spec.get("scale", "linear")
                lines.append(f"- {param}: [{spec['min']}, {spec['max']}] ({scale})")
            else:
                lines.append(f"- {param}: {spec}")
        return "\n".join(lines)
