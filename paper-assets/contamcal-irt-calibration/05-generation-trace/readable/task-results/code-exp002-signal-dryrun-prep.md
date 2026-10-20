# code exp002 signal dryrun prep

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp002-signal-dryrun-prep_20260514T075046_result.json`
- **Structured JSON:** [`6897866437b431b634b0.json`](../../sessions/68/6897866437b431b634b0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息收集完毕。以下是报告。

---

## exp-002 信号管线完整性检查报告

### 1. 信号脚本状态

| 信号 | 脚本 | 状态 | 核心函数 |
|------|------|------|---------|
| S1 Embedding | `signal_embedding.py` (7.8KB) | **已完成** | `compute_embedding_signal()`, `build_faiss_index()` |
| S2 Min-K%++ | `signal_minkpp.py` (9.6KB) | **已完成** | `compute_minkpp_signal()`, `minkpp_zscore_score()` |
| S3 ConStat | `signal_constat.py` (4.1KB) | **已完成** | `compute_constat_signal()` — 纯 eval 结果比较，不需要推理 |
| S4 Self-Critique | `signal_selfcritique.py` (9.1KB) | **已完成** | `compute_selfcritique_signal()`, `compute_yes_no_entropy()` |
| 主入口 | `compute_signals.py` (11.8KB) | **已完成** | `run_signal()`, `merge_signals()`, 完整 argparse，支持 `--dry-run` |
| 聚合 | `aggregate_rrf.py` (7.7KB) | **已完成** | RRF 排序融合 |
| Dry-run | `test_dryrun_v2.py` (3.9KB) | **已有** | 独立 dry-run 脚本，4 信号 + merge |

**结论：4 种信号脚本 + 主入口全部就绪，代码完整。**

### 2. 依赖状态

| 依赖 | 状态 |
|------|------|
| faiss-cpu 1.13.2 | **已装** |
| sentence-transformers | **已装** |
| peft | **已装** |
| torch | **已装** |
| transformers | **已装** |

**依赖全部就绪，无需额外安装。**

### 3. 数据/模型可用性

| 资源 | 路径 | 状态 |
|------|------|------|
| Base model (0.5B) | `/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B` | **可用** |
| d000 adapter (ref model) | `/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s42/lora_adapter/` | **可用** (adapter_config.json + safetensors) |
| d005 adapter | `/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d005_s42/lora_adapter/` | **可用** |
| d100 adapter | `/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s42/lora_adapter/` | **可用** |
| d000 eval results | `.../eval_results/Qwen2.5-0.5B_d000_s42/` | **可用** (3 files) |
| d005 eval results | `.../eval_results/Qwen2.5-0.5B_d005_s42/` | **可用** (3 files) |
| d100 eval results | `.../eval_results/Qwen2.5-0.5B_d100_s42/` | **可用** (3 files) |
| SFT 训练数据 | `/root/autodl-tmp/exp001/sft_data/sft_dosage_*.jsonl` | **可用** (d000/d005/d025/d050/d100) |
| Paraphrase 数据 | `/root/autodl-tmp/exp001/paraphrases/` | **可用** (mmlu/gsm8k/arc_challenge/humaneval JSON) |
| **Paraphrase eval 结果** | `Qwen2.5-0.5B_d000_s42_para/` | **空目录** — 只有 d000 有 para 目录且为空，d005/d100 无 para eval |

### 4. 问题和额外准备

**唯一阻塞项：ConStat (S3) 缺少 paraphrase eval 结果。**

ConStat 需要 `--original-eval-paths` 和 `--paraphrase-eval-paths` 参数（原始题和改写题的 eval_results.json）。当前只有原始题的 eval 结果，paraphrase eval 尚未运行。

**两个选项：**
- **Option A**: 先跑 S1/S2/S4 三个信号（不需要 paraphrase eval），ConStat 后补。`compute_signals.py` 已支持 `--signals` 选参数选择性运行。
- **Option B**: 先补跑 paraphrase eval（需要回 exp001 跑 paraphrase benchmark），然后一次跑全部 4 个信号。

### 5. Dry-run 命令建议

**3 信号 dry-run（跳过 ConStat）：**

```bash
cd /root/contamcal-irt-calibration/exp002
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base

CUDA_VISIBLE_DEVICES=0 python compute_signals.py \
  --model-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s42/lora_adapter/ \
  --ref-model-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s42/lora_adapter/ \
  --benchmark arc_challenge \
  --sft-data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_100.jsonl \
  --output-dir /root/autodl-tmp/exp002/signals/dry_run \
  --signals embedding minkpp selfcritique \
  --dry-run --max-items 5
```

**或直接用已有的 `test_dryrun_v2.py`**（CPU 模式，3 items，4 信号全测但 ConStat 用自身 eval 做 dummy 输入）：
```bash
cd /root/contamcal-irt-calibration/exp002
CUDA_VISIBLE_DEVICES="" python test_dryrun_v2.py
```

建议先跑 `test_dryrun_v2.py` 验证代码无运行时错误，再用 `compute_signals.py --dry-run` 在 GPU 上验证真实路径。

---
