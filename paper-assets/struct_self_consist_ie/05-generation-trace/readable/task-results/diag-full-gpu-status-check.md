# diag full gpu status check

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_full_gpu_status_check_20260518T114435_result.json`
- **Structured JSON:** [`9f0f69cad9185024c7d0.json`](../../sessions/9f/9f0f69cad9185024c7d0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据已收集。汇总如下：

---

## LLaMA Few-NERD 训练 v2
- **状态**: RUNNING
- **GPU**: cuda:1 (30888MiB, 43% util)
- **进度**: 14% (3499/24708 steps), 已运行 ~2h13m
- **Checkpoints**: checkpoint-1000, checkpoint-2000, checkpoint-3000
- **速度**: ~1.7-3.5 s/it
- **预计剩余**: ~21200 steps × ~1.8s ≈ **~10.6 小时**
- **输出**: `checkpoints/llama3.1-8b-fewnerd-lora/`, 无 trainer_state.json（训练中）

## Qwen Few-NERD seed=123 推理
- **状态**: COMPLETED (May 18 18:50:58)
- **GPU**: 已释放 (cuda:0 空闲)
- **关键结果**: 按类型 F1 — person 0.817, org 0.751, other 0.674, building 0.749, product 0.681, event 0.713, art 0.798
- **输出文件**: `output/exp_021_fewnerd_n8_seed123/samples.jsonl` — 37648 行
- **注意**: `results.json` 为空 `{}`，`full_signal_analysis.json` 未生成 — **分析脚本未运行**

## Qwen Few-NERD seed=456 推理
- **状态**: RUNNING (88% — 33240/37648)
- **GPU**: cuda:2 (30934MiB, 94% util, VLLM EngineCore)
- **速度**: ~30 prompts/s
- **预计剩余**: ~4400 prompts ÷ 30/s ≈ **~2.5 分钟**
- **输出**: 尚无 samples.jsonl（推理完成后才写入）

## Hidden State Probe — SciERC (exp_012)
- **状态**: COMPLETED
- **输出**: `output/hidden_state_probe/results_textbased_goldfiltered.json`

## Hidden State Probe — Few-NERD
- **状态**: COMPLETED
- **关键结果**:
  - MLP probe: rho=0.629, sel_f1=0.763, gap_closure=11.7%
  - Linear probe: rho=0.268, sel_f1=0.676, gap_closure=-57.9%
  - LP baseline: rho=0.606, sel_f1=0.764, gap_closure=12.3%
- **输出**: `output/hidden_state_probe_fewnerd/results_goldfiltered.json`

## Hidden State Probe — exp016
- **状态**: RUNNING (PID 969983, `hidden_state_probe_exp016.py`)
- **GPU**: 无 GPU 占用（CPU 运行中, 7151% CPU = 多核）
- **已有**: hidden_states.pt, labels.pt, logprobs.pt, metadata.json
- **缺失**: 无 results*.json — probe 训练仍在进行

## Token-level LP Aggregator
- **状态**: COMPLETED (3 个变体)
- **关键结果**:
  - Few-NERD: mean_lp rho=0.604, CNN rho=0.642, sel_f1=0.765
  - SciERC 10epoch: mean_lp rho=0.158, CNN rho=0.173
  - SciERC 3epoch: mean_lp rho=0.354, CNN rho=0.387
- **输出**: `output/token_lp_aggregator/`

## CoNLL 3-seed 数据
- **seed=123**: COMPLETED — 3453 行, full_signal_analysis.json 存在
- **seed=456**: COMPLETED — 3453 行, full_signal_analysis.json 存在

---

## GPU 状态总结

| GPU | 状态 | 内存 | Util | 进程 |
|-----|------|------|------|------|
| cuda:0 | **空闲** | 4MiB/32607MiB | 0% | — |
| cuda:1 | **占用** | 30888MiB/32607MiB | 43% | LLaMA Few-NERD 训练 (14%, ~10.6h 剩余) |
| cuda:2 | **占用** | 30934MiB/32607MiB | 94% | Qwen seed=456 推理 (88%, ~2.5min 剩余) |
| cuda:3 | **空闲** | 2MiB/32607MiB | 0% | — |

**空闲 GPU: 2 张** (cuda:0, cuda:3)

**需要注意**:
1. seed=123 推理已完成但 **分析未运行** (results.json 为空, 无 full_signal_analysis.json)
2. seed=456 即将完成（~2.5min），完成后 cuda:2 也将释放 → **3 张空闲**
3. exp016 probe 在 CPU 上运行，不占 GPU
4. 有残留 tmux session `exp_001_n16_seed456` (May 15) 和 `exp_011`/`exp_017` 系列可能已过时

---
