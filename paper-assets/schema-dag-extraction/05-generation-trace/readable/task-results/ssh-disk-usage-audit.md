# ssh disk usage audit

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_disk-usage-audit_20260515T063235_result.json`
- **Structured JSON:** [`a4fa36674af670e09733.json`](../../sessions/a4/a4fa36674af670e09733.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完毕。以下是审计结果：

---

## 磁盘空间审计报告

### 分区概览

| 分区 | 总量 | 已用 | 可用 |
|------|------|------|------|
| `/root/autodl-tmp` (数据盘) | 250G | 219G | 32G |
| `/` (根分区) | 30G | 27G | 4G |

### `/root/autodl-tmp/` 详细占用 (219GB)

| 目录 | 大小 | 状态 | 说明 |
|------|------|------|------|
| **`.hf_cache/Qwen/Qwen3-32B/`** | **62G** | ⚠️ 可能可清理 | Qwen3-32B **BF16 全精度**版本（17个 shard） |
| **`.hf_cache/qwen3-32b-fp8/`** | **32G** | ✅ 必须保留 | Qwen3-32B-FP8，当前实验在用 |
| **`output_seed0/`** | **92G** | ⚠️ 部分可清理 | 3轮实验输出 (G0/G1/G2 各~31G)，每轮含 5个 checkpoint×5.7G |
| **`dryrun2/`** | **27G** | 🗑️ 建议清理 | dry run 实验，G0+G1 各含旧 checkpoint |
| **`output_v7/`** | **6.3G** | ⚠️ 可能可清理 | 旧版本实验输出 |
| **`output_dryrun_seed0/`** | **446M** | 🗑️ 建议清理 | 另一个 dry run |
| **`pip_cache/`** | **1.4G** | 🗑️ 建议清理 | pip 下载缓存 |
| **`.hf_cache/` 其他** | **~250M** | ✅ 保留 | datasets, sentence-transformers 等小文件 |

### 清理方案

#### Tier 1: 确定可清理（无风险）

| 项目 | 释放空间 |
|------|---------|
| `dryrun2/` — dry run 实验，无正式结果价值 | **27G** |
| `output_dryrun_seed0/` — dry run | **0.4G** |
| `pip_cache/` — 可随时重建 | **1.4G** |
| **Tier 1 合计** | **~29G** |

#### Tier 2: Qwen3-32B BF16 全精度模型

| 项目 | 释放空间 |
|------|---------|
| `.hf_cache/Qwen/Qwen3-32B/` — BF16版，实验用的是 FP8 版 | **62G** |

如果当前实验确实只用 FP8 版本，这个 BF16 全精度版本可以删除。需要时可重新下载。

#### Tier 3: output_seed0 中间 checkpoint

`output_seed0/` 每轮 (G0/G1/G2) 都保存了 5 个 training checkpoint（每个 5.7G），总计 ~85G 的 checkpoint。如果只需要 `final_model/` 和 `metrics.jsonl`，可以删除中间 checkpoint：

| 项目 | 释放空间 |
|------|---------|
| `output_seed0/G*/training/` — 保留 final_model，删 checkpoint | **~85G** |

#### Tier 4: 旧版本实验

| 项目 | 释放空间 |
|------|---------|
| `output_v7/` — 看是否还有参考价值 | **6.3G** |

### 总结

| 清理方案 | 释放空间 | 清理后剩余 | 够装 LLaMA-70B？ |
|---------|---------|-----------|-----------------|
| Tier 1 only | ~29G | ~61G 可用 | ❌ 不够 |
| Tier 1 + Tier 2 | ~91G | ~123G 可用 | ✅ 够 |
| Tier 1 + Tier 2 + Tier 3 | ~176G | ~208G 可用 | ✅ 充裕 |
| 全部清理 | ~182G | ~214G 可用 | ✅ 充裕 |

**最小可行方案**：清理 Tier 1 + Tier 2（删 dry run + BF16 全精度 Qwen3-32B），释放 ~91G，足够下载 LLaMA-3.3-70B-FP8。

**推荐方案**：Tier 1 + Tier 2 + Tier 3（额外删 output_seed0 中间 checkpoint），释放 ~176G，留出充足空间。需确认 output_seed0 的 final_model 已经是最终结果、不需要从 checkpoint 恢复训练。

---
