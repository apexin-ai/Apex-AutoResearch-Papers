# research vericot deep dive

**svs formal verification** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_vericot_deep_dive_20260514T155230_result.json`
- **Structured JSON:** [`8450a12ee5d3c68fe540.json`](../../sessions/84/8450a12ee5d3c68fe540.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/vericot_deep_dive.md`。核心发现：

**VeriCoT 确认不做 chain selection**——仅单链验证+串行 self-reflection，判定为 binary pass/fail。Pass rate 极低（ProofWriter 45%，BioASQ 25%，SARA 15%）。

**SVS 的核心差异化成立**：
1. **Graded IC for chain selection** — 整个 2023-2026 文献中无人将 formal verification 连续分数用于 inference-time chain ranking。VeriCoT 做 binary，PRoSFI/LogicReward 做 graded 但仅用于 training reward，PC-CoT 做 binary filter+SC。
2. **PCV（题目 premises 驱动）** — VeriCoT 的 premises 由 LLM 生成，有 fabrication 风险；SVS 用题目给定 premises。
3. **实用性** — VeriCoT 15-45% pass rate vs SVS 85% formalization rate，graded 设计更鲁棒。

**关键下一步**：entailment IC 实验结果是决定性的。如果 d > 0.15，推荐 framing 为 "Graded Formal Verification as Test-Time Chain Selection"，必须补 binary filter+SC ablation。

---
