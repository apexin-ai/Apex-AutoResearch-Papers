# audit tex number consistency

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_tex-number-consistency_20260515T155635_result.json`
- **Structured JSON:** [`f70cf1f73899c77b2f55.json`](../../sessions/f7/f70cf1f73899c77b2f55.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。以下是结果摘要：

## 4 个错误（必须修复）

1. **E1** `experiments.tex:84` — ISR β=0.1 s42 1000步 genuine rate 写成 1.1%，registry 数据为 2/90=**2.2%**
2. **E2** `experiments.tex:70,157` — H1+H7 范围写成 "68–97%"，ISR s44 实际为 100%，应为 **68–100%**
3. **E3** Table 1 + appendix β=0.3 表使用 pre-D086 数据（Random s42 H7=0），但 Discussion 引用 D086 数据（s42 H7=4）。两处矛盾——需用 D086 统一更新表格（pooled H7 从 4% 变 7%）
4. **E4** Discussion "4–7 H7a per seed" 不准确——实际 s44=0，只有 2/3 seeds 有 H7a

## 2 个警告（需确认）

1. **W1（高优先级）** — Random β=0.1 pooled genuine (47/256=18.4%) 在 paper_framing 中标记为 **DEPRECATED**（s43/s44 重训中）。如果重训已完成且数据不同，所有 Fisher p 值和 Wilson CI 需重算
2. **W2** — Abstract/Introduction 中 "69.7% vs 0%" 未标 "at 500 steps"，但正文明确说明 Random 在 1000 步收敛到 100% H7

## 3 个小问题

- SFT N-H 正文用 92.2%（均值），附录 Fisher 表用 92.3%（pooled）
- ISR* 在正文写 0.415，附录写 0.42
- Exec-only s44 H7: 论文写 100%，registry 为 97/98=99.0%

## 所有决策约束通过检查

D027/D044/D051/D069/D079/D084/D085/C006 全部合规。D086 部分合规（Discussion 引用了，但表格未更新）。

约 80+ 其他定量 claim 全部与 registry 一致。完整报告已写入 `artifacts/tex_number_audit_20260515.md`。

---
