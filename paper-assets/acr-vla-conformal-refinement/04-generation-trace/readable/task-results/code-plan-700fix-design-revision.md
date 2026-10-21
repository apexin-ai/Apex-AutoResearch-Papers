# code plan 700fix design revision

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan_700fix-design-revision_20260517T141250_result.json`
- **Structured JSON:** [`19c4e27e5be85d96398e.json`](../../sessions/19/19c4e27e5be85d96398e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

**Part 1**: FiLM (静态 per-layer affine) 替换为 ACCG (Action-Conditioned Correction Gating, 动态 per-sample gate)。327,522 参数，通过 forward/gradient/norm-clipping 验证。

**Part 2**: 添加 `--no_wandb` flag (mode="disabled")；W&B log keys 加 train/val/ prefix。Batch precompute 已存在无需修改。

**Part 3**: 训练命令已准备（见 report），使用 `--auto` 自动触发 precompute + train。**未提交，等待 Director 批准。**

**Part 4**: `crm_k1_model.py` 和 `train_crm_k1.py` 已同步至 bjb2-28827、bjb1-18228、bjb1-32546，md5 全部一致。

Report 已注册为 artifact `plan_701_accg_report`，memory.md 已更新设计变更记录。

---
