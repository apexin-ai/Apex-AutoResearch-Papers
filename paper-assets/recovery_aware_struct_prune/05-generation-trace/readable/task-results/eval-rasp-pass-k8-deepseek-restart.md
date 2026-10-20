# eval rasp pass k8 deepseek restart

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_rasp_pass_k8_deepseek_restart_20260517T020027_result.json`
- **Structured JSON:** [`b432a8e00d85c939c321.json`](../../sessions/b4/b432a8e00d85c939c321.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

启动成功。汇报：

## GPU 状态

| 服务器 | GPU | 状态 | 显存占用 |
|--------|-----|------|----------|
| **westd-11672** | cuda:0 | ~~空闲~~ → 已启动 eval_pass_k8 | 0→加载中 |
| westd-11672 | cuda:1 | 占用 (PID 48541) | 28902/97887 MiB |
| westd-11672 | cuda:2 | 空闲 | 0 MiB |
| westd-11672 | cuda:3 | 占用 (PID 64889) | 29586/97887 MiB |
| **westb-23072** | cuda:0 | 占用 (PID 639423) | 28922/97887 MiB |
| westb-23072 | cuda:1 | 空闲 | 0 MiB |

## eval_pass_k8_rasp_20_grpo_deepseek

- **已成功启动** — PID 67876，westd-11672 cuda:0
- tmux session: `eval_pass_k8_rasp20`
- 日志: `/root/autodl-tmp/recovery_aware_struct_prune/logs/eval_pass_k8_rasp20.log`
- 参数: k=8, temperature=0.7, max_samples=200, max_new_tokens=4096
- 预估时间: 200 samples × 8 generations × 4096 tokens，约 2-4 小时

## eval_grpo_rasp_25 (PID 639423)

仍在运行，westb-23072 cuda:0，已跑约 6.5 小时（386 min），命令为 `eval_gsm8k.py --max_samples 1319`。

---
