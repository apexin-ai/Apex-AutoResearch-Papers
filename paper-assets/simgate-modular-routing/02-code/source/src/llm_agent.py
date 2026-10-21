"""LLM Agent: Qwen2.5-7B-Instruct ReAct agent for ScienceWorld.

Supports vLLM serving (default) or HuggingFace transformers local inference.
Provides:
  - select_action_react(): standard ReAct single-action selection
  - generate_candidate_actions(): top-n candidate generation for deterministic routing

Usage:
  agent = LLMAgent(model_path="/root/autodl-tmp/models/Qwen2.5-7B-Instruct", gpu_id=0)
  action = agent.select_action_react(obs, valid_actions, history)
"""

import os
import re
import glob
import json
import time
from typing import List, Optional, Tuple

# Detect model path: ModelScope or HuggingFace naming conventions
MODEL_SEARCH_PATHS = [
    "/root/autodl-tmp/models/Qwen2.5-7B-Instruct",
    "/root/autodl-tmp/models/Qwen/Qwen2.5-7B-Instruct",
    "/root/autodl-tmp/models/Qwen/Qwen2___5-7B-Instruct",
    "/root/autodl-tmp/models/qwen/Qwen2.5-7B-Instruct",
    "/root/autodl-tmp/.hf_cache/models--Qwen--Qwen2.5-7B-Instruct",
]


def find_model_path(hint: Optional[str] = None) -> str:
    """Find Qwen2.5-7B-Instruct model path on disk."""
    if hint and os.path.isdir(hint):
        return hint
    for p in MODEL_SEARCH_PATHS:
        if os.path.isdir(p):
            return p
    # Glob fallback
    for pattern in ["/root/autodl-tmp/models/**/Qwen2*7B*Instruct",
                    "/root/autodl-tmp/.hf_cache/**/Qwen2*7B*"]:
        matches = glob.glob(pattern, recursive=True)
        if matches:
            return matches[0]
    raise FileNotFoundError(
        "Cannot find Qwen2.5-7B-Instruct. Searched: " + str(MODEL_SEARCH_PATHS)
    )


# ---------------------------------------------------------------------------
# Prompt templates
# ---------------------------------------------------------------------------

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

