# paper discussion detach mechanism

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_discussion_detach_mechanism_20260523T101456_result.json`
- **Structured JSON:** [`d6abe6aaaccf45d82f0a.json`](../../sessions/d6/d6abe6aaaccf45d82f0a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Structure is correct now: L28 (gradient analysis) → L30 (new BN hypothesis paragraph) → L32 (TSR instability). All three are separate paragraphs.

**汇报：**

**(1) 数据合规检查**
- L28 梯度引用：只引用 Random OCC 和 Depth（有数据）vs Detach（有数据），并标注"A complete four-condition comparison awaits..."。**合规，无需修正。**
- L46 "significantly"：无统计检验支撑，已改为 "does not improve CAR beyond Vanilla"（后面括号已提供数值解释）。
- 未发现引用 Full OCC / Vanilla / Cutoff 梯度数据的违规声明。

**(2) 新增段落**
- 位置：§5.2 L30，介于梯度分析段落 (L28) 和 TSR instability 段落 (L32) 之间。
- 内容：BatchNorm contamination hypothesis。具体阐述 BN running statistics 在 Detach 模式下的不对称耦合机制（1.2M 参数的 parasitic pathway），明确标记为 hypothesis ("We hypothesize", "If this account is correct")，末尾以 italic 标注 Detach+LN (plan_027) 作为 discriminating test 及两种结果的解释。
- 删除了原 L28 末尾 "Ongoing experiments replace..." 句（已被新段落更完整地覆盖）。
- 未引用 Full OCC 或 Vanilla 梯度数据。

**(3) 一致性**
- 与 §5.1 三个 hypothesis 一致：新段落提出 BN 作为 forward-pass interference 的具体机制，不与三个宏观假说冲突。
- 与 §5.3 cutoff 分析无交叉。
- 与 §5.4 practical recommendation 一致：recommendation 基于经验发现（"gradients must flow"），不依赖于 BN vs gradient-flow 的机制区分。

---
