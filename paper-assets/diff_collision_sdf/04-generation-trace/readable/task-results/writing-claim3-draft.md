# writing claim3 draft

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_writing_claim3_draft_20260527T080803_result.json`
- **Structured JSON:** [`fd4a1c8fcd8a5da4c0e4.json`](../../sessions/fd/fd4a1c8fcd8a5da4c0e4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。`docs/paper/claim3.tex` 已更新：

**表格脚注** (L24): 补充了 stepwise curve 可用范围和 30K pending 说明。

**Dose-response 段落** (L34-37): 重写为两段结构：
1. **λ=0.1 stepwise 分析** — seed-0 六点曲线 (16K-28K, mean 55.3%) + 22K outlier 三证据排除 (cross-seed 56.5%, 24K-28K 回落, curve mean within 0.4σ) + `\placeholder` 标注 30K pending
2. **全域总结** — λ∈[0.005, 0.1] 三个条件的 CAR 数值汇总，无 dose-response，binding constraint 归因于 EE-only 结构性不匹配

注意：`\placeholder` 宏需要在 preamble 中定义（如 `\newcommand{\placeholder}[1]{\textcolor{red}{[#1]}}`），否则编译会报错。

---
