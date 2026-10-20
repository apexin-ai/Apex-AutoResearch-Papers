# check binoculars scoring status

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_binoculars_scoring_status_20260518T134240_result.json`
- **Structured JSON:** [`57202c21b57c3cffeba5.json`](../../sessions/57/57202c21b57c3cffeba5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### Binoculars Scoring: 不存在
westd-41312 上**没有任何 Binoculars 相关的代码、进程或输出文件**。Binoculars scoring 可能是在其他服务器上运行的，或者任务描述有误。

### 当前实际运行的 Scoring: GPT-2 Perplexity (进行中)
- **脚本**: `scoring/score_gpt2_ppl.py` (GPU 1)
- **进度**: 310,015 / 371,499 (**83.5%**)
- **速度**: 31.9 samples/s
- **ETA**: ~32 分钟
- **输出文件**: `data/scored_data_gpt2ppl.jsonl` (当前 311,771 行)

### GPU 状态 (4× RTX PRO 6000 Blackwell, 98GB)
| GPU | 利用率 | 显存 | 任务 |
|-----|--------|------|------|
| 0 | 0% | 0 MiB | 空闲 (eval_perplexity.py 在队列中) |
| 1 | 66% | 29 GB | `score_gpt2_ppl.py` |
| 2 | 100% | 62 GB | `pretrain_weighted.py` (adaptive, Qwen3-1.7B) |
| 3 | 100% | 62 GB | `pretrain_weighted.py` (uniform, Qwen3-1.7B) |

**4 张 GPU 中只有 GPU 0 空闲**，其余 3 张都在跑任务。

---
