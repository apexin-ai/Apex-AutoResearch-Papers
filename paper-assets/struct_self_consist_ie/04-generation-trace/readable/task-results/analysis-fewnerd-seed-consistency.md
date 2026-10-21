# analysis fewnerd seed consistency

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_fewnerd_seed_consistency_20260518T204335_result.json`
- **Structured JSON:** [`8b031b4144978cbe5faf.json`](../../sessions/8b/8b031b4144978cbe5faf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。以下是完整结果。

---

## 诊断结果

### 1. 各 seed 精确配置对比

| 实验 | 数据文件 | 总实例 | Gold-filter 后 | N | Seed | 模型 |
|---|---|---|---|---|---|---|
| `exp_027_fewnerd_n16` | `data/fewnerd_n16_subset/test.json` | 5000 | **4351** | **16** | 42 (default) | exp_021 adapter |
| `exp_021_inference` | `data/fewnerd/test.json` | 37648 | **32565** | **8** | 42 (default) | exp_021 adapter |
| `exp_021_fewnerd_n8_seed123` | `data/fewnerd/test.json` | 37648 | **32565** | **8** | 123 | exp_021 adapter |
| `exp_021_fewnerd_n8_seed456` | `data/fewnerd/test.json` | 37648 | **32565** | **8** | 456 | exp_021 merged |

### 2. 不一致根因

**两个独立差异叠加**：

1. **测试集不同**: `exp_027` 用的是 `fewnerd_n16_subset`（从全集 37648 中随机采样的 5000 条，ID 乱序），seed=123/456 用的是全集 `fewnerd/test.json`（37648 条）
2. **N 不同**: `exp_027` 用 N=16（当时做 N scaling 实验），seed=123/456 用 N=8

Gold-filter 逻辑一致（去除 entities 为空的实例），所以：
- 5000 - 649 gold-empty = 4351
- 37648 - 5083 gold-empty = 32565

### 3. 推荐方案

**方案 B 已可直接实施**：seed=42 的 N=8 全集数据已存在于 `exp_021_inference`（37648 实例，32565 gold-filtered，N=8，seed=42 default）。

三个可比的 seed=42/123/456 数据集：

| 目录 | Seed | N | Gold-filtered | Greedy F1 |
|---|---|---|---|---|
| `exp_021_inference` | 42 | 8 | 32565 | ~0.789* |
| `exp_021_fewnerd_n8_seed123` | 123 | 8 | 32565 | 0.7885 |
| `exp_021_fewnerd_n8_seed456` | 456 | 8 | 32565 | 0.7888 |

*（exp_021_inference 的 results.json 中未直接存 greedy_f1，但 paired_n8_baseline.json 显示在 5000 子集上 greedy_f1=0.7478，与 exp_027 的 0.7478 一致，说明模型相同）

**实施步骤**：
1. 对 `exp_021_inference` 用与 seed=123/456 相同的 `analyze_fewnerd_results.py` 生成统一格式的 report.json
2. 三组数据全部基于 `data/fewnerd/test.json` 全集、N=8、gold-filter=5083，直接可比
3. `exp_027_fewnerd_n16` 的 4351 实例数据可保留用于 N=8 vs N=16 scaling 分析（已有 `paired_n8_baseline.json`），但不参与 multi-seed 对比

补充：`exp_021_fewnerd_n8_seed789` 目录存在但为空，如需第四个 seed 可补跑。

---
