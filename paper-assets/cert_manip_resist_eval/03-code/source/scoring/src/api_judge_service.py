import json
import os
import re
import time
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Any, Dict, List, Optional

import requests

from src.judge_service import (
    LIKERT_SYSTEM_PROMPT,
    LIKERT_USER_TEMPLATE,
    PAIRWISE_SYSTEM_PROMPT,
    PAIRWISE_USER_TEMPLATE,
    _parse_judge_output,
)
from src.utils import setup_logging

logger = setup_logging("api_judge")

API_MODEL_REGISTRY = {
    "claude-opus-4-6":        {"tier": "strong",  "provider": "anthropic"},
    "gpt-5.5":                {"tier": "strong",  "provider": "openai"},
    "gemini-3.1-pro-preview": {"tier": "strong",  "provider": "google"},
    "gpt-4.1":                {"tier": "mid",     "provider": "openai"},
    "claude-sonnet-4-6":      {"tier": "mid",     "provider": "anthropic"},
    "gemini-3.5-flash":       {"tier": "mid",     "provider": "google"},
    "gpt-4.1-mini":           {"tier": "weak",    "provider": "openai"},
    "gpt-4.1-nano":           {"tier": "weak",    "provider": "openai"},
    "claude-3-haiku":         {"tier": "weak",    "provider": "anthropic"},
}

_NO_TEMP_ZERO = {"gpt-5.5", "o4-mini", "o3", "o3-mini", "o1", "o1-pro"}
_OPENROUTER_MODEL_MAP = {
    "gpt-4.1":                "openai/gpt-4.1",
    "gpt-4.1-mini":           "openai/gpt-4.1-mini",
    "gpt-4.1-nano":           "openai/gpt-4.1-nano",
    "gpt-5.5":                "openai/gpt-5.5",
    "claude-sonnet-4-6":      "anthropic/claude-sonnet-4.6",
    "claude-opus-4-6":        "anthropic/claude-opus-4.6",
    "claude-3-haiku":         "anthropic/claude-3-haiku",
    "gemini-3.1-pro-preview": "google/gemini-3.1-pro-preview",
    "gemini-3.5-flash":       "google/gemini-3.5-flash",
}



def _parse_judge_output_robust(text: str) -> Dict[str, Any]:
    result = _parse_judge_output(text)
    if "error" not in result or result.get("error") != "parse_failed":
        result["_parse_method"] = "direct_json"
        return result

    # Truncated JSON repair: extract fields with regex
    winner_m = re.search(r'"winner"\s*:\s*"([ABab]|tie)"', text, re.IGNORECASE)
    score_a_m = re.search(r'"score_a"\s*:\s*(\d)', text)
    score_b_m = re.search(r'"score_b"\s*:\s*(\d)', text)
    reasoning_m = re.search(r'"reasoning"\s*:\s*"((?:[^"\\]|\\.)*)', text)

    if winner_m and score_a_m and score_b_m:
        return {
            "winner": winner_m.group(1).upper() if winner_m.group(1).lower() != "tie" else "tie",
            "score_a": int(score_a_m.group(1)),
            "score_b": int(score_b_m.group(1)),
            "reasoning": reasoning_m.group(1)[:300] if reasoning_m else "(truncated)",
            "_repaired": True,
            "_parse_method": "regex_repair",
        }

    # Likert fallback
    score_m = re.search(r'"score"\s*:\s*(\d)', text)
    if score_m:
        return {
            "score": int(score_m.group(1)),
            "reasoning": reasoning_m.group(1)[:300] if reasoning_m else "(truncated)",
            "_repaired": True,
            "_parse_method": "regex_repair",
        }

    return {"error": "parse_failed", "raw": text[:500], "_parse_method": "failed"}


