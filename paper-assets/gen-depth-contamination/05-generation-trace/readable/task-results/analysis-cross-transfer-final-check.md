# analysis cross transfer final check

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_cross-transfer-final-check_20260520T025640_result.json`
- **Structured JSON:** [`c6a633e7c0abb4c0c42f.json`](../../sessions/c6/c6a633e7c0abb4c0c42f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据已收集。以下是汇总。

---

## 1. 新实验结果

### wiki_qwen7b → wiki_llama8b (完成)

| Pair | AUC | 95% CI | ci_lower > θ |
|------|-----|--------|-------------|
| 0v1 | 0.9998 | [0.9995, 1.0000] | ✓ |
| 1v2 | 0.7384 | [0.7308, 0.7464] | ✓ |
| 2v3 | 0.6278 | [0.6196, 0.6357] | ✓ |
| 3v4 | 0.5870 | [0.5795, 0.5941] | ✗ |
| 4v5 | 0.5519 | [0.5451, 0.5589] | ✗ |

**K\* = 3**, kstar_indexing = **MISSING**（JSON 中无此字段）, elapsed = 3621s

### wiki_llama8b → wiki_qwen7b (崩溃)

```
AssertionError: Invalid device id
```
脚本用 `--gpu 1` 启动，但 `cuda:1` 不可用。需用 `--gpu 0` 重跑。

---

## 2. 完整 13/14 对矩阵（按 train_model 分组）

| # | Train → Test | K\* | 0v1 AUC | 1v2 AUC | 2v3 AUC | 3v4 AUC | 4v5 AUC | indexing |
|---|-------------|-----|---------|---------|---------|---------|---------|----------|
| | **llama8b trains** | | | | | | | |
| 1 | llama8b → olmo | 1 | 0.9999 | 0.4984 | 0.4886 | 0.4999 | 0.4971 | 1-indexed |
| 2 | llama8b → pythia | 2 | 0.9998 | 0.6800 | 0.5958 | 0.5538 | 0.5502 | 1-indexed |
| 3 | llama8b → qwen7b | — | **崩溃，待重跑** | | | | | |
| | **mistral7b trains** | | | | | | | |
| 4 | mistral7b → pythia | 2 | 0.9999 | 0.6602 | 0.5746 | 0.5434 | 0.5393 | 1-indexed |
| | **olmo trains** | | | | | | | |
| 5 | olmo → llama8b | 2 | 0.9770 | 0.6439 | 0.5683 | 0.5424 | 0.5226 | 1-indexed |
| 6 | olmo → pythia | 1 | 0.9324 | 0.5864 | 0.5247 | 0.5066 | 0.5164 | 1-indexed |
| 7 | olmo → qwen7b | 2 | 0.9822 | 0.6331 | 0.5457 | 0.5310 | 0.5119 | 1-indexed |
| | **pythia trains** | | | | | | | |
| 8 | pythia → llama8b | 2 | 0.9999 | 0.6994 | 0.6073 | 0.5819 | 0.5473 | 1-indexed |
| 9 | pythia → mistral7b | 2 | 0.9999 | 0.6931 | 0.6013 | 0.5607 | 0.5496 | 1-indexed |
| 10 | pythia → olmo | 1 | 0.9998 | 0.4871 | 0.4907 | 0.4970 | 0.4980 | 1-indexed |
| 11 | pythia → qwen7b | 3 | 0.9999 | 0.7010 | 0.6095 | 0.5684 | 0.5466 | 1-indexed |
| | **qwen7b trains** | | | | | | | |
| 12 | qwen7b → llama8b | **3** | 0.9998 | 0.7384 | 0.6278 | 0.5870 | 0.5519 | **MISSING** |
| 13 | qwen7b → olmo | 1 | 0.9997 | 0.4920 | 0.4889 | 0.5014 | 0.4973 | 1-indexed |
| 14 | qwen7b → pythia | 2 | 0.9997 | 0.6651 | 0.5774 | 0.5468 | 0.5409 | 1-indexed |

---

## 3. 异常汇总

1. **wiki_llama8b → wiki_qwen7b**：崩溃（`Invalid device id`，cuda:1 不存在）。需用 `--gpu 0` 单独重跑。
2. **wiki_qwen7b → wiki_llama8b**：JSON 中缺少 `kstar_indexing` 字段（其余 12 个均为 `1-indexed`）。推测是新版脚本漏写，或旧版脚本补写的。功能上不影响结果，但应补上。
3. **→ olmo 方向 K\*=1 模式明显**：llama8b/pythia/qwen7b 训练后迁移到 olmo 测试集时，1v2 AUC 全部约 0.49（随机水平），K\* 一致为 1，说明 depth 信号完全不跨模型迁移到 olmo。

---
