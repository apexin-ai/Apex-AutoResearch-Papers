# diagnose check all 3 evals urgent

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_check_all_3_evals_urgent_20260518T192647_result.json`
- **Structured JSON:** [`539b118819813625b747.json`](../../sessions/53/539b118819813625b747.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
=== GPU Status ===
cuda:0: 26853MiB/32607MiB, 84% util — 8B SFT s44 训练 (PID 567995)
cuda:1: 11387MiB/32607MiB, 46% util — random_rsft_k1_eval 运行中 (PID 558325)
cuda:2: 0MiB/32607MiB, 空闲
cuda:3: 11387MiB/32607MiB, 44% util — grpo_bf16_g4_ckpt100_eval 运行中 (PID 558472)

=== plan019_1_7b_sft_s44_eval (cuda:0) ===
PID 558241: dead
状态: 完成 (02:17 May 19)
指标: ign_f1=0.4321, f1=0.4441, evi_f1_tp=0.819, evi_f1_joint=0.3482, EDCR=0.69
       format_ok=985/985 (100%), field_compliance=51.98%, truncated=473/985, predictions=20237
Registry: ✅ 已更新 (DONE/success)

=== random_rsft_k1_eval (cuda:1) ===
PID 558325: alive
状态: 运行中 — 214/247 (87%), ~25 min remaining
Registry: 待完成后更新

=== grpo_bf16_g4_ckpt100_eval (cuda:3) ===
PID 558472: alive
状态: 运行中 — 223/247 (90%), ~18 min remaining
Registry: 待完成后更新
```

**关键发现 — plan019_1_7b_sft_s44_eval:**
- ign_f1=0.4321 显著低于预期的 ~0.495（canonical 1.7B SFT s42 水平）
- field_compliance 仅 51.98%（512/985 文档有有效 evidence），truncated 高达 48%
- 这可能说明 1.7B 模型在 max_new_tokens=1024 下严重截断，导致大量输出不完整

两个 4B eval 预计 ~20 min 内完成。

---
