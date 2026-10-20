# ops westd progress correct

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd-progress-correct_20260519T210911_result.json`
- **Structured JSON:** [`6840b8c3cbf04189d92c.json`](../../sessions/68/6840b8c3cbf04189d92c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据已收集。汇总如下：

## westd-29999 训练进度（~05:10 CST, May 20）

### GPU 利用率
| GPU | 型号 | 利用率 | 显存 |
|-----|------|--------|------|
| 0 | RTX PRO 6000 96GB | 93% | 57.4/97.9 GB |
| 1 | RTX PRO 6000 96GB | 92% | 64.4/97.9 GB |
| 2 | RTX PRO 6000 96GB | 83% | 62.7/97.9 GB |
| 3 | RTX PRO 6000 96GB | 81% | 54.6/97.9 GB |

### 各 Family 完成情况

| Family | 已完成 (s123) | 当前训练 | 进度 | 剩余 |
|--------|--------------|----------|------|------|
| **Qwen2.5-7B** | d000, d005, d025, d050, d100 | — | **全部完成** | — |
| **Phi-4** (GPU 0) | d000, d005, d025 | **d050** | 1508/3642 (41%), ~1h22m 剩余 | d100 |
| **Qwen2.5-14B** (GPU 1) | d000, d005 | **d025** | 2341/3384 (69%), ~50m 剩余 | d050, d100 |
| **OLMo-2-7B** (GPU 2) | d000, d005, d025, d050 | **d100** | 810/4159 (19%), ~1h46m 剩余 | — |
| **Gemma-2-9B** (GPU 3) | d000, d005 | **d025** | 2806/3384 (83%), ~27m 剩余 | d050, d100 |

### 预估全部完成时间（CST May 20）

| Family | 当前完成 | 还差几个 dosage | 预估全部完成 |
|--------|---------|----------------|-------------|
| Qwen2.5-7B | 5/5 | 0 | **已完成** |
| OLMo-2-7B | 4/5 → d100 在跑 | 0 (最后一个在跑) | **~07:00** |
| Phi-4 | 3/5 → d050 在跑 | 1 (d100 ~2h40m) | **~09:15** |
| Gemma-2-9B | 2/5 → d025 在跑 | 2 (d050 ~3h, d100 ~3h20m) | **~12:00** |
| Qwen2.5-14B | 2/5 → d025 在跑 | 2 (d050 ~3h, d100 ~3h30m) | **~12:30** |

所有 family seed=123 训练预计 **May 20 ~12:30 CST** 全部完成。Qwen2.5-14B 是最慢的 bottleneck。

---
