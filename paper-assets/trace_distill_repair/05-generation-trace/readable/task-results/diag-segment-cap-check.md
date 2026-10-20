# diag segment cap check

**trace distill repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_segment_cap_check_20260515T053632_result.json`
- **Structured JSON:** [`60d650f7644968a4748d.json`](../../sessions/60/60d650f7644968a4748d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果清晰。汇总如下：

---

## 调查结果

### 1. 硬编码上限确认

**文件**: `/root/trace_distill_repair/structural_segmenter.py`，`_merge_and_deduplicate` 方法末尾。

```python
MAX_SEGMENTS = 20
if len(merged) > MAX_SEGMENTS:
    step = len(merged) / MAX_SEGMENTS
    merged = [merged[int(i * step)] for i in range(MAX_SEGMENTS)]
```

### 2. 截断策略

**均匀等间距采样**：按 `step = total / 20` 间隔从已排序（按 start_idx）的 segments 中选取 20 个，其余丢弃。不考虑 segment 类型、大小或重要性，纯机械采样。

### 3. 无上限测试结果

| 实例 | Events | 无上限 segments | 被截断到 20 |
|------|--------|----------------|------------|
| youtube-dl_2 | 49,974 | **814** | 是 (丢失 97.5%) |
| tornado_1 | 5,286 | **545** | 是 (丢失 96.3%) |
| luigi_2 | 9,284 | **449** | 是 (丢失 95.5%) |
| fastapi_1 | 3,566 | **263** | 是 (丢失 92.4%) |
| scrapy_1 | 160 | **20** | 恰好 20，无截断 |
| black_1 | 147 | **10** | 未超限 |
| httpie_1 | 5 | **1** | 未超限 |

youtube-dl_2 的 814 个 segment 中，类型分布：call_subtree 387, loop_iteration 305, basic_block 110, exception_chain 12。

### 4. 影响评估

- 大实例信息损失严重（95%+的 segments 被丢弃）
- 均匀采样策略进一步加剧问题——exception_chain 等高价值 segment 与 basic_block 等低价值 segment 同等概率被丢弃
- 但 814 个 segments 直接送 teacher scoring 的 API 成本不可接受

### 5. 建议

不应简单提高上限到 50/100，而应改用**分层采样策略**：

1. **保留所有 exception_chain**（通常很少，本例仅 12 个，是最高价值信号）
2. **按类型配额分配剩余名额**，例如 call_subtree 优先于 basic_block
3. **在同类型内按 segment 大小（event 数）排序**，优先保留大 segment（覆盖更多 trace）
4. 上限建议 **40-50**（在信息保留和 API 成本之间取平衡）

---
