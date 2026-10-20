# ssh w1c wikievents kappa

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_w1c_wikievents_kappa_20260519T064540_result.json`
- **Structured JSON:** [`73a8caa3eea4ce9c38be.json`](../../sessions/73/73a8caa3eea4ce9c38be.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。核心结果：

**κ 分布**：245 个 role，κ mean=0.8204，median=0.8889。84% 的 role κ≥0.80（仅允许 4 种或更少 entity type）。分布强烈右偏，41 个 role 只允许 1 种 type (κ=0.9630)。

**κ vs AC violation 率**：
- **Tight (κ≥0.90)**: 50% AC violation rate — 最高
- **Medium (0.80-0.90)**: 21% — 最低
- **Loose (κ<0.80)**: 30% — 中间
- Pearson r = 0.31（弱正相关）

**关键发现**：κ 与 AC violation 率正相关但非线性。高 κ 角色（如 Crime, Sentence, BodyPart）几乎 100% 违反约束，因为 LLM 倾向于生成 PER/ORG 等高频类型而非 CRM/SEN/BOD 等细粒度 KAIROS 类型。但部分高 κ 角色（Vehicle）因语义直觉性强而 0% 违反。**tightness + 类型非典型性的交互**才是真正决定 violation 率的因素。

---
