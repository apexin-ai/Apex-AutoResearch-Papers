# ssh westd olmo eval cuda3

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_westd-olmo-eval-cuda3_20260519T093927_result.json`
- **Structured JSON:** [`7d886a7c2247a0ae773b.json`](../../sessions/7d/7d886a7c2247a0ae773b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

GPU 3 已释放，PID 134065 已结束。两个 eval 全部完成。

---

## 最终汇报

### 1. OLMo-2-7B d050 (seed 42)

| Benchmark | Accuracy | Correct/Total |
|-----------|----------|---------------|
| **MMLU** | **59.18%** | 8310/14042 |
| **ARC-Challenge** | **80.89%** | 948/1172 |

输出路径：`/root/autodl-tmp/exp001/eval_results_cross_family/olmo2_d050_s42/`
- `mmlu_results.json`, `arc_challenge_results.json`, `eval_results.json`, `item_responses.json`, `correctness_matrix.json`

### 2. OLMo-2-7B d100 (seed 42)

| Benchmark | Accuracy | Correct/Total |
|-----------|----------|---------------|
| **MMLU** | **59.49%** | 8353/14042 |
| **ARC-Challenge** | **81.23%** | 952/1172 |

输出路径：`/root/autodl-tmp/exp001/eval_results_cross_family/olmo2_d100_s42/`
- `mmlu_results.json`, `arc_challenge_results.json`, `eval_results.json`, `item_responses.json`, `correctness_matrix.json`

### 3. 对比

| Benchmark | d050 | d100 | Delta |
|-----------|------|------|-------|
| MMLU | 59.18% | 59.49% | +0.31% |
| ARC-Challenge | 80.89% | 81.23% | +0.34% |

### 4. 异常

无异常。两个 eval 均在 GPU 3 (cuda:3) 上顺利完成，所有输出文件齐全（含 `.done` 标志文件），`lora_alpha=32` 合规。

---
