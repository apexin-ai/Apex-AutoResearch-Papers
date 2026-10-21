# ssh submit floor ablation 0p3 westd0

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_submit_floor_ablation_0p3_westd0_20260523T075001_result.json`
- **Structured JSON:** [`0041709f84d20db98480.json`](../../sessions/00/0041709f84d20db98480.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务已提交并运行中。

**汇报**:
- **PID**: 114044（tmux session: `floor_ablation_0p3_cka_only_20`）
- **进程状态**: 存活，正在执行 Step 1/4 — 剪枝 CKA-only, sparsity=20%, floor=0.3
- **GPU 0**: 当前显存 3MiB（模型刚加载完权重，还未上 GPU 做推理），空闲可用
- **日志前几行**:
  ```
  Floor Ratio Ablation: floor=0.3
  GPU: 0
  [Step 1/4] Pruning CKA-only, sparsity=20%, floor=0.3 ...
  Loading model from /root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B
  Loading weights: 100%|██████████| 339/339 [00:00<00:00, 12068.76it/s]
  ```
- **日志路径**: `~/runs/recovery_aware_struct_prune/floor_ablation_0p3_cka_only_20.log`

模型权重已加载完毕，pipeline 正常启动。

---
