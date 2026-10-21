# ssh westb checkpoint scan

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_westb_checkpoint_scan_20260521T013838_result.json`
- **Structured JSON:** [`c1cf2ebba3a6d9504df5.json`](../../sessions/c1/c1cf2ebba3a6d9504df5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总如下：

---

## westb-23072 资源清单

### GPU
| GPU | 型号 | 显存 | 利用率 |
|-----|------|------|--------|
| cuda:0 | NVIDIA RTX PRO 6000 Blackwell | 96 GB | 0% (空闲) |
| cuda:1 | NVIDIA RTX PRO 6000 Blackwell | 96 GB | 0% (空闲) |

### 磁盘
| 分区 | 总量 | 已用 | 可用 | 使用率 |
|------|------|------|------|--------|
| /root/autodl-tmp (数据盘) | 250G | 227G | 24G | 91% |
| / (根分区) | 30G | 7.9G | 23G | 27% |

### Checkpoint 列表

**Dense 基线模型：**
- `models/DeepSeek-R1-Distill-Qwen-1.5B/` — 3.4G

**7B 系列 (pruned → SFT → GRPO)：**

| 目录 | 阶段 | 大小 |
|------|------|------|
| `pruned_standard_25/` | pruned | 11G |
| `pruned_standard_20/` | pruned | 12G |
| `pruned_cka_only_20/` | pruned | 12G |
| `pruned_rasp_20/` | pruned | 12G |
| `pruned_rasp_rlvr_20/` | pruned | 12G |
| `pruned_cka_only_20_qwen_math/` | pruned | 12G |
| `pruned_standard_20_qwen_math/` | pruned | 12G |
| `sft_standard_25/` (checkpoint-1870) | SFT | 11G |
| `sft_cka_only_20/` | SFT | 12G |
| `sft_rasp_rlvr_20/` (checkpoint-1870) | SFT | 12G |
| `sft_qwen_math_cka_only_20/` (checkpoint-935) | SFT | 12G |
| `sft_qwen_math_cka_only_20_final/` | SFT | 12G |
| `sft_standard_20_qwen_math/` (checkpoint-935) | SFT | 12G |
| `sft_standard_20_qwen_math_final/` | SFT | 12G |
| `grpo_cka_only_20/` (checkpoint-100) | GRPO | 12G |
| `grpo_cka_only_20_seed123/` | GRPO | 12G |
| `grpo_random_20/` | GRPO | 220K (几乎为空) |

**1.5B 系列：**

| 目录 | 阶段 | 大小 |
|------|------|------|
| `pruned_standard_20_1p5b/` | pruned | 2.8G |
| `pruned_cka_only_20_1p5b/` | pruned | 2.8G |
| `pruned_rasp_20_1p5b/` | pruned | 2.8G |
| `sft_standard_20_1p5b/` | SFT | 2.8G |
| `sft_cka_only_20_1p5b/` | SFT | 2.8G |
| `sft_rasp_20_1p5b/` | SFT | 2.8G |
| `grpo_cka_only_20_1p5b/` (checkpoint-100) | GRPO | 2.8G |
| `grpo_standard_20_1p5b/` | GRPO | 2.8G |
| `grpo_rasp_20_1p5b/` (checkpoint-100) | GRPO | 2.8G |

### 缓存数据集
- **HF Hub**: `DeepSeek-R1-Distill-Qwen-1.5B`, `DeepSeek-R1-Distill-Qwen-7B`, `gsm8k`
- **本地 datasets cache**: `gsm8k`, `math-500`, `mbpp`, `openai_humaneval`, `parquet`

GSM8K / MBPP / HumanEval / MATH-500 均已缓存，无需重新下载。

### 已有 Eval 结果
results/ 目录下有 ~80+ 个结果文件，覆盖：
- GSM8K: dense/pruned/sft/grpo 各变体 (standard/cka_only/rasp, 7B+1.5B, 含 seed 实验)
- HumanEval: sft_rasp_20_1p5b, grpo_standard_20_1p5b
- MBPP: sft_cka_only_20_1p5b, sft_standard_20_1p5b
- CKA heatmap: 4个剪枝方法 (cka_only/random/rasp/standard)
- Gradient flow: v3
- Inference benchmark: cka_only
- Bootstrap CI, RCI diversity correlation
- Qwen-Math 变体: postprune + SFT eval

### 建议：可在 westb 上跑的 pending eval

两张 96GB GPU 均空闲，适合跑：
1. **缺失的 HumanEval/MBPP eval** — 7B 系列的 GRPO 和 SFT 变体大多只有 GSM8K 结果，HumanEval/MBPP 覆盖很少
2. **grpo_random_20 几乎为空** (220K)，可能训练失败需排查
3. **Qwen-Math 系列的 GRPO** — 只有 pruned + SFT，没有 GRPO checkpoint
4. **数据盘 91%** — 只剩 24G，跑新实验前可能需要清理旧的中间 checkpoint

---
