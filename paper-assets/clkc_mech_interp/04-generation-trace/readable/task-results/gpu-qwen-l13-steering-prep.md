# gpu qwen L13 steering prep

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_gpu_qwen-L13-steering-prep_20260522T133215_result.json`
- **Structured JSON:** [`01e627f30d0c0381308e.json`](../../sessions/01/01e627f30d0c0381308e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### Qwen L23 Steering 结果（negative）

| alpha | steering flips | control flips | Fisher p | p→c | c→p |
|-------|---------------|--------------|----------|-----|-----|
| -20 | 1/84 (1.2%) | 2/84 (2.4%) | 1.0 | 0 | 0 |
| -10 | 2/84 (2.4%) | 2/84 (2.4%) | 1.0 | 0 | 0 |
| -5 | 2/84 (2.4%) | 2/84 (2.4%) | 1.0 | 0 | 0 |
| +5 | 1/84 (1.2%) | 2/84 (2.4%) | 1.0 | 0 | 0 |
| +10 | 2/84 (2.4%) | 1/84 (1.2%) | 1.0 | 0 | 0 |
| +20 | 2/84 (2.4%) | 3/84 (3.6%) | 1.0 | 0 | 0 |

- Probe accuracy: 0.732
- Baseline: contextual=35, parametric=8, both=20, neither=21
- **结论**: L23 在 Qwen3-8B 上完全无因果效应，与 Llama L23 负结果一致

### Qwen L13 Steering 已启动
- **PID**: 490477
- **GPU**: cuda:0
- **exp_id**: steering_107_qwen_L13
- **状态**: RUNNING，模型加载中
- 预计运行 ~50 分钟（6 alphas × ~8 min/alpha）

---
