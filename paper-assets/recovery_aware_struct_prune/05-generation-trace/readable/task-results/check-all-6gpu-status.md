# check all 6gpu status

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_all_6gpu_status_20260520T141805_result.json`
- **Structured JSON:** [`1987a814bd375facb98b.json`](../../sessions/19/1987a814bd375facb98b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总完成。

| 服务器 | GPU | 实验 | 状态 | 进度/结果 |
|--------|-----|------|------|-----------|
| westd-29022 | cuda:0 | CKA-only 20% seed456 eval | **运行中** | 346/1319 (26%), acc@300=0.670 |
| westd-29022 | cuda:1 | CKA-only 15% eval (v2) | **运行中** | 419/1319 (32%), acc@400=0.745 |
| westd-29022 | cuda:2 | grpo_standard_15_v2 | **已完成** | 100/100 steps, checkpoint 13GB saved |
| westd-29022 | cuda:3 | — | **IDLE** | — |
| westb-23072 | cuda:0 | Qwen CKA-only SFT eval | **运行中** | 143/200 (72%), acc@100=0.540, eos_rate=32% |
| westb-23072 | cuda:1 | Qwen Standard SFT eval | **运行中** | 128/200 (64%), acc@100=0.180, eos_rate=35% |

**关键发现:**

1. **grpo_standard_15_v2 已完成** — 100 steps, 21m49s, checkpoint 已写入 `/root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_15_v2/model.safetensors`。wandb 为 offline 模式（run id: `kh15nsqz`），cuda:2 已释放空闲。

2. **westd-29022 两个 eval 预计还需 ~1.5-2h** — seed456 约 2.6s/it，15% v2 约 2.5s/it。

3. **Qwen eval 速度极慢（~90s/it）**，eos_rate 仅 32-35%，大量样本生成到 max_length 截断。CKA-only (0.540) 远优于 Standard (0.180)。westb 两个 eval 预计还需 ~1-1.5h。

---
