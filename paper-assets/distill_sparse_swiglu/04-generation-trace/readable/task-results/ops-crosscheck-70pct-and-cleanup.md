# ops crosscheck 70pct and cleanup

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_crosscheck_70pct_and_cleanup_20260515T225914_result.json`
- **Structured JSON:** [`b1d27474e0af08a502d9.json`](../../sessions/b1/b1d27474e0af08a502d9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

PID 171565 是另一个 Worker 刚启动的 `kl_s42` lm_eval 评估（44 秒前），合法进程。

---

## 报告

### 1. P0-C 结论：kl_sparsity70_s42_v2 sparsity_target 正确，数据点有效

- **predictor_hard_mask_ppl (13.84)**：`patch_predictor()` 用 `(_pred(x) > 0)` 硬阈值生成 mask，不使用 `--sparsity_target` 参数。`model_level_sparsity=0.699` 确认 predictor 自然达到 ~70% 稀疏度。
- **teal_sparse_ppl (17.91)**：`plan_007_all_ppl_fixed.json` 明确标注 sparsity70 使用了单独的 70% target（mode=`static_mask_70pct`）。旧值 136K 是 `_global_topk_masks` 归一化 bug，已修复。
- **结论：无需重跑。**

### 2. 清理结果

- **PID 169864**（dry run arc_challenge → /tmp/dryrun_test）：已自行退出，无需手动 kill
- **PID 163723**（lm_eval dense，11h）：保留，正在跑 MMLU tokenization
- 无卡死进程需要清理

### 3. 当前 GPU 状态

| GPU | PID | 任务 | 显存 | Util |
|-----|-----|------|------|------|
| cuda:0 | 171565 | `kl_s42` lm_eval（刚启动 44s） | 18318MiB/97887MiB | 0% (loading) |
| cuda:1 | 163723 | `dense` lm_eval（11h, MMLU tokenizing） | 20831MiB/97887MiB | 0% (CPU-bound) |

两张 GPU 都在执行合法的 lm_eval 评估任务。

---
