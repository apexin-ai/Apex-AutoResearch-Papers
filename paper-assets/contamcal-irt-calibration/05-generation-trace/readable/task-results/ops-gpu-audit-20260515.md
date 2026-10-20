# ops gpu audit 20260515

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu-audit-20260515_20260515T065953_result.json`
- **Structured JSON:** [`dfbebebf6f31ace2037b.json`](../../sessions/df/dfbebebf6f31ace2037b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据收集完毕。结论如下：

## 审计结果

### 1. GPU 状态：全部 6 张 GPU 均在工作

| GPU | PID | 实验 | 当前进度 | 预计剩余 |
|-----|-----|------|----------|----------|
| 0 | 513900 | eval 0.5B d025 s123 aligned | GSM8K 521/1319 (39%) | ~1h15m |
| 1 | 492660 | **eval 3B d000 v2 s123 aligned** ★ | HumanEval 156/164 (95%) | **~5min** |
| 2 | 506625 | **eval 3B d100 v2 s123 aligned** ★ | GSM8K 690/1319 (52%) | ~1h28m |
| 3 | 503791 | **eval 3B d025 v2 aligned** ★ | GSM8K 834/1319 (63%) | ~1h01m |
| 4 | 513826 | eval 3B d000 s42 v3 aligned | GSM8K 486/1319 (37%) | ~1h15m |
| 5 | 516729 | eval 3B d000 v3 s42 aligned | GSM8K 327/1319 (25%) | ~2h04m |

★ = Registry 中标记为 RUNNING 的 3 个实验

### 2. RUNNING 实验核查

**资源工具误报。** 3 个 RUNNING eval 全部在跑，PID 与 nvidia-smi 完全匹配：
- `exp_001_eval_3B_d000_v2_s123_aligned` (cuda:1) — HumanEval 95%，即将完成
- `exp_001_eval_3B_d100_v2_s123_aligned` (cuda:2) — GSM8K 52%
- `exp_001_eval_3B_d025_v2_aligned` (cuda:3) — GSM8K 63%

**Registry 状态正确，无需更新。**

### 3. seed=123 SFT 状态

全部已完成，Registry 已正确标记为 DONE/success：

| 实验 | Checkpoint 路径 | train_loss | token_accuracy | steps |
|------|----------------|------------|----------------|-------|
| 0.5B d005 s123 | `/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d005_s123` | 1.5422 | 0.6356 (final 0.6794) | 3177 |
| 1.5B d100 s123 | `/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d100_s123/lora_adapter` | 1.3002 | 0.7178 | 4159 |
| 3B d000 v2 s123 | `/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_v2_s123/lora_adapter` | 1.1361 | 0.748 | 3125 |

### 4. exp_001_sft_05B_d025_s123_v2

DONE/success. Checkpoint 路径：
```
/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d025_s123/lora_adapter
```
Metrics: train_loss=1.548, accuracy=0.697, 3384 steps

### 5. 未追踪进程

GPU 0/4/5 上各有 1 个 eval 进程不在 Registry RUNNING 列表中（可能是其他 worker 近期提交的）。

**结论：无 Registry 状态不一致，不需要 update_registry 操作。** GPU 1 上的 d000 v2 s123 eval 即将完成（~5min），完成后 cuda:1 将空闲。

---
