# infra westd41312 disk cleanup

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_westd41312_disk_cleanup_20260520T084753_result.json`
- **Structured JSON:** [`1a93d5372c800b0ccf83.json`](../../sessions/1a/1a93d5372c800b0ccf83.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 清理完成

| | 清理前 | 清理后 |
|---|---|---|
| **已用** | 250G (100%) | 75G (30%) |
| **可用** | 3.9M | **176G** |
| **output/models/** | 230G | 54G |

**释放：~175G**

### 删除清单

| 类别 | 目录 | 释放 |
|---|---|---|
| **1.7B中间checkpoint** (4个实验×3个) | adaptive_1_7b_seed{42,123}, uniform_1_7b_seed{123,resumed} 的 checkpoint-{5500,6000,6103,2500,3000,3051} | ~116G |
| **GPT2/detect中间checkpoint** (3个实验×3个) | gpt2_{uniform,adaptive}_seed42, detect_remove_q08_seed42 的 checkpoint-{5500,6000,6103} | ~30G |
| **ngram中间checkpoint** (2个实验) | ngram_{uniform,adaptive}_seed42 的 checkpoint-{5500,6000,6103} | ~7G |
| **失败实验** | uniform_1_7b_seed42 (旧版), uniform_1_7b_seed42_v4, adaptive_1_7b_seed42_v4 | ~11G |
| **小实验checkpoint** (11个) | 各实验的 checkpoint-6103 | ~12G |

### 保护确认
- 所有 39 个 success 实验的 final/ 目录完好
- 0 个 RUNNING 实验受影响
- eval 进程 (cuda:3) 未受影响
- 训练数据 (17G data/) 未动

### 重启 1.7B 训练
176G 可用空间远超需求（2个1.7B实验 × ~20G = ~40G 最低），可以直接重启。

---
