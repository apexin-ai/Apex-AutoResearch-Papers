# submit bce v3 force

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_submit_bce_v3_force_20260516T043540_result.json`
- **Structured JSON:** [`81cb449bb9a474be9505.json`](../../sessions/81/81cb449bb9a474be9505.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

**Step 1** — 找到 D029 父脚本 `run_bench_cuda1.sh`（PID 195904），顺序执行 5 个 benchmark，当前跑到第 4/5 个 bench_bce_iso50_s42（PID 204687，cuda:1 占 37GB）。已杀掉父子进程。

**Step 2** — cuda:1 释放到 0 MiB。

**Step 3** — 启动 BCE v3，首次因模型路径用了 HF cache snapshot 格式（已不存在）导致 `HFValidationError`。改用 `/root/autodl-tmp/models/llama-3.1-8b` 成功启动。

**Step 4** — 验证通过：
- PID 205597 运行中
- 模型加载完成（291/291 weights），Trainable 0.946%
- 数据集从缓存加载成功
- cuda:1 显存 90.7GB

**Step 5** — Registry 已推进到 RUNNING，cron 监控已注册（120s 间隔）。

---
