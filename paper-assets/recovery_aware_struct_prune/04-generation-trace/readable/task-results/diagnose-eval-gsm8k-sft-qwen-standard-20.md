# diagnose eval gsm8k sft qwen standard 20

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_gsm8k_sft_qwen_standard_20_20260520T154435_result.json`
- **Structured JSON:** [`1572cd769fa4207a5258.json`](../../sessions/15/1572cd769fa4207a5258.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结论

**实验没有失败。** Log 末尾明确显示 `EXIT_CODE=0`，不是 143。

### 结果摘要

| 实验 | 状态 | Accuracy | Correct/Total | EOS Rate | Avg Len |
|------|------|----------|---------------|----------|---------|
| Standard 20% SFT | **完成** | **0.2100 ± 0.0288** | 42/200 | 36.5% | 1639 |
| CKA-only 20% SFT | **完成** | **0.5150 ± 0.0353** | 103/200 | 27.0% | 1536 |

### 关键发现

- **Standard eval** 跑完了全部 200/200 sample，JSON 文件已写入（189KB，完整包含 200 个 example）
- 两个实验的 EXIT_CODE 都是 0，SIGTERM 信号可能在进程退出后被发送（或者是监控系统在进程正常退出后发的清理信号）
- CKA-only 23:34 结束，Standard 23:41 结束，差 7 分钟——符合预期（Standard 生成更长的 response）

### 值得注意的质量信号

- Standard SFT 20% accuracy **仅 21%**，远低于 CKA-only 的 51.5%（差距 ~30pp）
- Standard 的 truncated rate 更高（63.5% vs 73%），avg_response_length 也更长，说明模型倾向于生成冗长、不收敛的回答
- 第一个 example 中模型在给出正确答案后继续生成了重复内容（`assistant` token 后又重复推理），这是 SFT 质量问题而非 eval 问题

**不需要重跑。** 数据完整，可直接用于对比分析。

---
