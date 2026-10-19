# eval exp003s2 batch1 scp eval

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_exp003s2-batch1-scp-eval_20260520T162041_result.json`
- **Structured JSON:** [`8f9d5a73db83de13ed38.json`](../../sessions/8f/8f9d5a73db83de13ed38.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

### 汇报

**Phase 1 SCP**: 成功。通过 tar 打包中转（排除 optimizer.pt，eval 不需要），三个 checkpoint 的 adapter 文件完整传输到 28034。
- 源路径：`29046:/root/autodl-tmp/checkpoints/exp003_r3only_seed2/checkpoint-{500,1000,1500}`
- 目标路径：`28034:/root/autodl-tmp/checkpoints/exp003_s2/checkpoint-{500,1000,1500}`
- 每个 checkpoint 含 adapter_model.safetensors (245MB) + tokenizer + config，共 12 文件

**Phase 3 Eval Jobs**: 三个全部启动

| Job | GPU | PID | tmux session |
|-----|-----|-----|-------------|
| ckpt-500 | cuda:1 | 607796 | `exp-003-s2-eval-ckpt500` |
| ckpt-1000 | cuda:2 | 607932 | `exp-003-s2-eval-ckpt1000` |
| ckpt-1500 | cuda:3 | 608013 | `exp-003-s2-eval-ckpt1500` |

**tmux 确认**: 三个 s2 eval session 均在运行。

---
