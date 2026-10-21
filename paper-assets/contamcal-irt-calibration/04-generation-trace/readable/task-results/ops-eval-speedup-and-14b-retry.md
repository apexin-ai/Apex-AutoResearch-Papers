# ops eval speedup and 14b retry

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_eval-speedup-and-14b-retry_20260518T115631_result.json`
- **Structured JSON:** [`38823903960b28179a1e.json`](../../sessions/38/38823903960b28179a1e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 任务 1: evaluate.py 加速分析

完整代码 763 行，核心结构如下：

### 关键发现

| 维度 | 现状 |
|------|------|
| **batch_size** | `--batch-size` 参数存在（默认 8），但**完全未被使用** |
| **数据迭代** | 所有 4 个 benchmark 都是 `for row in tqdm(ds)` 逐条推理，无 DataLoader |
| **vLLM** | 无，使用原生 `transformers` 的 `model.generate()` |
| **max_new_tokens** | MCQ: 5 (generation mode) / GSM8K: 512 / HumanEval: 512 |

### 逐 benchmark 详情

**MMLU/ARC (MCQ)** — 两种模式：
- **Logprob mode**（默认，非 instruct）: `compute_choice_logprobs()` 逐条做前向传播，取最后 token logits 比较选项概率。**这个最容易 batch 化**，一次前向传播可处理多个 prompt
- **Generation mode**（instruct）: 逐条 `model.generate(max_new_tokens=5)`

**GSM8K** — 逐条 `model.generate(max_new_tokens=512, do_sample=False)`，8-shot CoT

**HumanEval** — 逐条 `model.generate(max_new_tokens=512)`，然后 subprocess 执行代码验证

### 加速方案（按 ROI 排序）

1. **vLLM offline batched inference** — 最大收益。MMLU 14K items 从小时级降到分钟级。替换 HF generate 为 vLLM `LLM.generate()`，一次性 batch 全部 prompt。需要改造 LoRA adapter 加载方式（vLLM 原生支持）
2. **Batch logprob scoring**（MCQ non-generation）— `compute_choice_logprobs()` 目前逐条前向传播，可以 pad+batch 多个 prompt 一次推理
3. **Batch generation**（GSM8K/HumanEval）— `tokenizer(prompts, padding=True)` + batch `model.generate()`，受限于 max_new_tokens=512 的长度方差

---

## 任务 2: 14B 下载重启状态

| 项目 | 状态 |
|------|------|
| 旧进程 PID 5066 | **已 kill** |
| 新进程 PID | 25989 (bash) / 25990 (python) |
| 当前大小 | **29G** |
| 进度 | Fetching 18 files: 0%（刚启动，正在恢复已下载的 shard） |
| 日志 | `/root/autodl-tmp/logs/dl_14b_retry.log` |

同时在下载的其他模型：
- gemma-2-9b (PID 6380)
- OLMo-2-1124-7B (PID 19571)
- phi-4 (PID 19608)

---
