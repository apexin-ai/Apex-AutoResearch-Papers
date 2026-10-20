# eval home mutation eval prep

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_home-mutation-eval-prep_20260515T221239_result.json`
- **Structured JSON:** [`f027d6bd3132f260d027.json`](../../sessions/f0/f027d6bd3132f260d027.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 检查报告

### 1. Home GPU 状态：**不可达**
home-1x5090 所有 SSH 命令均 10s 超时。服务器可能关机或网络不通。

### 2. 8B 模型：**无法确认**（服务器不可达）

### 3. CLS 8B ckpt-1000：**无法确认**（服务器不可达）
实验配置显示 checkpoint 来源为 `westd:/root/autodl-tmp/checkpoints_repo_cls_8b_conda/`，需要从 westd 同步到 home。

### 4. eval 脚本是否支持 per-mutation breakdown：**否**
`eval_repo_cls.py`（v1/v2）只计算整体 accuracy、F1、confusion matrix。**没有任何 mutation_type 相关逻辑。** 需要改动：
- 数据加载时保留 `mutation_type` 字段
- 推理结果中记录 `mutation_type`
- `compute_metrics` 后增加 per-mutation-type 分组计算 accuracy/F1
- 输出 summary JSON 中增加 `by_mutation_type` 字段

### 5. 数据中 mutation_type 字段：**有**
`build_data.py` 生成的数据包含 `mutation_type` 字段，共 6 种值：
- `original`（正确代码）
- `operator_swap`
- `off_by_one`
- `return_value`
- `boundary_removal`
- `variable_swap`

`extract_predictions_generic.py` 已经会透传 `mutation_type`，但 `eval_repo_cls.py` 不读这个字段。

### 6. 磁盘空间：**无法确认**（服务器不可达）

### 7. 总结：提交 per-mutation eval 还需要

| 步骤 | 状态 |
|------|------|
| home-1x5090 恢复在线 | **阻塞** — 当前不可达 |
| 改 `eval_repo_cls.py` 添加 per-mutation-type breakdown | **需要做** |
| Qwen3-8B 模型同步到 home | 待确认（服务器恢复后检查） |
| CLS 8B s42 ckpt-1000 LoRA adapter 同步到 home | 待确认（可能需要从 westd 同步） |
| test 数据集同步到 home | 待确认 |

**建议优先级**：先改 eval 脚本（本地可做，不依赖服务器），等 home 恢复后再检查模型/数据/磁盘状态。是否现在修改 eval 脚本？

---
