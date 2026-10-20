# audit related work reference check

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_related-work-reference-check_20260515T042836_result.json`
- **Structured JSON:** [`ae4b85ccb5f7202d278e.json`](../../sessions/ae/ae4b85ccb5f7202d278e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证完成。17 篇引用的审计结果：

---

### ❌ SUSPECT（1 篇）
- **luo2025vpl** — 作者归属错误。实际论文 "A Case for Validation Buffer in Pessimistic Actor-Critic" 作者是 **Nauman, Ostaszewski, Cygan**，非 "Luo F."。citation key 和作者均需修正。

### ⚠️ CORRECTED（2 篇）
- **nhu2025tawm** — 论文真实，ICML 2025 确认。但草稿称 "built on TD-MPC2" 不够准确，TAWM 是 model-agnostic 方法，只是在 TD-MPC2 上评估。建议改为 "evaluated on TD-MPC2"。
- **palenicek2025** — 论文存在（arXiv:2412.20537），作者正确。但 venue "RLC 2025" **无法公开确认**，建议暂标注为 arXiv preprint 或向作者核实。

### ✅ VERIFIED（14 篇）
hafner2025dreamerv4, li2025lsimagine (ICLR 2025 Oral 确认), kim2025deas, engstrom2020 (ICLR 2020), andrychowicz2021 (ICLR 2021), gumbsch2024thick, mattes2024hieros, hussing2024dissecting, voelcker2025madtd, frauenknecht2025rollouts, barkley2024stealing, zhang2026hwm, shaj2023mts3, farebrother2024stopregressing

---

**需要立即修正的 3 项操作**：
1. `luo2025vpl` → 改为 `nauman2025vpl`，修正作者
2. `nhu2025tawm` 草稿描述微调（"built on" → "evaluated on"）
3. `palenicek2025` venue 标注为 arXiv 直到确认 RLC 2025

报告已保存至 `artifacts/_project/paper/reference_audit_report.md`。

---
