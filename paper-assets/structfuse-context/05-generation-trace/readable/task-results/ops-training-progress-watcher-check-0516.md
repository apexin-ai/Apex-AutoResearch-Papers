# ops training progress watcher check 0516

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_training-progress-watcher-check-0516_20260515T164937_result.json`
- **Structured JSON:** [`0532b9730ba9951c16c1.json`](../../sessions/05/0532b9730ba9951c16c1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。汇总如下：

---

## 状态总结 (2026-05-16 01:00 CST)

### GPU
| GPU | 型号 | 利用率 | 显存 |
|-----|------|--------|------|
| 0 | RTX PRO 6000 Blackwell | 100% | 50/98 GiB |
| 1 | RTX PRO 6000 Blackwell | 100% | 55/98 GiB |

### Qwen 链 (cuda:0, PID 337267) — 正在跑 5/7

**当前**: dataflow_aware_s43, step 200

| subrun | best val_loss (step) | best R@1 (step) | early stop |
|--------|---------------------|-----------------|------------|
| random_s43 | 0.4476 (@500) | 0.5554 (@1500) | @1500 |
| random_s44 | 0.4252 (@500) | 0.6009 (@500) | @1500 |
| embed_dist_s43 | 0.4541 (@500) | 0.5606 (@1500) | @1500 |
| embed_dist_s44 | 0.4341 (@1000) | 0.5942 (@500) | @2000 |

剩余: dataflow_aware_s44, bm25_s42。**ETA ~May 16 14:00-18:00 CST**

### StarCoder 链 (cuda:1, PID 519791) — 2/9 完成，第 3 个即将开始

**当前**: random_s44 的 python 进程 (PID 913995, 8h23m) 在 early stop@1500 后做 final eval/save，尚未退出。bm25_s42 待启动。

| subrun | best val_loss (step) | best R@1 (step) | early stop |
|--------|---------------------|-----------------|------------|
| random_s43 | 0.5239 (@1500) | 0.4912 (@1500) | @2500 |
| random_s44 | 0.5913 (@500) | 0.4871 (@1500) | @1500 |

剩余 7 个 subrun。**ETA ~May 19-20 CST**

### Watcher 活性
- **PID 966920** (Qwen s42 supplement): 存活 (1d 1h)
- **PID 20226** (StarCoder s42 supplement): 存活 (51m)

### 关键观察
- Qwen 链未完成，watcher 966920 仍在等待。Qwen 预计今天下午完成，届时 watcher 应自动触发 s42 supplement (embed_s42 + dataflow_s42 + bm25_s42)
- StarCoder random_s44 进程 early stop 后仍在运行（8h+），可能在做较慢的 final eval/model save，**暂不需要干预但值得关注**——如果下次检查该进程仍未退出则需排查
- Qwen R@1 (~0.55-0.60) 显著优于 StarCoder (~0.49)，符合预期

---
