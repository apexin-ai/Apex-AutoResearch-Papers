# check gpu status medium

**The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_gpu_status_medium_20260514T005220_result.json`
- **Structured JSON:** [`fbf3a97cb82bf9cb218a.json`](../../sessions/fb/fbf3a97cb82bf9cb218a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

### GPU 状态
| GPU | 利用率 | 显存 |
|-----|--------|------|
| cuda:0 | 33% | 71.6/97.9 GB |
| cuda:1 | 0% | 28.7/97.9 GB |

### medium_rgds_seed42 (cuda:0) — ✅ 已完成
Gen 7/7 全部跑完，已自动衔接 **medium_random50** (当前 Gen 3/7 训练中)。

```
Gen 0: ppl=26.04, rankme=365.07, knn=0.988, rare=0.0346, corr=0.0196, ratio=0.9759
Gen 1: ppl=32.99, rankme=398.29, knn=0.988, rare=0.0286, corr=0.0402, ratio=0.9991
Gen 2: ppl=41.99, rankme=418.21, knn=0.988, rare=0.0232, corr=0.0014, ratio=0.9225
Gen 3: ppl=50.80, rankme=421.44, knn=0.988, rare=0.0198, corr=0.0058, ratio=0.9127
Gen 4: ppl=60.71, rankme=425.62, knn=0.988, rare=0.0187, corr=-0.0068, ratio=0.7989
Gen 5: ppl=66.29, rankme=424.71, knn=0.988, rare=0.0180, corr=-0.0235, ratio=0.9002
Gen 6: ppl=72.00, rankme=423.93, knn=0.988, rare=0.0168, corr=-0.0197, ratio=0.7622
Gen 7: ppl=82.84, rankme=424.72, knn=0.988, rare=0.0166, corr=-0.0286, ratio=0.8313
```

Registry 已更新为 DONE/success。

### medium_external_seed42 (cuda:1) — 🔄 进行中
当前 **Gen 3/7**，正在训练 student。tmux session `chain_cuda1` 运行中。cuda:1 利用率 0% 说明刚好在训练间隙或数据准备阶段。

### tmux sessions
- `chain_cuda0` ✅ 运行中（已衔接 medium_random50）
- `chain_cuda1` ✅ 运行中（medium_external Gen 3）

---
