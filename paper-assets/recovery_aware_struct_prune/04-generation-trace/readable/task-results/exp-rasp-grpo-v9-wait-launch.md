# exp rasp grpo v9 wait launch

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_rasp-grpo-v9-wait-launch_20260515T224025_result.json`
- **Structured JSON:** [`2255ad89c0de6f88a633.json`](../../sessions/22/2255ad89c0de6f88a633.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 摘要

**α sweep 仍在 cuda:0 上运行**（当前 α=0.5 eval，后续 α=1.0, 2.0）。15 次轮询内未完成（实际间隔 <5min，sweep 预计还需 ~90min）。

**已部署自动启动器** `auto_v9_launcher`（tmux session），逻辑：
1. 每 120s 检查 sweep 是否完成（4 个结果文件 or sweep 进程退出）
2. 等 GPU 0 显存释放 < 1000 MiB
3. 清理旧 GRPO v2-v8 目录
4. 启动 GRPO v9（tmux `grpo_rasp_v9`）
5. 验证 + 收集 α sweep 全部结果

**已有 α sweep 结果**：

| α | accuracy | eos_rate | avg_len |
|---|----------|----------|---------|
| 0.0 | 0.27 | 0.80 | 1192 |
| 0.25 | 0.23 | 0.63 | 1834 |
| 0.5 | pending | — | — |
| 1.0 | pending | — | — |
| 2.0 | pending | — | — |

**Registry 更新**：
- `grpo_stage2_rasp_20_v9`: QUEUED（auto-launcher 待启动）
- `alpha_ablation_sweep`: RUNNING（部分结果已记录）

**监控命令**：
```
ssh_read_only: tail -20 /tmp/auto_launch_grpo_v9.log
```

---
