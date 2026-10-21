# ops probe westd 16639

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_probe-westd-16639_20260525T204035_result.json`
- **Structured JSON:** [`03593fe223633dd6d8c1.json`](../../sessions/03/03593fe223633dd6d8c1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

探测完成。以下是完整摘要：

---

## westd-16639 服务器项目数据摘要

### 磁盘空间

| 分区 | 容量 | 已用 | 可用 | 使用率 |
|------|------|------|------|--------|
| 根分区 `/` | 30G | 12G | **19G** | 40% |
| 数据盘 `/root/autodl-tmp` | 350G | 230G | **121G** | 66% |

### 项目大小

| 路径 | 大小 |
|------|------|
| `/root/symb_invariant_consensus` | **1.1G** |
| `/root/autodl-tmp/symb_invariant_consensus` | **17G**（其中 models/ 占 17G） |
| `/root/autodl-tmp/.hf_cache` | **1.3G** |

### results 目录
- **大小**: 834M
- **文件/目录数**: 97 条（含 ~25 个 JSON 文件 + ~72 个实验子目录）
- 最大文件: `r11_3verifier_canonical.json` (126K)
- 典型实验目录: `multi_seed/`, `exp_d126_crossmodel_sica/`, `exp_d135_frontier_scb/` 等

### artifacts 目录
- **大小**: 176K
- **文件数**: 5 个（capability_gap_scatter.pdf/png, deberta_ft_combo_all.json, nli_recompute.json, nondeterminism_root_cause.md）

### HF Cache
- **大小**: 1.3G（位于 `/root/autodl-tmp/.hf_cache`）

### Checkpoint 文件
- **无** `.pt/.pth/.bin/.safetensors` 文件在项目根目录
- `/root/symb_invariant_consensus/checkpoints/deberta-large-pw-finetuned/` 存在但**为空** (0 bytes)
- `/root/autodl-tmp/symb_invariant_consensus/models/` 包含：`deberta-large-pw-owa` 和 `deberta-large-pw-owa-dryrun`（共 17G）

### Git 状态
- **项目无 `.git` 目录** — 非 git 仓库

### Figures
- `figures/`: f2_sc_vs_delta (pdf/png), f3_kt_sensitivity (pdf/png), 及生成脚本 gen_f2.py, gen_f3.py
- `docs/paper/figures/`: gen_f6_kappa_accuracy_scatter.py, gen_capability_gap_scatter.py

### 特殊发现
1. **项目不是 git 仓库**（无 .git 目录）
2. **wandb 目录不存在**（实验可能用的远端 wandb 或未启用）
3. **checkpoints 目录为空**，实际模型权重在数据盘 `/root/autodl-tmp/symb_invariant_consensus/models/`（17G）
4. 数据盘已用 66%，仍有 121G 可用空间充裕
5. `scripts/` 目录非常活跃（100+ 文件），包含大量实验运行/分析脚本，最近更新到 May 25

---
