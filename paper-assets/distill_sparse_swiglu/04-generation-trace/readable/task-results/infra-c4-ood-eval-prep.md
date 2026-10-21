# infra c4 ood eval prep

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_c4_ood_eval_prep_20260517T171948_result.json`
- **Structured JSON:** [`fafdcded3944499a6b5a.json`](../../sessions/fa/fafdcded3944499a6b5a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完整情况已清楚。总结如下：

---

## C4 数据状态

| 服务器 | 路径 | 状态 |
|--------|------|------|
| westd-34887 | `/root/autodl-tmp/data/c4_val/` | **已有** (785MB, Arrow 格式) |
| westd-41718 | `/root/autodl-tmp/data/` | **不存在** |

---

## Eval 方式分析

**现状**：`benchmark_eval.py` 对 C4 的支持是**半成品**：
- `data_utils.py:get_eval_dataset("c4", ...)` 已实现，能读取本地 `/root/autodl-tmp/data/c4_val`
- 但 `benchmark_eval.py` 只特殊处理 `wikitext2`，"c4" 会被当作 unknown task 忽略

**需要的代码修改**（约 10 行）：仿照 `run_wikitext2_ppl()` 加一个 `run_c4_ppl()`，并在 main 函数中加 `do_c4` 分支。

lm-eval-harness 也有 `c4` task（`/root/miniconda3/lib/python3.12/site-packages/lm_eval/tasks/c4/c4.yaml`），但它需要从 HF 下载 `allenai/c4` 的 json.gz 分片，不如用已有本地数据。

---

## Blocker

**需要修改 `benchmark_eval.py`** 加入 C4 PPL 支持。修改很小，我现在写好吗？

---

## 命令模板（修改完成后可用）

```bash
# KL-30% predictor (seed 42) on C4
python /root/distill_sparse_swiglu/src/benchmark_eval.py \
  --exp_id c4_ood_kl30_s42 \
  --checkpoint checkpoints/mvp_kl_norm_v2_s42/predictor_kl_normalized.pt \
  --sparsity_mode teal_global --sparsity_target 0.3 \
  --tasks c4 --gpu 0

# KL-30% predictor (seed 123)
python /root/distill_sparse_swiglu/src/benchmark_eval.py \
  --exp_id c4_ood_kl30_s123 \
  --checkpoint checkpoints/mvp_kl_norm_v2_s123/predictor_kl_normalized.pt \
  --sparsity_mode teal_global --sparsity_target 0.3 \
  --tasks c4 --gpu 0

# KL-30% predictor (seed 456)
python /root/distill_sparse_swiglu/src/benchmark_eval.py \
  --exp_id c4_ood_kl30_s456 \
  --checkpoint checkpoints/mvp_kl_norm_v2_s456/predictor_kl_normalized.pt \
  --sparsity_mode teal_global --sparsity_target 0.3 \
  --tasks c4 --gpu 0

# Dense baseline
python /root/distill_sparse_swiglu/src/benchmark_eval.py \
  --exp_id c4_ood_dense \
  --dense --tasks c4 --gpu 0

# TEAL baseline (vanilla activation magnitude)
python /root/distill_sparse_swiglu/src/benchmark_eval.py \
  --exp_id c4_ood_teal_vanilla_30 \
  --baseline_mode teal_vanilla --sparsity_target 0.3 \
  --tasks c4 --gpu 0
```

---

**下一步**：需要我写 `benchmark_eval.py` 的 C4 PPL 补丁吗？（~10行，加 `run_c4_ppl` + `do_c4` 分支）

---
