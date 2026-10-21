# diagnose exp code qwen7b

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp_code_qwen7b_20260519T121403_result.json`
- **Structured JSON:** [`a9d19f3d2a4b99bb31ac.json`](../../sessions/a9/a9d19f3d2a4b99bb31ac.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**exp_code_qwen7b 实验没有失败，EXIT_CODE=1 是误报。**

日志末尾明确输出 `Pipeline complete.` + `EXIT_CODE=0`，Python 进程正常退出。所有 pipeline 阶段（模型加载 → seed data → depth 1-5 生成 → 特征提取 → AUC/JSD/Ordinal 分析）均已完成，全部产出文件存在且完整。

实验结果：**K\* = 2**（code domain, Qwen2.5-7B）。depth 0→1 AUC=0.905，depth 1→2 AUC=0.728，depth 2→3 起降至 0.537（接近随机）。

EXIT_CODE=1 可能来自 job runner wrapper 层的退出码传递问题，建议排查。诊断报告已写入 artifacts。

---
