# ops restart 14b t10a050 cuda0

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_restart-14b-t10a050-cuda0_20260522T112359_result.json`
- **Structured JSON:** [`3acb90bf48c880d4af33.json`](../../sessions/3a/3acb90bf48c880d4af33.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**cuda:0 不可用** — 正在运行 `t15_a060_s42_fp32_14b`（pythia-1.4b-deduped, PID 664582, 29GB）。

westd-17855 全部 6 块 GPU 均被占用：

| GPU | 显存占用 | 利用率 |
|-----|---------|--------|
| 0 | 29 GB | 87% |
| 1 | 29 GB | 99% |
| 2 | 33 GB | 89% |
| 3 | 33 GB | 88% |
| 4 | 14 GB | 94% |
| 5 | 17 GB | 91% |

gpt2-large 缓存路径需注意：实际存储在 `models--gpt2-large`（非 `models--openai-community--gpt2-large`），snapshot 存在（`32b71b...`）。

需要你决定：
1. 等某个实验完成后复用该 GPU
2. 换其他服务器（如 westd-19828）
3. 其他安排

---
