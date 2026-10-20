# analysis c1c5 audit

**Cross-Representation Disagreement as a Diagnostic Signal for LLM Reasoning Errors** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_c1c5_audit_20260514T143419_result.json`
- **Structured JSON:** [`5bbda79d368e98b3e205.json`](../../sessions/5b/5bbda79d368e98b3e205.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。文件已写入 `artifacts/c1c5_audit.md`。

核心发现：

1. **C5 是同义反复** — evaluate_mvp.py 的 `predicted`（`disagreement.error_side`）和 `actual`（从 `fol_correct`/`code_correct` 推导）是同源数据，100% 是必然结果。用 analyze.py 的两层方法评估，C5=44.4% FAIL。MVP 真实状态是 **4/5 PASS**。

2. **三源矛盾根因** — Registry 引用 evaluate_mvp.py 口径（C3=3, C5=100%），ROADMAP 引用 analyze.py 口径（C3=5, C5=45.8%），两个脚本计算逻辑不同。Report.md 还存在 C3/C4/C5 编号错位。

3. **C4 方向拆分** — FOL targeted (50%) < FOL blind (75%)，delta=-25pp；Code targeted (83.3%) > Code blind (45.8%)，delta=+37.5pp。混合 +21.9pp 掩盖了 FOL 方向的负贡献。

4. **36.3pp 不可复现** — 在当前数据的所有切片上都无法得到此值，最接近的是 code-only delta (+37.5~39.1pp)，可能来自历史快照或编号错位。

---
