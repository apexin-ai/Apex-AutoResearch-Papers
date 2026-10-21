# ssh d1d3 eval mvp

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_d1d3_eval_mvp_20260514T160902_result.json`
- **Structured JSON:** [`0638907f8207d45f12a3.json`](../../sessions/06/0638907f8207d45f12a3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果如下：

```
=======================================================
=== FULL d1-d3 (N=15000, test=3000) ===
=======================================================
Sample counts: d1=5000, d2=5000, d3=5000
3-class acc: 0.7083 [95% CI: 0.6923, 0.7250]
MAE: 0.3203
Per-class recall:    d1=0.790, d2=0.607, d3=0.728
Per-class precision: d1=0.852, d2=0.605, d3=0.680
Per-class F1:        d1=0.820, d2=0.606, d3=0.703
Pairwise AUC: d1v2: 0.854, d1v3: 0.9569, d2v3: 0.7931

Confusion matrix:
         pred_d1  pred_d2  pred_d3
d1       790     147      63
d2       114     607     279
d3        23     249     728

Top-5 features: var_surprisal (0.1505), p90_ppl (0.1335), p75_ppl (0.0770),
                mean_ppl (0.0688), mean_surprisal (0.0640)

=======================================================
=== FILTERED d1-d3 (code/HTML removed) (N=12012, test=2403) ===
=======================================================
Sample counts: d1=4231, d2=4002, d3=3779
3-class acc: 0.7466 [95% CI: 0.7274, 0.7636]
MAE: 0.2759
Per-class recall:    d1=0.862, d2=0.635, d3=0.735
Per-class precision: d1=0.867, d2=0.659, d3=0.704
Per-class F1:        d1=0.864, d2=0.647, d3=0.719
Pairwise AUC: d1v2: 0.8926, d1v3: 0.9769, d2v3: 0.8272

Confusion matrix:
         pred_d1  pred_d2  pred_d3
d1       729      84      33
d2        91     509     201
d3        21     179     556

Top-5 features: p90_ppl (0.1577), var_surprisal (0.1482), p75_ppl (0.0829),
                mean_ppl (0.0669), mean_surprisal (0.0653)
```

**关键发现：**

- **d2 是瓶颈**：full 子集 d2 recall 仅 60.7%，d2 大量被误判为 d3（279/1000），印证了 Reviewer 的疑虑
- **Filtered 子集全面提升**：去除 code/HTML confound 后，3-class acc 从 70.8% 升至 74.7%，d2 recall 从 60.7% 升至 63.5%，所有 pairwise AUC 均上升。说明分类信号不依赖 content-type confound，filtered 后反而更干净
- **d1v3 区分能力很强**（AUC 0.957/0.977），主要难点在 d2 与 d3 的区分（AUC 0.793/0.827）
- **Top features 一致**：var_surprisal 和 p90_ppl 在两个子集中都是最重要的特征

---