class APIJudgeService:
    _MODEL_MAX_TOKENS = {
        "gemini-2.5-pro": 2048,
        "gemini-2.5-flash": 2048,
    }

    def __init__(
        self,
        model_id: str,
        api_base: str = "https://openrouter.ai/api/v1",
        api_key: [REDACTED] = None,
        max_rps: float = 5.0,
        max_retries: int = 3,
        timeout: int = 90,
    ):
        self.model_id = model_id
        self.api_base = api_base.rstrip("/")
        self.api_key = [REDACTED] or os.environ.get("OPENROUTER_API_KEY", "")
        self.max_retries = max_retries
        self.timeout = timeout
        self._min_interval = 1.0 / max_rps
        self._last_request_time = 0.0
        self._lock = threading.Lock()
        self._session = requests.Session()
        self._session.headers.update({
            "Content-Type": "application/json",
            "Authorization": [REDACTED]"Bearer {self.api_key}",
            "HTTP-Referer": "https://github.com/cert-manip-resist-eval",
            "X-Title": "cert_manip_resist_eval",
        })

    def _rate_limit(self):
        with self._lock:
            now = time.monotonic()
            wait = self._min_interval - (now - self._last_request_time)
            if wait > 0:
                time.sleep(wait)
            self._last_request_time = time.monotonic()

    def _call_api(self, system: str, user: str) -> Dict[str, Any]:
        payload = {
            "model": _OPENROUTER_MODEL_MAP.get(self.model_id, self.model_id),
            "messages": [
                {"role": "system", "content": system},
                {"role": "user", "content": user},
            ],
            "max_tokens": self._MODEL_MAX_TOKENS.get(self.model_id, 512),
        }
        if self.model_id not in _NO_TEMP_ZERO:
            payload["temperature"] = 0.0

        last_err = None
        for attempt in range(self.max_retries):
            self._rate_limit()
            t0 = time.monotonic()
            try:
                resp = self._session.post(
                    f"{self.api_base}/chat/completions",
                    json=payload,
                    timeout=self.timeout,
                )
                latency_ms = (time.monotonic() - t0) * 1000

                if resp.status_code == 200:
                    data = resp.json()
                    content = data["choices"][0]["message"]["content"]
                    usage = data.get("usage", {})
                    return {
                        "content": content,
                        "latency_ms": round(latency_ms, 1),
                        "input_tokens": usage.get("prompt_tokens", 0),
                        "output_tokens": usage.get("completion_tokens", 0),
                    }

                if resp.status_code == 429:
                    wait = 2 ** attempt * 2
                    logger.warning(f"Rate limited on {self.model_id}, retry in {wait}s")
                    time.sleep(wait)
                    last_err = f"HTTP {resp.status_code}: {resp.text[:200]}"
                    continue

                if resp.status_code >= 500:
                    wait = 2 ** attempt
                    logger.warning(f"Server error {resp.status_code} on {self.model_id}, retry in {wait}s")
                    time.sleep(wait)
                    last_err = f"HTTP {resp.status_code}: {resp.text[:200]}"
                    continue

                return {
                    "content": None,
                    "error": f"HTTP {resp.status_code}: {resp.text[:300]}",
                    "latency_ms": round(latency_ms, 1),
                    "input_tokens": 0,
                    "output_tokens": 0,
                }

            except requests.exceptions.Timeout:
                last_err = f"Timeout after {self.timeout}s"
                logger.warning(f"Timeout on {self.model_id} (attempt {attempt+1})")
            except requests.exceptions.ConnectionError as e:
                last_err = f"Connection error: {e}"
                logger.warning(f"Connection error on {self.model_id} (attempt {attempt+1})")

            if attempt < self.max_retries - 1:
                time.sleep(2 ** attempt)

        return {
            "content": None,
            "error": last_err or "Unknown error",
            "latency_ms": 0,
            "input_tokens": 0,
            "output_tokens": 0,
        }

    def score(self, question: str, response_a: str, response_b: str) -> Dict[str, Any]:
        user_msg = PAIRWISE_USER_TEMPLATE.format(
            question=question, response_a=response_a, response_b=response_b
        )
        api_result = self._call_api(PAIRWISE_SYSTEM_PROMPT, user_msg)

        if api_result.get("error"):
            return {
                "error": api_result["error"],
                "judge_id": self.model_id,
                "latency_ms": api_result["latency_ms"],
                "input_tokens": 0,
                "output_tokens": 0,
            }

        parsed = _parse_judge_output_robust(api_result["content"])
        parsed["judge_id"] = self.model_id
        parsed["latency_ms"] = api_result["latency_ms"]
        parsed["input_tokens"] = api_result["input_tokens"]
        parsed["output_tokens"] = api_result["output_tokens"]
        return parsed

    def score_likert(self, question: str, response: str) -> Dict[str, Any]:
        user_msg = LIKERT_USER_TEMPLATE.format(question=question, response=response)
        api_result = self._call_api(LIKERT_SYSTEM_PROMPT, user_msg)

        if api_result.get("error"):
            return {
                "error": api_result["error"],
                "judge_id": self.model_id,
                "latency_ms": api_result["latency_ms"],
                "input_tokens": 0,
                "output_tokens": 0,
            }

        parsed = _parse_judge_output_robust(api_result["content"])
        parsed["judge_id"] = self.model_id
        parsed["latency_ms"] = api_result["latency_ms"]
        parsed["input_tokens"] = api_result["input_tokens"]
        parsed["output_tokens"] = api_result["output_tokens"]
        return parsed

    def batch_score(
        self,
        items: List[Dict],
        mode: str = "pairwise",
        max_workers: int = 5,
    ) -> Dict[str, Any]:
        def _score_one(item):
            if mode == "pairwise":
                return self.score(item["question"], item["response_a"], item["response_b"])
            else:
                return self.score_likert(item["question"], item["response"])

        results = [None] * len(items)
        with ThreadPoolExecutor(max_workers=max_workers) as pool:
            future_to_idx = {pool.submit(_score_one, it): i for i, it in enumerate(items)}
            for future in as_completed(future_to_idx):
                idx = future_to_idx[future]
                try:
                    results[idx] = future.result()
                except Exception as e:
                    results[idx] = {"error": str(e), "judge_id": self.model_id}

        total = len(results)
        repair_count = sum(1 for r in results if r and r.get("_parse_method") == "regex_repair")
        parse_failed_count = sum(1 for r in results if r and r.get("_parse_method") == "failed")

        winner_dist = {"A": 0, "B": 0, "tie": 0, "unknown": 0}
        for r in results:
            if not r or r.get("error"):
                winner_dist["unknown"] += 1
            else:
                w = r.get("winner", "")
                if w in winner_dist:
                    winner_dist[w] += 1
                else:
                    winner_dist["unknown"] += 1

        return {
            "results": results,
            "_meta": {
                "repair_rate": repair_count / total if total else 0,
                "parse_failed_rate": parse_failed_count / total if total else 0,
                "total": total,
                "winner_distribution": winner_dist,
            },
        }
