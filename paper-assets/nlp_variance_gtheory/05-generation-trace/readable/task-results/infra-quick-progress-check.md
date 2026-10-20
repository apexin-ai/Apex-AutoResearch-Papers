# infra quick progress check

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_quick_progress_check_20260521T212745_result.json`
- **Structured JSON:** [`164a4c7846f6aeaddd37.json`](../../sessions/16/164a4c7846f6aeaddd37.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

### westd-32570 — GPU 状态

| GPU | 利用率 | 状态 |
|-----|--------|------|
| 0 | 0% | 空闲 |
| 1 | 0% | 空闲 |
| 2 | 87% | **运行中** |
| 3 | 0% | 空闲 |

### westd-19912 — GPU 状态

| GPU | 利用率 | 状态 |
|-----|--------|------|
| 0 | 0% | 空闲 |
| 1 | 0% | 空闲 |
| 2 | 0% | 空闲 |
| 3 | 0% | 空闲 |

### exp002 完成状态（目标 57,600 行/文件）

| Model | MMLU | ARC | HellaSwag | GSM8K | MATH |
|-------|------|-----|-----------|-------|------|
| Llama | ✅ | ✅ | ✅ | ✅ | ✅ |
| Qwen | ✅ | ✅ | ✅ | ✅ | ✅ |
| Mistral | ✅ | ✅ | ✅ | ✅ | ✅ |
| Gemma | ✅ | ✅ | ✅ | ✅ | ✅ |
| InternLM | ✅ | ✅ | ✅ | ✅ | ✅ |
| DeepSeek | ✅ | ✅ | ✅ | ✅ | ✅ |
| OLMo | ✅ | ✅ | ✅ | ✅ | ✅ |
| Yi | ✅ | ✅ | ✅ | ✅ | ✅ |

**全部 8 模型 × 5 benchmark = 40 个文件，每个都是 57,600 行，全部完成。**

注意：westd-32570 上还有一个 `deepseek_math_gpu2.jsonl`（36,200 行），看起来是额外/重复跑的文件，不影响主结果（`deepseek_math.jsonl` 已完成）。GPU2 仍在 87% 利用率运行，可能正在跑这个文件或其他任务。

---
