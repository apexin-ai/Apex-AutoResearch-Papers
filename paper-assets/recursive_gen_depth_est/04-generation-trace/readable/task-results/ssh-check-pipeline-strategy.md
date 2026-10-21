# ssh check pipeline strategy

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_pipeline_strategy_20260514T171230_result.json`
- **Structured JSON:** [`bc486cd14f661c4afcb1.json`](../../sessions/bc/bc486cd14f661c4afcb1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Now I have all the information needed. Here are the results for both tasks:

---

## Task 1: Pipeline 解码策略支持情况

### 1. `generate_next_depth.py` 参数支持

**已完整支持。** 脚本已有以下参数：
- `--decoding_strategy`: choices=`["nucleus", "topk", "temp_only"]`，默认 `nucleus`
- `--temperature`: 默认 1.0
- `--top_p`: 默认 0.95
- `--top_k`: 默认 50

生成逻辑按策略分支正确设置 `gen_kwargs`：
- `nucleus` → `top_p` + `temperature`
- `topk` → `top_k` + `temperature`
- `temp_only` → 仅 `temperature`

### 2. OLMo / GPT-2 XL pipeline 脚本

**两个脚本都硬编码了 nucleus（默认策略）**，`generate_next_depth.py` 调用中没有传 `--decoding_strategy` / `--temperature` / `--top_k` 参数，全部走默认值（nucleus, p=0.95, t=1.0）。

对比 Pythia 的 temp09/topk50 脚本，后者明确传了 `--decoding_strategy temp_only --temperature 0.9` 和 `--decoding_strategy topk --top_k 50`。

### 3. 需要修改的内容

为 OLMo 和 GPT-2 XL 各创建 2 个新脚本（temp09 + topk50），仿照 Pythia 的模式：

| 新脚本 | 基于 | 需加参数 | DATA_DIR / CKPT_DIR |
|--------|------|----------|---------------------|
| `run_pipeline_olmo_temp09.sh` | `run_pipeline_olmo.sh` | `--decoding_strategy temp_only --temperature 0.9` | `data/olmo_temp09`, `checkpoints/olmo_temp09` |
| `run_pipeline_olmo_topk50.sh` | `run_pipeline_olmo.sh` | `--decoding_strategy topk --top_k 50` | `data/olmo_topk50`, `checkpoints/olmo_topk50` |
| `run_pipeline_gpt2xl_temp09.sh` | `run_pipeline_gpt2xl.sh` | `--decoding_strategy temp_only --temperature 0.9` | `data/gpt2xl_temp09`, `checkpoints/gpt2xl_temp09` |
| `run_pipeline_gpt2xl_topk50.sh` | `run_pipeline_gpt2xl.sh` | `--decoding_strategy topk --top_k 50` | `data/gpt2xl_topk50`, `checkpoints/gpt2xl_topk50` |

每个 `generate_next_depth.py` 调用处（Step 2/4/6）加对应参数，同时加 log 重定向和时间戳（参考 Pythia 脚本格式）。

### 4. 预估时长

基于 Pythia temp09 pipeline 完成记录（22:51 → 00:29，约 **97 分钟**）：
- 3 次 LoRA finetune: ~269s × 3 ≈ 13.5 min
- 3 次 generate: 剩余 ~83.5 min，即每次 generate ~28 min
- **Pythia pipeline: ~1.5h/run**

OLMo-1B（参数更少）预估略快，**~1-1.5h/run**。GPT-2 XL（1.5B）正在跑的 finetuning 约 11.5min/epoch（939 steps @ 1.35 it/s），3 epoch ~35min，generate 可能更长，**预估 ~2-2.5h/run**。

**注意**: GPT-2 XL 的 nucleus pipeline 当前正在运行中（67% step 2 finetuning）。

---

## Task 2: DivEye 引用验证

**"Basani & Chen" 是真实作者，但发表地不是 ICLR 2026。**

- **真实引用**: Advik Raj Basani & Pin-Yu Chen (IBM Research), "Diversity Boosts AI-Generated Text Detection", **TMLR (Transactions on Machine Learning Research), February 2026**
- arXiv: [2509.18880](https://arxiv.org/abs/2509.18880)
- GitHub: [IBM/diveye](https://github.com/IBM/diveye)（标注 `[TMLR '26]`）
- 方法确实是 diversity-based statistical features（surprisal variance、entropy 等零样本检测）
- 另有 workshop 版本: DivEye at PAN 2025 (CLEF/CEUR-WS)

**需修正**: 将 baselines.py 中的引用从 "ICLR 2026" 改为 "TMLR 2026"，完整引用：
> Basani, A. R. & Chen, P.-Y. (2026). Diversity Boosts AI-Generated Text Detection. *Transactions on Machine Learning Research (TMLR)*.

---
