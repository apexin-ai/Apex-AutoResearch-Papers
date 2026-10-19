# fix westd vllm compat

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_westd-vllm-compat_20260517T144509_result.json`
- **Structured JSON:** [`c1237f6ea01a5c416b51.json`](../../sessions/c1/c1237f6ea01a5c416b51.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练已成功启动。

## 产出总结

### 1. 版本对比
两台服务器版本完全一致：
| 包 | bjb1-17606 | westd-47453 |
|---|---|---|
| torch | 2.10.0+cu128 | 2.10.0+cu128 |
| vllm | 0.18.1 | 0.18.1 |
| transformers | 4.57.6 | 4.57.6 |
| verl | 0.6.1 (editable) | 0.6.1 (editable) |

### 2. 修复方案
**根因**：`torch._inductor/select_algorithm.py` 的 `duplicate template name` 是 torch inductor 在特定 GPU 架构（RTX PRO 6000）上的已知 bug。bjb1 没触发可能因为其 A6000 架构的 inductor kernel 模板集不同。

**修复**：`export TORCH_COMPILE_DISABLE=1` — 禁用 torch.compile/inductor 编译路径。vLLM config 中已有 `enforce_eager: True`，但 `TORCH_COMPILE_DISABLE=1` 在更底层彻底阻断了 inductor 模板注册。

### 3. 重启信息
- **PID**: 85798
- **W&B run**: `gsweep-g050-h5-seed1` — https://wandb.ai/xiaoyucorynne-/cost-verify-agent-rl/runs/r6rgpd3p
- **Server**: westd-47453, cuda:2,3
- **tmux session**: `gsweep_g050_h5_seed1`

---
