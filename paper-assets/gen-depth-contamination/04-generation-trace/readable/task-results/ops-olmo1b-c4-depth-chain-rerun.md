# ops olmo1b c4 depth chain rerun

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_olmo1b_c4_depth_chain_rerun_20260521T100518_result.json`
- **Structured JSON:** [`f673f11547653dce53ad.json`](../../sessions/f6/f673f11547653dce53ad.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Step 7 结果报告：

```
MODEL: OLMo-1B
STATUS: completed
1v2_AUC: 0.5080 (主表: 0.6145, Δ=-0.1065)
ALL_PAIRWISE_AUC: {0v1: 0.9860, 1v2: 0.5080, 2v3: 0.4973, 3v4: 0.5024, 4v5: 0.4942}
K_STAR_AT_060: 1
CONFIG_SAVED: yes
```

关键发现：1v2 AUC 从原始的 0.6145 降到了 0.5080（接近随机），差异显著（Δ=-0.1065）。0v1 仍然很高（0.9860），说明 depth 0→1 的区分度极好，但 depth 1 之后所有相邻对 AUC 全部在 0.50 附近（随机水平），说明从 depth 1 开始特征已经饱和，无法区分更深的生成层次。

这与原始 0.6145 的差异可能来源于：原始实验可能使用了不同的 scorer、不同的 feature pipeline 版本、或不同的数据子集。当前 rerun 使用标准化 pipeline + Qwen2.5-1.5B scorer 的结果是 0.5080。

---