Generate the top {n} most promising actions from the valid actions list, ranked by how likely they are to make progress on the task. Output exactly {n} actions, one per line, in this format:
1. <action>
2. <action>
3. <action>"""


def sanitize_messages_for_template(messages, tokenizer):
    """将 system message 合并到第一条 user message（兼容不支持 system role 的模型如 Gemma）"""
    try:
        tokenizer.apply_chat_template(messages, tokenize=False)
        return messages
    except Exception as e:
        if "system" in str(e).lower():
            new_messages = []
            system_content = ""
            for msg in messages:
                if msg["role"] == "system":
                    system_content += msg["content"] + "\n\n"
                else:
                    if system_content and msg["role"] == "user":
                        msg = dict(msg)
                        msg["content"] = system_content + msg["content"]
                        system_content = ""
                    new_messages.append(msg)
            return new_messages
        raise


def _format_history(history: List[dict], last_k: int = 10) -> str:
    """Format recent action history for prompt."""
    if not history:
        return "(none)"
    recent = history[-last_k:]
    parts = []
    for h in recent:
        if isinstance(h, dict):
            parts.append(f"- {h.get('action', str(h))}")
        else:
            parts.append(f"- {h}")
    return "\n".join(parts)


def _format_valid_actions(actions: List[str], max_show: int = 50) -> str:
    """Format valid actions list, truncating if too long."""
    if len(actions) <= max_show:
        return "\n".join(f"  [{i}] {a}" for i, a in enumerate(actions))
    shown = actions[:max_show]
    return "\n".join(f"  [{i}] {a}" for i, a in enumerate(shown)) + \
           f"\n  ... and {len(actions) - max_show} more actions"


def parse_action(text: str, valid_actions: List[str]) -> Optional[str]:
    """Parse LLM output to extract action. Tries multiple patterns."""
    # Pattern 1: "Action: <action>"
    m = re.search(r"Action:\s*(.+?)(?:\n|$)", text, re.IGNORECASE)
    if m:
        action_str = m.group(1).strip().strip('"').strip("'")
        if action_str in valid_actions:
            return action_str
        # Fuzzy match: case-insensitive
        for va in valid_actions:
            if va.lower() == action_str.lower():
                return va

    # Pattern 2: Exact match anywhere in text
    for va in valid_actions:
        if va in text:
            return va

    # Pattern 3: Bracketed index "[0]", "[1]" etc.
    m = re.search(r"\[(\d+)\]", text)
    if m:
        idx = int(m.group(1))
        if 0 <= idx < len(valid_actions):
            return valid_actions[idx]

    return None


def parse_candidates(text: str, valid_actions: List[str], n: int) -> List[str]:
    """Parse top-n candidates from LLM output."""
    candidates = []
    # Pattern: "1. <action>" or "1: <action>"
    for line in text.split("\n"):
        m = re.match(r"\d+[.):\s]+(.+)", line.strip())
        if m:
            action_str = m.group(1).strip().strip('"').strip("'")
            matched = None
            if action_str in valid_actions:
                matched = action_str
            else:
                for va in valid_actions:
                    if va.lower() == action_str.lower():
                        matched = va
                        break
            if matched and matched not in candidates:
                candidates.append(matched)

    # If we didn't get enough, try Action: pattern
    if len(candidates) < n:
        for va in valid_actions:
            if va in text and va not in candidates:
                candidates.append(va)
                if len(candidates) >= n:
                    break

    return candidates[:n]


class LLMAgent:
    """ReAct agent using Qwen2.5-7B-Instruct."""

    def __init__(
        self,
        model_path: Optional[str] = None,
        use_vllm: bool = True,
        gpu_id: int = 0,
        max_new_tokens: int = 256,
        temperature: float = 0.3,
        tensor_parallel_size: int = 1,
    ):
        self.model_path = find_model_path(model_path)
        self.use_vllm = use_vllm
        self.gpu_id = gpu_id
        self.max_new_tokens = max_new_tokens
        self.temperature = temperature
        self.tensor_parallel_size = tensor_parallel_size
        self._model = None
        self._tokenizer = None
        self._llm = None  # vLLM engine

        print(f"[LLMAgent] Model path: {self.model_path}")
        print(f"[LLMAgent] Backend: {'vLLM' if use_vllm else 'HF transformers'}, GPU: {gpu_id}")

    def _load_vllm(self):
        if self._llm is not None:
            return
        from vllm import LLM, SamplingParams
        os.environ["CUDA_VISIBLE_DEVICES"] = str(self.gpu_id)
        self._llm = LLM(
            model=self.model_path,
            tensor_parallel_size=self.tensor_parallel_size,
            gpu_memory_utilization=0.85,
            max_model_len=4096,
            trust_remote_code=True,
        )
        self._SamplingParams = SamplingParams

    def _load_hf(self):
        if self._model is not None:
            return
        import torch
        from transformers import AutoModelForCausalLM, AutoTokenizer
        self._tokenizer = AutoTokenizer.from_pretrained(
            self.model_path, trust_remote_code=True
        )
        self._model = AutoModelForCausalLM.from_pretrained(
            self.model_path,
            torch_dtype=torch.float16,
            device_map=f"cuda:{self.gpu_id}",
            trust_remote_code=True,
        )
        self._model.eval()

    def _generate(self, messages: List[dict], temperature: Optional[float] = None) -> str:
        """Generate text from chat messages."""
        temp = temperature if temperature is not None else self.temperature
        if self.use_vllm:
            return self._generate_vllm(messages, temp)
        else:
            return self._generate_hf(messages, temp)

    def _generate_vllm(self, messages: List[dict], temperature: float) -> str:
        self._load_vllm()
        from vllm import SamplingParams
        # Build prompt from messages using chat template
        from transformers import AutoTokenizer
        if self._tokenizer is None:
            self._tokenizer = AutoTokenizer.from_pretrained(
                self.model_path, trust_remote_code=True
            )
        messages = sanitize_messages_for_template(messages, self._tokenizer)
        prompt = self._tokenizer.apply_chat_template(
            messages, tokenize=False, add_generation_prompt=True
        )
        params = SamplingParams(
            temperature=max(temperature, 0.01),
            max_tokens=self.max_new_tokens,
            stop=["Observation:", "\nObservation"],
        )
        outputs = self._llm.generate([prompt], params)
        return outputs[0].outputs[0].text.strip()

    def _generate_hf(self, messages: List[dict], temperature: float) -> str:
        self._load_hf()
        import torch
        messages = sanitize_messages_for_template(messages, self._tokenizer)
        text = self._tokenizer.apply_chat_template(
            messages, tokenize=False, add_generation_prompt=True
        )
        inputs = self._tokenizer(text, return_tensors="pt").to(self._model.device)
        with torch.no_grad():
            outputs = self._model.generate(
                **inputs,
                max_new_tokens=self.max_new_tokens,
                temperature=max(temperature, 0.01),
                do_sample=temperature > 0,
                top_p=0.9,
            )
        new_tokens = outputs[0][inputs["input_ids"].shape[1]:]
        return self._tokenizer.decode(new_tokens, skip_special_tokens=True).strip()

    def select_action_react(
        self,
        observation: str,
        valid_actions: List[str],
        history: List[dict],
    ) -> Tuple[str, str]:
        """Standard ReAct: LLM picks one action.

        Returns (action, raw_llm_output).
        Falls back to first valid action if parsing fails.
        """
        messages = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": REACT_USER_TEMPLATE.format(
                observation=observation,
                valid_actions_str=_format_valid_actions(valid_actions),
                history_str=_format_history(history),
            )},
        ]
        raw = self._generate(messages)
        action = parse_action(raw, valid_actions)
        if action is None:
            action = valid_actions[0]  # fallback
        return action, raw

    def generate_candidate_actions(
        self,
        observation: str,
        valid_actions: List[str],
        history: List[dict],
        n: int = 3,
    ) -> Tuple[List[str], str]:
        """Generate top-n candidate actions for deterministic evaluation.

        Returns (list of actions, raw_llm_output).
        Pads with random valid actions if fewer than n parsed.
        """
        messages = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": CANDIDATE_USER_TEMPLATE.format(
                observation=observation,
                valid_actions_str=_format_valid_actions(valid_actions),
                history_str=_format_history(history),
                n=n,
            )},
        ]
        raw = self._generate(messages, temperature=0.5)
        candidates = parse_candidates(raw, valid_actions, n)

        # Pad if needed
        import random
        remaining = [a for a in valid_actions if a not in candidates]
        while len(candidates) < n and remaining:
            pick = random.choice(remaining)
            candidates.append(pick)
            remaining.remove(pick)

        return candidates, raw


def build_agent(args) -> LLMAgent:
    """Build LLMAgent from argparse namespace."""
    return LLMAgent(
        model_path=getattr(args, "model_path", None),
        use_vllm=getattr(args, "use_vllm", True),
        gpu_id=getattr(args, "gpu_id", 0),
    )


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--model_path", type=str, default=None)
    parser.add_argument("--use_vllm", type=bool, default=True)
    parser.add_argument("--gpu_id", type=int, default=0)
    args = parser.parse_args()
    agent = build_agent(args)
    print(f"Agent initialized. Model: {agent.model_path}")
