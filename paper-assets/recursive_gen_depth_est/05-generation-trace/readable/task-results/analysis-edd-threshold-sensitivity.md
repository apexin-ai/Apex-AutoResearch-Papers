# analysis edd threshold sensitivity

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_edd_threshold_sensitivity_20260515T032002_result.json`
- **Structured JSON:** [`d5a8b77c16aa5eb3f788.json`](../../sessions/d5/d5a8b77c16aa5eb3f788.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。核心结果：

**EDD=3 计数随阈值变化：** 9/9 → 8/9 → 7/9 → 5/9（T=0.65/0.70/0.75/0.80）

**关键发现：**
- **瓶颈统一是 d2v3 pair**，d0v1（>0.98）从不是限制因素
- **topk50 策略最敏感**：3 个 topk50 cell 占了 4 个敏感 cell 中的 3 个
- **5 个 cell 全阈值稳定**（EDD=3）：pythia_nucleus、olmo_nucleus、olmo_temp09、gpt2xl_nucleus、gpt2xl_temp09
- **pythia_topk50 最脆弱**：EDD 从 3→2→2→1，唯一降到 EDD=1 的 cell
- **推荐默认阈值 T=0.75**：7/9 维持 EDD=3，仅 topk50 掉队；T=0.80 过于激进（5/9），T=0.65/0.70 过于宽松

**注：** 原 Atlas v2 声称 T=0.80 下"6/7 cells EDD=3"，但实际数据显示 pythia_temp09 的 d2v3=0.7928 < 0.80，应为 EDD=2。完整 9-cell 分析下 T=0.80 实际为 5/9 EDD=3。

产出已注册：`art_20260515_acdedc`

---
