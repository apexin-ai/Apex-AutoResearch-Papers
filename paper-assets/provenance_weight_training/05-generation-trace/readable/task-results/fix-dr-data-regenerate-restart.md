# fix dr data regenerate restart

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_dr_data_regenerate_restart_20260521T145127_result.json`
- **Structured JSON:** [`17b9a0814907d6de3044.json`](../../sessions/17/17b9a0814907d6de3044.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

模型和数据已加载（153725 条），训练正在启动。

---

### 汇报

| 项目 | 结果 |
|------|------|
| **1. cuda:0 kill** | 成功，PID 601614 已终止，显存已释放 |
| **2. 过滤脚本逻辑** | 正确：`q_score <= threshold` 保留（即保留低分真实数据）。脚本无 bug，旧文件应该是用其他方式生成的 |
| **3. 旧文件 vs 新文件** | 见下表 |
| **4. contamination_ratio** | 仅用于 config_summary 日志记录，不参与任何权重计算。D&R 用 `uniform` 方法，完全无影响 |
| **5. 新实验** | 已提交。PID=623042，tmux session=`dr_epoch_matched_indep_lr_v2_seed42`，cuda:0 |

**数据文件对比：**

| 指标 | 旧文件（错误） | 新文件（正确） |
|------|----------------|----------------|
| 总行数 | 217,774 | 153,725 |
| depth=0 (real) | 31,994 (14.7%) | 132,895 (86.4%) |
| depth=1 (synth) | 185,780 (85.3%) | 20,830 (13.6%) |
| mean q_score | 0.8899 | 0.1863 |
| q_score 范围 | [0.50, 1.00] | [0.00, 0.50] |

---
