# code ssh check server b

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_ssh_check_server_b_20260519T081927_result.json`
- **Structured JSON:** [`49b49e31eb2ddadaa5aa.json`](../../sessions/49/49b49e31eb2ddadaa5aa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Server B (autodl-5090-b) 状态汇报

### GPU
- **4× RTX 5090**，全部 100% 利用率，显存 31.9/32.6 GB
- vLLM TP=4 运行中（Worker_TP0-TP3）

### 推理进程
- 脚本：`zeroshot_inference_72b.py --datasets scierc conll2003 fewnerd`
- 启动时间：15:58（约 21 分钟前）
- 速度：~9,500 toks/s input，~1,678 toks/s output

### 各数据集进度

| 数据集 | 状态 | 详情 |
|--------|------|------|
| **SciERC** | **已完成** | 551 行 output，529 instances × 8 samples，signal report 已生成 |
| **CoNLL2003** | **进行中 ~87%** | 23,952 / 27,624 prompts（3,453 × 8），预计 ~2 分钟完成 |
| **FewNERD** | **未开始** | 排在 CoNLL 之后 |

### SciERC 初步信号（full_signal_report.json）
- Greedy baseline: 39.9% F1
- Majority vote: 41.3% F1
- Oracle: 54.9% F1（oracle-greedy gap ~15pt，选择空间大）
- 最强信号：VC (ρ=0.277)，FK (ρ=0.227)，SJ (ρ=0.217)

### 结论
CoNLL 推理还剩约 2 分钟即完成，之后自动进入 FewNERD。FewNERD 规模取决于实例数，预计需要额外时间。全部完成无需人工干预。

---
