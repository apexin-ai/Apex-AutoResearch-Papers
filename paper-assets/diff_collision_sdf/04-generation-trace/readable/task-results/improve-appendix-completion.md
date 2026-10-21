# improve appendix completion

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_improve_appendix_completion_20260527T220539_result.json`
- **Structured JSON:** [`edea7e8bfe8b30b12f43.json`](../../sessions/ed/edea7e8bfe8b30b12f43.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

主文引用了 3 个 appendix label，appendix.tex 全部覆盖：
- `sec:appendix_null` ✓ (Section A.2)
- `sec:appendix_ssr` ✓ (Section A.3)  
- `sec:appendix_stepwise` ✓ (Section A.5)

没有 main.tex 和编译基础设施，无法 latexmk 编译。

---

**已补充内容清单（8 个 section，254 行）：**

| Section | Label | 内容 |
|---------|-------|------|
| A.1 Per-Task CAR | `appendix_pertask` | 4 个表：LoRA-only / λ=0.005 / λ=0.01 / baseline 的 per-task×per-seed CAR；分析 task difficulty ordering |
| A.2 Null Distribution | `appendix_null` | 零假设构造（6 值 pooled null）、排列检验过程、λ=0.01 和 λ=0.1 的具体 p 值 |
| A.3 SSR/TSR Ratio | `appendix_ssr` | 9 条 per-seed SSR/TSR 数据，baseline 0.39 → fine-tuned 0.48–0.62 |
| A.4 Threshold Sensitivity | `appendix_threshold` | dfCAR 在 τ_d ∈ [2,300]mm 的稳定性表（8 条件 × 7 阈值） |
| A.5 Stepwise Ablation | `appendix_stepwise` | λ=0.1 的 16K–28K checkpoint 分析 |
| A.6 SDF Pipeline | `appendix_sdf_pipeline` | mesh 修复统计、SDF 采样、梯度验证、符号约定 |
| A.7 Hyperparameters | `appendix_hyperparams` | 完整训练/评估超参数表 |
| A.8 Eval Protocol | `appendix_eval_protocol` | 任务描述、4 个 metric 定义 |

**仍需补充但缺少数据的内容：**

| 内容 | 缺失原因 |
|------|----------|
| λ=0.1 per-task CAR 表 | 无 reeval JSON（只有 2 seed 的 aggregate 数据 58.0, 58.5） |
| 训练 loss 曲线图 | artifacts 中无 loss curve 文件，需从 wandb 导出 |
| Phase-2 ablation 详情 | 单 seed (s2) 实验，数据不足 |
| experiments.tex | 文件不存在，非 appendix 范围 |

**编译结果：** 无法编译——`docs/paper/` 下无 `main.tex`、`.bib`、`.cls` 文件。appendix.tex 是独立 section 文件，需集成到完整论文后编译。

---
