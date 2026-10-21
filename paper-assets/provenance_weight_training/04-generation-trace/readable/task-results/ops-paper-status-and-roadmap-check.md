# ops paper status and roadmap check

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_paper_status_and_roadmap_check_20260525T093456_result.json`
- **Structured JSON:** [`c43dfb1e227bc6cf7f36.json`](../../sessions/c4/c43dfb1e227bc6cf7f36.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报：

### Step 1: 编译状态
- **编译成功**，无 fatal error，无 undefined reference，无 missing figure
- **PDF 共 15 页**：正文 + Limitations 到第 8 页底，References 从第 9 页开始，附录在后 → **正文 ≤ 8 页 ✓**
- 仅有 10 条 `h float specifier changed to ht` 警告（无害）

### Step 2: Paper Agent 修改写入核实
- **2a D&R 叙事重构** ✓ — `results.tex:28-34` 包含完整 D&R 阈值扫描（q>0.3: 17.250, q>0.5: 17.280, q>0.7: 17.320）和 epoch-matched 分解叙事，明确 D&R 优于 adaptive
- **2b Figure 修复** ✓ — 10 个 `\includegraphics` 路径均指向 `artifacts/figures/` 下已存在的 PDF 文件，无缺失
- **2c 附录引用** ✓ — 正文中大量 `\ref{app:*}` 引用，编译 log 零 undefined reference

### Step 3: ROADMAP 核实
- **3a Random-subset = Uniform** ✓ — registry `random_subset_epoch_seed42` DONE/success，holdout_ppl=17.694 与 uniform 一致 → 已勾选
- **3b OOD eval adaptive seeds** ✓ — `adaptive_ood_seed123/456` + `uniform_ood_seed123/456` 均 DONE/success，results.tex 已写入 OOD 数据 → 已勾选
- **3c ρ=0.6 p 值 "uncorrected" 标注** — `results.tex:115` 报告 `p_BH=0.064`（Bonferroni-Holm 校正后），正文**未标注** "uncorrected"。`appendix.tex:478` 提到 uncorrected p=0.010 但仅在附录统计讨论段。**正文 ρ=0.6 段落本身没有 "uncorrected" 字样**（未修改，仅汇报）

### Step 4: ROADMAP 更新
已将以下 3 项标记完成：论文更新 N=5 统计量、Random-subset baseline、OOD eval adaptive seeds。`ρ=0.6 uncorrected` 项保持未勾选。

---
