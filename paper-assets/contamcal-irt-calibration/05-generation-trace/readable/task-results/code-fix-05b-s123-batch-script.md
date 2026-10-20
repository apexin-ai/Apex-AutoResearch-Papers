# code fix 05B s123 batch script

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-05B-s123-batch-script_20260516T035329_result.json`
- **Structured JSON:** [`489d85ad27018825048c.json`](../../sessions/48/489d85ad27018825048c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

### 脚本状态
- **0.5B 脚本** (`run_05B_s123_signals.sh`): 已更新，添加 skip 逻辑，语法验证通过
- **1.5B 脚本** (`run_15B_s123_signals.sh`): 已更新，添加 skip 逻辑，语法验证通过
- 两个脚本原本已存在（10:28 创建）但**缺少跳过已完成任务的检查**，现已补上

### compute_signals.py 参数
| 参数 | 是否必需 | 说明 |
|------|---------|------|
| `--model-path` | 必需 | 基座模型路径 |
| `--adapter-path` | 可选 | LoRA adapter 路径 |
| `--benchmark` | 必需 | mmlu/gsm8k/arc_challenge/humaneval |
| `--signal` | 必需 | s1/s2/s3/s4/all |
| `--output-dir` | 必需 | 输出目录 |
| `--cache-dir` | 可选 | 默认 /root/autodl-tmp/.hf_cache |
| `--sft-data-dir` | 可选 | 默认 /root/autodl-tmp/exp001/sft_data |
| `--ref-model-path` | 可选 | S2 参考模型，**无 `--ref-adapter-path`** |
| `--k-percent` | 可选 | 默认 20 |
| `--batch-size` | 可选 | 默认 8 |

### 当前进度
- **PID 687036 仍在运行**（已 49 分钟），命令：`compute_signals.py ... --benchmark mmlu --signal all`
- d000_s123: s1 ✓, s2 ✓, s4 运行中（mmlu）。gsm8k/arc_challenge 尚未开始
- d005_s123, d025_s123, d100_s123: 目录不存在，0 个信号

### 跳过逻辑
脚本检查每个 model×benchmark 组合的 3 个信号文件（s1_embedding, s2_minkpp, s4_selfcritique）是否都存在，全存在则跳过。d000_s123/mmlu 完成后运行脚本，该组合会被自动跳过，从 d000_s123/gsm8k 继续。

### 不要立即运行——等 d000_s123/mmlu 的 PID 687036 结束后提交。

---
