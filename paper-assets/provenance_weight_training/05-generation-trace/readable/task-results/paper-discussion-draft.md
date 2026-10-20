# paper discussion draft

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_discussion-draft_20260516T002413_result.json`
- **Structured JSON:** [`cf9d2dfc48d5c22bd984.json`](../../sessions/cf/cf9d2dfc48d5c22bd984.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**章节结构和字数：**

**Discussion（3段，~0.5 page）：**
1. **Why minimum intervention works** — ESS-only PPL=17.723 > uniform 17.694 的机制分析：过度 downweighting 丢弃 borderline samples 梯度信号；α_eff binding 时 b*=1.67 vs ESS-only 4.15
2. **τ as a practical dial** — [0.5, 0.8] safe range，asymmetric sensitivity（under-cleaning 代价小，over-cleaning 代价大），推荐 τ=0.8
3. **Connection to convergence theory** — Wang et al. (2026) α 理论 motivation，诚实定位 τ 为 empirical HP with theoretical motivation

**Limitations（7段）：**
Scale / Contamination distribution / Detector coverage / Threshold / Evaluation / Effect size / Batch size sensitivity

所有定量 claim 均引用 Table 1/Table 2 数据。总计约 550 词，符合 0.5 page 目标。已注册为 `art_20260516_270aaa`。

---
