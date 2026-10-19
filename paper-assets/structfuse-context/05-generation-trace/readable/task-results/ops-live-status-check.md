# ops live status check

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_live-status-check_20260516T023311_result.json`
- **Structured JSON:** [`e665240ecbf914b9f9f7.json`](../../sessions/e6/e665240ecbf914b9f9f7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## bjb1-42106 状态报告 (2026-05-16 ~10:40 UTC+8)

### GPU 状态
| GPU | Util | VRAM | 进程 |
|-----|------|------|------|
| 0 | 99% | 51.0 / 95.6 GB | PID 18427 (Qwen dataflow_aware_s43) |
| 1 | 100% | 53.5 / 95.6 GB | PID 129747 (StarCoder embed_s43) |

---

### 1. Qwen 训练 (cuda:0) — dataflow_aware_s43

**状态：Early stopped @ step 1500**

| Eval | val_loss | R@1 | R@5 | R@10 |
|------|----------|-----|-----|------|
| @500 | **0.4617** | 0.5495 | 0.9728 | 1.0 |
| @1000 | 0.4984 | 0.5174 | 0.9581 | 1.0 |
| @1500 | 0.5186 | **0.5541** | 0.9564 | 1.0 |

- Best val_loss = 0.4617 @ step 500
- Best R@1 = 0.5541 @ step 1500（已保存 checkpoint）
- PID 337267 (wrapper): **ALIVE**, 1d 15h — 下一个 subrun: **dataflow_aware_s44**，之后 bm25_s42
- PID 18427 (train): **ALIVE**, 10h41m — 刚完成 early stop，等 wrapper 启动下一个

已完成的 Qwen subruns: random_s42, random_s43, random_s44, embedding_distance_s43, embedding_distance_s44, dataflow_aware_s43 (6/7)

---

### 2. StarCoder 训练 (cuda:1)

**embed_s42 — 已完成（3 epochs full run, 无 early stop）**

| Eval | val_loss | R@1 | R@5 | R@10 |
|------|----------|-----|-----|------|
| @500 | **0.6154** | **0.4372** | **0.9094** | 1.0 |
| @1000 | 0.6466 | 0.4567 | 0.9128 | 1.0 |
| @1500 | 0.6835 | 0.4473 | 0.8973 | 1.0 |
| Final | 0.6926 | 0.4376 | 0.8977 | 1.0 |

Best checkpoint (by val_loss & R@1) 都在 @500。

**embed_s43 — 刚启动，step 100**
- PID 129747: **ALIVE**, 28min
- step 100, loss=0.9788, lr=7.05e-06
- Checkpoint 目录已创建但为空
- PID 519791 (wrapper): **ALIVE**, 1d 8h30m

---

### 3. SWE-bench eval (random_s42_100)

**已完成** @ 2026-05-16 10:30:36

| Metric | Value |
|--------|-------|
| R@1 | 0.04 |
| R@5 | 0.11 |
| R@10 | 0.14 |
| R@20 | 0.16 |
| MRR | 0.0698 |
| Gold coverage | 1.0 |

100/100 instances, 0 errors。PID 61328/61320: **DEAD**（正常退出）。

---

### 4. Watcher PID 966920

**ALIVE**, 1d 11h
- CMD: `bash /root/structfuse/watch_and_chain_qwen_s42.sh`
- 每 5min 轮询 Qwen wrapper (PID 337267)，等其完成后触发 s42 supplement（embedding_distance_s42 + dataflow_aware_s42）

---

### 5. m1_reextract_v2

**卡死在 getmoto__moto**。CodeQL `call_graph.ql` 对 moto 仓库持续返回 exit code 33，每 5 分钟重试一次，已积累 329 次失败（从 2026-05-15 09:47 至今超 24 小时）。536 个 moto instance 全部 pending。

其他 repo 的提取已完成，`/root/autodl-tmp/structfuse/full_m1_data/` 下有大量 json 产出（输出截断，数量极大）。进程可能仍在运行（无显式 PID 可查，日志 10:35 还在更新）。

---
