# code plan 007 lm eval script

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan_007_lm_eval_script_20260515T210739_result.json`
- **Structured JSON:** [`9b288ef8d5e245ca0347.json`](../../sessions/9b/9b288ef8d5e245ca0347.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Plan 007 eval_benchmark 交付完成。总结：

**已完成：**
- `src/eval_benchmark.py` (640行) — 支持 9 个条件、6 个 benchmark、增量保存、markdown 表格输出
- `scripts/run_plan007_benchmark.sh` — 三步流程（验证→PPL→lm-eval），默认 GPU 1
- 全部 9 个条件的 WikiText-2 PPL 已验证通过
- 离线错误处理测试通过（C4 streaming 和 lm-eval 数据集均优雅报错）
- 结果已整合到 `results/plan_007/consolidated/`
- 两个 artifact 已注册

**核心发现：** 学习型预测器（KL=9.65, STE=8.18, SPON=9.41）在 50% 稀疏度下保持接近 dense（6.48）的质量，而所有静态 mask 基线都严重退化（R-Sparse=151, WINA=2126, TEAL=48715）。

**待完成（需联网）：**
1. C4 validation 数据集预缓存（streaming 模式离线不可用）
2. lm-eval 下游数据集预缓存：`allenai/ai2_arc`, `allenai/winogrande`, `hails/mmlu_no_train`, `openai/gsm8k`
3. 预缓存后执行完整 benchmark（C4 PPL + 4 个下游任务 × 9 条件）

---
