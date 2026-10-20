# check westd 21461 status

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_westd_21461_status_20260521T045549_result.json`
- **Structured JSON:** [`3d9b7d4178a24a4bf52e.json`](../../sessions/3d/3d9b7d4178a24a4bf52e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### 1. Trie Baseline (PID 241846) — 已完成

4 个 config 全部跑完，各 551 行。Trie 约束消除了 ET% 和 RV%（均 0%），但 DR% 仍然很高：

| Config | E-F1 | R-F1 | parse_fail% | ET% | RV% | DR% | CF |
|--------|------|------|-------------|-----|-----|-----|----|
| **Qwen FT** | 0.6673 | 0.4257 | 9.1% | 0% | 0% | **95.5%** | 1 |
| **Qwen ZS** | 0.3097 | 0.0864 | 0% | 0% | 0% | 29.3% | 0 |
| **Llama FT** | 0.6537 | 0.4142 | **50.8%** | 0% | 0% | 15.2% | 0 |
| **Llama ZS** | 0.2323 | 0.0290 | 0% | 0% | 0% | **84.4%** | 4 |

要点：
- Trie 约束成功将 ET%/RV% 压到 0%，但 **DR% 完全无法控制**（trie 只约束词汇不约束组合）
- Llama FT 有 50.8% parse failure，严重影响有效样本量
- FT 模型的 F1 远高于 ZS（符合预期）

### 2. Qwen Beam 998 (PID 226609) — 仍在运行

- 已跑 8h36m，进度 929/998（**93.1%**）
- 预计还需 ~40 分钟完成

结果已写入 `artifacts/r16_verification/westd21461_check.json`。

---
