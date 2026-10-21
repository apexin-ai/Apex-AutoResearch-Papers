# eval 8b ckpt3000 test westd gpu1

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_8b-ckpt3000-test-westd-gpu1_20260514T202216_result.json`
- **Structured JSON:** [`9f06c90c8cde3fdd61ec.json`](../../sessions/9f/9f06c90c8cde3fdd61ec.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

推理正常运行中。10 samples 用了 ~4 秒，每 sample ~0.4 秒。按此速度预计 ~65 分钟完成 9784 samples。

**汇总：**
- **ckpt-3000 位置**：`/root/autodl-tmp/checkpoints_repo_cls_8b/checkpoint-3000`（不在 `_conda` 目录，那个只到 step 600）
- **可用 checkpoints（_conda 目录）**：checkpoint-200, 400, 600
- **可用 checkpoints（原目录）**：checkpoint-3000 确认存在且完整
- **已启动 test eval**：
  - PID: 282767
  - tmux session: `cls8b-ckpt3000-test-v2`
  - log: `~/runs/exec-sim-repair-verifier/cls8b-ckpt3000-test-v2.log`
  - GPU 1, batch_size=1（GPU 1 同时跑着 4B v5 val eval，空间紧张，batch_size=16 OOM 后降到 1 成功）
  - 速度 ~0.4s/sample，预计 **~65 分钟**完成
- **注意**：GPU 1 并非空闲，PID 281646（4B v5_conda ckpt-400 val eval）正占 13.6 GiB。4B eval 结束后 8B eval 会有更多余量，但当前已在正常推理。

---
