# ssh check status teal30

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_status_teal30_20260516T034540_result.json`
- **Structured JSON:** [`b409819ed8963b0da5b9.json`](../../sessions/b4/b409819ed8963b0da5b9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### 1. Mistral KL 50% downstream eval (PID 195242)

**状态: Running** | 已运行 49 分钟

- 已完成: arc_challenge, winogrande, 全部 mmlu 子任务
- 当前: gsm8k `generate_until` 请求 **64% (841/1319)**，~2.9s/it
- 预计剩余: ~25 分钟
- 结果目录 `results/lm_eval_mistral_kl_50pct/` 存在但尚无输出文件（完成后写入）
- 运行在 cuda:1 (16524MiB)

### 2. TEAL 30% 完整 downstream metrics

| Task | Metric | Value |
|------|--------|-------|
| **arc_challenge** | acc | 0.3933 |
| **arc_challenge** | acc_norm | 0.4155 |
| **winogrande** | acc | 0.6559 |
| **mmlu** (overall) | acc | 0.3598 |
| - mmlu_stem | acc | 0.3130 |
| - mmlu_humanities | acc | 0.3305 |
| - mmlu_social_sciences | acc | 0.4108 |
| - mmlu_other | acc | 0.4010 |
| **gsm8k** | exact_match (strict) | 0.0849 |
| **gsm8k** | exact_match (flexible) | 0.0925 |

实际稀疏度: 30.00%。确认 negative — 各项指标均显著低于 dense baseline 预期水平，尤其 gsm8k (<9%) 严重退化。

### 3. GPU 状态

| GPU | 显存 | 利用率 | 状态 |
|-----|------|--------|------|
| **cuda:0** | 0 / 97887 MiB | 0% | **空闲可用** |
| **cuda:1** | 62082 / 97887 MiB | 96% | 占用 |

**注意**: cuda:1 上除 PID 195242 (16524MiB) 外，还有一个未知进程 **PID 195911** (45544MiB)。这不是 mistral eval 的一部分，需要确认来源。

---
