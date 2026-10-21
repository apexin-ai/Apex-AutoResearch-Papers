# code fixes abc

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fixes-abc_20260518T180914_result.json`
- **Structured JSON:** [`eb50b35ac2572eeeec7e.json`](../../sessions/eb/eb50b35ac2572eeeec7e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个 fix 全部完成。验证结果：

### Fix A: python not found — **新修复**
- 创建了 `/usr/local/bin/python` → `/root/miniconda3/bin/python3` 的 symlink
- 验证：`which python` → `/usr/local/bin/python`，`python --version` → `Python 3.12.4`
- 无需 conda activate 即可直接用 `python`

### Fix B: StrategyQA extraction prompt — **已修复（上个 session）**
- `COMMONSENSE_EXTRACTION_PROMPT` 存在于 `sica/constraint_extractor.py`
- `COMMONSENSE_SOLVE_PROMPT` 存在于 `sica/trace_generator.py`
- `run_full_mvp.py` 中 strategyqa → `extractor.domain = "commonsense"` + `pipeline.trace_generator.domain = "commonsense"` 映射正确
- import 验证通过

### Fix C: Z3 Feedback 模型路径 — **新修复**
- `/root/models/` 不存在，模型实际在 `/root/autodl-tmp/models/Qwen2.5-14B-Instruct/`
- 已将 `run_z3_feedback_folio.sh` 中的 `--model /root/models/Qwen2.5-14B-Instruct` 修正为 `--model /root/autodl-tmp/models/Qwen2.5-14B-Instruct`
- `run_z3_feedback_folio.py` 中 `--model` 默认值是 `Qwen2.5-14B-Instruct`（模型名而非路径），由 shell 脚本传入，无需改

---
