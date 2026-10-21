# ssh westb disk analysis

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_westb_disk_analysis_20260523T122458_result.json`
- **Structured JSON:** [`cd682ce7704040f72519.json`](../../sessions/cd/cd682ce7704040f72519.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。

```
总磁盘：250G，已用 241G，剩余 9.2G (97%)

=== 占用分布 ===
recovery_aware_struct_prune/     226G  (94%)
models/Qwen2.5-Math-7B           15G  (6%)
data/                            1.5G
其他 (.hf_cache/logs/etc.)       <1G

=== 清理方案 ===

【可删 — 中间 checkpoint 副本（final model 已存在）】~24G
1. grpo_qwen_math_cka_only_20/checkpoint-100/  — 12G
   已有顶层 model.safetensors，checkpoint-100 是冗余副本（含 scheduler.pt/rng_state.pth 等训练恢复文件）
2. grpo_rasp_alpha0p5_20/checkpoint-100/        — 12G
   同上，顶层已有 final model.safetensors

【可删 — 空目录】~0
3. grpo_random_20_seed456/   — 0 (空目录)
4. grpo_rasp_alpha3p0_20/    — 132K (仅 README + completions，无模型文件，疑似失败/未完成的 run)

可释放空间：~24G（97% → 87%）

=== 需确认 ===
5. models/Qwen2.5-Math-7B                 — 15G  — Qwen Math base model，如果 Qwen Math 实验已完成且不再需要 base model，可删
6. pruned_standard_25/                     — 11G  — 25% 剪枝率实验，其他实验均为 20%，确认是否仍需要
7. pruned_rasp_rlvr_20/ + sft_rasp_rlvr_20/ — 24G — 早期 RLVR 方案实验，如已被 alpha 系列取代可删
8. grpo_alpha4_20_eval/                    — 2.9G — alpha=4 的 eval 模型，确认是否仍需要

如全部确认可删：额外释放 ~53G，合计 ~77G（97% → 66%）

=== 不可删除 ===
- models/DeepSeek-R1-Distill-Qwen-1.5B    — 3.4G — 1.5B base model
- 所有 final model.safetensors            — 各实验的最终模型权重
- results/ + eval_results/                 — 评测结果
- 1.5B 系列 (9 个目录 × 2.8G = 25G)       — 1.5B 实验完整流水线
- data/                                    — 训练/评测数据
- sft_rasp_rlvr_20/checkpoint-1870         — 该目录唯一的模型，不可删
- sft_rasp_alpha3p0_20/checkpoint-935      — 同上
- grpo_cka_only_20/checkpoint-100          — 同上（顶层无 model.safetensors）
```

---
