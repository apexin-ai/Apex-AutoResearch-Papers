# code threecond multiseed r2 v2

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_threecond_multiseed_r2_v2_20260518T080515_result.json`
- **Structured JSON:** [`5b5f35cd01739908942d.json`](../../sessions/5b/5b5f35cd01739908942d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

进程在运行，GPU:0 用了 711 MiB（probe 模型很小，正常）。GPU util 0% 说明当前可能在做 CPU 端数据加载。

任务已正常提交。总结：

**v2 脚本修改了两个 bug**：
1. **Train/val split**：删除 `rng.shuffle(indices)`，改为顺序切分 `i < n_train`（demo 0-39 train, 40-49 val），所有 seed 共享同一 split
2. **R² 空间**：v1 在归一化空间计算 R²（`y_val` 已 z-score），v2 改为反归一化后在原始空间计算（`pred_orig = pred_norm * y_std + y_mean`），匹配 `fulllayer_action_probe.py`

**额外优化**：`build_train_val` 每 layer 只调用一次（split 固定，不依赖 seed），然后 3 个 seed 只改 probe 初始化权重。

**已提交**：`threecond_multiseed_r2_v2` → westd-19183 cuda:0，registry 已更新。日志因 Python pipe buffer 暂时为空，属正常现象，结果会在运行结束时 flush 出来。

---
