# verify benign file check

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_benign-file-check_20260517T141521_result.json`
- **Structured JSON:** [`9a9a5525e95a0b2f1dda.json`](../../sessions/9a/9a9a5525e95a0b2f1dda.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

| 项目 | 状态 |
|------|------|
| **benign_topic_matched.jsonl** | 存在，230 条，528KB，最后修改 May 17 22:14 |
| **crescendo_all.jsonl** | 存在，250 条 |
| **数据格式** | 正常 — 含 conversation_id, label, attack_type, topic, source, turns 字段 |
| **Sanity check** | 有 3 个 log 版本（v1/v2/v3），v3 log 包含 TF-IDF 特征分析结果，运行已完成 |
| **GPU (0-3)** | 全部空闲，0% 利用率，0 MiB 显存占用 |
| **运行进程** | 无 python/generate/sanity 相关进程在跑 |

Benign 数据已生成完毕（230 条 topic-matched），sanity check 也已跑完（TF-IDF 特征看起来合理：benign 偏向日常对话词如 "oh", "like", "cool"；crescendo 偏向 "her", "researcher" 等）。服务器当前空闲。

---
