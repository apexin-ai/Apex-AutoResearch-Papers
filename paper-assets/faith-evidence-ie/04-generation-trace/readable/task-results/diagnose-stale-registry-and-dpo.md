# diagnose stale registry and dpo

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_stale-registry-and-dpo_20260523T034459_result.json`
- **Structured JSON:** [`51dbe4f30b223837af8d.json`](../../sessions/51/51dbe4f30b223837af8d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

### 1. 6 个 stale 实验 — 全部已完成，registry 已标记 DONE

| 实验 | ign_f1 | 关键指标 | 状态 |
|------|--------|---------|------|
| test_eval_14b_rsft_s42 | 0.3849 | evi_f1_joint=0.2688, edcr=0.7865 | success |
| eval_llama_rsft_s42_no_evi_2048 | 0.5559 | fair_tax_pp=+2.17 | success |
| d140_4b_sft_s42_with_evi_2048 | 0.3946 | evi_f1_dreeam=0.3129, fair_tax_pp=+0.73 | success |
| d140_8b_sft_s42_no_evi_2048_fix | 0.5019 | fair_tax_pp=+0.04 | success |
| d140_1_7b_sft_s42_no_evi_2048_fix | 0.4233 | fair_tax_pp=-5.63 | success |
| d140_4b_sft_s42_no_evi_2048_fix | 0.4016 | fair_tax_pp=+0.73 | success |

所有结果文件（metrics.json + predictions.json）完整存在，PID 均已终止。Registry 此前已更新为 DONE，无需处理。

### 2. DPO 训练 — 已完成

- **路径**: `/root/autodl-tmp/dpo_output_rebuilt_1ep/`
- **Base model**: Qwen3-4B (`/root/autodl-tmp/models/Qwen3-4B`)
- **SFT adapter**: `/root/autodl-tmp/sft_output` (merged into base)
- **配置**: LoRA r=64, alpha=128, dropout=0.05, beta=0.1, sigmoid loss, lr=5e-6, bs=2×8 grad_accum, 1 epoch
- **数据**: 2977 DPO pairs
- **训练指标**: loss=0.5932, rewards_accuracy=81.6%, rewards_margins=1.008, runtime=34min
- **输出文件**: adapter_model.safetensors (528MB), checkpoint-100, checkpoint-187

### 3. DPO eval — 已在运行

- **exp_id**: `dpo_rebuilt_1ep_eval`
- **PID**: 221951, **GPU**: cuda:2 (11.7GB/96GB)
- **进度**: 18/247 batches (~7%), 已运行 ~15min，预计总耗时 ~3.5h
- **命令**: `python -m freige.eval.inference --model_path dpo_output_rebuilt_1ep --base_model Qwen3-4B --sft_adapter sft_output --max_new_tokens 2048 --seed 42`
- **输出**: `/root/autodl-tmp/eval_results/dpo_rebuilt_1ep_eval`

### 4. 当前 4 个活跃进程

| GPU | PID | 运行时间 | 任务 | 进度 |
|-----|-----|---------|------|------|
| 0 | 220069 | 52min | test_eval_8b_rsft_s43_no_evi | 运行中 |
| 1 | 194682 | 9h29m | plan017_14b_rsft_s43_generate | 13144 行 (~54% of 24216) |
| 2 | 221951 | 15min | dpo_rebuilt_1ep_eval | 18/247 (7%) |
| 3 | 214028 | 2h37m | test_eval_1_7b_rsft_s43_with_evi | 运行中 |

4 卡全在工作，无需额外操作。DPO eval 已由之前的 session 提交，不需要重复启动。

---
