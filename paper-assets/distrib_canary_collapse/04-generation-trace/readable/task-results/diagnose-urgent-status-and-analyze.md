# diagnose urgent status and analyze

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_urgent_status_and_analyze_20260517T233942_result.json`
- **Structured JSON:** [`cc78e04ed88cf5733bda.json`](../../sessions/cc/cc78e04ed88cf5733bda.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 产出总结

### 1. 实验状态

| 实验 | 状态 |
|------|------|
| **Pythia-1.4B / Wiki (s42)** | 完成 (EXIT_CODE=0, gen_0~gen_10 全部完成) |
| **Pythia-1B / C4 (s43)** | 运行中 — gen_9 training (1537/5000 steps, ~30%), 预计 ~25min 完成全部 |

### 2. Pythia-1.4B 8-pair 分析结果

8 canonical pairs: {token_entropy, ECE} → {perplexity, distinct_1, distinct_2, distinct_3}

| Method | Significant pairs |
|--------|------------------|
| Naive | 7/8 |
| Diff XCorr | 6/8 |
| Threshold | 8/8 |
| PermG (fwd) | 5/8 |
| PermG (rev) | **0/8** |
| TY | 0/8 |
| K≥4/5 | **5/8** |

**对比 410M baseline (K≥4=6/8, PermG=6/8, TY=6/8):**
- K≥4 降低 (5/8 vs 6/8)，主要因为 token_entropy→perplexity (K=1) 和 token_entropy→distinct_3 (K=3) 两对未达阈值
- TY 全部失效 (0/8) — 与 GPT-2-medium 相同，短时序 + 高积分阶数导致 df_resid 过低
- PermG fwd 也有所下降 (5/8 vs 6/8)
- 反向 PermG 保持 0/8 — 方向性完美，与所有其他实验一致
- Threshold 表现最强 (8/8) — 与 OPT-1.3B 相同模式

### 3. Table 7 已更新

`docs/paper/experiments.tex` Scale 行已填入:
```
Scale ($3.4\times$) & Pythia-1.4B / Wiki & 7/8 & 6/8 & 8/8 & 5/8 & 0/8 & 0/8 & 5/8
```
Caption 中 `[TBD]` 注释已移除。

### 4. C4 seed-43 进度

gen_0~gen_8 完整，gen_9 正在训练 (30% done, ~8.63 it/s)。预计 ~25 分钟完成全部 10 代。

---
