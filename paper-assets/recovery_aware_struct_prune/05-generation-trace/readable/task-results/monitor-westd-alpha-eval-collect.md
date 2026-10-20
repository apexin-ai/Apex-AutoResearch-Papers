# monitor westd alpha eval collect

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_westd-alpha-eval-collect_20260515T150453_result.json`
- **Structured JSON:** [`e0425f5fe76eab52e4e9.json`](../../sessions/e0/e0425f5fe76eab52e4e9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

### 三个进程全部在运行

| 任务 | PID | GPU | 进度 | ETA |
|------|-----|-----|------|-----|
| GraSP N=100 eval | 38120 | cuda:0 (90%, 13GB) | **48/100** samples, ~51s/sample | ~44 min |
| α=1.0 SFT eval | 42535 | cuda:1 (29GB) | **34/100** samples, 速度不均(3s~8min/sample) | 不确定 |
| α=2.0 SFT | 43065 | cuda:1 (51GB) | **240/1870** steps (12.8%), ~1.7s/step, loss=0.871 | ~47 min |

### α=2.0 SFT 训练趋势
Loss 稳步下降: 1.113 → 1.056 → 1.039 → 1.029 → 0.963 → 0.871，token accuracy 从 0.743 升至 0.785。

### α=0.5 SFT — 无需启动
`/root/autodl-tmp/recovery_aware_struct_prune/sft_ablation/alpha_0.5/` 已有完整模型（model.safetensors + config），SFT 已完成。

### 结论
三个任务都在正常推进，无异常。cuda:0 上 GraSP eval 完成后会释放 GPU，但 α=0.5 SFT 已经做过了，不需要再启动。等 GraSP eval 和 α=1.0 eval 完成后可收集结果 JSON。

---
