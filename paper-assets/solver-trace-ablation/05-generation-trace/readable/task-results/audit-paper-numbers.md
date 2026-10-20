# audit paper numbers

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_paper-numbers_20260514T192349_result.json`
- **Structured JSON:** [`557049974c98a4465374.json`](../../sessions/55/557049974c98a4465374.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。结果：

**127 个数字，119 个匹配 ✅，1 个不匹配 ⚠️，7 个无法追溯 ❓**

关键发现：

**⚠️ 需修正** — introduction.tex line 50: `"<16% under any RL condition"` 不准确。Random β=0.1 三 seed 均值 genuine=18.7%，ISR s42 genuine=30.9%。建议改为 `"≤20%"` 或定性表述。

**❓ 无法从 registry 验证（7 项）**：
- plan002-b03 的 eval PR=18% 和 ISR*=0.143（registry 仅有训练指标）
- 100 步 component count 6.58（plan003 无此字段）
- 94.8% ISR=0（需 raw 数据）
- s43 exec-only "87% max token"（registry 无）

**引用**：22 个 cite key 全部在 bib 中，关键论文均已引用。Bib 有 32 个未被引用条目，提交前应清理。

**paper_framing 笔误**：s42 genuine 主表写 32.1%(26)，D038 段和 registry 均为 30.9%(25)。论文采用了正确的 30.9%。

报告已注册到 `artifacts/paper_number_audit.md`。

---
