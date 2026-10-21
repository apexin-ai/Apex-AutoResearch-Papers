# verify text temperature check

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_text-temperature-check_20260518T112833_result.json`
- **Structured JSON:** [`37c74e2aafb56e610805.json`](../../sessions/37/37c74e2aafb56e610805.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All information collected. Here's the report:

---

## 温度设置审计报告

### 1. `sica/constraint_extractor.py` 默认温度

| 类 | 默认 T_ext | 行号 | 备注 |
|---|---|---|---|
| **VLLMBackend** | **0.3** (硬编码) | L134 | `call()` 方法内直接写死 `temperature=0.3`，构造函数无 temperature 参数，外部无法覆盖 |
| **APIBasedLLM** | **0.1** | L182 | 构造函数参数 `temperature: float = 0.1`，外部可覆盖 |

### 2. `run_full_mvp.py` 温度传递

- L201: `--temperature` CLI 参数，**default=0.7**
- L84/L92: 构造 VLLMBackend / APIBasedLLM 时传 `temperature=args.temperature`

**关键问题**: VLLMBackend 的 `__init__` 不接受 temperature 参数。L84 传了 `temperature=args.temperature`，但 VLLMBackend 构造函数里不会使用它（`call()` 里硬编码 0.3）。所以即使 CLI 传 `--temperature 0.7`，VLLMBackend 实际使用的仍然是 **0.3**。

### 3. `sica/pipeline.py`

pipeline.py 中**无 temperature 相关代码**（grep 无匹配）。

### 4. exp-001 实际 T_ext

exp-001 使用 `run_full_mvp.py --mode vllm`（默认模式）。

- CLI default: `--temperature 0.7`（但传给 VLLMBackend 无效）
- VLLMBackend `call()` 硬编码: **0.3**
- **exp-001 实际 T_ext = 0.3**

### 5. 新脚本温度设置

| 脚本 | T_ext 设置 | 行号 |
|---|---|---|
| `run_case_study_extract.sh` | **0.7** | L64 |
| `run_folio_trace_regen.sh` | **0.7** | L65 |
| `run_cross_model_mistral.sh` | **0.1** | L72 |
| `cross_model_extract.py` | **0.1** (default) | L33 |

### 6. 不一致汇总

存在 **三重不一致**：

1. **VLLMBackend 硬编码 bug** (`constraint_extractor.py` L134): `temperature=0.3` 写死在 `call()` 里，忽略外部传入值。构造函数不接受 temperature 参数，导致 `run_full_mvp.py` 传的 `temperature=args.temperature` 静默失效。

2. **新脚本之间不一致**: `run_case_study_extract.sh` 和 `run_folio_trace_regen.sh` 用 T=0.7，`run_cross_model_mistral.sh` 用 T=0.1。

3. **新脚本与 exp-001 不一致**: exp-001 实际 T=0.3，新脚本用 0.7 或 0.1，没有一个匹配。

### 需要修改的文件

| 文件 | 问题 | 建议 |
|---|---|---|
| `sica/constraint_extractor.py` L116-136 | VLLMBackend 不接受/使用外部 temperature | 构造函数加 `temperature` 参数，`call()` 使用 `self.temperature` |
| `scripts/run_case_study_extract.sh` L64 | T=0.7 与 exp-001 不匹配 | 确认目标 T_ext 后统一 |
| `scripts/run_folio_trace_regen.sh` L65 | T=0.7 与 exp-001 不匹配 | 同上 |

---
