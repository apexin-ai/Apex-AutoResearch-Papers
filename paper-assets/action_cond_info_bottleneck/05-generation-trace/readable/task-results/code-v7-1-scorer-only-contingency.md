# code v7 1 scorer only contingency

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_v7_1-scorer-only-contingency_20260516T203549_result.json`
- **Structured JSON:** [`1ad7aa5f401483370611.json`](../../sessions/1a/1ad7aa5f401483370611.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run 完成，训练正常结束。

## 总结

**修改的文件：**
1. `/root/acib/scripts/train_acib.py` — 添加 `--train_scorer_only` / `--freeze_action_expert` CLI 参数，传递到 `ACIBConfig`，添加日志
2. `/root/acib/scripts/run_v7.1_scorer_only.sh` — 新建启动脚本

**冻结逻辑实现：**
- `ACIBConfig` 的 `train_scorer_only=True` 触发 `_setup_freeze()` 中 `self.base_policy.parameters()` 全部 `requires_grad=False`
- `freeze_action_expert=True` 额外冻结 `self._vlm_with_expert.lm_expert`
- 最后强制 `self.scorer.parameters()` 全部 `requires_grad=True`
- optimizer 已有 `trainable_params = [p for p in policy.parameters() if p.requires_grad]`，自动只优化 scorer

**参数数量：**
- Total: 450,169,185
- Trainable (scorer only): 123,009 (0.03%)
- Frozen: 450,046,176

**Dry-run 结果：** 2 步训练成功完成，checkpoint 正常保存。

---
