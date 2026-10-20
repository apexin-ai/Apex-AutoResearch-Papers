# check urgent gpu status

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_urgent_gpu_status_20260524T054011_result.json`
- **Structured JSON:** [`d6c8ea05e9ad569e575d.json`](../../sessions/d6/d6c8ea05e9ad569e575d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告

### GPU 状态：**正常运行中，不需要恢复**

GPU 0% util 是 nvidia-smi 瞬时采样，实际上 PID 149136 正在运行 MMLU eval，占用 17.6GB VRAM。

### Chain 进度（7 步全串行）

| Step | 任务 | 状态 |
|------|------|------|
| 1/7 | SS s123 eval | Done |
| 2/7 | SS s456 resume training | Done |
| 3/7 | SS s456 eval | Done |
| 4/7 | Qwen-1.5B Phase 1 diag | Done |
| 5/7 | Qwen-1.5B TG training | Done |
| 6/7 | Qwen-1.5B eval | Done |
| **7/7** | **MMLU eval (6 checkpoints)** | **Running — 5/6 done, ss_v8b_s42 in progress** |

### MMLU 5-shot 结果（已完成 5/6）

| Condition | Acc |
|-----------|-----|
| base_qwen | 0.7423 |
| pcgrad_v9_s42 | 0.7386 |
| lo_s42 | 0.7357 |
| tg_v7_s42 | 0.7347 |
| ug_s42 | 0.7346 |
| ss_v8b_s42 | **running** |

### Post-chain v2 状态

PID 136975 存活，正在 `while kill -0 108997` 循环中每 60s 轮询等待 chain 完成。Chain 一结束就会自动启动：
1. s123 TF re-eval（GAR-ours + GAR-Dongre）
2. Per-head KL divergence

### 结论

**无需手动干预。** ss_v8b_s42 MMLU eval 大约还需 ~15min 完成，之后 chain 自动结束，post-chain v2 自动接管执行 s123 TF re-eval 和 per-head KL。所有进程链条完整，自动衔接正常。

---
