# analysis eval perdof object norm03 seed44

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval-perdof-object-norm03-seed44_20260517T044304_result.json`
- **Structured JSON:** [`a8aad3cb3332919a9949.json`](../../sessions/a8/a8aad3cb3332919a9949.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验分析完成。结果如下：

## eval-perdof-object-norm03-seed44 结果

| 指标 | 值 |
|------|-----|
| **Overall success rate** | **4.0% (4/100)** |
| Total episodes | 100 (10 tasks × 10 rollouts) |
| 异常 | 无（EXIT_CODE=0，所有 100 episodes 正常完成） |
| W&B run_id | **无** — 日志中无 W&B 记录，该评估未上传 W&B |

### Per-task breakdown

| Task | Success |
|------|---------|
| alphabet_soup | 0/10 |
| cream_cheese | 1/10 |
| salad_dressing | 0/10 |
| bbq_sauce | 1/10 |
| ketchup | 0/10 |
| tomato_sauce | 0/10 |
| butter | 1/10 |
| milk | 0/10 |
| chocolate_pudding | 1/10 |
| orange_juice | 0/10 |

### 关键观察

**seed44 = 4%，与 seed42 = 4% 完全一致。** 多 seed 确认 perdof 在 norm=0.3 下的 progressive collapse 是确定性现象，不是随机波动。

对比：
- perdof norm=0.3: seed42=4%, seed44=4% → 稳定退化
- obs_only norm=0.3: seed42=19%（作为参照）

结论：perdof 在高修正幅度下的 collapse 机制得到多 seed 验证。4% 几乎等于随机成功，说明 perdof 的 per-DOF correction 在 norm=0.3 时系统性地破坏了动作质量。

---
