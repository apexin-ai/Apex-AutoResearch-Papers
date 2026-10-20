# analysis exp 005 qwq regime

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp-005-qwq-regime_20260516T204929_result.json`
- **Structured JSON:** [`70add001a580d99a00a1.json`](../../sessions/70/70add001a580d99a00a1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

exp-005 完成。

**产出**：
- `art_20260516_bf444f` — `operating_regime_data.json`：结构化 JSON，含 4 组实验的完整 metrics + 对比模型数据 + operating regime boundary 定义
- `art_20260516_d6966d` — `operating_regime_report.md`：paper section draft，含 summary table、per-problem case study、temperature ablation、operating regime 定义

**关键数字验证**（与 registry 一致）：

| 指标 | QwQ-32B | Qwen2.5-14B |
|------|---------|-------------|
| C0 (effective) | 2.6% | 46% |
| Diversity ratio | — | 17.7× |
| AIME Δ(SICA−SC) | 0.0pp | — |
| ProofWriter Δ | −5.9pp | — |
| C0 threshold | < 20% (FAIL) | ≥ 20% (PASS) |

Registry `exp-005` 已标记 DONE (conclusion: negative)。

---
