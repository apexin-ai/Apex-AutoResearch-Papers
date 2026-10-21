# ops check t15 a050 s43 completion

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-t15-a050-s43-completion_20260523T201552_result.json`
- **Structured JSON:** [`65f0dce7a32ff9d0f752.json`](../../sessions/65/65f0dce7a32ff9d0f752.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

## 实验 scale_14b_t15_a050_s43_fp32

**状态**: DONE (success), EXIT_CODE=0, 16 generations 全部完成

**最终指标**: ppl=37.09, distinct_3=0.500, entropy=2.271, ece=0.157

## D102 Lead-Lag 分析 (downstream=distinct_3)

| Pair | Votes | Robust? |
|------|-------|---------|
| token_entropy → distinct_3 | 2/5 (diff, ty) | No |
| ece → distinct_3 | **4/5** (naive, diff, perm, ty) | **Yes** |

**Robust pairs: 1/2** — 只有 ece 是可靠 canary。

关键发现：α=0.50 时 entropy 表现为 drop-then-stabilize（2.97→2.17→2.27），打破了 lead-lag 检测的单调性假设，因此不再 robust。相比 α=0.60 时两个 canary 都 4/5 robust，α=0.50 的 entropy 信号明显弱化，但 ece 仍保持检测能力。

**产出文件**:
- 远程: `results/analysis/D102_14b_t15_a050_s43_fp32_d3.json`
- 本地 JSON: `artifacts/D102_14b_t15_a050_s43_fp32_d3.json`
- 分析报告: `artifacts/_project/d102_t15_a050_s43_d3_result_20260523.md`

---
