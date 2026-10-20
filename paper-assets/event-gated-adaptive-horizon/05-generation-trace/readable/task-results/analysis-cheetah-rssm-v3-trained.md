# analysis cheetah rssm v3 trained

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_cheetah-rssm-v3-trained_20260526T074545_result.json`
- **Structured JSON:** [`8b97604e08dd8d7bf552.json`](../../sessions/8b/8b97604e08dd8d7bf552.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

日志只显示 FutureWarning——这是 Python stdout 缓冲导致（nohup 非终端模式），不影响运行。两个进程 CPU 使用率都很高（2098% / 4258%），说明在正常计算。

汇报：

1. **分析已成功启动** — 模型加载、数据读取均通过，正在计算中
2. **PID**: 540343（Python 子进程），父 shell PID 540342
3. **输出日志**: `/tmp/rssm_v3_cheetah_trained.log`
4. **结果文件**: `logdir/rssm_v3_cheetah_trained_dt_emb.json`
5. **预估完成时间**: 参考先前运行（PID 234523 已跑 ~114 分钟处理 2 个模型），单模型预估 30-60 分钟，当前已运行 ~17 分钟

注意事项：
- 未设置 `CUDA_VISIBLE_DEVICES=""`（因为 `MLP.__init__` 硬编码 `device="cuda"` 为默认值，阻断 CUDA 会导致模型构建失败）。MLP 的 `_std` scalar 会占用极少 GPU 内存，不影响 exp_100 训练
- 服务器上还有一个先前启动的分析进程（PID 234523），同时跑 trained_dt_emb + no_dt_emb，输出到 `rssm_v3_cheetah_results.json`。两个进程不冲突

---
