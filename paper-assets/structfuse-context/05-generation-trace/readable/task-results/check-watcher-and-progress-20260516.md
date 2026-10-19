# check watcher and progress 20260516

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_watcher_and_progress_20260516_20260516T062647_result.json`
- **Structured JSON:** [`19280bcc2c44c1dfa512.json`](../../sessions/19/19280bcc2c44c1dfa512.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇报

### 1. Watcher PID 966920: ✅ ALIVE

| 字段 | 值 |
|------|-----|
| 状态 | `Ss+` (sleeping, session leader) |
| 运行时间 | 1d 14h 53min |
| 命令 | `bash /root/structfuse/watch_and_chain_qwen_s42.sh` |
| 行为 | 每 5 分钟 poll Qwen PID 337267，主链完成后自动触发 `run_m2_s42_supplement.sh`（embed_s42 + dataflow_s42 on cuda:0）|

**无需手动处理。**

---

### 2. Qwen (cuda:0, PID 337267)

| 字段 | 值 |
|------|-----|
| 进程状态 | `S+`，运行 1d 19h 3min |
| 当前 subrun | **dataflow_aware_s44**（第 6/7 个） |
| 进度 | step 600/1408（epoch 1，43%）|
| 最新 loss | 0.1119 @ step 600 |
| eval@500 | val_loss=0.4944, R@1=0.5701, R@5=0.9382 |
| 已完成 | random_s43, random_s44, embedding_distance_s43, embedding_distance_s44, dataflow_aware_s43 |
| 剩余 | 当前 run 完成 + bm25_s42（最后 1 个）|
| ETA | ~12-16h（主链完成） → 之后 watcher 自动触发 s42 supplement |

---

### 3. StarCoder (cuda:1, PID 519791)

| 字段 | 值 |
|------|-----|
| 进程状态 | `Ss+`，运行 1d 12h 24min |
| 脚本 | `run_m2_full_starcoder_resume.sh`（9 runs 总）|
| 当前 subrun | **embedding_distance_s43**（第 5/9 个）|
| 进度 | step 500/1405（epoch 1，36%）|
| 最新 loss | 0.5415 @ step 500 |
| eval@500 | val_loss=0.5229, R@1=0.4810, R@5=0.9535 |
| 已完成 | random_s43, random_s44, bm25_s42, embedding_distance_s42（4/9）|
| 剩余 | 当前 run 完成 + embedding_distance_s44 + dataflow_aware_s42/s43/s44（4 个）|
| ETA | ~38-42h（每 run ~8.5h）|

---

### 4. GPU 利用率

| GPU | 利用率 | VRAM |
|-----|--------|------|
| cuda:0 (Qwen) | 100% | 64.4 / 97.9 GB |
| cuda:1 (StarCoder) | 100% | 71.6 / 97.9 GB |

---

### 5. 风险评估

无风险。Watcher 存活，两条链正常推进。Qwen 主链预计 ~12-16h 完成后 watcher 会自动触发 supplement chain，embed_s42 不会被遗漏。

---
