# infra gpu status check both servers

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_gpu_status_check_both_servers_20260521T193330_result.json`
- **Structured JSON:** [`1a5943490d3935a422a4.json`](../../sessions/1a/1a5943490d3935a422a4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据收集完毕。

---

## westd-32570 GPU 状态

| GPU | 任务 | 进度 | ETA |
|-----|------|------|-----|
| 0 | InternLM MATH | 29800/57600 (52%) | ~1.2h (400行/min) |
| 1 | InternLM GSM8K | 50200/57600 (87%) | ~15min |
| 2 | DeepSeek MATH | 12400/57600 (22%) | ~3.5h (207行/min) |
| 3 | DeepSeek GSM8K | 32000/57600 (56%) | ~1.2h (356行/min) |

**空闲 GPU**: 无，4 张全满

**Watcher 状态**:
- Symlink watcher: **存活**，最新报告 internlm_math_gpu0 进度 29800/57600
- Gemma→DeepSeek MATH watcher: **已完成使命**，Gemma MATH 02:35 跑完后创建了 deepseek_math placeholder 并启动 DeepSeek MATH

**Placeholder 状态**:
- `internlm_math.jsonl`: **仍是 placeholder** (`{"_placeholder": true}`)，实际数据在 `internlm_math_gpu0.jsonl`
- `deepseek_math.jsonl`: **仍是 placeholder** (`{"_placeholder": true}`)，实际数据在 `deepseek_math_gpu2.jsonl`

---

## westd-19912 GPU 状态

| GPU | 任务 | 进度 | ETA |
|-----|------|------|-----|
| 0 | **空闲** | — | — |
| 1 | OLMo MATH | 38400/57600 (67%) | ~1-1.5h |
| 2 | Yi MATH | 51800/57600 (90%) | ~30min |
| 3 | **空闲** | — | — |

**空闲 GPU**: GPU 0 和 GPU 3 — 原因是其他 benchmark（arc/hellaswag/mmlu/gsm8k）已全部跑完，只剩 MATH 任务各占一张卡

---

## 完成度汇总

### westd-32570: 8 模型 × 5 benchmarks (原4 + InternLM + DeepSeek)

| 模型 | MMLU | ARC | HellaSwag | GSM8K | MATH |
|------|------|-----|-----------|-------|------|
| Qwen | ✅ | ✅ | ✅ | ✅ | ✅ |
| LLaMA | ✅ | ✅ | ✅ | ✅ | ✅ |
| Gemma | ✅ | ✅ | ✅ | ✅ | ✅ |
| Mistral | ✅ | ✅ | ✅ | ✅ | ✅ |
| InternLM | ✅ | ✅ | ✅ | 87% | 52% |
| DeepSeek | ✅ | ✅ | ✅ | 56% | 22% |

**26/30 完成，4 个进行中**

### westd-19912: 2 模型 × 5 benchmarks

| 模型 | MMLU | ARC | HellaSwag | GSM8K | MATH |
|------|------|-----|-----------|-------|------|
| OLMo | ✅ | ✅ | ✅ | ✅ | 67% |
| Yi | ✅ | ✅ | ✅ | ✅ | 90% |

**8/10 完成，2 个进行中**

---

**总计: 34/40 完成 (85%)**。westd-19912 有 2 张空闲 GPU（GPU 0, GPU 3），可以分配新任务。Yi MATH 预计最先完成（~30min），之后 GPU 2 也会释放。

---
