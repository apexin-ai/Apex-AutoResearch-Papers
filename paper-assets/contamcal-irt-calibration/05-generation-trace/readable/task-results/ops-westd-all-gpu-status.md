# ops westd all gpu status

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd-all-gpu-status_20260520T000425_result.json`
- **Structured JSON:** [`c77d403d09b480cc32ab.json`](../../sessions/c7/c77d403d09b480cc32ab.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

cuda:2 已加载模型（14.5GB 显存占用），eval 启动成功。

---

## westd-29999 全卡状态汇总

| GPU | 任务 | 进度 | 预计完成 (CST) |
|-----|------|------|---------------|
| **cuda:0** | Phi-4 s123 SFT | 2385/4159 (57%), epoch 0.57 | ~09:10 |
| **cuda:1** | Qwen-14B s123 SFT | 2300/3642 (63%), epoch 0.63 | ~09:10 |
| **cuda:2** | OLMo-2 s123 GSM8K eval | **刚启动** | ~08:50 |
| **cuda:3** | Gemma-2 s123 SFT | 2982/3642 (82%), epoch 0.79 | ~08:40 |

**OLMo-2 s42 GSM8K eval 结果（已完成）：**
- **d000**: 68.46% (903/1319)
- **d100**: 70.20% (926/1319)
- contamination effect: +1.74pp

cuda:3 Gemma-2 预计最先完成（~33min），cuda:0/1 约 1h 后完成。OLMo-2 s123 eval 已提交到 cuda:2，预计 ~45min 完成。

---
