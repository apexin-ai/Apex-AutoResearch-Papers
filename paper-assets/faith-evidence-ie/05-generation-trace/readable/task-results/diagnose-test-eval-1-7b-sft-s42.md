# diagnose test eval 1 7b sft s42

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_test_eval_1_7b_sft_s42_20260522T022529_result.json`
- **Structured JSON:** [`591413bbbb10f5137314.json`](../../sessions/59/591413bbbb10f5137314.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

**根因：假阳性失败。Eval 实际已成功完成，但监控系统找不到 sentinel/W&B 信号，5 次健康检查发现进程已退出后自动标记为 failed。**

### 证据

1. **输出完整** — `/root/autodl-tmp/eval_results/test_eval_1_7b_sft_s42/` 包含全部 3 个产出文件（均创建于服务器本地时间 May 22 10:13，即 UTC 02:13，比失败标记时间 02:23 早 10 分钟）：
   - `predictions.json` (8MB)
   - `codalab_submission.json`
   - `test_summary.json`

2. **Summary 指标完整**：
   - 500/500 文档处理完毕，format_ok_rate = 1.0
   - 推理耗时 12179 秒（~3.4 小时）
   - RE F1 = 0.2579, Precision = 0.3977, Recall = 0.1908
   - Evidence F1 = 0.5918
   - 409/500 文档被截断（`n_truncated: 409`）

3. **无日志文件** — `~/runs/faith-evidence-ie/test_eval_1_7b_sft_s42.log` 不存在，这是监控系统无法追踪进度的原因。

4. **GPU 0 已释放** — 当前 0MiB 占用，进程正常退出。

5. **模型/adapter 路径均存在**，无路径问题。

### 结论

- **不需要重跑**，结果已完整可用。
- 需要在 registry 中将状态从 failed 更新为 completed。
- 注意 `n_truncated: 409`（82% 文档被截断），这可能影响 recall（当前仅 0.19），可考虑增大 `max_new_tokens`。
- config 中 `base_model` 显示为 `/root/autodl-tmp/models/Qwen3-4B`，与命令行传入的 `Qwen3-1.7B` 不一致，值得确认是否影响结果。

---
