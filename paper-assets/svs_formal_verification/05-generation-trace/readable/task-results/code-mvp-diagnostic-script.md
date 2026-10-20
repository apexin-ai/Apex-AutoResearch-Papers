# code mvp diagnostic script

**svs formal verification** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_mvp_diagnostic_script_20260514T115752_result.json`
- **Structured JSON:** [`b0fbe3e9c0b0b691a646.json`](../../sessions/b0/b0fbe3e9c0b0b691a646.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run 成功，24 题 192 chains，全部 7 个 section 正常输出。

关键观察（partial data）：
- **P2 FAIL**: Cohen's d = -0.0437，IC 完全不区分 correct/wrong chains，CI 宽跨零
- **4 个 inversion case**（SVS 错 SC 对），其中 3 个是 Unknown/True 被 CCLC 加成的 True 组反超
- **All-SAT 27.1%**，True 链最高（31.1%）
- **FC weight 无关紧要**：纯 IC / 默认 / 纯 FC 几乎没差，问题在 IC 本身不区分正确性
- Section 4 显示 IC 在各 label×correctness 格子间差异极小，确认 IC 目前更像 noise 而非 signal

脚本就绪在 `/root/scripts/mvp_diagnostic.py`，mvp_003 跑完后直接 `python /root/scripts/mvp_diagnostic.py /root/outputs/results_partial.json` 即可。

---
