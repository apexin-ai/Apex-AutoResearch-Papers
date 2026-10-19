# code plan 007 eval prep

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan_007_eval_prep_20260515T210552_result.json`
- **Structured JSON:** [`93f57bba2f5af287aa30.json`](../../sessions/93/93f57bba2f5af287aa30.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**产出：**
- `src/benchmark_eval.py` — benchmark 评估脚本，已部署到服务器
- `lm-eval 0.4.12` — 新安装的依赖

**脚本支持 4 种模式：**

| 模式 | 参数 | 说明 |
|------|------|------|
| per_token predictor | `--checkpoint ... --sparsity_mode per_token` | PredictorWrapper 动态逐 token 硬掩码 |
| TEAL global mask | `--checkpoint ... --sparsity_mode teal_global` | predictor 在校准集上计算静态全局掩码 |
| Training-free baseline | `--baseline_mode teal_vanilla/wina/rsparse/...` | 无 checkpoint，基于激活幅值的掩码 |
| Dense | `--dense` | 无稀疏，原始模型 |

**评估任务：** wikitext2 (PPL), arc_challenge (25-shot), winogrande (5-shot), mmlu (5-shot), gsm8k (8-shot)

**输出：** `results/benchmark/{exp_id}/results.json`

自动检测并加载 compensation network（bce_comp checkpoint）。模型只加载一次，所有任务批量评估。

---
