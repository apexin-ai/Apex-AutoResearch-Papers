# figure r2 collapse and l1

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_figure_r2_collapse_and_l1_20260522T063259_result.json`
- **Structured JSON:** [`e397807f21e1a45ebf17.json`](../../sessions/e3/e397807f21e1a45ebf17.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。输出文件：

| 文件 | 大小 |
|------|------|
| `fig_r2_collapse.pdf` | 27 KB |
| `fig_cross_arch_l1.pdf` | 17 KB |
| `nora_goal_r2_trained.json` | 596 B |
| `nora_goal_r2_untrained.json` | 602 B |

**数据来源**:
- OpenVLA trained: `results/libero_goal/action_r2_probing.json` (32 层, last_preaction)
- OpenVLA untrained: 硬编码稀疏数据 + 线性插值 (16 个点 → 32 层)
- TracVLA trained/untrained: `results/tracvla_goal/{trained,untrained}/action_r2_probing.json` (32 层)
- NORA trained/untrained: `results/nora_goal/{trained,untrained}/action_r2_probing.json` (36 层)

**fig_r2_collapse**: NORA L35 trained R²=-0.0039（极端 collapse），TracVLA L30 降到 0.31，OpenVLA exit 层几乎无衰减（Δ≈0.02）。每个 subplot 标注了 peak 值和 peak-to-exit Δ。

**fig_cross_arch_l1**: 归一化分数 + 原始计数标注。所有模型 trained/untrained 的 instruction-dominant head 比例都很高（0.72–1.0）。

---
