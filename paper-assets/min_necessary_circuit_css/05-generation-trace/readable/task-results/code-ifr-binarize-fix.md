# code ifr binarize fix

**Transformer Model EAP-IG** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_ifr_binarize_fix_20260512T184514_result.json`
- **Structured JSON:** [`e4a77e7747af14e58bde.json`](../../sessions/e4/e4a77e7747af14e58bde.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成。产出文件：`artifacts/css.py` + `artifacts/test_css.py`，8/8 测试通过。

### 各策略对 IFR 同质性问题的处理效果

| 策略 | IFR 同分边处理 | 适用场景 |
|------|---------------|---------|
| **topn** | **有问题**。36 个同分 IFR 边任意挑 N 个占满配额，排挤 EAP-IG/EP 的边 | 仅适用于 per-edge 粒度方法（EAP-IG、EP） |
| **threshold** | 无同质性问题，但阈值是绝对值，跨方法不可比 | 单方法内部筛选 |
| **percentile_threshold** | **解决**。36 个同分边算 1 个 unique value 参与百分位计算，超过阈值则全部纳入。不存在配额抢占 | CSS 跨方法对比的默认选择 |
| **unique_score_rank** | **解决**。按 unique score 排名取 top-N，同分边整组纳入或整组排除，不会截断 | 需要控制"有效层级数"时使用 |

结论：CSS 流程中 IFR 应使用 `percentile_threshold` 或 `unique_score_rank`，避免 `topn` 的 block-vote 问题。

---
