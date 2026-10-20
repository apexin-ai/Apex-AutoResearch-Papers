# diag plan009 sft baseline s44 1000

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_plan009-sft-baseline-s44-1000_20260515T125154_result.json`
- **Structured JSON:** [`985b5cefd7f2de75793f.json`](../../sessions/98/985b5cefd7f2de75793f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

## 结果

**GPU 当前状态：**
- GPU 0: s43 实验 (pid 352142) 正常运行中，占用 63852 MiB，100% 利用率
- GPU 1: 完全空闲，0 MiB 占用

**OOM 根因：CUDA_VISIBLE_DEVICES 设置错误，不是孤儿进程。**

进程 352142 就是 s43 实验（seed 43），不是孤儿进程。s44 的日志明确显示 `Set CUDA_VISIBLE_DEVICES=0`，这意味着 s44 被错误地映射到了物理 GPU 0（s43 所在的卡），而不是分配的 cuda:1（物理 GPU 1）。两个实验挤在同一张卡上，backward pass 时 OOM 崩溃。

s44 进程已退出（EXIT_CODE=1），输出目录为空，无需清理。

**cuda:1 当前完全空闲可用。** 重试 s44 时需确保 `CUDA_VISIBLE_DEVICES=1`（不是 0）。需要检查 submit_training_job 的 GPU 映射逻辑是否有 bug，或者提交时的参数是否传错了。

---
