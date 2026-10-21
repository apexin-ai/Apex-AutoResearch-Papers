# analysis null t15 s43 d102

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_null_t15_s43_d102_20260524T094413_result.json`
- **Structured JSON:** [`d37e47fb1f9c08671379.json`](../../sessions/d3/d37e47fb1f9c08671379.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。

**null_t15_s43_fp32 D102: PermG fwd 0/8, rev 0/8, K≥3 1/8**

注：脚本实际产出 8 pairs（2 canary × 4 downstream），不是 6。PermG FPR 完美归零，符合 null 预期。唯一 K≥3 pair 是 ece<distinct_1（naive+diff+threshold 投票），无 PermG 参与，不影响 FPR claim。Threshold onset 在 5/8 pairs 有虚报，但被 PermG 过滤掉了——这正好说明 PermG 的 FPR 控制优于单一方法。

---
