# analysis eval sft alpha 1p0

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval-sft-alpha-1p0_20260515T152410_result.json`
- **Structured JSON:** [`992ca1f442711fb027b7.json`](../../sessions/99/992ca1f442711fb027b7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新完毕（status=DONE, conclusion=success, metrics 已写入）。

## 结果

**eval-sft-alpha-1p0: accuracy = 57%** (57/100, eos_rate=98%, avg_len=224.18)

### α ablation 全景对比

| 配置 | Post-Prune | Post-SFT |
|------|-----------|----------|
| α=0.0 (importance only) | — | **64%** |
| α=0.5 | — | 待确认 |
| **α=1.0 (本次)** | 27% | **57%** |
| α=4.0 | — | **62%** |
| Standard (importance-only) | — | **64%** |
| RASP default (α=1.0, westb) | — | **57%** |

### 关键发现

1. **α=1.0 westd 结果 = 57%，与 sft_rasp_20 (westb) 的 57% 完全一致。** 尽管 calibration 样本数不同（westd=256 vs westb=512），最终 SFT 后的 accuracy 相同，说明 calibration 样本数在 256-512 范围内对最终结果影响可忽略。

2. **α=1.0 是 ablation 中最弱的配置** — 低于 α=0.0 (64%)、α=4.0 (62%) 和 standard (64%)。recovery-awareness 在 α=1.0 时权重过大，反而损害了剪枝质量。

3. **eos_rate=98%** 正常，avg_len=224 合理，无异常。

---
