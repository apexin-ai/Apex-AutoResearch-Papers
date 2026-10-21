# monitor rsft gen progress

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_rsft_gen_progress_20260515T025444_result.json`
- **Structured JSON:** [`da22943fd7899af9e89c.json`](../../sessions/da/da22943fd7899af9e89c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## RSFT 生成进度报告

### 进程状态
4 个进程全部存活，运行时间 1h05m ~ 1h14m。

### 各 Shard 进度

| Shard | 范围 | 已完成 | 总数 | 进度 | 输出行数 |
|-------|------|--------|------|------|----------|
| 0 | [302:984] | **289** | 682 | 42.4% | 2312 |
| 1 | [984:1665] | **323** | 681 | 47.4% | 2584 |
| 2 | [1665:2346] | **321** | 681 | 47.1% | 2568 |
| 3 | [2346:3027] | **262** | 681 | 38.5% | 2096 |

**总计**: 1195/2725 docs = **43.9%**（加上已完成的前 302 docs，全局 1497/3027 = **49.5%**）

### GPU 利用率

| GPU | 利用率 | 显存占用 |
|-----|--------|----------|
| 0 | 57% | 17.9/32.6 GB |
| 1 | 62% | 15.7/32.6 GB |
| 2 | 62% | 19.4/32.6 GB |
| 3 | 49% | 18.3/32.6 GB |

### 质量指标（最近 100 docs batch）
- format_ok_rate: **100%**
- truncation_rate: **5.5~6.9%**
- mean_diversity: **7.6~7.7/8**

### 预计剩余时间
基于 tqdm 平均速度 ~15-18 s/doc：
- 瓶颈 shard（shard 3，419 docs remaining）≈ **2 小时**
- 预计全部完成：约 **UTC 13:00**（即从现在起 ~2h）

### 异常
无 OOM、无报错、无卡死。一切正常。

---
