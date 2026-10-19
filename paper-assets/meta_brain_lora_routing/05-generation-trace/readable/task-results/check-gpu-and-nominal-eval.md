# check gpu and nominal eval

**Meta-Brain: Perturbation-Diagnostic Routing of LoRA Experts for Parameter-E cient VLA Robustness** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_gpu_and_nominal_eval_20260516T204327_result.json`
- **Structured JSON:** [`22c142d255b434c73253.json`](../../sessions/22/22c142d255b434c73253.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### GPU 使用情况

| GPU | Util | Mem | 进程 |
|-----|------|-----|------|
| 0 | 0% | 7799/97887 MiB | PID 29928: `serve_policy.py --port 8000` (pi0_libero_finetuned_openpi_format) |
| 1 | 99% | 12851/97887 MiB | PID 118486: `train_lora_expert.py --perturbation_type universal --lora_rank 48` (v3_lora_universal_r48, 10000 steps) |
| 2 | 0% | 空闲 | — |
| 3 | 0% | 空闲 | — |

4x NVIDIA RTX PRO 6000 Blackwell Server Edition (98GB each)

### PID 117988 (nominal 50-ep eval)

**已结束。** 进程不存在。无 eval 相关进程在跑。

### Nominal 50-ep Eval 结果

**文件**: `/tmp/eval_50ep_baseline.log`  
**Checkpoint**: `pi0_libero_openpi` (base, no LoRA, routing=none)  
**时间**: 2026-05-17 04:29  
**Suite**: libero_spatial (9 tasks × ~5-6 seeds each = 50 episodes)

**Success rate: 33/50 = 66.0%**

逐 episode 结果（按 task 聚合）：

| Task | 结果 (按 seed 轮次) | 成功率 |
|------|---------------------|--------|
| between plate and ramekin | ✓✗✓✓✓✓ | 5/6 |
| top drawer of wooden cabinet | ✗✓✗✓✓✓ | 4/6 |
| next to cookie box | ✓✓✓✓✓✓ | 6/6 |
| next to plate | ✓✗✓✗✓✗ | 3/6 |
| next to ramekin | ✗✓✗✓✗✓ | 3/6 |
| on cookie box | ✓✓✓✓✗— | 4/5 |
| on the ramekin | ✗✗✗✗✓— | 1/5 |
| on the stove | ✗✓✓✓✓— | 4/5 |
| on wooden cabinet | ✓✗✓✓✗— | 3/5 |

**最难 task**: "on the ramekin" (1/5 = 20%)  
**最易 task**: "next to cookie box" (6/6 = 100%)

### 另有一个 10-ep 预跑

`/tmp/eval_base_no_lora.log` — 同一 checkpoint，10 episodes，6/10 = 60.0%（与 50-ep 结果基本一致）

---
