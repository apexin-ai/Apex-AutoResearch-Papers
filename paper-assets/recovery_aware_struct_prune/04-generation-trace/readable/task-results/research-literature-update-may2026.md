# research literature update may2026

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_literature_update_may2026_20260514T132612_result.json`
- **Structured JSON:** [`5d611083b16e08667307.json`](../../sessions/5d/5d611083b16e08667307.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

### literature_map.yaml 更新（19 → 24 篇）

新增 5 篇论文：

| ID | 标题 | 年份 | 类别 | 相关度 |
|---|---|---|---|---|
| `dppo_2026` | DPPO: Unbiased Dynamic Pruning for GRPO | 2026.03 | method-component | 5 |
| `arrol_2026` | ARRoL: Online Rollout Pruning for RLVR | 2026.03 | method-component | 5 |
| `task_neurons_2026` | Task-Specific Neurons, Model Collapse, and Recovery | 2026.04 | background | 6 |
| `ddp_2026` | Deterministic Differentiable Structured Pruning | 2026.03 | background | 5 |
| `pruning_vlm_recovery_2026` | Structural Pruning of VLMs: Dynamics, Recovery, Data Efficiency | 2026.04 | background | 5 |

**未入选但值得关注的论文：**
- STOP (2605.13165) — 剪裁推理 trace 而非模型权重，与 RASP 问题不同
- UniComp (2602.09130) — 通用压缩评估框架，relevance 4
- SlimLLM (2505.22689) — 结构化剪枝+线性回归恢复，2025 年 5 月，信息不足未入

**搜索未发现的空白：** 无论文同时使用 CKA + width pruning + RLVR recovery，确认 RASP 的 novelty 仍然成立。

### 产出文件
- `literature_map.yaml` — 已更新
- `artifacts/related_work_notes.md` — 5 个 subsection + usable claims + RASP 定位 narrative

---
