# ops westd41074 disk cleanup m64 restart

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd41074-disk-cleanup-m64-restart_20260521T024216_result.json`
- **Structured JSON:** [`97a958f48beaf1bf42ec.json`](../../sessions/97/97a958f48beaf1bf42ec.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

### 执行结果

| Step | 操作 | 回收空间 | 状态 |
|------|------|---------|------|
| 1 | 删除损坏 M64 checkpoint | ~14G | 完成 |
| 2 | 删除 OpenVLA spatial/goal/10 | ~45G | 完成 |
| 3 | .hf_cache 清理 | 跳过 (仅 164M，无大文件) | N/A |
| 4 | M96 save_every | 运行时无法修改 | 见下方说明 |
| 5 | M64 重训 cuda:3 | - | 已启动，初始化中 |

**磁盘**: 250G → 194G used, **57G 可用** (78%)

**M96 说明**: `save_every` 在启动时读取 (line 527)，运行中改配置文件无效。当前 step ~40550，~5.3h 后到 step 50000 触发保存。57G 可用空间远大于 checkpoint 大小 (~14G)，**不会再因磁盘满 crash**。

**M64 重训**: `train_openvla_sc_m64_seed42_v4` 在 cuda:3 启动，save_every=10000，PID 738642，正在计算 action statistics (273K 样本，需几分钟)，预计很快进入训练 step。

---
