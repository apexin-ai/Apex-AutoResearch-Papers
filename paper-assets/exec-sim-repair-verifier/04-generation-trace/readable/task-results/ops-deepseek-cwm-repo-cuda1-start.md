# ops deepseek cwm repo cuda1 start

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_deepseek-cwm-repo-cuda1-start_20260516T080023_result.json`
- **Structured JSON:** [`31925872c205a6b65c26.json`](../../sessions/31/31925872c205a6b65c26.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练正常运行。

## 报告

### 1. cuda:1 之前状态
- cwm-func **已完成**（无 tmux session，GPU 空闲 0 MiB），无需 kill

### 2. Dry-run 结果
- 数据加载正常：train=70,748, val=9,335
- get_target 对 swebench_full 数据工作正常（执行输出格式化为 PASS/FAIL 预测）
- 9.5% 训练样本被截断至 max_seq_length=2048

### 3. 训练启动确认
- **PID**: 479953
- **tmux session**: `deepseek-cwm-repo`
- **总 steps**: 13,266（3 epochs × 70,748 / (batch_size=2 × grad_accum=8)）
- **速度**: ~7.6s/step → 预计 **~28h**（比预估的 20h 长）
- LoRA: rank=16, alpha=32, targets=q/k/v/o_proj, trainable 0.25% (16.7M params)
- Registry 已更新为 RUNNING

### 4. 4 卡 nvidia-smi 快照
| GPU | Util | Memory |
|-----|------|--------|
| 0 | 98% | 19,557 / 32,607 MiB (deepseek-cls-repo) |
| 1 | 99% | 19,713 / 32,607 MiB (**deepseek-cwm-repo** ✓) |
| 2 | 0% | 0 MiB |
| 3 | 89% | 28,099 / 32,607 MiB (eval-cwm-func-s123) |

> 注意：参数名修正了 `--gradient_accumulation_steps` → `--grad_accumulation`，`--learning_rate` → `--lr`。项目路径是 `/home/sonny/exec-sim-repair-verifier`（不是 `/root/autodl-tmp/`）。

---
