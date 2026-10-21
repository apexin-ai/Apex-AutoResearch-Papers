# paper tsr collapse integration

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_tsr_collapse_integration_20260526T062246_result.json`
- **Structured JSON:** [`2a3755f7113036da4ef9.json`](../../sessions/2a/2a3755f7113036da4ef9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

编辑完成。变更内容：

**Table~\ref{tab:avoidance_source}**（已有表）：填入 3 个 EE Disp placeholder — Pi0.5 baseline 无数据用 `---`，SDF λ=0.005 填 0.50m，λ=0.01 填 0.47m。

**TSR collapse 段落**：从 1 段扩展为完整小节，包含：
- **Table~\ref{tab:per_task_tsr}**：4 任务 × 4 条件的 TSR 分解表，数据来自 11 个 eval JSON（2+4+3+2 seeds）
- **三条证据链**：EE displacement 0.47–0.50m（非冻结）、obstacle displacement 0.143→0.059m（避障保留）、safe failure rate 0.5%→49.8%（100× 增长）
- **Figure~\ref{fig:failure_modes}**：引用 `failure_mode_comparison.pdf`
- **Chocolate Pudding 异常**：唯一保留 ~25% TSR 的任务，提示 task-specific forgetting vulnerability

已有骨架（avoidance source 表、lambda curve placeholder、λ=0.1 pending 文本）全部保留。图文件需从 `westd-35807:/root/colliforce-vla/figures/` 复制到 `docs/paper/figures/`。

---
