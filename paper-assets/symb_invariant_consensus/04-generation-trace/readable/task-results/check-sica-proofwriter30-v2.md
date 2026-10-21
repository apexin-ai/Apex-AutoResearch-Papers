# check sica proofwriter30 v2

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_sica_proofwriter30_v2_20260516T012108_result.json`
- **Structured JSON:** [`30a84ca714b27f76b585.json`](../../sessions/30/30a84ca714b27f76b585.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## sica_proofwriter30_v2 实验状态报告

### 1. 进程状态: **RUNNING**
- PID 155077 存活，tmux session `sica_proofwriter30_v2` 活跃
- 启动时间: 2026-05-16 06:19，已运行约 3 小时

### 2. vLLM 状态: **ALIVE**
- PID 129131，QwQ-32B，tensor-parallel=1，max-model-len=16384
- HTTP 请求持续 200 OK

### 3. 输出文件: **存在（部分）**
- `/root/symb_invariant_consensus/results/proofwriter_30_v2.json` — 29757 bytes
- 当前进度: **16/30 完成**，正在处理第 17 题
- 每题平均 ~11 分钟，预计还需 ~2.5 小时完成

### 4. 日志关键内容
- 大量 `No JSON found in response for trace` 警告（FOL 约束提取失败的 trace）
- 当前 Scorer 报告 `satisfied_ratio=1.000`，MaxSAT 全部满足，未排除任何 trace

### 5. D012 指标（部分结果 16/30）

```
C0 多候选率:    3/16 = 18.8%  — FAIL (≥20%)
C1 约束提取率:  93/192 = 48.4% — FAIL (≥50%)
C2 矛盾检测:    0 题          — FAIL (≥1)
C3 SICA-SC gap: -6.2 pp       — FAIL (>0)
```

**全部 4 项 FAIL。**

关键问题：
- **SICA 比 SC 差 6.2pp**（87.5% vs 93.8%）。Problem `RelNeg-498_Q8` SICA 答错 (True)、SC 答对 (False)——多候选场景下 SICA 被约束误导，选了错误答案
- **0 矛盾检测**：MaxSAT 从未排除任何 trace（excluded=0 全场），约束系统形同虚设
- 3 个多候选问题中，2 个约束提取 twc=0（无约束可用），SICA 退化为随机选择
- C0/C1 都在阈值边缘，剩余 14 题可能略有改善，但 C2/C3 趋势很难翻转

### 6. 结论预判

实验尚未完成，但当前趋势 **strongly negative**。即使剩余 14 题表现更好，C3（SICA-SC gap）从 -6.2pp 翻正的可能性很低。建议等实验跑完后再做最终判定，但应开始准备分析 failure mode——核心问题是约束提取质量不足以驱动有意义的 MaxSAT 筛选。

---
