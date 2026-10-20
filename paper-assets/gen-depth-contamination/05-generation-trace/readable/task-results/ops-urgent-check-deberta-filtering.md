# ops urgent check deberta filtering

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_urgent_check_deberta_filtering_20260520T191854_result.json`
- **Structured JSON:** [`b39c4cfa7e7947e4dd63.json`](../../sessions/b3/b39c4cfa7e7947e4dd63.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态汇总

### exp_deberta_filtering_comparison — 仍在运行

**Phase 1（DeBERTa OOF 预测）：** 已完成，`predictions.npz` 已保存

**Phase 2（LoRA 训练 + 评估）：**

| 策略 | GPU | 训练 | 评估 |
|------|-----|------|------|
| no_filter | cuda:1 | 完成（03:18 merged） | 进行中（下载 MMLU） |
| obd_binary | cuda:2 | 完成（03:15 merged） | 进行中（下载 MMLU） |
| deberta_binary | cuda:3 | 完成（03:16 merged） | 进行中（下载 MMLU） |
| **deberta_graduated** | — | **未提交** | **未提交** |

3 个策略的 MMLU eval 正在通过 hf-mirror 逐个下载 subject（datasets-server 503，速度慢）。无 eval 结果 JSON 产出。

### exp_expanded_downstream_eval — 仍在运行（GPU 0）
- 当前：`graduated_seed1` 训练中，步骤 1457/1875（78%）
- 已出结果：`binary_ours_seed1` → piqa=0.752, truthfulqa=0.446, winogrande=0.642, arc=0.519, gsm8k=None（xethub 401 失败）
- GSM8K 下载持续失败（401 Unauthorized from xethub）

### 其他
- `sweep_r10_nofilter`：已失败（exit code 1，无法下载 ai2_arc 数据集，OfflineModeIsEnabled）
- westd-42896：完全空闲

### 问题
1. **deberta_graduated 未提交** — registry spec 中标记为 `"pending"`，需要手动提交到空闲 GPU 或等 westd
2. **GSM8K 基准持续 401 错误** — xethub 认证问题，影响 expanded_eval 实验
3. **MMLU 下载缓慢** — datasets-server 503，逐个 subject 下载，3 个策略的 eval 预计还需较长时间

需要我执行什么操作？比如：
- 提交 deberta_graduated 到空闲 GPU
- 等 eval 完成后再收集结果
- 处理 GSM8K 401 问题

---
