# code k supplement and greedy

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_k_supplement_and_greedy_20260514T005021_result.json`
- **Structured JSON:** [`39991ded06ebcaab55c8.json`](../../sessions/39/39991ded06ebcaab55c8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两阶段实验全部完成。

---

## 阶段 1：k={10,12} 补充 sweep

| max_2bit | PPL | 2bit | 4bit | 8bit | 16bit | mem_ratio |
|----------|-------|------|------|------|-------|-----------|
| 0 | 15.45 | 0 | 112 | 0 | 0 | 0.2500 |
| 4 | 11.77 | 4 | 104 | 4 | 0 | 0.2500 |
| **8** | **11.23** | 8 | 100 | 4 | 0 | 0.2500 |
| **10** | **11.50** | 10 | 98 | 4 | 0 | 0.2478 |
| **12** | **11.42** | 12 | 96 | 3 | 1 | 0.2500 |
| 16 | 11.81 | 16 | 88 | 4 | 4 | 0.2500 |

**k=8 仍是极值点 (11.23)**。k=10 (11.50) 和 k=12 (11.42) 均高于 k=8，确认 U 型曲线底部在 k=8。

---

## 阶段 2：RateQuant Greedy vs MCKP

| Method | PPL | 2bit | 4bit | 8bit | 16bit | mem_ratio |
|--------|-------|------|------|------|-------|-----------|
| Greedy RateQuant | **32.45** | 68 | 30 | 4 | 10 | 0.2500 |
| MCKP (k=8, L0 excl) | **11.23** | 8 | 100 | 4 | 0 | 0.2500 |

**Delta PPL = +21.22**。Greedy 在 {2,4,8,16} 非均匀 bit-width 上 dramatically suboptimal：
- Greedy 将 **68/112** heads 推至 2-bit（MCKP 仅 8 个），同时保留 10 个 16-bit head
- 非均匀间距导致 greedy 过度激进：16→8 省 8 bit "看似高效"，但驱动大量 head 继续降至 2-bit
- Greedy L0 分配: 3×8bit + 1×16bit（未完全保护 L0）
- PPL 劣化 3 倍，conclusively 证明 constrained MCKP 的价值

---
