# research supplementary checklist

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_supplementary_checklist_20260528T191045_result.json`
- **Structured JSON:** [`4c3107f19455ed14377f.json`](../../sessions/4c/4c3107f19455ed14377f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已创建 `supplementary_checklist.md` 并注册为 artifact (`art_20260528_a06d89`)。

清单包含 6 大类：

| 编号 | 内容 | 数据完备度 |
|------|------|-----------|
| **S1** | Multi-seed 完整结果表（CAR/TSR/EE-disp/per-task, 3 seeds × 4 条件） | 完整 |
| **S2** | Multi-eval-seed 鲁棒性（LoRA 5 eval seeds, SDF 5 eval seeds） | 完整，缺专属图表 |
| **S3** | Lambda 消融（λ=0/0.005/0.01/0.1 + permutation test + stepwise curve） | 完整，已有 fig5 |
| **S4** | Oracle 实验（5 个变体 per-task breakdown + refinement statistics） | 完整，已有 fig_oracle_bar |
| **S5** | 训练曲线 | **缺失**：registry 无 W&B ID，仅有标量 best/final loss |
| **S6** | 附加数据（SSR, threshold sensitivity, fake safety, spatial bowl） | 完整 |

待办：
- 检查服务器上是否存在 W&B runs（registry 未记录）
- 制作 multi-eval-seed CAR 对比图
- 制作 stepwise CAR 曲线图（λ=0.1, 16K–30K）

---
