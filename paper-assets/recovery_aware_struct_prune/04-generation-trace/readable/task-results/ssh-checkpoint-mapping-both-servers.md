# ssh checkpoint mapping both servers

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_checkpoint_mapping_both_servers_20260523T152215_result.json`
- **Structured JSON:** [`d718563b11964348e817.json`](../../sessions/d7/d718563b11964348e817.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据已收集完毕。

## Checkpoint 完整映射表

| checkpoint | westd-32935 | westb-23072 | model size |
|---|---|---|---|
| **grpo_alpha4_20** | ✓ | ✗ | 11.5G |
| **grpo_alpha4_20_eval** | ✗ | ✓ | 2.8G |
| **grpo_cka_only_15_seed123** | ✓ | ✗ | 1.5G |
| grpo_cka_only_15_seed456 | ✗ (dir only) | ✗ | — |
| **grpo_cka_only_20** | ✗ | ✓ (ckpt-100) | 11.5G |
| **grpo_cka_only_20_1p5b** | ✗ | ✓ (ckpt-100) | 2.7G |
| **grpo_cka_only_20_floor_0.3** | ✓ | ✗ | 11.5G |
| **grpo_cka_only_20_floor_0.5** | ✓ | ✗ | 11.5G |
| **grpo_cka_only_20_floor_0.6** | ✓ (+ckpt-100) | ✗ | 11.5G |
| **grpo_cka_only_20_seed123** | ✗ | ✓ | 11.5G |
| **grpo_cka_only_20_seed456** | ✓ | ✗ | 11.5G |
| **grpo_cka_only_25** | ✓ | ✗ | 10.8G |
| **grpo_depth_first_20** | ✓ | ✗ | 11.5G |
| **grpo_qwen_math_cka_only_20** | ✗ | ✓ | 11.5G |
| grpo_random_20 | ✗ (dir only) | ✗ | — |
| **grpo_random_20_seed123_v2** | ✓ | ✗ | 11.3G |
| **grpo_rasp_20_1p5b** | ✗ | ✓ (ckpt-100) | 2.7G |
| grpo_rasp_20_seed456 | ✗ (dir only) | ✗ | — |
| **grpo_rasp_25** | ✓ | ✗ | 10.8G |
| grpo_rasp_25_transfer_log | ✗ (dir only) | ✗ | — |
| **grpo_rasp_alpha0p5_20** | ✗ | ✓ | 11.5G |
| **grpo_rasp_alpha2p0_20** | ✓ | ✗ | 11.5G |
| grpo_rasp_alpha3p0_20_v2 | ✗ (dir only) | ✗ | — |
| **grpo_stage2_rasp_20_fair** | ✓ | ✗ | 11.5G |
| **grpo_stage2_standard_20_fair** | ✓ | ✗ | 11.5G |
| **grpo_standard_20_1p5b** | ✗ | ✓ | 2.7G |
| **grpo_standard_20_seed123** | ✓ | ✗ | 11.5G |
| **grpo_standard_20_seed456** | ✓ | ✗ | 11.5G |
| **grpo_standard_25** | ✓ | ✗ | 10.8G |
| **pruned_alpha4_20** | ✓ | ✗ | 11.5G |
| **pruned_cka_only_15** | ✓ | ✗ | 12.2G |
| **pruned_cka_only_20_1p5b** | ✗ | ✓ | 2.7G |
| **pruned_cka_only_20_floor_0.3** | ✓ | ✗ | 11.5G |
| **pruned_cka_only_20_floor_0.5** | ✓ | ✗ | 11.5G |
| **pruned_cka_only_20_floor_0.6** | ✓ | ✗ | 11.5G |
| **pruned_cka_only_20_qwen_math** | ✗ | ✓ | 11.5G |
| **pruned_cka_only_25** | ✓ | ✗ | 10.8G |
| **pruned_cka_only_30** | ✓ | ✗ | 10.1G |
| **pruned_depth_first_20** | ✓ | ✗ | 11.5G |
| **pruned_rasp_20_1p5b** | ✗ | ✓ | 2.7G |
| **pruned_rasp_25** | ✓ | ✗ | 10.8G |
| **pruned_rasp_alpha0p5_20** | ✓ | ✗ | 11.5G |
| **pruned_rasp_alpha2p0_20** | ✓ | ✗ | 11.5G |
| **pruned_rasp_alpha3p0_20** | ✗ | ✓ | 11.5G |
| **pruned_rasp_rlvr_20** | ✗ | ✓ | 11.5G |
| **pruned_standard_15** | ✓ | ✗ | 12.1G |
| **pruned_standard_20_1p5b** | ✗ | ✓ | 2.7G |
| **pruned_standard_20_qwen_math** | ✗ | ✓ | 11.5G |
| **pruned_standard_25** | ✓ | ✗ | 10.8G |
| **pruned_standard_30** | ✓ | ✗ | 10.1G |
| **sft_alpha4_20** | ✓ | ✗ | 11.5G |
| **sft_cka_only_15** | ✓ | ✗ | 12.2G |
| **sft_cka_only_20** | ✗ | ✓ | 11.5G |
| **sft_cka_only_20_1p5b** | ✗ | ✓ | 2.7G |
| **sft_cka_only_20_floor_0.3** | ✓ | ✗ | 11.5G |
| **sft_cka_only_20_floor_0.5** | ✓ | ✗ | 11.5G |
| **sft_cka_only_20_floor_0.6** | ✓ | ✗ | 11.5G |
| **sft_cka_only_25** | ✓ | ✗ | 10.8G |
| **sft_depth_first_20** | ✓ | ✗ | 11.5G |
| **sft_qwen_math_cka_only_20_final** | ✗ | ✓ | 11.5G |
| **sft_random_20** | ✗ | ✓ | 11.3G |
| **sft_rasp_20_1p5b** | ✗ | ✓ | 2.7G |
| **sft_rasp_20_westd** | ✓ (11.5G) | ⚠️ (0.1G) | 见备注 |
| **sft_rasp_25** | ✓ | ✗ | 10.8G |
| **sft_rasp_alpha0p5_20** | ✓ | ✗ | 11.5G |
| **sft_rasp_alpha2p0_20** | ✓ | ✗ | 11.5G |
| **sft_rasp_alpha3p0_20** | ✗ | ✓ (ckpt-935) | 11.5G |
| **sft_rasp_rlvr_20** | ✗ | ✓ (ckpt-1870) | 11.5G |
| **sft_standard_15** | ✓ | ✗ | 12.1G |
| **sft_standard_20** | ✓ | ✗ | 11.5G |
| **sft_standard_20_1p5b** | ✗ | ✓ | 2.7G |
| **sft_standard_20_qwen_math_final** | ✗ | ✓ | 11.5G |
| sft_standard_25 | ✗ (dir only) | ✗ | — |

**统计**: westd 有 44 个有效 checkpoint，westb 有 25 个有效 checkpoint，6 个空目录（无 model.safetensors）。

### 备注

- **sft_rasp_20_westd@westb**: 仅 114MB，疑似损坏或未完成写入（westd 上同名为正常的 11.5G）
- **westb 的 1.5B 系列**（`*_1p5b`）为 DeepSeek-R1-Distill-Qwen-1.5B 实验，模型约 2.7G
- westb 还存有基础模型 `models/DeepSeek-R1-Distill-Qwen-1.5B`（3.3G）

---

## GPU 占用状态

### westd-32935 (4×RTX PRO 6000, 96GB each)
| GPU | 利用率 | 显存占用 |
|---|---|---|
| cuda:0 | 99% | 29659 / 97887 MiB |
| cuda:1 | 0% | 0 / 97887 MiB |
| cuda:2 | 97% | 16767 / 97887 MiB |
| cuda:3 | 97% | 16767 / 97887 MiB |

### westb-23072 (2×RTX PRO 6000, 96GB each)
| GPU | 利用率 | 显存占用 |
|---|---|---|
| cuda:0 | 90% | 29639 / 97887 MiB |
| cuda:1 | 0% | 0 / 97887 MiB |

westd cuda:0 和 westb cuda:0 正在运行任务（~30GB 显存），westd cuda:2/3 也在运行（~16GB 显存各）。westd cuda:1 和 westb cuda:1 空闲。

---
