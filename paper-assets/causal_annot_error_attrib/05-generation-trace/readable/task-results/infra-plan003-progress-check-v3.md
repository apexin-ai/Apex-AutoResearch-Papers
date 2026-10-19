# infra plan003 progress check v3

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_plan003-progress-check-v3_20260520T160942_result.json`
- **Structured JSON:** [`0ffe6dc5b546616e5ee5.json`](../../sessions/0f/0ffe6dc5b546616e5ee5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## plan_003 标注进度报告（第 3 次，~09:10）

### 进程状态
3 路全部存活：llama4 (438497)、qwen3 (438843)、deepseek (439116)。

### 进度明细

目前只有 `humaid/zero-shot` 在产出，其他 dataset/prompt 组合尚未开始写入：

| 模型 | 当前完成 | 总量 | 进度 | 上次 | 近1h速率 | 上次速率 |
|------|---------|------|------|------|---------|---------|
| llama4 | **1378** | 13500 | 10.2% | 339 (2.5%) | **17.3/min** | 6.2/min |
| qwen3 | **697** | 13500 | 5.2% | 189 (1.4%) | **8.5/min** | 3.5/min |
| deepseek | **1084** | 13500 | 8.0% | 274 (2.0%) | **13.5/min** | 5.2/min |

三路速率均加速至上次的 **2.4\~2.8x**，初期慢可能是启动开销+API 缓存预热。

### 日志状态
- **llama4**: 已到 [1350/1500]，humaid/zero-shot 即将完成，偶发 429/503 自动重试
- **qwen3**: [650/1500]，最慢，偶发 502
- **deepseek**: [1050/1500]，humaid/zero-shot 也接近完成，偶发 502

### 输出文件
全部在 `results/humaid/`，仅 `{model}_zero-shot.jsonl`，尚无 vast/civil_comments 目录。

### 预估剩余时间（按近 1h 速率）

| 模型 | 剩余样本 | 预估时间 |
|------|---------|---------|
| llama4 | 12122 | **~11.7h**（今晚 ~21:00） |
| deepseek | 12416 | **~15.3h**（明早 ~00:30） |
| qwen3 | 12803 | **~25.1h**（明天 ~10:00） |

qwen3 显著慢于其他两路，若 API 速率不提升，总耗时瓶颈在 qwen3。

---
