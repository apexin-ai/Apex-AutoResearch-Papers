# investigate data file diff D021

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_investigate_data-file-diff-D021_20260514T071513_result.json`
- **Structured JSON:** [`e360aa78ed51da1dfe4a.json`](../../sessions/e3/e360aa78ed51da1dfe4a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。总结关键发现：

---

## 调查结论

### "数据文件不同"假说被证伪

v3 和 ablation-b 的数据**完全相同**（MD5: `c9b59e04de78`），但 v3 仍然 loss 异常。数据不是根因。

v2 的数据确实不同（标签比例反转：internal 67% vs 10%，仅 4 个 task_type vs 11 个），但 **v2 实际收敛了**（eval_loss 0.49），并非完全失败。

### 真正的根因：`upsample_minority`

ablation-b 和 v3 使用同一份数据，配置差异只有两个：

| 配置 | ablation-b (正常) | v3 (异常) |
|---|---|---|
| **upsample_minority** | **true** | false |
| gradient_accumulation | 1 | 8 |

数据极端不平衡（det 89.7% vs int 10.3%）。`upsample_minority=true` 通过 WeightedRandomSampler 让 internal 样本被充分采样，这是 ablation-b 成功的关键。

### class_weights 分析

代码实现正确（`sample_idx` 传递链完整），但 class_weights 只是 0.74x~1.53x 的乘法缩放，不改变 loss 数量级。v2 (有 weights) 和 v3 (无 weights) step 10 loss 一致（48.15），证实 class_weights 无显著影响。

### plan-002 (explicit router)

用 `results/plan_c/` 目录（11 个 labeled_steps.jsonl），同源数据。**也退化了**：全预测 deterministic（internal: 0/30）。

### 建议下一步

1. 重跑 v3 数据但加 `--upsample_minority`（不加 gradient_accumulation=8），验证是否恢复正常
2. 对已收敛的 v2 跑 eval 看 internal recall

---
