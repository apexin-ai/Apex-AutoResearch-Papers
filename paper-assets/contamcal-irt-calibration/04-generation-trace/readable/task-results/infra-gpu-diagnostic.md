# infra gpu diagnostic

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_gpu-diagnostic_20260516T171928_result.json`
- **Structured JSON:** [`6126c0481667aa49bc28.json`](../../sessions/61/6126c0481667aa49bc28.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。以下是完整状况：

## GPU 实际占用 (全部 6 张在用，无空闲)

| GPU | PID | VRAM | Util | 实验 | Registry |
|-----|-----|------|------|------|----------|
| cuda:0 | 804570 | 16252MiB | 98% | Llama-3.2-3B d005 s42 SFT | ✓ `exp_001_sft_llama32_3B_d005_s42` (tmux parent 804565) |
| cuda:1 | 807025 | 6904MiB | 80% | Llama-3.2-3B d000 s42 eval v3 | ✓ `exp_001_eval_llama32_3B_d000_s42_v3` |
| cuda:2 | 815287 | 586MiB | 0% | **1.5B-Instruct GSM8K signals** | ⚠️ `exp_002_signals_15B_instruct_gsm8k` — 缺 gpu/pid 字段 |
| cuda:3 | 801766 | 17848MiB | 100% | Llama-3.2-3B d025 s42 SFT | ✓ `exp_001_sft_llama32_3B_d025_s42` (tmux parent 801761) |
| cuda:4 | 810809 | 3552MiB | 45% | **1.5B-Instruct MMLU signals** | ❌ **无 registry 条目** |
| cuda:5 | 804791 | 20580MiB | 86% | Llama-3.2-3B d100 s42 SFT | ✓ `exp_001_sft_llama32_3B_d100_s42` (tmux parent 804786) |

## CPU 任务

| PID | 实验 | Registry |
|-----|------|----------|
| 818742 | MMLU domain gamma N=24 v3 (Stan IRT fitting) | ❌ **无 registry 条目** |

## 需修复的 Registry 问题

1. **`exp_002_signals_15B_instruct_gsm8k`** — 缺少 `gpu` 和 `pid` 字段。实际值：`gpu: "cuda:2"`, `pid: 815287`（从 /proc/815287/environ 确认 `CUDA_VISIBLE_DEVICES=2`）

2. **1.5B-Instruct MMLU signals (PID 810809, cuda:4)** — 完全未注册。命令：`python compute_signals.py --model-path Qwen2.5-1.5B-Instruct --benchmark mmlu --signal all --ref-model-path Qwen2.5-1.5B --output-dir /root/autodl-tmp/exp002/signals/Qwen2.5-1.5B-Instruct/ --batch-size 8`。环境确认 `CUDA_VISIBLE_DEVICES=4`。

3. **exp_006_mmlu_domain_gamma_n24_v3 (PID 818742, CPU)** — 完全未注册。命令：`python run_mmlu_domain_gamma_n24.py --rrf-path .../exposure_scores.json --output-dir /root/autodl-tmp/exp006/results_mmlu_domain_gamma_n24_v3`

4. **`exp_001_eval_05B_instruct`** — 已标记 DONE，无问题。

## 关键发现

- **cuda:2 和 cuda:4 并非空闲**，是 1.5B-Instruct 的 signals 任务（模型小，显存占用低，被误判为空闲）
- cuda:2 显示 0% util 可能是 batch 间隙或 IO 等待，但进程确实存活
- 资源工具误报原因：这两个 signals 进程的 registry 条目缺失/不完整，导致 reconcile 无法匹配

---
