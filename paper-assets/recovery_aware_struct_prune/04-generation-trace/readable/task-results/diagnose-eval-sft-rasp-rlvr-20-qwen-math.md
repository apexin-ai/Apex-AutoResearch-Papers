# diagnose eval sft rasp rlvr 20 qwen math

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_sft_rasp_rlvr_20_qwen_math_20260516T181852_result.json`
- **Structured JSON:** [`81434c2e61f395b27e53.json`](../../sessions/81/81434c2e61f395b27e53.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验实际上**成功完成**了。日志显示评估跑完了 200/200 样本，结果已保存。问题出在 Cron 监控端没能正确读取 W&B metrics。

关键信息：

**实验结果**：
- **GSM8K Accuracy: 73.00% ± 3.14% (146/200)**
- EOS rate: 100%, avg response length: 127 tokens
- 结果文件: `/root/autodl-tmp/recovery_aware_struct_prune/results/eval_sft_rasp_rlvr_20_qwen_math.json` (已保存, 141KB)

**失败原因**：实验本身成功完成，但脚本没有将结果上报 W&B（或上报时网络不可达）。日志中可见 `[Errno 101] Network is unreachable` 错误——HuggingFace Hub 网络不通（数据集加载时触发，虽然通过本地缓存 fallback 解决了数据加载问题，但 W&B 上报大概率也因同样的网络问题失败）。Cron 监控依赖 W&B metrics 判断完成状态，所以报了 "exited without valid W&B metrics"。

**修复方案**：
1. 无需重跑实验——结果已存在，accuracy 73.00%
2. 如果需要 W&B 记录，可在网络恢复后手动补报（从 JSON 文件读取结果 post 到 W&B）
3. 长期：eval 脚本应在 W&B 上报失败时 graceful fallback，Cron 监控应同时检查本地 JSON 文件是否生成作为成功判据

---
