# diagnose eval gsm8k grpo rasp 20 fair

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_gsm8k_grpo_rasp_20_fair_20260519T153024_result.json`
- **Structured JSON:** [`ea92b48edaec685b5581.json`](../../sessions/ea/ea92b48edaec685b5581.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断文件名不在白名单中，直接汇报结果。

## 诊断结论：实验已成功完成

**实验未失败。** 最新一次运行（2026-05-19 20:49 启动）已完整执行 1319/1319 样本并于 23:20 正常退出。

### 结果

- **GSM8K Accuracy: 60.88% ± 1.34% (803/1319)**
- EOS rate: 98.79%, avg response length: 195.7 tokens
- 结果文件已写入: `eval_gsm8k_grpo_rasp_20_fair.json` (1.0MB)
- Sentinel 文件已写入: `eval_gsm8k_grpo_rasp_20_fair.json.done`

### 关于 "process dead 5×" 的解释

此前 cron 监控报告的 5 次 process dead 可能来自更早的失败尝试。最终这次运行完整跑完了。运行过程中有两个小插曲但均自动恢复：

1. **HuggingFace Hub 不可达** — 脚本自动回退到本地缓存数据集，未影响结果
2. **sample 1309 附近短暂减速**（~2s/it → 107s/it，约 6 分钟）— 可能是 GPU 瞬时负载，之后恢复

### 无需任何操作

结果文件和 sentinel 均已就绪，下游流程可正常消费。

---
