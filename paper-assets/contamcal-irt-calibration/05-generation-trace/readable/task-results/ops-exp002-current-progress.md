# ops exp002 current progress

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_exp002-current-progress_20260514T114152_result.json`
- **Structured JSON:** [`308dc7bcd366ed7eea6b.json`](../../sessions/30/308dc7bcd366ed7eea6b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp-002 Signal Pipeline 进度报告

### 当前状态：Task 1/9，selfcritique 阶段

**活跃进程** (PID 353390, 已运行 56 分钟):
```
compute_signals.py --benchmark mmlu --model Qwen2.5-0.5B_d000_s42
  signals: embedding, minkpp, selfcritique
  GPU 0: 2141 MiB / 24564 MiB
```

### 已产出信号文件

**d000_s42 目录** (5 个文件):
| 文件 | 大小 | 时间 | 来源 |
|------|------|------|------|
| `signal_embedding_gsm8k.json` | 556KB | 18:38 | 先前运行 |
| `signal_embedding_arc_challenge.json` | 504KB | 18:41 | 先前运行 |
| `signal_embedding_mmlu.json` | 5.8MB | 18:50 | 当前运行 |
| `signal_minkpp_mmlu.json` | 2.0MB | 18:55 | 当前运行 |
| `signal_embedding_mmlu_*.json` | 2KB | 16:00 | 测试/旧文件 |

**d005_s42 目录** (1 个文件):
| 文件 | 大小 | 时间 |
|------|------|------|
| `signal_embedding_mmlu.json` | 5.8MB | 18:45 | 先前运行 |

**d100_s42 目录**: 不存在

### 关键发现

- **selfcritique**: 无任何 `signal_selfcritique_*.json` 文件产出。当前正在计算 d000/mmlu 的 selfcritique，已耗时 ~47 分钟（embedding 4min, minkpp 5min 后开始）。MMLU ~14K items，selfcritique 逐条生成，极慢。
- **constat**: 无任何 `signal_constat_*.json`。（本次运行的信号列表是 embedding/minkpp/selfcritique，不含 constat）
- **signals_merged**: 无。0 个 task 完成全部信号。
- **batch_report**: 只记录了之前 dry-run 的一次 FAIL (`d005/arc_challenge, rc=-15`)，非当前运行。

### 时间估算

| 阶段 | MMLU (~14K) | gsm8k (~1.3K) | arc (~1.1K) |
|------|-------------|---------------|-------------|
| embedding | ~4 min | ~2 min | ~2 min |
| minkpp | ~5 min | ~1 min | ~1 min |
| selfcritique | **~60+ min** (进行中) | ~5 min | ~4 min |

每个 dosage 3 个 benchmark, 共 3 个 dosage = 9 tasks:
- 3 个 MMLU task: ~70 min × 3 = **210 min**
- 6 个非 MMLU task: ~10 min × 6 = **60 min**
- **总计 ~270 min (4.5 小时)**

已用 ~56 min，当前 task 1/9 还未完成。**预计剩余 ~3.5-4 小时**。

selfcritique 对 MMLU 的处理是瓶颈，占总时间 ~78%。

---
