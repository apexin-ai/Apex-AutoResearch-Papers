# ssh diagnose occ loss 34685

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_diagnose-occ-loss-34685_20260528T223551_result.json`
- **Structured JSON:** [`be0e75ba8d232458d1f5.json`](../../sessions/be/be0e75ba8d232458d1f5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结论

### 根因：训练命令缺少 `--occ_data_dir` 参数

**调用链分析**：

1. `finetune.py` 中 `occ_data_dir` 默认值为 `""` (空字符串)，训练命令未显式设置
2. 空字符串传入 `RLDSBatchTransform`，`__post_init__` 中 `if self.occ_data_dir:` 为 False → occ 标签从未加载
3. 每个 batch 中不含 `"occ_labels"` 键
4. `run_forward_pass` 中 `if occ_head is not None and "occ_labels" in batch:` 第二个条件始终 False → `metrics["occ_loss"]` 从未被设置
5. 打印时 `metrics.get('occ_loss', 0)` 返回默认值 0

**证据对比**：

| | s1 (成功) | s2_r2 (失败) |
|---|---|---|
| 启动日志 | `Loaded occ index: 9 tasks from /root/occsafe_vla/occ_data/occ_index.json` | **无此行** |
| step 0 occ_loss | 0.1853 | 0.0000 |
| step 50000 occ_loss | 0.0100 | — |

**回答**：
- `occ_loss_weight` 默认 0.01，训练命令未显式设置（但这不是问题）
- 日志中 occ_loss 是真的 0，不是精度问题。`metrics["occ_loss"]` 根本没被赋值
- 历史 s1 实验 occ_loss 非零（0.1853→0.0100），正常
- **这是 bug**：训练命令缺少 `--occ_data_dir /root/occsafe_vla/occ_data`。occ head 虽然初始化了（1,213,313 参数），但从未参与 loss 计算。s2 (非 r2) 也有同样问题

**修复**：重启训练时加上 `--occ_data_dir /root/occsafe_vla/occ_data`。

---
