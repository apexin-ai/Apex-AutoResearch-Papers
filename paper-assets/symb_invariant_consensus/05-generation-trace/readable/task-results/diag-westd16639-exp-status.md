# diag westd16639 exp status

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_westd16639-exp-status_20260518T180510_result.json`
- **Structured JSON:** [`2f80153d6b713d7da293.json`](../../sessions/2f/2f80153d6b713d7da293.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断报告：westd-16639

### GPU 状态

| GPU | 型号 | 利用率 | 显存 | 进程 |
|-----|------|--------|------|------|
| 0 | RTX PRO 6000 Black | 100% | 88.4/97.9 GB | vLLM (PID 6584) |
| 1 | RTX PRO 6000 Black | 100% | 88.4/97.9 GB | vLLM (PID 7589) |
| 2 | RTX PRO 6000 Black | 100% | 88.4/97.9 GB | vLLM (PID 8790) |
| 3 | RTX PRO 6000 Black | 100% | 88.4/97.9 GB | vLLM (PID 11246) |

### 4 个实验状态

**注意：实际实验编号与预期不同（032/033/036/038，不是 039/040/041/038）。**

| GPU | tmux | 实验 | 模型 | 数据集 | 端口 | 进度 | 状态 | ETA |
|-----|------|------|------|--------|------|------|------|-----|
| 0 | exp032 | Qwen2.5-14B PW-600 | Qwen2.5-14B-Instruct | proofwriter_full (600) | 8000 | **20/600** | RUNNING | ~624 min (~10.4h) |
| 1 | exp033 | Qwen3-14B PW-600 | Qwen3-14B (thinking=off) | proofwriter_full (600) | 8001 | **12/600** | RUNNING | ~1013 min (~16.9h) |
| 2 | exp036 | Qwen2.5-14B FOLIO-204 | Qwen2.5-14B-Instruct | folio_full (204) | 8002 | **~29/204** | RUNNING | (未显示 ETA) |
| 3 | exp038 | Qwen2.5-14B LogiQA-200 | Qwen2.5-14B-Instruct | logiqa_200 (200) | 8003 | **24/200** | RUNNING | ~113 min (~1.9h) |

### 中间指标（截至当前进度）

| 实验 | sica_accuracy | sc_accuracy | delta |
|------|--------------|-------------|-------|
| exp032 (Qwen2.5-14B PW) | 0.789 | 0.789 | — |
| exp033 (Qwen3-14B PW) | 0.818 | 0.818 | — |
| exp036 (Qwen2.5-14B FOLIO) | 0.750 | 0.821 | — |
| exp038 (Qwen2.5-14B LogiQA) | 0.696 | 0.696 | 0.0 |

### vLLM 服务

4 个 vLLM 实例全部正常运行：
- `:8000` — Qwen2.5-14B-Instruct (GPU 0)
- `:8001` — Qwen3-14B, `enable_thinking=false` (GPU 1)
- `:8002` — Qwen2.5-14B-Instruct (GPU 2)
- `:8003` — Qwen2.5-14B-Instruct (GPU 3)

### 缓存模型

`/root/autodl-tmp/models/` 下有：Qwen2.5-14B-Instruct, Qwen3-14B, Mistral-7B-Instruct-v0.3, deepseek-r1-0528-qwen3-8b, gemma-3-27b-it, llama-4-scout, phi-4-reasoning

### 网络状态

`HF_ENDPOINT=https://hf-mirror.com` 已在 `.bashrc` 中设置（重复两行），但当前 shell 环境变量为空（需 `source` 才生效，不影响已运行的实验）。

### 总结

4 个实验全部正常运行中，无失败。预计完成顺序：exp038 (LogiQA, ~2h) → exp036 (FOLIO, ~数小时) → exp032 (PW, ~10h) → exp033 (PW Qwen3, ~17h)。exp033 (Qwen3-14B) 速度最慢，约为 Qwen2.5 的 1.6 倍。另外还有个空目录 `exp037_mistral7b_folio204`，看起来是之前创建但未启动的实验。

---
