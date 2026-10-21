# paper r2 group b abs claim method

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_r2-group-b-abs-claim-method_20260528T065024_result.json`
- **Structured JSON:** [`72e2ef777b3e4312fb16.json`](../../sessions/72/72e2ef777b3e4312fb16.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

claim3.tex 中 "20$\times$" 出现在 L3（保留）、L32（保留）、L46（保留），L26 已替换为 "the tested range"。正确。

全部修改完成，汇总：

| # | 优先级 | 文件 | 修改内容 |
|---|--------|------|----------|
| P0 #2 | P0 | abstract.tex | "account for **all**" → "account for **nearly all**" |
| P1 #5 | P1 | claim2.tex | TSR≈70-80% caveat 不成立（Pi0 LoRA Collapsed=99.4%），改为承认 LoRA baseline 本身 action-collapsed，structural finding 应仍成立但需 functional policy 验证 |
| P2 #6 | P2 | method.tex | 在等价性声明后补充数值："collapsed episodes cluster below 1 μm while active episodes exceed 200 mm" |
| P2 #7 | P2 | method.tex | "velocity-based...left to future work" → "alternative displacement metrics...would yield equivalent classification...we adopt maximum displacement for interpretability" |
| P2 #8 | P2 | claim3.tex L26 | "across a 20×range" → "across the tested range"（L3/L32/L46 三处保留） |
| P2 #8 | P2 | abstract.tex L6 | "across a 20× loss-weight range" → "across the tested loss-weight range" |
| P2 #9 | P2 | abstract.tex 末句 | "rather than geometric supervision" → "rather than EE-only geometric supervision" |

**#5 数据验证结论**：Table (claim2.tex) 明确显示 Pi0 LoRA baseline Collapsed=99.4%，原文声称 "TSR≈70-80%" 无数据支撑。claim3.tex 中 Pi0.5 LoRA TSR 也仅 51.5%，Pi0.5 baseline 为 71.5%——均不匹配 70-80%。已将 caveat 改为诚实承认 baseline 本身 collapsed，结构性结论应仍成立但需 future work 验证。

---
