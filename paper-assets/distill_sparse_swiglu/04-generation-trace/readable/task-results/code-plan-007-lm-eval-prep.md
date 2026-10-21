# code plan 007 lm eval prep

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan_007_lm_eval_prep_20260515T225501_result.json`
- **Structured JSON:** [`3138a92ed32bfb041046.json`](../../sessions/31/3138a92ed32bfb041046.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有信息已收集完毕。

---

## 报告

### 1. lm-eval-harness
- **已安装**，版本 0.4.12
- `lm_eval.models.huggingface.HFLM` 可用，eval_benchmark.py 已集成

### 2. 集成脚本
- **已有**，无需创建：
  - `src/eval_benchmark.py` — 完整的 plan_007 评估脚本，支持所有 10 个 condition（dense, kl_s42, bce_s42 等）
  - `scripts/run_plan007_benchmark.sh` — Shell 启动器
  - lm-eval 通过 `HFLM(pretrained=model, tokenizer=tokenizer)` 传入已 patch 的模型，sparse mode 无缝集成

### 3. 数据集缓存（离线服务器）
| 数据集 | 状态 |
|--------|------|
| arc_challenge (allenai/ai2_arc) | 已缓存 |
| winogrande (allenai/winogrande) | 已缓存 |
| mmlu (cais/mmlu + hails/mmlu_no_train) | 已缓存 |
| gsm8k (openai/gsm8k) | 已缓存 |
| **hellaswag** | **未缓存，blocker** |

### 4. KL predictor checkpoint
- `/root/distill_sparse_swiglu/checkpoints/mvp_kl_norm_v2_s42/predictor_kl_normalized.pt` — 存在 ✓

### 5. 已有结果
- WikiText-2 PPL：所有 condition 已完成（consolidated/results.json）
- **lm-eval 下游任务：无完整结果**，之前的运行被中断

### 6. 当前 GPU 状态
- **cuda:0**：空闲（0 MiB）
- **cuda:1**：正在跑 dense lm-eval（PID 163723，已运行 ~10min，20831 MiB）
  - 命令：`python -u src/eval_benchmark.py --condition dense --tasks lm_eval --skip_ppl --gpu 0 --batch_size 4`

### 7. Dry-run
- 模块导入全通过，HFLM/predictor/conditions 配置正确
- 实际推理验证：正在运行的进程已证明 pipeline 可工作

### 8. 可否立即开跑？

**可以部分开跑**：
- cuda:0 **现在就能启动 kl_s42 sparse lm-eval**，与 GPU 1 上正在跑的 dense 并行
- cuda:1 上的 dense 正在运行，等它完成即可

**需要先处理的问题**：
1. **HellaSwag (blocker)**：未缓存 + 服务器离线无法下载。需要从有网机器下载后传上去，或者先跳过 HellaSwag
2. **eval_benchmark.py 缺 hellaswag 配置**：`LM_EVAL_TASKS` dict 中没有 hellaswag，需加一行 `("hellaswag", 10)`
3. **确认运行中的 dense 进程**是否正常：输出目录暂无 results.json（尚未写入），需持续观察

**建议下一步**：
- 先跳过 HellaSwag 或者提供下载方案
- 在 cuda:0 上立即启动 kl_s42 的 4 个任务 (arc_challenge, winogrande, mmlu, gsm8k)
- 等 dense 进程完成后确认结果

---
