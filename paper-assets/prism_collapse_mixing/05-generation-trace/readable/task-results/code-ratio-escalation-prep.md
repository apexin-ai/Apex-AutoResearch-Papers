# code ratio escalation prep

**prism collapse mixing** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_ratio_escalation_prep_20260516T032402_result.json`
- **Structured JSON:** [`759a7572f773d69e79ea.json`](../../sessions/75/759a7572f773d69e79ea.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`base` 仅用于：`data/`、脚本路径（`compute_signals.py` / `generate_synthetic.py` / `train.py` / `analyze_correlation.py`）、`exp_base` 构造。完全正确。

---

**修改汇报：**

### 修改的文件
- `run_pipeline.py` — 7 处修改（backup 在 `run_pipeline.py.bak`）

### 新增参数
| 参数 | 类型 | 默认值 | 说明 |
|---|---|---|---|
| `--synthetic_ratio` | float | 0.5 | 合成数据占比。0.8=80%合成+20%真实，1.0=纯合成 |
| `--exp_name` | str | "" | 实验名。非空时 synthetic/mixed/checkpoints/results 输出到 `{base_dir}/{exp_name}/`，data 共享 |

### 混合逻辑变更（`mix_data` 函数）
- `ratio=0.5`（默认）：行为与原来完全一致（全量 concat）
- `ratio=0.8`：保留全部 synthetic，对 real 做随机子采样使最终比例为 80/20
- `ratio=1.0`：纯 synthetic，跳过 real 读取和 `split_real_pool`

### 新增配置脚本
```
configs/ratio_escalation/
├── run_ratio_0.8.sh   # --synthetic_ratio 0.8 --exp_name ratio_0.8
├── run_ratio_0.9.sh   # --synthetic_ratio 0.9 --exp_name ratio_0.9
└── run_ratio_1.0.sh   # --synthetic_ratio 1.0 --exp_name ratio_1.0
```

每组单 seed (42)，3 代，`--skip_data_prep`（复用已有 data），输出隔离到各自 `ratio_X.X/` 子目录。

### 运行命令
```bash
bash configs/ratio_escalation/run_ratio_0.8.sh
bash configs/ratio_escalation/run_ratio_0.9.sh
bash configs/ratio_escalation/run_ratio_1.0.sh
```

---
