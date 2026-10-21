# ssh kill rsync and list hf

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_kill_rsync_and_list_hf_20260523T043651_result.json`
- **Structured JSON:** [`116d6318725b9d6ed561.json`](../../sessions/11/116d6318725b9d6ed561.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

### 1. rsync 终止确认
4 个 rsync 相关进程（372886/372887/372894/372895）已全部终止，当前无 rsync 运行。

### 2. HF 格式 checkpoint 盘点

位置：`/root/autodl-tmp/checkpoints/`（项目目录下无 checkpoints 目录）

| Checkpoint | 大小 |
|---|---|
| `qwen_exp029_seed8_step5_hf` | 3.8G |
| `intervention_c_hard_cap_step7_hf` | 3.8G |
| `intervention_c_hard_cap_step5_hf` | 3.8G |
| `exp029_seed7_high_kl_step7_hf` | 3.8G |
| `exp029_seed7_high_kl_step5_hf` | 3.8G |
| `qwen_c_prime_step5_hf` | 3.8G |
| `exp029_seed2_step15_hf` | 3.8G |
| `exp029_seed42_step5_hf` | 3.8G |
| `exp029_seed100_step5_hf` | 6.5G |
| `qwen_exp029_seed100_step10_hf` | 3.8G |

**有效 checkpoint：10 个**，总计约 **40.1G**。

另有 11 个 `0` 字节的空目录（多为 `qwen_` 前缀的符号链接或空壳），列表：
`qwen_exp029_seed6_step15_hf`, `qwen_exp029_seed5_step10_hf`, `qwen_exp029_seed4_step15_hf`, `qwen_intervention_c_hard_cap_step7_hf`, `qwen_intervention_c_hard_cap_step5_hf`, `qwen_exp029_seed7_high_kl_step7_hf`, `qwen_exp029_seed7_high_kl_step5_hf`, `qwen_seed2048_step5_hf`, `qwen_exp029_seed2_step15_hf`, `qwen_exp029_seed42_step5_hf`, `qwen_exp029_seed100_step5_hf`。

---
