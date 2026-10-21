# eval bypass imm100k retry

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_bypass_imm100k_retry_20260517T033907_result.json`
- **Structured JSON:** [`4a12eca60c9b3c421806.json`](../../sessions/4a/4a12eca60c9b3c421806.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

1. **PID 876813 已终止**（原错误进程）
2. **PID 876817/876818 已终止**（之前遗留的旧进程）
3. **新 eval 已启动** — PID 882658，运行正常
   - 模型加载成功 (14s)
   - 正在评估 libero_object (10 tasks, 50 episodes)
   - 无 error，只有 robosuite 常规 warnings
4. **Registry 已更新**

注意：Director 原始命令中 `--device cuda:0` 是无效参数，脚本实际使用 `--gpu 0`，已修正。

---
