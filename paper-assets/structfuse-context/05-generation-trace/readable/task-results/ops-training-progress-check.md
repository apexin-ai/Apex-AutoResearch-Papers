# ops training progress check

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_training-progress-check_20260515T204124_result.json`
- **Structured JSON:** [`24805b46bfcf6e259613.json`](../../sessions/24/24805b46bfcf6e259613.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据采集完毕。汇总如下：

---

## 服务器状态

### GPU 利用率
| GPU | Utilization | Memory |
|-----|------------|--------|
| 0 (Qwen) | 100% | 74,175 / 97,887 MiB |
| 1 (StarCoder) | 100% | 54,767 / 97,887 MiB |

### 进程状态
| PID | Model | Uptime | Script |
|-----|-------|--------|--------|
| 337267 | Qwen (cuda:0) | 1d 09h 17m | `run_m2_full_qwen.sh` |
| 519791 | StarCoder (cuda:1) | 1d 02h 38m | `run_m2_full_starcoder_resume.sh` |

两个进程均存活，GPU 满载运行。

---

## 当前训练进度

### StarCoder embed_s42 (cuda:1) — step ~600/4242
- **eval@500 已出**: val_loss=**0.6154**, R@1=**0.4372**, R@5=0.9094
- 下次 eval@1000

### Qwen dataflow_s43 (cuda:0) — step ~900/2810
- **eval@500 已出**: val_loss=**0.4617**, R@1=**0.5495**, R@5=0.9728
- 下次 eval@1000

---

## 已完成 Subruns 汇总

### Qwen (m2_full_qwen)

| Subrun | Best val_loss (step) | Best R@1 (step) | Stop Step | Status |
|--------|---------------------|-----------------|-----------|--------|
| random_s42 | 0.4651 (1000) | 0.5527 (1000) | 4000 (full) | completed |
| random_s43 | 0.4476 (500) | 0.5554 (1500) | 1500 | early stopped |
| random_s44 | **0.4252** (500) | **0.6009** (500) | 1500 | early stopped |
| embed_dist_s43 | 0.4541 (500) | 0.5606 (1500) | 1500 | early stopped |
| embed_dist_s44 | 0.4341 (1000) | 0.5942 (500) | 2000 | early stopped |
| dataflow_s43 | 0.4617 (500) | 0.5495 (500) | — | **training** |

### StarCoder (m2_full_starcoder)

| Subrun | Best val_loss (step) | Best R@1 (step) | Stop Step | Status |
|--------|---------------------|-----------------|-----------|--------|
| random_s42 | 0.6134 (1000) | 0.4604 (2500) | 4000 (full) | completed |
| random_s43 | 0.5239 (1500) | 0.4912 (1500) | 2500 | early stopped |
| random_s44 | 0.5913 (500) | 0.4871 (1500) | 1500 | early stopped |
| embed_dist_s42 | 0.6154 (500) | 0.4372 (500) | — | **training** |

---

**要点**：
- Qwen 全面优于 StarCoder，最佳 R@1 达 0.6009 (random_s44) vs StarCoder 最佳 0.4912 (random_s43)
- Qwen dataflow_s43 首次 eval 的 R@1=0.5495 表现正常，在 random 策略的范围内，还需更多 eval 才能判断 dataflow 策略效果
- StarCoder embed_s42 首次 eval R@1=0.4372 偏低（对比 random_s43 的 0.4912），后续 eval 可能回升

---
