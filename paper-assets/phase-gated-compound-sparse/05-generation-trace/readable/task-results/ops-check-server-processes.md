# ops check server processes

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_server_processes_20260515T120628_result.json`
- **Structured JSON:** [`d2be9524d3184d7e9f2d.json`](../../sessions/d2/d2be9524d3184d7e9f2d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Sensitivity 分析进程状态

| PID | 脚本 | 状态 | 运行时长 | GPU | GPU 利用率 | 显存占用 |
|-----|-------|------|----------|-----|-----------|---------|
| 218877 | `seg_sensitivity_v2.py --model deepseek` | **running** | 2h31m | GPU 0 | 97% | 19,336 MiB / 97,887 MiB |
| 219130 | `seg_sensitivity_v2.py --model qwen` | **completed** | — | GPU 2 | 0% | 空闲 |
| 220988 | `mpl_sensitivity.py --model deepseek` | **running** | 2h21m | GPU 1 | 76% | 15,380 MiB / 97,887 MiB |
| 221265 | `mpl_sensitivity.py --model qwen` | **running** | 2h20m | GPU 3 | 77% | 15,380 MiB / 97,887 MiB |

### 已完成：PID 219130 (seg_sensitivity_v2 qwen)

输出文件：
- `analysis_output/qwen_segmentation_sensitivity.json` — 4.7KB, 181 行, 最终结果（JSON 数组，包含 wilcoxon_p / bonf_p_k4 / significance 字段，正常结束）
- `analysis_output/seg_sens_v2_partial_qwen.json` — 4.7KB, 169 行, 中间 checkpoint

### 仍在运行的进程 checkpoint 文件

- `mpl_sens_partial_deepseek.json` — 992KB, 最后更新 19:53 (约 10 分钟前)
- `mpl_sens_partial_qwen.json` — 983KB, 最后更新 19:59 (约 4 分钟前)
- `seg_sens_v2_partial_deepseek.json` — 4.5KB, 最后更新 17:35 (较早，可能写入频率低)

### GPU 空闲情况

**GPU 2 完全空闲**（0% 利用率，3 MiB 占用），可立即使用。其余 3 张卡均在工作中。

---
