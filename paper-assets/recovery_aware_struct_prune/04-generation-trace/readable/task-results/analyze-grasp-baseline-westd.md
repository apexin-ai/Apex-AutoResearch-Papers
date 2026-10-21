# analyze grasp baseline westd

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_grasp_baseline_westd_20260515T150711_result.json`
- **Structured JSON:** [`57ebfff038dd46d85eb4.json`](../../sessions/57/57ebfff038dd46d85eb4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**实验仍在运行，尚未完成。**

进程状态：
- **PID 38120** 仍在运行（CPU 105%），当前进度 **51/100**
- 日志最后修改时间：23:07:18（刚刚）

中间结果（50/100 checkpoint）：
- **GSM8K accuracy = 6.0%**（6/100 correct so far）
- EOS rate = 2.00%（模型很少自行停止，几乎都跑满 4096 tokens）
- 平均生成长度 = 4018 tokens

没有 JSON 结果文件或 checkpoint，因为评估尚未完成。

警告：
- HuggingFace 网络不可达（已自动 fallback 到本地缓存，无影响）
- 无 ERROR 或 Traceback

同服务器还有 3 个进程在跑：
1. `sft_grasp_20_westd` — GraSP pruned model 的 SFT 恢复训练（cuda:0）
2. `eval-sft-alpha-1p0` — alpha=1.0 SFT 模型的 GSM8K eval（cuda:1）
3. `sft_alpha2_0` — alpha=2.0 模型的 SFT 训练（cuda:1）

按 ~51s/sample 估算，剩余 49 个样本约需 **42 分钟**完成。

---
