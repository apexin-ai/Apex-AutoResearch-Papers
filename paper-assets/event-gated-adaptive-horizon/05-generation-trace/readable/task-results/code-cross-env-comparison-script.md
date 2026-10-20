# code cross env comparison script

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_cross-env-comparison-script_20260524T235556_result.json`
- **Structured JSON:** [`a325007d67ee97026862.json`](../../sessions/a3/a325007d67ee97026862.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部输出文件已生成：
- `cross_env_civo_table.tex` — LaTeX 表格
- `cross_env_civo_summary.json` — JSON 汇总数据
- `cross_env_nve_bars.png/pdf` — NVE 分组柱状图（含 1.5x 阈值线）
- `cross_env_ve_ratio_timelines.png/pdf` — 三环境 ve_ratio 时间线

脚本保存在本地 `artifacts/scripts/cross_env_civo_comparison.py`，服务器上同步了一份。Walker Walk 和 Cheetah Run 的 trained dt_emb 均触发 CIVO，no dt_emb control 均未触发，验证了 CIVO 泛化性 claim。Cartpole 的 exp_062（no dt_emb control）尚不存在，exp_061 目前 NVE 很低，待训练进一步推进后重跑脚本即可更新。

---
