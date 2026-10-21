# audit main text numbers

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_main-text-numbers_20260523T102152_result.json`
- **Structured JSON:** [`a323c9d49be2a8f2d723.json`](../../sessions/a3/a323c9d49be2a8f2d723.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。检查了 45 个数字，结果：

**需修复的 2 处不一致：**

1. **conclusion.tex:7 "within 3.9 pp"** — registry (exp41_tost_10seed) 显示 scrambled vs 9-class 在 AA 上差距为 **3.0pp**，非 3.9pp
2. **conclusion.tex:15 "d<0.1"** — DD 的 |d|=0.136，不满足 d<0.1。Introduction 的写法 "|d|≤0.14" 是正确的，conclusion 过于宽松

**4 个无法追溯到 registry 的数字：**
- Cohen's κ=0.78 (n=50)：标注质量指标，不在实验记录中
- 4–20× variance ratio：需多实验交叉计算，无单一 exp_id
- 12–14pp dual-OOD drop 和 0.3pp recovery：无独立实验，可能来自 appendix 推算

其余 36 个数字全部与 registry 一致（含 3 个可接受的舍入差异）。报告已写入 `artifacts/audit_main_text.md`。

---
