# code gpt2 medium prep

**The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_gpt2_medium_prep_20260513T184816_result.json`
- **Structured JSON:** [`a94c91a37040b7fa260f.json`](../../sessions/a9/a94c91a37040b7fa260f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部正常。以下是产出汇总：

---

### 1. 3 个脚本已写入服务器

| 脚本 | 方法 | 输出目录 |
|------|------|----------|
| `run_medium_uncurated.sh` | uncurated (100%) | `results_medium_uncurated/` |
| `run_medium_rgds.sh` | RGDS (50% embedding) | `results_medium_rgds/` |
| `run_medium_random50.sh` | random_50 (50%) | `results_medium_random50/` |

共同配置：`gpt2-medium`, seed=42, 8 代, 500K tokens/gen, lr=5e-5, epochs=3, bs=4, grad_accum=8, seq_len=512。用法：`bash run_medium_xxx.sh &lt;GPU_ID>`。

### 2. 显存 dry-run 结果

| batch_size | grad_accum | peak VRAM | 状态 |
|------------|------------|-----------|------|
| 4 | 8 | **11.4 GB** | OK |
| 2 | 16 | 8.7 GB | OK |
| 1 | 32 | 7.4 GB | OK |

**推荐配置：batch_size=4, grad_accum=8**（和 GPT2-125M 相同）。RTX PRO 6000 有 98GB 显存，11.4GB 毫无压力。脚本已按此配置写好，无需降 batch size。

### 3. gpt2-medium 缓存

已缓存在 `/root/.cache/huggingface/hub/models--gpt2-medium/`，355M 参数，TRANSFORMERS_OFFLINE=1 可直接加载。

### 4. 现有实验未受影响

- cuda:0: 79.9GB 占用（random_50 实验正常）
- cuda:1: 15.4GB 占用（seed456_methods 正常，dry-run 已清理完毕）
- 3 个 tmux session 均在线：`random_50_seed123`, `random_50_seed456`, `seed456_methods`

---
