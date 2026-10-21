# analysis formal shape test

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_formal-shape-test_20260522T114131_result.json`
- **Structured JSON:** [`726dba4d7317bf0d3ac3.json`](../../sessions/72/726dba4d7317bf0d3ac3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。输出文件：
- `artifacts/shape_test/shape_test_results.json`
- `artifacts/shape_test/shape_test_analysis.md`

核心结果：

**Version A（排除 sync-dip）：**

| Row | ΔAIC(smooth vs step) | Preferred |
|-----|---------------------|-----------|
| T=5 phase | — | trivial (all 0) |
| T=10 phase (3pt) | +2.0 | step |
| T=10 dense (14pt) | **−63.8** | **smooth** |
| T=15 phase (3pt) | +2.0 | step (LL 相同) |
| T=20 phase (3pt) | +1.4 | step |
| T=25 phase (4pt) | +1.9 | step |

**Version B（含 sync-dip）：**

| Row | ΔAIC(smooth vs step) | Preferred |
|-----|---------------------|-----------|
| T=10 phase (4pt) | +0.8 | step |
| T=10 dense (17pt) | **−110.0** | **smooth** |
| T=15 phase (4pt) | −3.1 | smooth |
| T=20 phase (4pt) | −5.1 | smooth |
| T=25 phase (4pt) | +1.9 | step |

关键发现：

1. **Phase diagram 各行只有 3-4 个数据点**，区分能力极弱——sigmoid 优化后收敛到 step function（k→500），LL 与 step 相同。排除 sync-dip 后全部 favor step（纯因参数惩罚）。

2. **T=10 dense（14-17 点）是唯一有真实区分力的数据**，sigmoid 以 ΔAIC=−64 到 −110 碾压 step。拟合参数：k≈15, α_0≈0.68-0.72，描述 α≈0.5-0.7 区间的渐进上升。

3. **Version B 中 T=15/T=20 smooth 胜出完全由 sync-dip 驱动**——α=0.60 的 0/8 让 step model 承受巨大 LL 惩罚（−11.09），sigmoid 通过降低整体预测概率来缓冲。排除 sync-dip 后这一优势消失。

4. Smooth(P_max free) 相比 smooth(P_max=0.75 fixed) 几乎无额外收益——拟合出的 P_max≈0.75-0.78，多一个参数不值得。

---
