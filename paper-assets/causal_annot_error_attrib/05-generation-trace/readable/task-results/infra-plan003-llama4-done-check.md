# infra plan003 llama4 done check

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_plan003-llama4-done-check_20260520T224918_result.json`
- **Structured JSON:** [`ce0fec9d70ad57ee2ae0.json`](../../sessions/ce/ce0fec9d70ad57ee2ae0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果汇总

### 1. PID 状态

| PID | 模型 | 状态 | 运行时长 |
|-----|------|------|----------|
| 438497 | llama4 | **DEAD** | 已退出 |
| 438843 | qwen3 | ALIVE | 8h48m（空跑，持续产出 402 错误） |
| 439116 | deepseek | ALIVE | 8h47m（空跑，持续产出 402 错误） |

### 2. 根因：API 额度耗尽

API 端点 `http://47.94.22.126/v1` 返回 **HTTP 402 Payment Required**。三个模型共享同一端点，在运行过程中某个时间点同时失效。

### 3. 各模型解析情况

**llama4** (9/9 完成，但后 4 个无效)：

| 数据集/策略 | 解析率 | 准确率 |
|-------------|--------|--------|
| humaid/zero-shot | 1500/1500 ✓ | 65.8% |
| humaid/few-shot-3 | 1498/1500 ✓ | 66.6% |
| humaid/few-shot-5 | 1471/1500 ✓ | 67.4% |
| vast/zero-shot | 1496/1500 ✓ | 52.3% |
| vast/few-shot-3 | 1500/1500 ✓ | 50.1% |
| vast/few-shot-5 | **346/1500** ⚠️ | 72.8% |
| civil_comments × 3 | **0/1500** ❌ | 402 |

**deepseek** (7/9 完成，后 4 个无效)：

| 数据集/策略 | 解析率 |准确率 |
|-------------|--------|--------|
| humaid/zero-shot | 1500/1500 ✓ | 67.6% |
| humaid/few-shot-3 | 1345/1500 ✓ | 69.3% |
| humaid/few-shot-5 | 1237/1500 ✓ | 68.8% |
| vast/zero-shot | 1000/1500 (500条402) ⚠️ | 68.9% |
| vast/few-shot-3 onwards | 0/1500 ❌ | 402 |

**qwen3** (6/9 完成，后 7 个无效)：

| 数据集/策略 | 解析率 | 准确率 |
|-------------|--------|--------|
| humaid/zero-shot | 1500/1500 ✓ | 68.1% |
| humaid/few-shot-3 | 1423/1500 ✓ | 68.0% |
| humaid/few-shot-5 onwards | 0/1500 ❌ | 402 |

### 4. 数据字段名（for plan_006）

```json
{
  "idx": int,
  "text": str,
  "gold_label": str,       // ← 真实标签
  "pred_label": str|null,  // ← 模型预测
  "raw_response": str,
  "model": str,
  "prompt_type": str,
  "error": str|null,
  "topic": str             // 仅 VAST 数据集
}
```

每个任务还输出 `{model}_{prompt}_confusion_matrix.npz`。

### 5. 可用数据统计

完整或高解析率的任务组合：**~10/27**（需充值后重跑剩余 17 个任务）

### 6. 建议操作

1. **终止 qwen3/deepseek 进程**——它们在空烧 CPU 产出全 null 数据
2. **充值 API 额度**（`http://47.94.22.126`）
3. 充值后重跑失败任务（annotate.py 支持 `--dataset`/`--model`/`--prompt` 选择性重跑）
4. **plan_006 phase 1 暂不可触发**——civil_comments 数据完全缺失，vast 部分缺失

是否要我终止 qwen3 和 deepseek 进程？

---
