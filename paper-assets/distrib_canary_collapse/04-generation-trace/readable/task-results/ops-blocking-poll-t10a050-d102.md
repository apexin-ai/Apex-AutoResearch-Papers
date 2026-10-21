# ops blocking poll t10a050 d102

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_blocking-poll-t10a050-d102_20260522T181729_result.json`
- **Structured JSON:** [`a4e8119deaa47dcc8d33.json`](../../sessions/a4/a4e8119deaa47dcc8d33.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

D102 分析完成，结果如下：

---

```
数据点数: 11 generations (gen_0 to gen_10)
D102 脚本 md5: 318853fa69384ada42458177fdb80940
n_perm: 5000, threshold: true_3sigma_d105

PermG fwd (FDR): 4/8 (vs 截断版 3/8) ← 增加 1 pair
PermG rev (FDR): 2/8 (mauve→te, mauve→ece)
K≥3 consensus:   3/8 (ece→d1, ece→d2, ece→d3)
```

**每个 pair 的 PermG FDR p-value (forward):**
| Pair | p_raw | p_fdr | sig |
|------|-------|-------|-----|
| te→d1 | 0.0236 | **0.0472** | **True** |
| te→d2 | 0.0428 | 0.0683 | False |
| te→d3 | 0.0512 | 0.0683 | False |
| te→mauve | 0.2817 | 0.3220 | False |
| ece→d1 | 0.0042 | **0.0112** | **True** |
| ece→d2 | 0.0026 | **0.0112** | **True** |
| ece→d3 | 0.0042 | **0.0112** | **True** |
| ece→mauve | 0.4581 | 0.4581 | False |

**5 methods forward rate:**
| Method | Forward sig |
|--------|------------|
| PermG (FDR) | 4/8 |
| DiffXCorr (FDR) | 4/8 |
| Threshold 3σ | 2/8 |
| TY Granger | 0/8 |
| NaiveXCorr | (see consensus) |

**与截断版 (gen_0–9) 对比:**
- PermG fwd: 3/8 → **4/8** (加了 gen_10 后 te→d1 从 borderline 翻过 FDR 阈值)
- K≥3: 3/8 → 3/8 (不变)
- gen_10 MAUVE 暴跌至 0.028（vs gen_0 的 0.035），确认 collapse 加剧

**注意:** gen_0/gen_1 的 MAUVE 原为 null，已通过补算脚本 (`fix_mauve_gen01.py`, HF_HOME 指向本地缓存) 填补。all_metrics.json 已 mv 为 .bak 以避免脚本读取旧缓存。

---
