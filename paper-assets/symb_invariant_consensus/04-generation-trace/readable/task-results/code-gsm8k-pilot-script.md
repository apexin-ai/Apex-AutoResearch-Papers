# code gsm8k pilot script

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_gsm8k-pilot-script_20260516T080120_result.json`
- **Structured JSON:** [`b3ab75bb9a2e0043767e.json`](../../sessions/b3/b3ab75bb9a2e0043767e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`--help` 正常。脚本已部署到 `/root/symb_invariant_consensus/scripts/run_gsm8k_pilot.py`。

与 `eval_gsm8k.py` 的区别：
- 默认 k=6（非12）、n_problems=30（非200）
- 新增 **C0 指标**（第一条 trace 的准确率，作为 single-pass baseline）
- 使用 `pipeline.run_single(prob)`（正确 API，eval_gsm8k.py 用的 `pipeline.run()` 实际不存在）
- pilot 专用报告格式：表格化 per-problem 详情 + C0/SC/SICA 三方对比
- 输出到 `results/gsm8k_pilot.json`

---
