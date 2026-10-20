# research dose response literature

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_dose-response-literature_20260515T010151_result.json`
- **Structured JSON:** [`bf5e1085bbb595067aa5.json`](../../sessions/bf/bf5e1085bbb595067aa5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。产出：

1. **`literature_map.yaml`** — 14篇论文，覆盖4个方向：
   - dose-response/threshold: 4篇 (Rolnick 2017, Li ICLR 2024, Dohmatob ICLR 2025, Beyond Clean Data 2024)
   - error-injection: 4篇 (Wang 2024, ETO ACL 2024, PALADIN 2025, AgentHER 2025)
   - data-mixing: 4篇 (Dong ACL 2024, Ye ICLR 2025, Li ICML 2025, Seddik 2024)
   - curriculum/quality: 2篇 (Robust Curriculum 2024, WKM NeurIPS 2024)

2. **Survey report** (`artifacts/dose_response_literature_survey.md`, registered as `art_20260515_1b989f`)

核心定位：**没有先前工作报告过 agent SFT 中直接错误注入的 dose-response 曲线**。现有方法要么用 contrastive/DPO 框架（ETO），要么配对 recovery 演示（PALADIN），都回避了直接混入问题。我们的 10%→25% 阈值发现是该设定下的首个实证锚点，与理论 mixing-law 文献（Ye et al., Seddik et al.）的预测一致。

---
