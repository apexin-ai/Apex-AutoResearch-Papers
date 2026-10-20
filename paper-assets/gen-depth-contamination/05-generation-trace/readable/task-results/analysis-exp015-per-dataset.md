# analysis exp015 per dataset

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp015-per-dataset_20260514T030259_result.json`
- **Structured JSON:** [`1cb8fbc00cc20cd00560.json`](../../sessions/1c/1cb8fbc00cc20cd00560.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp-015 Neural Probe 结果报告

### 执行概况

| 数据集 | 状态 | 原因 |
|--------|------|------|
| **Pythia** | OOM 崩溃 | embedding extraction 第一个 batch 即 OOM（RTX 4090D 23GB，Qwen2.5-1.5B + `output_hidden_states=True` 内存不足） |
| **OLMo** | 未执行 | Pythia OOM 后脚本被 SIGHUP (EXIT_CODE=129) 终止 |
| **Qwen-cont** | 完成 | 第二次运行（仅跑 Qwen-cont），30000 样本，1875 batches，~7 分钟 embedding + 5-fold MLP |

日志显示两次运行拼接：第一次从 Pythia 开始立即 OOM，第二次只跑了 Qwen-cont 并成功。

### 训练方式：Independent probe per dataset

脚本使用 `run_one_dataset()` 函数逐数据集运行完整 pipeline：
- **Embedding**: Frozen Qwen2.5-1.5B last hidden state → avg pool → 1536-dim
- **Probe**: MLP (1536→512→256→6), 5-fold GroupKFold CV, early stopping
- 每个数据集独立训练独立 probe，非 pooled

### Qwen-cont Pairwise AUC 表

| Pair | Neural Probe AUC | ±std | LightGBM AUC | θ=0.60 判定 |
|------|:-:|:-:|:-:|:-:|
| **0v1** | 0.9873 | 0.0021 | 0.9972 | **PASS** |
| **1v2** | 0.6983 | 0.0073 | 0.6114 | **PASS** |
| **2v3** | 0.6195 | 0.0094 | 0.5609 | **PASS** |
| **3v4** | 0.5930 | 0.0051 | 0.5408 | FAIL |
| **4v5** | 0.5747 | 0.0072 | 0.5139 | FAIL |

Non-adjacent pairs (neural probe) 也可用：0v2=0.9944, 0v3=0.9959, 0v4=0.9978, 0v5=0.9984, 1v3=0.7901, 1v4=0.8536, 1v5=0.8896, 2v4=0.7113, 2v5=0.7728, 3v5=0.6676。距离越远 AUC 越高，符合预期。

### K* 分解

| 方法 | K* | 含义 |
|------|:--:|------|
| **Neural Probe** | **3** | depth 0-1-2-3 四层可区分，3v4 边界（0.593）跌破 θ=0.60 |
| **LightGBM (15D 手工特征)** | **2** | depth 0-1-2 三层可区分，2v3 边界（0.5609）跌破 θ=0.60 |

Neural probe 比 LightGBM **多探测到一个可区分边界**（2v3: 0.6195 vs 0.5609）。1536-dim frozen representation 比 15D 手工特征有更强的区分力，将 K* 从 2 提升到 3。

### 关键发现

1. **K*=3 来源**：仅来自 Qwen-cont 数据集的独立 probe，无跨数据集聚合
2. **与 LightGBM 的差异**：neural probe 在所有 adjacent pairs 上 AUC 均高于 LightGBM（除 0v1 略低 0.9873 vs 0.9972），表明 frozen LLM embeddings 捕捉到了手工特征遗漏的信号
3. **分类精度**：6-class accuracy 仅 43.35%，因为 depth 3-4-5 互相混淆严重
4. **结果只覆盖 Qwen-cont**，Pythia/OLMo 的 K* 尚未知

---
