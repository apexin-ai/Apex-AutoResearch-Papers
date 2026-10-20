# ops data archive

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_data-archive_20260525T204422_result.json`
- **Structured JSON:** [`6debfa2ea3b10307db3e.json`](../../sessions/6d/6debfa2ea3b10307db3e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`du -shL` 对 data/paper/results 返回 0，因为它们指向的是已被 code/project 统计过的同一目录。这是正确的——`du` 默认不重复统计已计数的 inode。逻辑数据量是对的。

归档完成。汇报如下：

---

## 归档结果

**归档路径**: `/root/persuasion_turn_jailbreak_detect_archive/`

**目录结构**（全部符号链接，磁盘新增 ≈ 0）:

| 子目录 | 链接目标 | 逻辑大小 |
|--------|---------|----------|
| `code/project` | 整个项目目录 | 17G |
| `checkpoints/all_checkpoints` | 24 个实验 checkpoint（exp26/27/36/59/70/lora/mixed/plan_016v2） | 17G |
| `results/experiment_results` | ~200+ 实验结果文件 (json/txt/log) | 13M |
| `results/logs` | 训练日志 | 1.2M |
| `data/project_data` | 自定义数据集（train/val/test splits, exp42-52 数据等） | 554M |
| `paper/latex_source` | LaTeX 源码 + main.pdf + .bib | 1.3M |
| `paper/figures_root` | figures/paper/ 下的图表 PDF/PNG | 1.1M |
| `paper/figure_scripts/` | 3 个绘图脚本（plot_fig2, exp50_figure_beautify, fig4_svd） | ~20K |

**归档总大小**: 0（纯符号链接，无额外磁盘占用）

**磁盘现状**: 30G 总量，26G 已用，**4.2G 剩余**

**tar.gz 可行性**: 不可行。项目实际 17G（checkpoints 占 17G），即使压缩后也远超 4.2G 剩余空间。如需打包归档，建议：
1. 只打包非 checkpoint 部分（~570M，压缩后约 200-300M），checkpoint 单独处理
2. 或挂载外部存储后再 tar

**其他说明**:
- 无 wandb 本地目录
- 无 .git 目录
- 无 .npy 文件
- 绘图脚本已包含

---
