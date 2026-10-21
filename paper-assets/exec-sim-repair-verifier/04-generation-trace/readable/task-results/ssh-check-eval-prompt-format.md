# ssh check eval prompt format

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check-eval-prompt-format_20260520T054821_result.json`
- **Structured JSON:** [`5c8901c293ace4d6f761.json`](../../sessions/5c/5c8901c293ace4d6f761.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

以下是原始结果汇总：

---

### eval_repo_cwm.py prompt 相关代码

**SYSTEM_PROMPT (L31-34):**
```python
SYSTEM_PROMPT = (
    "You are a code execution simulator. Given a code patch (git diff) and a test name, "
    "predict the execution result when the test is run against the patched code."
)
USER_TEMPLATE = "## Code\n{code}\n\n## Test\n{test}\n\nWhat is the execution result?"
```

**build_prompt_ids (L108-124):**
```python
def build_prompt_ids(tokenizer, code, test, tmpl_kw, max_len):
    user_msg = USER_TEMPLATE.format(code=code, test=test)
    msgs = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_msg},
    ]
    ids = _apply_chat_template_safe(
        tokenizer, msgs, tmpl_kw, tokenize=True, add_generation_prompt=True,
    )
```

---

### train_unified.py prompt 相关代码（对比）

**SYSTEM_PROMPTS (L38-47):**
```python
SYSTEM_PROMPTS = {
    "cwm": (
        "You are a code execution simulator. Given a code snippet and a test case, "
        "predict the execution result."
    ),
    "cls": (
        "You are a code verifier. Given a code patch and a test name, "
        "predict whether the test will pass or fail when run against the patched code."
    ),
}
```

**USER_TEMPLATES (L49-52):**
```python
USER_TEMPLATES = {
    "cwm": "## Code\n{code}\n\n## Test\n{test}\n\nWhat is the execution result?",
    "cls": "## Patch (git diff)\n{code}\n\n## Test\n{test}\n\nWill this test pass or fail?",
}
```

**build_messages (L121-129):**
```python
def build_messages(code, test, target=None, task="cwm"):
    user_msg = USER_TEMPLATES[task].format(code=code, test=test)
    msgs = [
        {"role": "system", "content": SYSTEM_PROMPTS[task]},
        {"role": "user", "content": user_msg},
    ]
    if target is not None:
        msgs.append({"role": "assistant", "content": target})
    return msgs
```

---
