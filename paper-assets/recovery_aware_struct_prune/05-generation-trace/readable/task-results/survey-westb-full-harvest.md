# survey westb full harvest

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_survey_westb_full_harvest_20260522T003605_result.json`
- **Structured JSON:** [`0284a6e40e37c7a02a1e.json`](../../sessions/02/0284a6e40e37c7a02a1e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westb-23072 状态汇总

### GPU 状态

| GPU | 显存占用 | 利用率 | 状态 |
|-----|---------|--------|------|
| cuda:0 | 0 / 97887 MiB | 0% | **空闲** |
| cuda:1 | 36244 / 97887 MiB | 100% | 占用（2 个 eval 进程） |

### 运行中的 Eval

| PID | 任务 | 运行时长 | 进度 | 预估剩余 |
|-----|------|---------|------|----------|
| 104592 | eval_math500_**sft_standard_25** (ckpt-1870) | 9h16m | **382/500 (76%)** | ~6h（~180s/it） |
| 118095 | eval_math500_**sft_cka_only_20** (v6) | 5h03m | **312/500 (62%)** | ~5h（~57-100s/it） |

两个 eval 都仍在运行，尚未产出 results.json。按当前速度预计还需 5-6 小时完成。

### 磁盘

`/root/autodl-tmp/`: **34GB 可用** (87% used, 217/250GB)

### 本地 Checkpoint 列表（/root/autodl-tmp/recovery_aware_struct_prune/）

**剪枝模型：**
- pruned_cka_only_20, pruned_cka_only_20_1p5b, pruned_cka_only_20_qwen_math
- pruned_rasp_20, pruned_rasp_20_1p5b, pruned_rasp_rlvr_20
- pruned_standard_20, pruned_standard_20_1p5b, pruned_standard_20_qwen_math, pruned_standard_25

**SFT 模型：**
- sft_cka_only_20, sft_cka_only_20_1p5b, sft_qwen_math_cka_only_20_final
- sft_rasp_20_1p5b, sft_rasp_rlvr_20
- sft_standard_20_1p5b, sft_standard_20_qwen_math_final, sft_standard_25

**GRPO 模型：**
- grpo_cka_only_20, grpo_cka_only_20_1p5b, grpo_cka_only_20_seed123
- grpo_random_20, grpo_rasp_20_1p5b, grpo_standard_20_1p5b, grpo_standard_25_westb

---

**结论：** cuda:0 完全空闲可安排新任务。cuda:1 上两个 MATH-500 eval 预计今晚（~UTC+8 凌晨）完成，无需干预。

---
