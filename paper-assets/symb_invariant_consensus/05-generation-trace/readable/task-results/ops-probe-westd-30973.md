# ops probe westd 30973

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_probe-westd-30973_20260525T204041_result.json`
- **Structured JSON:** [`a76c20a1a97454d4c803.json`](../../sessions/a7/a76c20a1a97454d4c803.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据收集完毕。以下是完整报告：

---

## westd-30973 服务器数据探测报告

### 磁盘空间

| 分区 | 总量 | 已用 | 可用 | 使用率 |
|------|------|------|------|--------|
| 根分区 `/` | 30G | 13G | **18G** | 42% |
| 数据盘 `/root/autodl-tmp` | 250G | 54G | **197G** | 22% |

### 项目总大小

- `/root/symb_invariant_consensus`: **226M**
- `/root/autodl-tmp/symb_invariant_consensus`: **不存在**

### results 目录

- 大小: **1.2M**
- 文件数: **3 个** JSON 文件（均在 `results/multi_seed/` 下）
  - `llama8b_pw_seed456_v2/results.json`
  - `llama8b_pw_seed789_v2/results.json`
  - `qwen25_pw_seed789_v3/results.json`

### artifacts 目录

- 大小: **176K**
- 文件数: **5 个**
  - `capability_gap_scatter.pdf` / `.png`
  - `deberta_ft_combo_all.json`
  - `nli_recompute_exp091_exp092.json`
  - `nondeterminism_root_cause.md`

### HF cache

- `/root/autodl-tmp/.hf_cache`: **1.4M**（几乎为空，仅有元数据）

### checkpoint 文件

- `checkpoints/deberta-large-pw-finetuned/` 目录存在但**大小为 0**（空占位符）
- 整个项目内**无 .pt / .pth / .bin / .safetensors 文件**

### Git 状态

- **`.git` 目录不存在**——项目代码不是 git 仓库（可能是通过 scp/rsync 复制过来的）

### autodl-tmp 子目录明细

| 目录 | 大小 | 内容 |
|------|------|------|
| `models/Meta-Llama-3.1-8B-Instruct` | 16G | LLM 权重 |
| `models/Qwen2.5-14B-Instruct` | 28G | LLM 权重 |
| `nli_models/` | 11G | bart-large-mnli, deberta-large-mnli, roberta-large-mnli |
| `folio_traces/` | 2.5M | 推理 trace 数据 |
| `folio_nli_combo/` | 0 | 空目录 |
| `results/` | 768K | 额外结果数据 |
| `run_folio_nli_combo.py` | — | 脚本文件 |

### 特殊发现

1. **无 git 仓库** — 代码是裸复制，无版本控制，sync_code 不可用
2. **无 wandb 目录** — 该服务器未配置 wandb 本地日志
3. **models 目录空** — `/root/symb_invariant_consensus/models/` 为空，实际模型全在 `/root/autodl-tmp/models/`
4. **checkpoints 空壳** — `deberta-large-pw-finetuned` 目录存在但无实际权重文件
5. **figures 源数据** — 仅一个 `gen_capability_gap_scatter.py`，对应 artifacts 中的 scatter 图
6. **autodl-tmp 主要被 LLM 权重占据** — 44G models + 11G nli_models = 55G（占数据盘 54G 已用的绝大部分）

---
