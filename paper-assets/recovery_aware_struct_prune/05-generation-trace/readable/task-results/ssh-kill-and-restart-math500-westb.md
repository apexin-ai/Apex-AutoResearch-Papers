# ssh kill and restart math500 westb

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_kill_and_restart_math500_westb_20260521T134845_result.json`
- **Structured JSON:** [`cfad9ee1a7642d947fe0.json`](../../sessions/cf/cfad9ee1a7642d947fe0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

状态正常。进程 99426 存活，VmRSS=15GB（模型正在 CPU 加载中），232 线程。GPU 0 显示 100% utilization 但无 GPU 进程——这是之前 kill 的进程留下的 stale utilization 计数器，模型还没移到 GPU 上。

**汇报：**

| 项目 | 状态 |
|------|------|
| Kill 90585 (grpo_standard_25) | 已杀死 |
| Kill 95278 (grpo_cka_only_20_v3) | 已杀死 |
| 新 eval PID | **99426** (cuda:0, @2048) |
| GPU 占用 | cuda:0 模型加载中（CPU→GPU），cuda:1 空闲 |
| v1 SFT Standard 25% max_new_tokens | **2048**（JSON 无显式 config 字段，但 response_length 上限=2048，truncated=318/500 = 63.6%） |

注意：首次启动用了错误参数名（`--output_dir`/`--n_samples`/`--temperature`），已更正为 `--output_path`/`--max_samples`（未传=全量500）/无 temperature 参数（脚本无此选项）。

---
