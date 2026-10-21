# launch grpo dual gpu

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_launch_grpo_dual_gpu_20260514T171025_result.json`
- **Structured JSON:** [`683484bf27361ea7edc1.json`](../../sessions/68/683484bf27361ea7edc1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

双 GPU 全部在线训练中。汇报：

### 结果

1. **Qwen3.5-9B 已删除**，autodl-tmp 剩余 190GB（25% 使用）

2. **cuda:0 — GRPO rasp_20** ✅
   - PID 221271，01:08 启动，tmux session `grpo_rasp_20`
   - 62.9GB VRAM, 95% GPU util, 0/5604 steps 开始训练
   - 模型路径：`/root/autodl-tmp/pruned_rasp_20` → 输出 `/root/autodl-tmp/recovered_rasp_20`

3. **cuda:1 — GRPO standard_20** ✅
   - PID 221911，01:14 开始训练，tmux session `grpo_standard_20`
   - 13.3GB VRAM, 94% GPU util, 0/5604 steps
   - 模型路径：`/root/autodl-tmp/pruned_standard_20` → 输出 `/root/autodl-tmp/recovered_standard_20`

4. **cuda:1 上的 25% eval 已 kill**
   - 被 kill 时进度：rasp_20 eval 已完成（结果在 `results/eval_pruned_rasp_20_quick.json`），standard_25 eval 在 71/100，rasp_25 eval 未开始

---
