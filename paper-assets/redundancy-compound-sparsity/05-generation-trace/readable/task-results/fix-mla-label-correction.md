# fix mla label correction

**When Does KV Redundancy Predict MLP Sparsity? Architecture Dependence of Cross-Axis Signals in Reasoning Inference** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_mla-label-correction_20260512T040912_result.json`
- **Structured JSON:** [`dd4f118612fc29a4769b.json`](../../sessions/dd/dd4f118612fc29a4769b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两项任务完成，汇总如下：

---

### 1. MLA 误标修复 ✓

两个文件中所有 "MLA" 引用已替换为 "Qwen2 GQA 4KV"：
- `llama_vs_deepseek_analysis.py` — 4 处（行 1, 120, 215, 267）
- `llama_vs_deepseek_summary.md` — 2 处（行 5, 57）
- 架构解释从 "MLA low-rank compressed KV 导致 decorrelation" 改为 "Qwen2 GQA 4 KV heads 导致相关性减弱"
- 分析脚本已重新运行，6 张图表（PDF+PNG）已更新

### 2. confound-ctrl-001 状态

| 指标 | 值 |
|------|-----|
| PID 24628 | **存活**，已运行 5h48m |
| 日志行数 | 25 行 |
| GPU 利用率 | 56%，15959 MiB |

**问题：HuggingFace 网络不通。** 日志显示进程在尝试下载 `HuggingFaceH4/MATH-500` 和 `hendrycks/competition_math` 数据集时反复失败（`Network is unreachable`），两个数据集各重试 5 次均超时。最后一行是 transformers 的 generation flags 警告，说明模型已加载，但日志只有 25 行且 5h48m 没有新的推理输出——**进程大概率卡死在数据集加载阶段**。

**建议：** 需要先在服务器上启用网络代理（`source /etc/network_turbo`）或提前缓存数据集到本地，然后重启实验。

---
