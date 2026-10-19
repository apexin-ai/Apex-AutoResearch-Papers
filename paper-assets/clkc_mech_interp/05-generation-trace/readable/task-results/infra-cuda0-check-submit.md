# infra cuda0 check submit

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_cuda0-check-submit_20260522T081608_result.json`
- **Structured JSON:** [`d3d1676124c54073961b.json`](../../sessions/d3/d3d1676124c54073961b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**COMET Qwen 还在跑，cuda:0 不可用。**

状态汇总：

| GPU | PID | 任务 | 显存 |
|-----|-----|------|------|
| **cuda:0** | 59412 | `validate_translation.py` (COMET Qwen, qwen3 train) | 16520 MiB |
| cuda:1 | 85171 | `translate_to_zh.py` (Gemma2) | 16518 MiB |
| cuda:2 | 59571 | `validate_translation.py` (COMET Qwen, llama31 train) | 16520 MiB |
| cuda:3 | 462040 | `translate_to_de.py` (Llama31) | 16194 MiB |

**COMET Qwen (qwen3 train) 进度：740/798 back-translated (~93%)**。还剩 58 个 batch，按当前速度估计 **5-10 分钟内完成** back-translation 阶段，之后还有 COMET 打分步骤。

输出文件 `zh_conflict_train_validated.jsonl` 尚未生成（test 集已完成）。

**结论：cuda:0 当前被占用，预计 10-20 分钟后释放。**

---
