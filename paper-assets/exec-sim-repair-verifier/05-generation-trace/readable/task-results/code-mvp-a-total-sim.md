# code mvp a total sim

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_mvp-a-total-sim_20260511T192502_result.json`
- **Structured JSON:** [`a2a9f2fae06731db9c5b.json`](../../sessions/a2/a2a9f2fae06731db9c5b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 模拟完成 — 结果汇总

### Total (F2P+P2P) 模拟结果

| Reg.Rate | Noise | 70-85% Mean Adv | Pass(≥5%)? |
|----------|-------|-----------------|------------|
| **5%** | i.i.d. | **-1.0%** | **FAIL** |
| **5%** | block | **-0.5%** | **FAIL** |
| **10%** | i.i.d. | **+13.2%** | **PASS** |
| **10%** | block | **+8.3%** | **PASS** |
| **20%** | i.i.d. | **+35.7%** | **PASS** |
| **20%** | block | **+27.8%** | **PASS** |

### F2P-only vs Total 对比

| Scenario | Noise | 70-85% Mean Adv | Pass |
|----------|-------|-----------------|------|
| F2P-only | i.i.d. | +2.0% | FAIL |
| F2P-only | block | +10.9% | PASS |
| Total (reg=5%) | i.i.d. | -1.0% | FAIL |
| Total (reg=5%) | block | -0.5% | FAIL |
| Total (reg=10%) | i.i.d. | +13.2% | PASS |
| Total (reg=10%) | block | +8.3% | PASS |
| Total (reg=20%) | i.i.d. | +35.7% | PASS |
| Total (reg=20%) | block | +27.8% | PASS |

### 关键发现

**Per-test 优势 critically depends on P2P regression rate:**

- **reg=5%**: 优势为**负** — P2P 中仅 ~2.5/50 个测试被破坏，正确/错误 patch 在 P2P 上几乎无区别，额外的 P2P 测试反而 **稀释** F2P 信号。甚至 block noise 也无法挽救。
- **reg=10%**: 优势明确，~5/50 个 P2P 测试被破坏，信号足够强。两种 noise model 均 PASS。
- **reg=20%**: 优势巨大，~10/50 个 P2P 测试被破坏，per-test verifier 全面碾压 trajectory。

输出文件：
- 结果 JSON: `/home/sonny/exec-sim-repair-verifier/mvp_a_total_results.json`
- 可视化 PDF: `/home/sonny/exec-sim-repair-verifier/mvp_a_total_curves.pdf`
- 脚本: `/home/sonny/exec-sim-repair-verifier/mvp_a_total_sim.py`

---
