# analysis paper data summary

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_paper_data_summary_20260526T004721_result.json`
- **Structured JSON:** [`7ea1a9d6e7977155facb.json`](../../sessions/7e/7ea1a9d6e7977155facb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文件已创建并注册。

**汇总**: `artifacts/paper_data_summary.md` 包含 **42 个已确认数据点**，**5 个待收集占位符**：

- **Table 1**: 3 seeds × 2 lambdas 的 30K eval 全部完成；best checkpoint 完成 2 个（seed1_16K, seed2_10K），seed0 因训练未保存 best/ ckpt 无法 eval，λ=0.01 的 best 待执行
- **Claim 1 (A1 fake safety)**: 800 episodes 确认 99.6% fake safe，per-task 分解完整
- **Claim 2 (LoRA baseline)**: object CAR=82% TSR=0%，Pi0.5 3-seed baseline TSR=74.7% CAR=26.8%；displacement-fixed eval 待收集
- **Claim 3 (Oracle)**: 5 个变体全部 negative，GT SDF refinement 96-98% fake safe
- **Over-avoidance**: 4 组 displacement-fixed 对比确认 30K 非 frozen（ee_disp 0.47-0.50m, fake_safe=0%）

---
