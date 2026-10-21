# cpu mv unified recompute

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_cpu_mv_unified_recompute_20260521T125213_result.json`
- **Structured JSON:** [`24917039eadf34cdb669.json`](../../sessions/24/24917039eadf34cdb669.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果摘要：

### v4 Main Table（strict MV > N/2）

| Dataset | greedy | mv | oracle | Δ_SC | δ | α_crit |
|---------|--------|-----|--------|------|---|--------|
| FewNERD (3 seeds) | 0.7912 | 0.7638 | 0.8852 | **−2.74pp** | 8.8% | 0.6179 |
| CoNLL (s42 only) | 0.9123 | 0.9101 | 0.9538 | **−0.22pp** | 60.1% | 0.8351 |
| SciERC (3 seeds) | 0.6670 | 0.6596 | 0.7808 | **−0.74pp** | 12.2% | 0.4920 |

### 关键发现

1. **严格阈值 (>4) 使 MV 全面劣于 greedy**：所有 7 个 (dataset, seed) 组合 Δ_SC < 0。v3 的 inclusive (≥4) 下 CoNLL/SciERC 有微弱正增益，strict 后全部消失。
2. **FewNERD 受影响最大**：mv_f1 从 ~0.78 降到 ~0.76（约 −2pp），因为 4/8 票的 entities 在 inclusive 下净正贡献，strict 下被删除。
3. **CoNLL s123/s456 数据缺失**，标记 pending。CoNLL s42 数据疑似被 regenerate（greedy/δ 与 v3 有偏移）。

Artifact 已注册：`alpha_crit_table_v4.md`。

---
