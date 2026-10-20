# train 8b dryrun and launch

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_8b-dryrun-and-launch_20260522T031501_result.json`
- **Structured JSON:** [`705b942143f863c24b35.json`](../../sessions/70/705b942143f863c24b35.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**阻塞：GPU 0 被 s46 训练占用。**

PID 947050 正在运行 `exec_only_s46_1000_k4.yaml`，已跑 ~59 分钟（10:16 启动），占用 63.7GB 显存。按 s45 的 8139s/1000步 估算，还需 ~76 分钟完成。

服务器只有 1 张 GPU，无法并行跑 dry-run。

**Phase 3 (s45) 结果已出：**
- checkpoint: 模型权重直接存在输出目录（非 checkpoint-1000 子目录）
- eval_sta.json: 存在 (183KB)
- reward_log.jsonl: 1003 行（1000 步完成）
- 最终指标: parse_rate=1.0, prove_rate=0.1495, mean_isr=0.0734

**需要你决定：** kill s46 训练立即开始 8B dry-run + s42，还是等 s46 跑完（~76 min）再开始？

---
