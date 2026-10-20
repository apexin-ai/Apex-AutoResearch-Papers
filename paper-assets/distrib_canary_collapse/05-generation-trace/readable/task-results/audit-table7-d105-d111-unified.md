# audit table7 d105 d111 unified

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_table7_d105_d111_unified_20260520T012835_result.json`
- **Structured JSON:** [`24c232a09ef215c50e8b.json`](../../sessions/24/24c232a09ef215c50e8b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/table7_d105_d111_unified_audit.md`。

核心结果：

**K≥3 变化 (old→new):**

| Model | Seed | K≥3 | K≥4 | flags |
|-------|------|------|------|-------|
| Pythia-6.9B | s42 | 8/8→5/8 | 3/8→1/8 | MISSING_3SIGMA |
| Qwen3.5-0.8B | s42 | 8/8→8/8 | 6/8→3/8 | MISSING_3SIGMA |
| GPT-2m | s42 | 6/8→**0/8** | 2/8→0/8 | |
| GPT-2m | s43 | 6/8→**1/8** | 4/8→0/8 | |
| OPT-1.3B | s42 | 6/8→**0/8** | 2/8→0/8 | |
| Padding-410M | s42 | 6/8→6/8 | 6/8→**0/8** | MISSING_3SIGMA |
| SmolLM3-3B | s42 | 0/8→0/8 | 0/8→0/8 | |
| Pythia-410M | s43 | 6/8→6/8 | 0/8→0/8 | MISSING_3SIGMA |
| C4 Pythia-1B | s42 | 8/8→5/8 | 4/8→1/8 | |
| C4 Pythia-1B | s43 | 8/8→5/8 | 5/8→2/8 | |
| Pythia-1.4B | s42 | 2/8→1/8 | 0/8→0/8 | |
| Pythia-1.4B | s43 | 6/8→7/8 ↑ | 3/8→4/8 ↑ | K_INCREASED |
| OPT-1.3B | s43 | 0/8→0/8 ✓ | — | verification ✓ |

**两个最大冲击源：**
1. **D111**: diff_xcorr 的 peak_lag 几乎全部 ≤ 0，diff_fwd 跨所有实验最高仅 2/8。这是 K≥4 暴跌的主因。
2. **D105**: 3σ threshold 在 GPT-2m/OPT/SmolLM3 全部为 False，直接把这些实验的 K≥3 打到 0-1。

**高风险项：** 4 个 17855 实验 (Pythia-6.9B, Qwen, Padding-410M, Pythia-410M s43) 缺少 `significant_3sigma` 字段，使用了 2σ fallback。如果重跑 3σ analysis，Padding-410M 和 Pythia-410M s43 的 K≥3=6/8 可能进一步降为 0/8（当前 K=3 的 6 个 pair 都依赖 thresh+permG+TY 恰好=3）。

---
