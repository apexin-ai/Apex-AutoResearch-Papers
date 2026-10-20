# analysis j2 nonstationary sim

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_j2_nonstationary_sim_20260520T213210_result.json`
- **Structured JSON:** [`4900e04a4c5285f794dc.json`](../../sessions/49/4900e04a4c5285f794dc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

JSON 已确认写入正确 (n_reps=1000)。汇总结果：

---

### Size (FPR at α=0.05, H0: β=0)

| φ | Raw Granger | First-Diff | Perm Granger |
|---|---|---|---|
| 0.50 | **6.4%** | 6.6% | 6.8% |
| 0.95 | **10.0%** | 5.9% | 9.5% |
| 0.99 | **11.2%** | 4.2% | 10.7% |

### Power (rejection rate at α=0.05, H1: β>0)

| φ | β | Raw Granger | First-Diff | Perm Granger |
|---|---|---|---|---|
| 0.50 | 0.1 | 6.1% | 5.1% | 5.9% |
| 0.50 | 0.3 | 15.6% | 8.4% | 15.4% |
| 0.50 | 0.6 | 37.7% | 17.7% | 36.8% |
| 0.95 | 0.1 | 11.5% | 6.7% | 11.9% |
| 0.95 | 0.3 | 17.6% | 11.5% | 17.5% |
| 0.95 | 0.6 | 44.3% | 28.7% | 41.5% |
| 0.99 | 0.1 | 12.4% | 5.9% | 12.2% |
| 0.99 | 0.3 | 19.7% | 10.7% | 16.7% |
| 0.99 | 0.6 | 46.4% | 24.6% | 41.7% |

### 关键发现

1. **Raw Granger FPR 膨胀**：φ=0.99 下 FPR 达 11.2%（是名义 5% 的 2.2 倍），但膨胀幅度不如经典文献中 T→∞ 场景那么极端——T=11 的短序列本身就削弱了检测能力
2. **First-Diff 保持 size control**：所有 φ 下 FPR 在 4.2%-6.6%，与名义 5% 一致
3. **Perm Granger 也有 size 膨胀**：φ=0.99 下 FPR=10.7%，因为 permutation 破坏了 x 的自相关结构导致 null distribution 偏移
4. **Power 很低**：T=11 下即使 β=0.6（大效应），校正后的方法 (first-diff) power 也只有 18-29%
5. **Size-adjusted 比较**：Raw/Perm 的高 "power" 部分来自 size inflation。First-diff 是唯一有 proper size control 的方法

---
