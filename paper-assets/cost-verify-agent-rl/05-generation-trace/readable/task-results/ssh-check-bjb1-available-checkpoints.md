# ssh check bjb1 available checkpoints

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_bjb1_available_checkpoints_20260522T195631_result.json`
- **Structured JSON:** [`f9ca17b2f544a2f3b5c2.json`](../../sessions/f9/f9ca17b2f544a2f3b5c2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### 可用 HF Checkpoint（全部含 `model.safetensors` + 完整 tokenizer/config）

| Checkpoint | 大小 | 来源 | Symlink |
|---|---|---|---|
| `c_prime_step5_hf` | 3.8G | C' baseline step5 | `qwen_c_prime_step5_hf` |
| `exp029_seed42_step5_hf` | 3.8G | exp029 seed42 step5 | — |
| `exp029_seed300_step5_hf` | 3.8G | exp029 seed300 step5 | `qwen_exp029_seed300_step5_hf` |
| `exp029_seed7_high_kl_step5_hf` | 3.8G | exp029 seed7 high-KL step5 | `qwen_exp029_seed7_high_kl_step5_hf` |
| `exp029_seed7_high_kl_step7_hf` | 3.8G | exp029 seed7 high-KL step7 | — |
| `exp029-seed4/global_step_15_hf` | (含在25G目录) | exp029 seed4 step15 | `qwen_exp029_seed4_step15_hf` |
| `exp021_ragen_sft_v4/final` | (含在23G目录) | SFT v4 baseline | `qwen3_exp021_ragen_sft_v4` |

共 **7 个完整 HF checkpoint** 可直接用于 OOD eval。

注：`exp029-seed4-ood` 和 `seed7-step5-mask-check` 是空目录。Symlink `qwen3_sft_final` 指向已删除的 `exp008_sft/final`（断链），`qwen3-1.7b-exp019b-sft-v3` 和 `qwen3_exp019b_sft` 指向已删除的 `exp019b_expert_sft_v3/final`（断链）。

### 磁盘
`/root/autodl-tmp`: 250G 总量，130G 已用，**121G 可用（52%）**——空间充足。

### GPU
2× NVIDIA RTX PRO 6000 (96GB)，**全部空闲**，0% 利用率，0MiB 显存占用。可立即启动 eval。

---
