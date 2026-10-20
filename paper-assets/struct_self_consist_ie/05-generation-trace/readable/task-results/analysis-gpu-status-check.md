# analysis gpu status check

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_gpu_status_check_20260515T160848_result.json`
- **Structured JSON:** [`1ebbbacee5e1dab89b04.json`](../../sessions/1e/1ebbbacee5e1dab89b04.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## autodl-5090 GPU 状态汇总

### GPU 状态（4× RTX 5090 32GB）

| GPU | 显存占用 | GPU利用率 | 温度 | 状态 |
|-----|---------|----------|------|------|
| cuda:0 | 2MiB / 32607MiB | 0% | 29°C | **空闲** |
| cuda:1 | 2MiB / 32607MiB | 0% | 29°C | **空闲** |
| cuda:2 | 2MiB / 32607MiB | 0% | 28°C | **空闲** |
| cuda:3 | 2MiB / 32607MiB | 0% | 27°C | **空闲** |

**无 GPU 进程运行。** 四张卡全部空闲。

### tmux 会话

存在一个 tmux 会话 `exp_001_n16_seed456`，但对应的 Python 进程已结束（ps 中无 python 进程），属于**残留会话**，可清理。

### 实验结果（已完成，待收集）

所有 ROADMAP 中标记的实验均已完成并有输出：

| 实验 | 完成时间 | 输出文件 |
|------|---------|---------|
| **exp_017_llama_conll_n8_t07** (cuda:0) | May 15 23:38 | `report.json` (1.7KB) + `samples.jsonl` (9.5MB) |
| **exp_lp_scierc_t07** (cuda:1) | May 15 23:40 | `report.json` (1.7KB) + `samples.jsonl` (3.8MB) |
| **exp_re_scierc_seed123** (cuda:2) | May 15 23:45 | `report.json` (3.4KB) + `samples.jsonl` (3.8MB) |
| **exp_re_scierc_seed456** (cuda:3) | May 15 23:45 | `report.json` (3.4KB) + `samples.jsonl` (3.8MB) |

另外 `analysis_round8/` 目录下有 3 个新的分析 JSON 文件。

### 结论

- **4 张 GPU 全部空闲**，无训练进程
- **无僵尸进程**（仅系统服务 + 1 个残留 tmux 会话）
- **4 个实验全部完成**，结果待收集（均在 May 15 23:38-23:45 完成）

---
