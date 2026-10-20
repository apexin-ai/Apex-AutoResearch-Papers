# diagnose exp 002 signals 3B v6

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp_002_signals_3B_v6_20260515T204224_result.json`
- **Structured JSON:** [`6d32bc3d5206c3fe45bf.json`](../../sessions/6d/6d32bc3d5206c3fe45bf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。诊断结论：

**exp_002_signals_3B_v6 → failed（部分完成）**

| 信号 | mmlu | gsm8k | arc_challenge |
|------|------|-------|---------------|
| s1_embedding | ✅ | ✅ | ✅ |
| s2_minkpp | ✅ | ✅ | ✅ |
| s3_constat | ❌ | ❌ | ❌ |

**失败原因**：`s3_constat.py:50` 抛出 `ValueError: Item count mismatch: expected 1172, got 697`。constat 信号计算出的向量长度与预期 item 数不一致，是代码 bug。

**已保存产出**（6 个文件）：`/root/autodl-tmp/exp002/signals/Qwen2.5-3B_d000_v2_s42/`

**需要修复**：`s3_constat.py` 中向量长度与 item count 的不一致问题，然后重跑 s3。s1/s2 的产出可复用。

---
