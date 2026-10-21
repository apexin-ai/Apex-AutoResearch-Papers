# exec fix westd multiseed

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exec_fix_westd_multiseed_20260517T045654_result.json`
- **Structured JSON:** [`03955761e9b263f66c70.json`](../../sessions/03/03955761e9b263f66c70.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个 eval 全部正常运行。模型正在 CPU 内存加载中（每个进程 ~14-17GB RSS），还没移到 GPU。这是正常行为——pruned model 文件大，CPU 加载完才会 `.to(device)`。

## 结果

4 个 multi-seed eval job 已修复并成功启动：

| tmux session | GPU | 模型 | seed | PID |
|---|---|---|---|---|
| `eval_sft_rasp_20_seed123` | cuda:0 | sft_rasp_20_westd | 123 | 75158 |
| `eval_sft_standard_20_seed123` | cuda:1 | sft_standard_20_westd | 123 | 75234 |
| `eval_sft_rasp_20_seed456` | cuda:2 | sft_rasp_20_westd | 456 | 75308 |
| `eval_sft_standard_20_seed456` | cuda:3 | sft_standard_20_westd | 456 | 75384 |

**修复的问题：**
- 脚本路径：`src/eval_gsm8k.py`（从 `src/` 子目录执行）
- 模型路径：`/root/autodl-tmp/recovery_aware_struct_prune/sft_{rasp,standard}_20_westd`
- 参数确认：`--max_samples 200` 正确

所有进程 CPU 占用率 ~500%+ 且内存 ~14GB，正处于模型加载阶段，即将转入 GPU 推理。

---
