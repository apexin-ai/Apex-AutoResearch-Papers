# ssh emergency disk cleanup westd

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_emergency_disk_cleanup_westd_20260523T091741_result.json`
- **Structured JSON:** [`ee199803c77648710968.json`](../../sessions/ee/ee199803c77648710968.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

wandb 很小，不需要清理。

**清理完成。汇报：**

| 指标 | 清理前 | 清理后 |
|------|--------|--------|
| 已用 | 650G (100%) | 475G (73%) |
| 可用 | 1.3M | **176G** |
| 释放总量 | — | **~175G** |

**删除内容：**
1. **optimizer.pt** × 1（~14G，grpo_cka_only_20_floor_0.3）
2. **scheduler.pt** × 7（grpo_alpha4_20, grpo_random_20, grpo_random_20_seed123_v2, grpo_cka_only_20_floor_0.3, grpo_rasp_alpha0p5_20, grpo_rasp_alpha2p0_20, grpo_depth_first_20）
3. **training_args.bin** × 5
4. **重复 checkpoint 目录** × 9（与顶层 model.safetensors 重复，~109G）：grpo_alpha4_20, grpo_cka_only_15_seed123, grpo_cka_only_20_floor_0.3, grpo_depth_first_20, grpo_random_20_seed123_v2, grpo_rasp_alpha0p5_20, grpo_rasp_alpha2p0_20, sft_alpha4_20, sft_cka_only_20_floor_0.3
5. **跨服务器副本** × 5（westb-23072 上有原始，~60G）：grpo_cka_only_20, grpo_rasp_alpha0p5_20, sft_cka_only_20, sft_random_20, sft_rasp_alpha3p0_20

---
