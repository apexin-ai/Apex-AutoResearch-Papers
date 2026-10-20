# monitor rsft gen progress

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_rsft-gen-progress_20260515T023424_result.json`
- **Structured JSON:** [`3fca5ed70e211a5930ad.json`](../../sessions/3f/3fca5ed70e211a5930ad.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

每行输出包含 `generation_idx` (0-7)，即每个 doc 生成 8 行。实际 doc 完成数 = 行数 / 8。

## RSFT 生成进度汇总

| Shard | PID | 运行时间 | 已完成 docs | 应完成 | 完成% | 速率 (docs/min) | 剩余 ETA | GPU 利用率 | 显存占用 |
|-------|-----|---------|------------|--------|------|----------------|---------|-----------|---------|
| s0 | 135867 | 54:00 | 219 | 757 | 28.9% | 4.06 | ~2h 13m | 54% | 16.6/32.6 GB |
| s1 | 136270 | 53:23 | 231 | 757* | 30.5% | 4.33 | ~2h 02m | 57% | 15.2/32.6 GB |
| s2 | 136649 | 52:52 | 231 | 757 | 30.5% | 4.37 | ~2h 00m | 51% | 19.4/32.6 GB |
| s3 | 137985 | 44:47 | 175 | 757 | 23.1% | 3.91 | ~2h 29m | 58% | 18.3/32.6 GB |

**注意**：实际输出路径是 `/root/autodl-tmp/rsft_generations/shard_*/generations.jsonl`（不是 `rsft_output`）。

*s1 断点续传说明：当前文件只有 231 docs (1848 行)，少于之前提到的 302 docs。如果 302 docs 在别处保存且当前进程只处理剩余 455 docs，则 s1 实际完成 231/455 = 50.8%，ETA 约 52 分钟。

**全部输出格式正常**，每行解析正确，包含 doc_id、generation_idx、prompt、output、parsed_triples、gold_triples 等字段。

### 全部完成预计时间

瓶颈是 s3（启动最晚、完成最少），预计 **约 2.5 小时后** 全部 shard 完成。

---
