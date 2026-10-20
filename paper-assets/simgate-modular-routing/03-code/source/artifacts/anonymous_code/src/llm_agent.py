"""LLM Agent: ReAct agent for ScienceWorld.

Supports vLLM serving (default) or HuggingFace transformers local inference.
Provides:
  - select_action_react(): standard ReAct single-action selection
  - generate_candidate_actions(): top-n candidate generation for deterministic routing
"""

import os
import re
import glob
import json
import time
from typing import List, Optional, Tuple

DEFAULT_MODEL_NAME = "Qwen/Qwen2.5-7B-Instruct"


def find_model_path(hint: Optional[str] = None) -> str:
    if hint and os.path.isdir(hint):
        return hint
    return hint or DEFAULT_MODEL_NAME


SYSTEM_PROMPT = """You are an agent interacting with a ScienceWorld text environment. Your goal is to complete the given task by choosing actions from the available action list.

Use the following format for each step:
Thought: <your reasoning about what to do next>
Action: <exact action string from the valid actions list>

Rules:
- You MUST choose an action from the valid actions list. Do not invent actions.
- Think step by step about what physical/scientific process is needed.
- Pay attention to the current observation for clues about object states."""

REACT_USER_TEMPLATE = """Current observation:
{observation}

Valid actions:
{valid_actions_str}

Previous actions taken: {history_str}

Choose your next action."""

CANDIDATE_USER_TEMPLATE = """Current observation:
{observation}

Valid actions:
{valid_actions_str}

Previous actions taken: {history_str}

Suggest the top {n} most promising actions from the valid actions list, ranked by likelihood of making progress. Output one action per line, prefixed with a number."""


class LLMAgent:
    """ReAct-style LLM agent for interactive environments."""

    def __init__(self, model_path: str = None, gpu_id: int = 0,
                 api_url: str = "http://localhost:8000/v1",
                 use_vllm_api: bool = True):
        self.model_path = find_model_path(model_path)
        self.gpu_id = gpu_id
        self.api_url = api_url
        self.use_vllm_api = use_vllm_api
        self._llm = None
        self._tokenizer = None
        self.max_new_tokens = 512

    def _call_vllm_api(self, messages: List[dict]) -> str:
        import requests
        resp = requests.post(
            f"{self.api_url}/chat/completions",
            json={
                "model": self.model_path,
                "messages": messages,
                "max_tokens": self.max_new_tokens,
                "temperature": 0.0,
            },
            timeout=60,
        )
        resp.raise_for_status()
        return resp.json()["choices"][0]["message"]["content"]

    def _call_local(self, messages: List[dict]) -> str:
        if self._llm is None:
            from transformers import AutoTokenizer, AutoModelForCausalLM
            import torch
            self._tokenizer = AutoTokenizer.from_pretrained(self.model_path)
            self._llm = AutoModelForCausalLM.from_pretrained(
                self.model_path,
                torch_dtype=torch.float16,
                device_map=f"cuda:{self.gpu_id}",
            )

        text = self._tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
        inputs = self._tokenizer(text, return_tensors="pt").to(self._llm.device)
        import torch
        with torch.no_grad():
            out = self._llm.generate(**inputs, max_new_tokens=self.max_new_tokens, do_sample=False)
        return self._tokenizer.decode(out[0][inputs["input_ids"].shape[1]:], skip_special_tokens=True)

    def _generate(self, messages: List[dict]) -> str:
        if self.use_vllm_api:
            return self._call_vllm_api(messages)
        return self._call_local(messages)

    def _parse_action(self, text: str, valid_actions: List[str]) -> str:
        match = re.search(r"Action:\s*(.+)", text)
        if match:
            action = match.group(1).strip()
            if action in valid_actions:
                return action
            best = min(valid_actions, key=lambda a: _edit_distance(a.lower(), action.lower()))
            return best
        return valid_actions[0] if valid_actions else "look around"

    def select_action_react(self, obs: str, valid_actions: List[str],
                            history_dicts: List[dict]) -> str:
        history_str = " -> ".join(h["action"] for h in history_dicts[-5:]) or "(none)"
        valid_str = "\n".join(f"  - {a}" for a in valid_actions[:30])

        messages = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": REACT_USER_TEMPLATE.format(
                observation=obs, valid_actions_str=valid_str, history_str=history_str)},
        ]
        response = self._generate(messages)
        return self._parse_action(response, valid_actions)

    def generate_candidate_actions(self, obs: str, valid_actions: List[str],
                                   history_dicts: List[dict],
                                   n: int = 3) -> Tuple[List[str], str]:
        history_str = " -> ".join(h["action"] for h in history_dicts[-5:]) or "(none)"
        valid_str = "\n".join(f"  - {a}" for a in valid_actions[:30])

        messages = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": CANDIDATE_USER_TEMPLATE.format(
                observation=obs, valid_actions_str=valid_str,
                history_str=history_str, n=n)},
        ]
        response = self._generate(messages)

        candidates = []
        for line in response.split("\n"):
            line = line.strip()
            match = re.match(r"\d+[\.\)]\s*(.+)", line)
            if match:
                action = match.group(1).strip()
                best = min(valid_actions, key=lambda a: _edit_distance(a.lower(), action.lower()))
                if best not in candidates:
                    candidates.append(best)
            if len(candidates) >= n:
                break

        if not candidates:
            candidates = valid_actions[:n]

        return candidates, response


def _edit_distance(s1: str, s2: str) -> int:
    if len(s1) < len(s2):
        return _edit_distance(s2, s1)
    if len(s2) == 0:
        return len(s1)
    prev = list(range(len(s2) + 1))
    for i, c1 in enumerate(s1):
        curr = [i + 1]
        for j, c2 in enumerate(s2):
            curr.append(min(prev[j + 1] + 1, curr[j] + 1, prev[j] + (c1 != c2)))
        prev = curr
    return prev[-1]
