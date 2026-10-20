# analysis rho consistency audit

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_rho_consistency_audit_20260515T131810_result.json`
- **Structured JSON:** [`c4fe5f6d78589e1c886b.json`](../../sessions/c4/c4fe5f6d78589e1c886b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

## 审计结论

**根因**：`compute_metrics.py`（旧管道）包含 gold 为空的实例，且对全空 sample 返回 FK=0（应为 1.0）。CoNLL2003 有 697/3453 (20%) 的 gold-empty 实例，导致：
- FK rho 被 697 个 (FK≈0, F1=0) 点人为膨胀：0.48 → **0.81**
- SJ rho 被 697 个 (SJ≈1, F1=0) 点人为压低：0.48 → **0.18**
- 造成 FK vs SJ 的**排名反转**

**修正后的值**（gold-filtered, n=2756）：

| 实验 | 信号 | 旧值 | 修正值 |
|------|------|------|--------|
| LLaMA CoNLL s42 | FK | 0.8095 | **0.4752** |
| LLaMA CoNLL s42 | SJ | 0.1815 | **0.4836** |
| LLaMA CoNLL s456 | FK | 0.8085 | **0.4690** |
| LLaMA CoNLL s456 | SJ | 0.1895 | **0.4734** |
| SciERC s456 | FK | 0.3448 | **0.2723** |
| SciERC s456 | SJ | 0.4134 | **0.4098** |

**已完成**：
- 3 个 registry 条目已更新为统一管道值
- 审计报告 → `artifacts/rho_consistency_audit.md`
- 统一 rho JSON → `artifacts/analysis_unified_rho.json`
- 服务器审计脚本 → `/root/autodl-tmp/struct_self_consist_ie/rho_audit.py`

**对论文的影响**：原来 "FK dominates (rho=0.81)" 的叙述需要改为 "所有结构信号 rho 相当 (~0.47-0.48)，logprob 较弱 (0.31)"——这其实是更干净的 finding。

---
