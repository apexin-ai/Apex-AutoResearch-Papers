"""
双表征生成器。
两个独立 prompt 分别生成 FOL→Z3 代码 和 Python constraint 代码，无信息泄漏。
包含全局 API usage 追踪器供 pipeline/baseline 按样本计费。
"""

import re
import time
from typing import Tuple, List

import openai

from config import (
    API_BASE_URL, API_KEY, MODEL_NAME,
    API_MAX_RETRIES, API_RETRY_DELAY, API_TIMEOUT,
    PRICE_PER_INPUT_TOKEN, PRICE_PER_OUTPUT_TOKEN,
)

# ---------------------------------------------------------------------------
# Prompts
# ---------------------------------------------------------------------------

FOL_SYSTEM_PROMPT = """\
You are an expert in formal logic and the Z3 theorem prover.
Your task: formalize a natural-language reasoning problem into First-Order Logic
and output an executable Z3 Python script that checks entailment.

Output ONLY a complete Python script inside a ```python``` block.

## Requirements
1. `from z3 import *`
2. Define sorts with `DeclareSort`, constants with `Const`, predicates with `Function`.
3. Encode EVERY premise as Z3 constraints added to a Solver.
4. Entailment check:
   a. Push, add Not(conclusion). If unsat → print "True".
   b. Pop, push, add conclusion. If unsat → print "False".
   c. Otherwise print "Unknown".
5. Print EXACTLY one word: True, False, or Unknown. No other output.

## Critical Z3 Rules (violations cause crashes)
- ForAll/Exists MUST use bound variables created with Const, wrapped in a list:
  `x = Const('x', MySort); ForAll([x], body)` ✓
  `ForAll(MySort, body)` ✗ CRASH
  `ForAll(MySort(), body)` ✗ CRASH
- For Boolean predicates, use `BoolSort()` — NEVER `DeclareSort('Bool')`.
  `is_happy = Function('is_happy', Person, BoolSort())` ✓
  `Bool = DeclareSort('Bool'); is_happy = Function('is_happy', Person, Bool)` ✗
- Do NOT mix Datatype and EnumSort for the same sort name.
- If the domain is small and known, prefer ground constants over ForAll:
  enumerate each entity and add constraints individually.

## Example 1: With ForAll (universal quantifier)
Premises: "All employees who have meetings with customers appear in the company. James has a meeting with customers."
Conclusion: "James appears in the company."

```python
from z3 import *
Employee = DeclareSort('Employee')
meeting = Function('meeting_with_customers', Employee, BoolSort())
appear = Function('appear_in_company', Employee, BoolSort())
james = Const('james', Employee)
s = Solver()
x = Const('x', Employee)
s.add(ForAll([x], Implies(meeting(x), appear(x))))
s.add(meeting(james))
conclusion = appear(james)
s.push()
s.add(Not(conclusion))
if s.check() == unsat:
    print("True")
else:
    s.pop()
    s.push()
    s.add(conclusion)
    if s.check() == unsat:
        print("False")
    else:
        print("Unknown")
```

## Example 2: Ground constants only (no quantifiers needed)
Premises: "The Legend of Zelda was created by a Japanese game company. If a game sells more than one million copies, it is in the top 10. The Legend of Zelda sold more than one million copies."
Conclusion: "The Legend of Zelda is in the top 10."

```python
from z3 import *
Game = DeclareSort('Game')
zelda = Const('zelda', Game)
sold_1m = Function('sold_1m', Game, BoolSort())
top10 = Function('top10', Game, BoolSort())
s = Solver()
s.add(Implies(sold_1m(zelda), top10(zelda)))
s.add(sold_1m(zelda))
conclusion = top10(zelda)
s.push()
s.add(Not(conclusion))
if s.check() == unsat:
    print("True")
else:
    s.pop()
    s.push()
    s.add(conclusion)
    if s.check() == unsat:
        print("False")
    else:
        print("Unknown")
```

## Example 3: Mixed quantifiers and existential
Premises: "All cats are mammals. Some pets are cats. No mammals can fly."
Conclusion: "Some pets cannot fly."

```python
from z3 import *
Animal = DeclareSort('Animal')
cat = Function('cat', Animal, BoolSort())
mammal = Function('mammal', Animal, BoolSort())
pet = Function('pet', Animal, BoolSort())
can_fly = Function('can_fly', Animal, BoolSort())
s = Solver()
x = Const('x', Animal)
s.add(ForAll([x], Implies(cat(x), mammal(x))))
witness = Const('witness', Animal)
s.add(pet(witness))
s.add(cat(witness))
s.add(ForAll([x], Implies(mammal(x), Not(can_fly(x)))))
conclusion = Exists([x], And(pet(x), Not(can_fly(x))))
s.push()
s.add(Not(conclusion))
if s.check() == unsat:
    print("True")
else:
    s.pop()
    s.push()
    s.add(conclusion)
    if s.check() == unsat:
        print("False")
    else:
        print("Unknown")
```"""

FOL_USER_TEMPLATE = """\
Premises:
{premises}

Conclusion:
{conclusion}

Generate a complete, executable Z3 Python script."""


