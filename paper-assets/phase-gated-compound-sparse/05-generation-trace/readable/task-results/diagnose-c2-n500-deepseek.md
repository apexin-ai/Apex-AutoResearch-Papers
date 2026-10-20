# diagnose c2 n500 deepseek

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_c2_n500_deepseek_20260515T075008_result.json`
- **Structured JSON:** [`10df17136e8f1a27b9e4.json`](../../sessions/10/10df17136e8f1a27b9e4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**诊断结果：SUCCESS**

全部 8 conditions 完成 (500/500)，Verdict 均 PASS：
- GPU0 (importance × 4 sparsity): 02:31 → 15:44 完成
- GPU1 (random × 4 sparsity): 02:05 → 15:19 完成

关键发现：importance masking 的 II 呈明显 phase 依赖（low >> mid >> high，如 s030: 10.63 vs 1.74 vs 0.05），random masking 各 phase 差异小（s030: 4.15 vs 3.37 vs 3.48），符合假设。

Registry 已更新为 ANALYZING，诊断报告已注册为 artifact `art_20260515_e21731`。

---
