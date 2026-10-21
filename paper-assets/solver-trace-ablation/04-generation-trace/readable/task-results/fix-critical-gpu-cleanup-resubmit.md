# fix critical gpu cleanup resubmit

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_critical-gpu-cleanup-resubmit_20260516T040520_result.json`
- **Structured JSON:** [`e8cf3a1f5da11d6911ec.json`](../../sessions/e8/e8cf3a1f5da11d6911ec.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Step 1-2: GPU 清理
- GPU 0: 16293 MiB → 0 MiB ✓ (kill 631194)
- GPU 1: 80077 MiB → 0 MiB ✓ (kill 626802)
- 额外残留: PID 631803 (GPU 0, 重新出现) → kill → 0 MiB ✓
- 额外残留: PID 632790 (eval_sta.py on GPU 0) → kill → 0 MiB ✓

## Step 3: 模型一致性
- 之前实验模型: Qwen3ForCausalLM (sweep_isr_b005_s42 checkpoint)
- config yaml 模型: `/root/autodl-tmp/models/Qwen3-4B`
- 一致性: **MATCH** ✓
- 修正动作: 无

## Step 5: 提交前验证
- GPU 0: 0 MiB ✓
- GPU 1: 0 MiB ✓

## Step 6-7: 提交
- cuda:0 sweep-isr-b02-s43: PID=633515, tmux=✓
- cuda:1 sweep-isr-b02-s42: PID=633657, tmux=✓
- **注意**: 添加了 `--no_wandb` 参数（服务器 wandb API key 缺失，与之前 worker 处理方式一致）

## Step 8: 30s 后验证
- cuda:0: 80719 MiB, 94% utilization, PID 633515 alive ✓
- cuda:1: 78887 MiB, 94% utilization, PID 633657 alive ✓
- **结论: 双卡满载正常** ✓

---