CODE_SYSTEM_PROMPT = """\
You are an expert Python programmer specializing in logical reasoning.
Translate a natural-language reasoning problem into a self-contained Python
script that evaluates whether the conclusion follows from the premises.

Output ONLY a complete Python script inside a ```python``` block. Requirements:
1. Use ONLY standard Python — no z3, sympy, or other external libraries.
2. Model entities, categories, and relationships with Python data structures
   (sets, dicts, dataclasses, etc.).
3. Encode EVERY premise explicitly.
4. Evaluate entailment:
   - "True"  if the conclusion must hold given the premises.
   - "False" if the conclusion is contradicted.
   - "Unknown" if the premises are insufficient.
5. For universal quantifiers ("All X are Y"), iterate over all relevant elements.
   For existential ("Some X"), check existence.
6. Print EXACTLY one word: True, False, or Unknown. No other output.
7. Do NOT include any comments, explanations, or reasoning — just the code.

## Example
Premises: "All employees who study hard pass the exam. John is an employee. John studies hard."
Conclusion: "John passes the exam."

```python
employees = {"John"}
studies_hard = {"John"}
passes_exam = set()
for e in employees:
    if e in studies_hard:
        passes_exam.add(e)
if "John" in passes_exam:
    print("True")
else:
    print("Unknown")
```"""

CODE_USER_TEMPLATE = """\
Premises:
{premises}

Conclusion:
{conclusion}

Generate a complete, executable Python script."""

# ---------------------------------------------------------------------------
# Usage tracking
# ---------------------------------------------------------------------------

_usage_log: List[dict] = []


def reset_usage():
    """清空当前样本的 usage 累计。在每个样本处理开始时调用。"""
    _usage_log.clear()


def get_usage() -> dict:
    """返回自上次 reset 以来的累计 usage。"""
    total_in = sum(u["input_tokens"] for u in _usage_log)
    total_out = sum(u["output_tokens"] for u in _usage_log)
    total_cost = sum(u["cost_usd"] for u in _usage_log)
    return {
        "calls": len(_usage_log),
        "input_tokens": total_in,
        "output_tokens": total_out,
        "cost_usd": round(total_cost, 6),
    }


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _get_client() -> openai.OpenAI:
    return openai.OpenAI(
        base_url=API_BASE_URL,
        api_key=[REDACTED],
        timeout=API_TIMEOUT,
    )


def _strip_thinking(text: str) -> str:
    text = re.sub(r"<think>[\s\S]*?</think>", "", text)
    if "<think>" in text:
        text = text[:text.index("<think>")]
    return text.strip()


def _extract_code(response_text: str) -> str:
    for pattern in [r"```python\s*\n(.*?)```", r"```\s*\n(.*?)```"]:
        matches = re.findall(pattern, response_text, re.DOTALL)
        if matches:
            return matches[-1].strip()
    return response_text.strip()


def _call_llm(
    system_prompt: str,
    user_prompt: str,
    max_tokens: int = 4096,
    enable_thinking: bool = True,
) -> str:
    client = _get_client()
    kwargs = {}
    if not enable_thinking:
        kwargs["extra_body"] = {
            "chat_template_kwargs": {"enable_thinking": False}
        }
    for attempt in range(API_MAX_RETRIES):
        try:
            resp = client.chat.completions.create(
                model=MODEL_NAME,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt},
                ],
                temperature=0.7,
                max_tokens=max_tokens,
                **kwargs,
            )
            content = resp.choices[0].message.content or ""

            # Track usage
            usage = resp.usage
            if usage:
                in_tok = usage.prompt_tokens or 0
                out_tok = usage.completion_tokens or 0
                cost = getattr(usage, "cost", None)
                if cost is None:
                    cost = in_tok * PRICE_PER_INPUT_TOKEN + out_tok * PRICE_PER_OUTPUT_TOKEN
                _usage_log.append({
                    "input_tokens": in_tok,
                    "output_tokens": out_tok,
                    "cost_usd": float(cost),
                })

            return _strip_thinking(content)
        except Exception as e:
            if attempt < API_MAX_RETRIES - 1:
                time.sleep(API_RETRY_DELAY * (attempt + 1))
            else:
                raise RuntimeError(
                    f"LLM call failed after {API_MAX_RETRIES} retries: {e}"
                ) from e

# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def generate_fol_code(premises: str, conclusion: str) -> Tuple[str, str]:
    """返回 (raw_response, extracted_z3_code)。"""
    user = FOL_USER_TEMPLATE.format(premises=premises, conclusion=conclusion)
    raw = _call_llm(FOL_SYSTEM_PROMPT, user)
    return raw, _extract_code(raw)


def generate_python_code(premises: str, conclusion: str) -> Tuple[str, str]:
    """返回 (raw_response, extracted_python_code)。"""
    user = CODE_USER_TEMPLATE.format(premises=premises, conclusion=conclusion)
    raw = _call_llm(CODE_SYSTEM_PROMPT, user, enable_thinking=False)
    return raw, _extract_code(raw)


SYNTAX_FIX_PROMPT = """\
The following Z3 Python script crashed with an error. Fix ONLY the bug — \
do not change the logical meaning. Output the complete corrected script \
inside a ```python``` block.

--- ORIGINAL CODE ---
{code}

--- ERROR ---
{error}

Output the fixed script."""


def syntax_fix_z3(code: str, error: str) -> str:
    """Given crashed Z3 code and its error, ask LLM to fix syntax/API issues."""
    prompt = SYNTAX_FIX_PROMPT.format(code=code, error=error[:1500])
    raw = _call_llm(
        "You are a Z3/Python debugging expert. Fix the code bug.",
        prompt,
        max_tokens=4096,
    )
    return _extract_code(raw)
