# ssh harvest rasp 20 eval

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_harvest_rasp_20_eval_20260520T180905_result.json`
- **Structured JSON:** [`45c8a001b3e54310556c.json`](../../sessions/45/45c8a001b3e54310556c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Eval 状态汇总

| Eval | GPU | PID | 状态 | 进度 | 当前 Accuracy |
|------|-----|-----|------|------|---------------|
| **sft_rasp_20** | cuda:3 (已释放) | 267009 | **完成** | 1319/1319 | **0.6149 ± 0.0134** (811/1319) |
| **sft_cka_only_15** | cuda:1 | 262728 | 运行中 | ~1180/1319 (87%) | 0.7252 |
| **sft_cka_only_20** | cuda:2 | 264522 | 运行中 | ~878/1319 (66%) | 0.6318 |
| **sft_standard_20** | cuda:0 | 266847 | 运行中 | ~420/1319 (32%) | 0.6150 |

### sft_rasp_20 详细结果
- Accuracy: **61.49%** (811/1319)
- EOS rate: 98.26%, avg response length: 216.5 tokens
- 结果已写入 `eval_gsm8k_sft_rasp_20_n1319.json` + `.done` sentinel

### 预计剩余时间
- **cka_only_15**: ~139 samples remaining, ~3s/it → **~7 min**
- **cka_only_20**: ~441 samples remaining, ~3s/it → **~22 min**
- **sft_standard_20**: ~899 samples remaining, 有间歇性卡顿（偶发 100s+/it spikes），正常速度 ~2.5s/it → **~40-60 min**（含卡顿可能更长）

### GPU 状态
4× RTX PRO 6000。cuda:0/1/2 满载 (91-99%, 84°C/78°C/68°C)，cuda:3 空闲。

---
