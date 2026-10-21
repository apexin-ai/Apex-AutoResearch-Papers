# ops download training monitor

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_download-training-monitor_20260518T162108_result.json`
- **Structured JSON:** [`c44830282a63a15f8c3e.json`](../../sessions/c4/c44830282a63a15f8c3e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总如下：

---

## GPU 状态 (4x RTX PRO 6000, 96GB)

| GPU | PID | 显存占用 | GPU Util | 温度 |
|-----|------|---------|----------|------|
| 0 | 36665 | 61.9/97.9 GB | 65% | 68°C |
| 1 | 34011 | 80.0/97.9 GB | 87% | 69°C |
| 2 | 38920 | 63.6/97.9 GB | 79% | 65°C |
| 3 | 36943 | 62.2/97.9 GB | 90% | 54°C |

4 卡全部在跑，正常。

---

## 训练进度

| GPU | 任务 | 进度 | Loss | Token Acc | ETA |
|-----|------|------|------|-----------|-----|
| 0 | 7B d100 s42 | **1880/4159 (45%)** | 0.993 | 0.761 | ~1h04m |
| 1 | 7B d050 s42 | **3547/3642 (97%)** | 0.886 | 0.781 | **~3min，即将完成** |
| 2 | 14B d005 s42 | **386/3177 (12%)** | 0.907 | 0.779 | ~2h20m |
| 3 | 7B d005 s123 | **1427/3177 (45%)** | 0.889 | 0.787 | ~58min |

GPU 1 的 d050 训练马上结束。

---

## 模型下载

| 模型 | 实际路径 | 已下载 shard | 预期 shard | 大小 | 状态 |
|------|---------|-------------|-----------|------|------|
| **Phi-4** | `phi-4/` | 4/6 (00001-00003, 00006) | 6 | ~19G/~28G | **进行中** — PID 19608 存活，log 显示 13/21 files (62%)，速度慢 |
| **OLMo-2** | `OLMo-2-1124-7B/` | 4/6 (00001,00002,00005,00006) | 6 | ~18.3G/~28G | **卡住** — 无活跃进程，log 显示 model-00003 下载超时后进程退出 |
| **Gemma-2-9B** | `gemma-2-9b/` | 6/8 (00001-00003,00005,00007,00008) | 8 | ~25.7G/~36G | **卡住** — 无活跃进程，log 显示 model-00004 下载超时后进程退出 |

**OLMo-2 和 Gemma-2 下载均因 xet-bridge read timeout 导致进程退出，需要手动重启下载。** Phi-4 虽然还活着但速度很慢（最后一个 shard 花了 4+ 小时）。

---

## 磁盘

`/root/autodl-tmp`: 126G/250G (51%), 剩余 125G — 空间充足。

---
