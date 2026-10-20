# diagnose qwen14b retrain exit

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_qwen14b-retrain-exit_20260520T052638_result.json`
- **Structured JSON:** [`81520ea61b89b6a07002.json`](../../sessions/81/81520ea61b89b6a07002.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。汇总：

## 诊断结果

**sft_qwen14b_d100_s123_retrain: 训练成功完成 ✓**

| 项目 | 状态 |
|------|------|
| PID 246779 | 已退出（正常完成） |
| .done marker | 存在 |
| epoch | 1.0 (4159/4159 steps) |
| final loss | 0.925 |
| token accuracy | 0.761 |
| adapter size | 275MB |
| lora_alpha | 32 ✓ (非废弃 alpha=16) |
| checkpoint | `/root/autodl-tmp/exp001/checkpoints/Qwen2.5-14B_d100_s123/lora_adapter/` |

**注意**: sweep log 末尾有一条 `No space left on device` 错误（09:15 CST），但这是更早的一次失败尝试。实际训练在 13:21 CST 完成，checkpoint 完整。

## cuda:1 状态

**westd-29999 cuda:1 空闲可用**: 0% GPU util, 0 MiB 显存。可接 GSM8K eval。

（注：数据盘 `/root/autodl-tmp` 使用率 79% (196G/250G)，eval 应该没问题但后续大任务需注意磁盘空间。）

---
