# analysis eval official smolvla baseline

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval_official_smolvla_baseline_20260518T135729_result.json`
- **Structured JSON:** [`16ea6870eaab937f49de.json`](../../sessions/16/16ea6870eaab937f49de.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE。总结如下：

## 结果

**Overall SR: 59.2% (296/500)**, 95% Wilson CI: [54.8%, 63.4%]

| Task | Object | SR |
|------|--------|-----|
| 0 | alphabet soup | 64% |
| 1 | cream cheese | 40% |
| 2 | salad dressing | 44% |
| 3 | bbq sauce | **38%** (最低) |
| 4 | ketchup | 60% |
| 5 | tomato sauce | 46% |
| 6 | butter | 78% |
| 7 | milk | 52% |
| 8 | chocolate pudding | **90%** (最高) |
| 9 | orange juice | 80% |

## 与 hypothesis 对比

Official checkpoint 的 **59.2%** 显著高于我们 fine-tuned baseline 的 **44.8%**，差距约 14.4 个百分点。这说明：

1. **Official checkpoint 训练质量更高**：可能使用了更多数据、更长训练、或更优超参数，其 unpruned 性能本身就更强。
2. **我们的 fine-tuned checkpoint 存在训练效果损失**：44.8% 并非 SmolVLA 在 LIBERO-Object 上的性能上限，fine-tuning 流程可能有改进空间。
3. **对论文的意义**：pruning 实验如果以 official checkpoint 为基准，baseline 更高（59.2%），pruning 后的性能下降幅度会更有说服力。论文中应报告 official checkpoint baseline 作为更可靠的参考点，或至少在两个 baseline 上都展示 pruning 效果。

---
