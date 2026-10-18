# eval random prune baseline

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_random_prune_baseline_20260517T080830_result.json`
- **Structured JSON:** [`493ec67bc26ec58dd4d1.json`](../../sessions/49/493ec67bc26ec58dd4d1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

eval 正常运行中。Task 0 前 19 episodes 全部 FAIL，与 ACIS pruning 模式一致。

**总结：**
- random_prune eval 已在 westd-27271 GPU 0 启动，tmux session: `eval_random_prune_k05`
- 模式确认：`compute_random_mask` 用 `torch.rand` 生成随机 scores，保留 50% tokens
- Hook 使用 offset-tracking 方法正确执行 masking
- 代码中无 AUDIT 打印（但 hook 逻辑已通过代码审查确认正确）
- 当前进度：Task 0 ep 19/50，全部 FAIL
- 预计 ~40-50 min 完成全部 10 tasks × 50 episodes
- 日志：`eval_results/eval_random_prune_k05.log`
- 结果输出：`eval_results/eval_random_prune_k05_object.json`

初步趋势：random_prune 也是 0% SR，和 ACIS pruning 一致，倾向于**模型结构性不容忍 50% token pruning**（而非 ACIS ranking 错误）。

---
