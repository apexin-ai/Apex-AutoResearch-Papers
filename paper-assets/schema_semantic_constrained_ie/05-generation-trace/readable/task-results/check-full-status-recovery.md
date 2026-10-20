# check full status recovery

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_full-status-recovery_20260523T053924_result.json`
- **Structured JSON:** [`a84af95b5009b7015b37.json`](../../sessions/a8/a84af95b5009b7015b37.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态盘点报告

### 1. GPU 状态

| 服务器 | GPU | 显存占用 | 利用率 | 进程 |
|--------|-----|---------|--------|------|
| westd-21461 | cuda:0 | 0 / 98GB | 0% | **空闲** |
| westd-21461 | cuda:1 | 41.6 / 98GB | 87% | PID 88995 (python) — S2 eval 运行中 |
| westd-16980 | cuda:0 | 0 / 98GB | 0% | **空闲** |
| westd-16980 | cuda:1 | 0 / 98GB | 0% | **空闲** |

westd-16980 完全空闲，INT4/GoLLIE 实验已全部完成。

### 2. S2 进度

- 文件：`70b_lora_docred_200_full_s2.jsonl`
- 进度：**137 / 200 行**（68.5%）
- 最后写入：13:37（2分钟前，正在活跃写入）
- 预计还需一段时间完成剩余 63 条

### 3. Prompt Sensitivity 状态

**未启动。** cuda:0 空闲，无任何 prompt sensitivity 输出文件或目录。仅存在 `compare_prompts.py` 脚本，但未执行。

### 4. Paper 写作文件状态

最近 2 小时内更新的 tex 文件（共 7 个）：

| 文件 | 时间 | 大小 | 备注 |
|------|------|------|------|
| `appendix_gollie_comparison.tex` | 05:37 | 1.4KB | **新增** |
| `section6_related_work.tex` | 05:36 | 2.6KB | |
| `section5_runtime.tex` | 05:36 | 2.9KB | |
| `main.tex` | 05:36 | 9.3KB | |
| `appendix_quantization.tex` | 05:36 | 1.5KB | **新增** |
| `section5_scierc_draft.tex` | 04:25 | 8.0KB | |
| `appendix_discussion.tex` | 04:22 | 49KB | |

Quantization 和 GoLLIE 对比的 appendix 文件均已创建。

---
