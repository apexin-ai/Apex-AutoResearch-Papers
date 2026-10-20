# data rerun trace segment v2

**trace distill repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data_rerun_trace_segment_v2_20260514T152039_result.json`
- **Structured JSON:** [`d741c6d6ffd6d9d808cb.json`](../../sessions/d7/d741c6d6ffd6d9d808cb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全量运行完成。现在整理 v1 vs v2 对比汇总。

## 全量重跑结果汇总

### 总体

| 指标 | v1（旧） | v2（新） |
|------|---------|---------|
| 实例 ready | 25/30 | 27/30 |
| Trace 成功 | 18/25 | 26/27 |
| Trace 失败 | 7 | 1 (fastapi_3) |
| 平均 events | ~4,133 | 5,891 |

### 修复效果 — 之前失败的 7 个实例

| 实例 | v1 events | v2 events | v2 structural segs | 状态 |
|------|-----------|-----------|---------------------|------|
| fastapi_1 | 0 (FAIL) | 718 | 20 | **修复** |
| fastapi_2 | 0 (FAIL) | 714 | 20 | **修复** |
| fastapi_3 | 0 (FAIL) | 0 | - | 仍失败 |
| tqdm_1 | 0 (FAIL) | 466 | 20 | **修复** |
| tqdm_2 | 0 (FAIL) | 8 | 2 | **修复** `too_small` |
| youtube-dl_1 | 0 (FAIL) | 67,244 | 20 | **修复** |
| youtube-dl_2 | 0 (FAIL) | 59,653 | 20 | **修复** |

### 全量实例 v1 vs v2 对比

| 实例 | v1 events | v2 events | v1 struct segs | v2 struct segs | v2 segment types | 标注 |
|------|-----------|-----------|----------------|----------------|------------------|------|
| thefuck_1 | 31 | 31 | 2 | 4 | call=2, block=1, exc=1 | |
| thefuck_2 | 31 | 31 | 2 | 4 | call=2, block=1, exc=1 | |
| thefuck_4 | 30 | 30 | 2 | 3 | call=2, exc=1 | |
| black_1 | 51 | 51 | 2 | 4 | call=2, block=1, exc=1 | |
| black_2 | 46 | 46 | 1 | 3 | call=1, block=1, exc=1 | |
| cookiecutter_1 | 185 | 185 | 2 | 20 | call=15, block=4, loop=1 | |
| cookiecutter_2 | 185 | 185 | 2 | 20 | call=15, block=4, loop=1 | |
| cookiecutter_3 | 37 | 37 | 2 | 6 | call=3, block=2, exc=1 | |
| fastapi_1 | 0 | 718 | 0 | 20 | call=5, loop=13, block=2 | |
| fastapi_2 | 0 | 714 | 0 | 20 | call=5, loop=14, block=1 | |
| httpie_1 | 5 | 5 | 1 | 1 | exc=1 | `too_small` |
| httpie_2 | 1,459 | 646 | 8 | 20 | block=6, loop=13, call=1 | |
| luigi_1 | 7,536 | 3,329 | 6 | 20 | call=12, block=4, exc=2, loop=2 | |
| luigi_2 | 7,536 | 3,317 | 6 | 20 | call=11, exc=2, loop=5, block=2 | |
| luigi_5 | - | 1,952 | - | 3 | block=1, exc=2 | 新实例 |
| sanic_1 | 78 | 78 | 1 | 8 | block=4, call=3, exc=1 | |
| sanic_2 | 700 | 700 | 2 | 20 | block=2, call=8, loop=10 | |
| scrapy_1 | 13,229 | 202 | 3 | 18 | loop=10, block=5, exc=3 | |
| scrapy_2 | 132 | 166 | 2 | 20 | loop=10, block=7, call=2, exc=1 | |
| tornado_1 | 21,327 | 7,059 | 59 | 20 | call=2, loop=16, block=2 | |
| tornado_2 | 21,237 | 4,950 | 59 | 20 | call=1, loop=18, block=1 | |
| tornado_5 | - | 1,362 | - | 20 | call=2, block=1, loop=17 | 新实例 |
| tqdm_1 | 0 | 466 | 0 | 20 | block=8, loop=2, call=9, exc=1 | |
| tqdm_2 | 0 | 8 | 0 | 2 | call=1, exc=1 | `too_small` |
| youtube-dl_1 | 0 | 67,244 | 0 | 20 | call=9, loop=9, block=1, exc=1 | |
| youtube-dl_2 | 0 | 59,653 | 0 | 20 | call=6, loop=11, exc=1, block=2 | |

### 标注

- **`too_small`**: httpie_1 (5 events, 1 seg), tqdm_2 (8 events, 2 segs)
- **`truncated`**: 无 — youtube-dl_1/2 分别 67K/60K events，未达到 100K 上限
- **仍失败**: fastapi_3 (0 events)

### 统计

- **Structural segments 中位数**: **20**（26 个实例中有 17 个达到 20 个上限）
- **≥5 segments**: 18/26（69%）。未达标的 8 个：httpie_1(1), tqdm_2(2), luigi_5(3), thefuck_4(3), black_2(3), thefuck_1(4), thefuck_2(4), black_1(4)
- **Segment type 分布** (v2 全量): call_subtree 最多，其次 loop_iteration 和 basic_block，exception_chain 最少
- **v1→v2 segment 变化**: 小 trace（≤50 events）从 1-2 涨到 3-4；中大 trace 几乎全部达到 20 上限（之前多数只有 1-8）

### 关键变化

1. 修复后 6 个之前失败的实例恢复（fastapi_1/2, tqdm_1/2, youtube-dl_1/2），成功率 18→26
2. basic_block 是新增的 segment type，显著增加了小 trace 的 segment 数
3. 部分实例 event 数下降（scrapy_1: 13K→202, tornado: 21K→7K），可能是 line events 模式下 trace collector 的过滤行为不同
4. 新增 2 个实例：tornado_5, luigi_5

数据已写入 `/root/trace_distill_repair/pipeline_output/`，summary.json 已更新。

---
