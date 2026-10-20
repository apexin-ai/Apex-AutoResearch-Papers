# code exp ctrl contam mistral setup

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp-ctrl-contam-mistral-setup_20260521T042208_result.json`
- **Structured JSON:** [`2f89a0d391a332db3364.json`](../../sessions/2f/2f89a0d391a332db3364.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部就绪，4 个 GPU 都在工作：

| GPU | 用途 | 显存 | 利用率 |
|-----|------|------|--------|
| 0 | Mistral clean | 8.9 GB | 87% |
| 1 | Mistral contam_15 | 8.4 GB | 92% |
| 2 | (已有 post-rl SFT) | 8.7 GB | 82% |
| 3 | Mistral contam_50 | 7.8 GB | 97% |

Mistral-7B ctrl-contam 三组实验已全部启动并行训练：
- `exp-ctrl-contam-mistral-clean` → cuda:0
- `exp-ctrl-contam-mistral-contam15` → cuda:1  
- `exp-ctrl-contam-mistral-contam50` → cuda:3

模型通过 ModelScope 下载（跳过 consolidated.safetensors），symlink 解决了路径命名差异，dry-run 验证通过后提交。report_to 改为 "none"（wandb 未配置）。

---
