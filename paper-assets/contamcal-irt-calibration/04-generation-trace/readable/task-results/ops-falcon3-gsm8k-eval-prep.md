# ops falcon3 gsm8k eval prep

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_falcon3-gsm8k-eval-prep_20260522T180723_result.json`
- **Structured JSON:** [`22886aac664cdb7554c7.json`](../../sessions/22/22886aac664cdb7554c7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。写入 `artifacts/falcon3_gsm8k_eval_commands.md`。

**关键问题：d000 checkpoint 不在 cqa1 上**，仅有 d100_s42。d000 需从源服务器传输后才能 eval。

已准备内容：
- d100 GSM8K eval 命令：S4 完成后直接可用
- d000 GSM8K eval 命令：需先传输 checkpoint
- 所有命令遵循 C001-C009 约束（md5 校验、显式 CUDA_VISIBLE_DEVICES、alpha=32 检查）
- 参数与现有 Qwen7B/Gemma2 GSM8K eval 一致（8-shot CoT, batch_size=8）
- 预估运行时间 ~30-45 分钟/dosage

---
