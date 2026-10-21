# code proofwriter prompt adapt

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_proofwriter-prompt-adapt_20260515T184126_result.json`
- **Structured JSON:** [`41cf7152258811b66fe2.json`](../../sessions/41/41cf7152258811b66fe2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Artifacts 同步不是必须的，关键改动已在服务器上验证通过。

---

## 汇报

### 1. Prompt template 机制

**改动文件**：
- `sica/trace_generator.py` (267→304 行, +37 行)
- `sica/pipeline.py` (1 行改动)
- `eval_proofwriter.py` (dry-run 增强 + 移除 TODO)

**接口变化**：
- `TraceGenerator.generate()` 新增 `task_type: str = "math"` 参数（默认值保持 math，零回归）
- `VLLMGenerator._build_prompt()` 通过 `PROMPT_TEMPLATES` 字典选 template
- `pipeline.run_single()` 自动从 `problem["dataset"]` 推导 domain，传给 `generate(task_type=domain)`

**新增组件**：
| 组件 | 说明 |
|------|------|
| `LOGIC_PROMPT` | 逻辑推理 prompt，要求 step-by-step + `\boxed{True/False/Unknown}` |
| `PROMPT_TEMPLATES` | `{"math": SOLVE_PROMPT, "logic": LOGIC_PROMPT}` |
| `normalize_logic_answer()` | 标准化 True/False/Unknown（含 yes/no/proved 等同义词） |
| fallback pattern | `r'(?:answer\|conclusion\|statement)\s+is\s*(True\|False\|Unknown)'` |

### 2. Dry-run 结果

**Prompt 拼装**：10/10 题全部 OK
- 所有 prompt 包含 context (facts/rules)、question、`\boxed{True/False/Unknown}` 指令

**答案提取**：8/8 测试 ALL OK
| 输入 | 提取结果 | 方法 |
|------|---------|------|
| `\boxed{True}` | True | boxed |
| `\boxed{False}` | False | boxed |
| `\boxed{Unknown}` | Unknown | boxed |
| `the answer is True.` | True | fallback |
| `The conclusion is False.` | False | fallback |
| `The statement is Unknown.` | Unknown | fallback |
| `The final answer is True.` | True | fallback |
| `\boxed{true}` (小写) | True (normalize) | boxed |

### 3. Constraint extraction prompt

已适配——`constraint_extractor.py` 在服务器上早已有 `LOGIC_EXTRACTION_PROMPT`，且 `pipeline.run_single()` 已通过 `self.constraint_extractor.domain = domain` 自动切换。无需额外改动。

### v3 实验状态

PID 129992 正常运行（已 3h+），未受影响。

---
