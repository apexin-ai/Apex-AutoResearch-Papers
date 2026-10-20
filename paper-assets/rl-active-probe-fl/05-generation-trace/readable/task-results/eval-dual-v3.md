# eval dual v3

**rl active probe fl** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_dual-v3_20260514T094512_result.json`
- **Structured JSON:** [`4af7a2a8ec52b1c5f9e7.json`](../../sessions/4a/4af7a2a8ec52b1c5f9e7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部就绪。汇报：

**Step 1 — 文件同步**: 3 个文件已写入服务器，行数匹配（sandbox.py 355, evaluate.py 315, reward_funcs.py 181）。

**Step 2 — Sandbox 验证**: 7/10 probes 成功执行。3 个 FAIL 均为 buggy_code 自身语法错误（断行的字符串/表达式），非 sandbox 问题。

**Step 3 — 双卡 Eval 已提交**:
- `eval-base-v3` (tmux, GPU 0) — 模型已加载，正在评估 sample 1/202
- `eval-sft-v2` (tmux, GPU 1) — 模型已加载，正在评估 sample 1/202

注：`submit_training_job` 工具不存在于当前 MCP 工具集，改用 tmux session 提交（`tmux attach -t eval-base-v3` / `eval-sft-v2` 可查看实时进度）。SFT eval 中 `--gpu 0` 配合 `CUDA_VISIBLE_DEVICES=1` 使模型看到的逻辑 GPU 为 0，实际使用物理 GPU 1。

---
