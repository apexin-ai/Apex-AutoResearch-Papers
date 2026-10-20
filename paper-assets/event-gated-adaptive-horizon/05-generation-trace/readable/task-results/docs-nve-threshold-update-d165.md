# docs nve threshold update d165

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_docs_nve-threshold-update-d165_20260527T111946_result.json`
- **Structured JSON:** [`9e4a60449596287389b1.json`](../../sessions/9e/9e4a60449596287389b1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部更新完成。汇总：

**本地文件**：
- `paper_framing.md` — 所有 NVE 阈值 1.5→2.0（~20 处），分类统计更新（F1=1.0, 0 FP），R10 reviewer concern 更新为完美分离区间描述
- `paper/method.md` — τ 定义 1.5→2.0，诊断阈值段重写（F1=1.0，完美分离区间 [1.89×, 3.77×]），Collapse association 和 Link 2 中 "three consecutive"→"two consecutive"，009b 从 transient exceedance 改为 sub-threshold
- `ROADMAP.md` — θ=1.5×→θ=2.0×
- `artifacts/_project/paper/method.md`（副本同步更新）

**服务器脚本**（westd-51268）：
- `analyze_hopper_nve.py` — `NVE_TAU = 1.5`→`2.0`
- `scripts/analyze_018_full_sgs.py` — 函数默认值 + argparse default + help 文本
- `scripts/eval_nve_maniskill.py` — 同上
- `value_distribution_analysis.py` — 绘图阈值线 y=1.5→2.0 + label

**未改**（正确保留）：
- 所有实验测量值（1.71×, 1.62×, 1.88× 等）
- RAVE ceiling=1.5（超参，非 NVE 阈值）
- `plan034_nve_sensitivity.py`/`nve_threshold_analysis.py` 中的多阈值列表 `[1.3, 1.5, 1.7, 2.0]`
- `nve_audit.py`/`nve_audit_v2.py` 中的实验 NVE 数据（1.53）
- 绘图 `linewidth=1.5`

---
