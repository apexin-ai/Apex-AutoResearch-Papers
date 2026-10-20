# ops check sensitivity status

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_sensitivity_status_20260515T120230_result.json`
- **Structured JSON:** [`a3043f80b14078657293.json`](../../sessions/a3/a3043f80b14078657293.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总报告

### 进程状态

| # | PID | 脚本 | 模型 | GPU | 状态 | 运行时间 |
|---|-----|------|------|-----|------|---------|
| 1 | 218877 | seg_sensitivity_v2.py | deepseek | 0 | **运行中** | 2h27m |
| 2 | 219130 | seg_sensitivity_v2.py | qwen | 2 | **已完成** | — |
| 3 | 220988 | mpl_sensitivity.py | deepseek | 1 | **运行中** | 2h17m |
| 4 | 221265 | mpl_sensitivity.py | qwen | 3 | **运行中** | 2h17m |

### GPU 状态

| GPU | 利用率 | 显存占用 | 状态 |
|-----|--------|---------|------|
| 0 | 89% | 15.3/97.9 GB | PID 218877 占用 |
| 1 | 78% | 15.3/97.9 GB | PID 220988 占用 |
| 2 | **0%** | **3 MB** | **空闲** |
| 3 | 80% | 15.4/97.9 GB | PID 221265 占用 |

### 已完成的输出

**seg_sensitivity_v2 qwen** — 完整完成，24 个配置 (2 masking × 4 sparsity × 3 segmentation)，每个配置 n=499~500：
- `/root/autodl-tmp/pacs/analysis_output/seg_sens_v2_partial_qwen.json` (4.7 KB)

### 运行中进程的进度

**seg_sensitivity_v2 deepseek (PID 218877)**
- 脚本不写中间 checkpoint（只在 `process_model()` 结束时写一次）
- 当前磁盘上的 `seg_sens_v2_partial_deepseek.json` 是之前一次 n=10 的测试运行残留，不代表当前进度
- qwen 同脚本跑完用了 ~1h51m（17:33→19:24），deepseek 已跑 2h27m，可能 DeepSeek 生成序列更长导致更慢
- **预计剩余：0~30 分钟**（可能很快完成）

**mpl_sensitivity deepseek (PID 220988) & qwen (PID 221265)**
- 脚本每 50 个 problem 写一次 checkpoint
- 两个进程均已处理 **200/500** 个 problem（40% 完成）
- 速率约 200 problems / 137 min ≈ 1.46 problem/min
- **预计剩余：~3h26m**（约 23:25 完成）

### 全部输出文件（analysis_output/）

| 文件 | 说明 |
|------|------|
| `seg_sens_v2_partial_qwen.json` | seg v2 qwen — **完成** |
| `seg_sens_v2_partial_deepseek.json` | seg v2 deepseek — 旧测试残留，待当前进程覆盖 |
| `mpl_sens_partial_deepseek.json` (~992 KB) | mpl deepseek — 200/500，更新于 19:53 |
| `mpl_sens_partial_qwen.json` (~983 KB) | mpl qwen — 200/500，更新于 19:59 |

---
