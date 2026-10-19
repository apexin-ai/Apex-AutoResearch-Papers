# research trace paper numbers

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_trace-paper-numbers_20260517T162155_result.json`
- **Structured JSON:** [`1aeb8298ee8606d6e205.json`](../../sessions/1a/1aeb8298ee8606d6e205.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

找到了精确来源。两个数字都来自 **W&B run 7o9bjszm (hsweep-h2-seed1)** 的 `train/AlfworldSG/action_is_valid`：

| 数字 | W&B Step | Metric Key | 精确值 | 四舍五入 |
|------|----------|------------|--------|----------|
| **89.3%** | Step 2 | `train/AlfworldSG/action_is_valid` | 0.89316233 | 89.3% |
| **43.1%** | Step 4 | `train/AlfworldSG/action_is_valid` | 0.43055209 | 43.1% |

论文描述完全一致（experiments.tex:79）："Action validity at step 2 is 89.3%, dropping to 43.1% by step 4"。

补充说明：
- 这是 **train** 指标而非 val 指标。hsweep-h2-seed1 的 **val** step 0 = 0.88125（registry 里的 0.881）
- `paper_provenance.yaml` 里把这个 claim (C028) 错误关联到了 exp028c，实际来源是 hsweep-h2-seed1
- 完整训练轨迹验证了论文的 "two-phase collapse" 叙事：Step 0→2 validity 从 0.835 升到 0.893（Phase 1 保持高位），Step 4 骤降到 0.431（Phase 2 崩溃），之后继续降到 step 14 的 0.063

---
