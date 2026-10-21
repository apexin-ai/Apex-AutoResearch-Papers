# diagnose matched ablation controls

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_matched_ablation_controls_20260519T041002_result.json`
- **Structured JSON:** [`885d1c1c2928fb903e47.json`](../../sessions/88/885d1c1c2928fb903e47.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成，报告已写入 `artifacts/matched_ablation_controls_diagnosis.md`。

**核心发现：**

1. **matched_ablation_controls** — 实际已正常完成（10500 passes, return_code=0），不是"异常退出"。无 W&B metrics 是因为脚本根本没集成 W&B，结果只存 JSON。Registry 应更新为 COMPLETED。

2. **behavioral_smoketest** — 进程已正常退出，不是 RUNNING。Baseline 3 episodes 全部失败（SR=0.00），脚本按设计提前终止。Registry 应更新为 COMPLETED (baseline_zero)。

3. **环境注意事项** — 磁盘 95% 已满（剩 15G），后续实验前需要清理空间。

---
