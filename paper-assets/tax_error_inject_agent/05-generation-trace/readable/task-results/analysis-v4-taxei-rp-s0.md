# analysis v4 taxei rp s0

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_v4-taxei-rp-s0_20260516T061331_result.json`
- **Structured JSON:** [`60eeabb3bff0c2e0f890.json`](../../sessions/60/60eeabb3bff0c2e0f890.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部更新完成。

## 总结

**v4-taxei-rp-s0 指标：**

| 指标 | s0 | s1 | s42 | s123 |
|------|----|----|-----|------|
| train_loss | 0.3847 | 0.3853 | 0.3847 | 0.3852 |
| token_acc | 0.9065 | 0.9176 | 0.9249 | 0.9137 |
| duration (min) | 231.07 | 226.3 | 226.67 | 226.5 |
| peak_memory (GiB) | 30.37 | 30.17 | 30.68 | 30.66 |
| samples/s | 3.124 | 3.19 | 3.185 | 3.187 |

**Checkpoint 路径（全部 4 seeds）：**
- s0: `/root/autodl-tmp/tax_error_inject_agent/output/v4-taxei-rp-s0/v0-20260516-101706/checkpoint-5415`
- s1: `/root/autodl-tmp/tax_error_inject_agent/output/v4-taxei-rp-s1/v0-20260516-101834/checkpoint-5415`
- s42: `/root/autodl-tmp/tax_error_inject_agent/output/v4-taxei-rp-s42/v0-20260516-101703/checkpoint-5415`
- s123: `/root/autodl-tmp/tax_error_inject_agent/output/v4-taxei-rp-s123/v0-20260516-101708/checkpoint-5415`

**一致性：** train_loss 高度一致（0.3847-0.3853）。s0 的 token_acc（0.9065）比其他 3 个 seed 低约 1%，duration 多 ~5 min（可能因 cuda:1 略有调度差异），总体正常。所有 4 个 seed 均已 DONE + checkpoint_path 已更新。

---
