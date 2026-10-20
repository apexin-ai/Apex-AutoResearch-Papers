# recon reviewer info collect 20260522

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_recon_reviewer_info_collect_20260522_20260522T045516_result.json`
- **Structured JSON:** [`7f87d7d9ba425cf2943f.json`](../../sessions/7f/7f87d7d9ba425cf2943f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 完整信息收集报告

---

### 1. MBPP/HumanEval eval 可行性

**eval 脚本存在性:**
| 服务器 | eval_humaneval.py | eval_mbpp.py | code_eval |
|--------|:-:|:-:|:-:|
| westb-23072 | ✅ (May 19, 6948B) | ✅ (May 20, 7086B) | ❌ |
| westd-32935 | ✅ (May 19, 6462B) | ✅ (May 19, 7086B) | ❌ |

**依赖包:**
| 服务器 | lm_eval | human_eval (OpenAI) |
|--------|:-:|:-:|
| westb-23072 | ✅ `/root/miniconda3/lib/python3.12/site-packages/lm_eval` | ❌ 未安装 |
| westd-32935 | ❌ 未安装 | ❌ 未安装 |

**eval 脚本实现方式:** 自定义 sandbox 执行（subprocess + tempfile），不依赖 `human_eval` 包：
- `eval_humaneval.py`: "Evaluates model on OpenAI HumanEval (164 problems) by generating code completions and running functional tests in sandboxed subprocesses."
- `eval_mbpp.py`: "Evaluates code generation models on MBPP sanitized subset (374 tasks). Uses sandbox execution to verify generated code against test cases."
- 两个脚本都有 `--max_samples` 参数（default=None），支持子集评估

**Tokenizer（两台一致）:**
```json
{
  "tokenizer_class": "Qwen2Tokenizer",
  "model_max_length": 16384,
  "bos_token": "<｜begin▁of▁sentence｜>",
  "eos_token": "<｜end▁of▁sentence｜>",
  "pad_token": "<｜end▁of▁sentence｜>",
  "unk_token": null
}
```

---

### 2. Qwen2.5-Math-7B 跨架构资源

**westb-23072（资源齐全）:**
- 基础模型: `/root/autodl-tmp/models/Qwen2.5-Math-7B/` (4 shards safetensors, 完整)
- 已有分数: `importance_scores_qwen_math_7b.pt`, `cka_scores_qwen_math_7b.pt`
- 已有剪枝模型:
  - `pruned_cka_only_20_qwen_math`
  - `pruned_standard_20_qwen_math`
- 已有 SFT 恢复:
  - `sft_qwen_math_cka_only_20_final`
  - `sft_standard_20_qwen_math_final`

**westd-32935:** 无任何 Qwen/cross-architecture 资源

**N=200 实现方式（eval_math500.py）:**
- `--max_samples` 参数（line 191, default=None）
- Line 213: `dataset = dataset.shuffle(seed=args.seed).select(range(min(args.max_samples, len(dataset))))`
- 用 `--max_samples 200` 控制采样数量

**eval_gsm8k.py 同理:** `--max_samples` (line 321, default=None)

---

### 3. RASP α 剪枝代码

**主剪枝脚本: `/root/recovery_aware_struct_prune/src/prune.py`**
- westb-23072: 21953B (May 17)
- westd-32935: 19346B (May 18) — 略有不同版本

**argparse 参数 (westb-23072):**
```
--model_path     (required)
--importance_path (for standard/rasp/rasp-rlvr/gradient)
--cka_path       (CKA overlap scores .pt)
--mode           choices=[standard, rasp, rasp-rlvr, magnitude, gradient, random, cka_only]
--sparsity       default=0.35
--alpha          default=1.0  "RASP alpha parameter"
--output_path    (required)
--seed           default=42
--dtype          default=bfloat16
--skip_attention (flag, only prune MLP)
```

**Alpha 使用逻辑 (prune.py):**
- Line 210 (rasp mode): `attn_scores[k] = attn_importance[k].float() * (1.0 - attn_overlap[k].float()).pow(args.alpha)`
- Line 213 (同上 mlp): `mlp_scores[k] = mlp_importance[k].float() * (1.0 - mlp_overlap[k].float()).pow(args.alpha)`
- Line 218 (rasp-rlvr mode): `attn_scores[k] = attn_importance[k].float() * attn_overlap[k].float().pow(args.alpha)`

**rasp_scoring.py (独立模块):**
```
S(h) = I(h) * (1 - F(h))^alpha
```
- Line 23: `compute_rasp_scores(importance, overlap, alpha=1.0)`
- Line 61: `--alpha` argument (default=1.0)

**含 alpha 的文件:**
- `rasp_scoring.py`, `prune.py`, `correlation_analysis.py`, `run_unstructured_baseline.py`, `plot_cka_figures.py`, `gradient_flow_analysis.py`

**westd-32935 prune.py alpha 行（相同逻辑）:**
- 也有相同的 alpha 参数和 RASP scoring 公式

**剪枝架构:** GQA-group 粒度 — 每组移除 7 Q heads + 1 KV head + 对应 MLP channel groups

---

### 4. 当前实验进度快照

**westb-23072:**
```
GPU 0: 4237 / 97887 MiB,  56% util
GPU 1: 4239 / 97887 MiB,  93% util
```

| 任务 | 进度 | 速度 |
|------|------|------|
| eval_math500_sft_standard_20_1p5b | 64/500 (13%) | ~30s/it |
| eval_math500_sft_rasp_20_1p5b | 66/500 (13%) | ~33s/it |

两个 eval 都在今天 12:31-12:32 启动，MATH-500 全量 500 题评测，预计各需 ~4h。

**westd-32935:**
```
GPU 0: 16767 / 97887 MiB,  93% util
GPU 1: 15329 / 97887 MiB,  97% util
GPU 2: 16507 / 97887 MiB,  90% util
GPU 3: 16507 / 97887 MiB,  90% util
```

| GPU | 任务 | 进度 | Acc | 速度 |
|-----|------|------|-----|------|
| 0 | eval_math500_grpo_standard_20_fair_2048_v2 | 88/500 (18%) | 0.3800 @50 | ~60-80s/it |
| 1 | eval_math500_sft_random_20_v3 | 35/500 (7%) | — | ~65-100s/it |
| 2 | eval_gsm8k_sft_alpha4_20_v5 | 858/1319 (65%) | 0.6224 @850 | ~2-3s/it (burst ~30s on long outputs) |
| 3 | eval_gsm8k_grpo_alpha4_20_v3 | 891/1319 (68%) | 0.6282 @850 | ~2-3s/it (burst ~30s on long outputs) |

westd GPU2/3 的 GSM8K 评测预计再 ~30min 完成。westd GPU0/1 的 MATH-500 评测非常慢（7B 模型），预计还需 8-10h。westb 两个 1.5B 评测预计还需 ~3.5h。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "tokenizer_class": "Qwen2Tokenizer",
    "model_max_length": 16384,
    "bos_token": "<｜begin▁of▁sentence｜>",
    "eos_token": "<｜end▁of▁sentence｜>",
    "pad_token": "<｜end▁of▁sentence｜>",
    "unk_token": null
  }
}
```

</details>

---
