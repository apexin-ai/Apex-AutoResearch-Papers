# submit eval 3B d005 s42 para

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_submit_eval-3B-d005-s42-para_20260516T060913_result.json`
- **Structured JSON:** [`2034a9c10c355b2339bd.json`](../../sessions/20/2034a9c10c355b2339bd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

提交完成。

**总结：**
- `exp_001_eval_3B_d005_s42_para_aligned` 已在 cuda:1 上启动（PID 713640）
- 修正了原始命令：`--mc-format para_aligned` 不是合法选项，改为 `--mc-format aligned --paraphrase-dir /root/autodl-tmp/exp001/paraphrases`
- Checkpoint `Qwen2.5-3B_d005_s42` 虽在 C006 目录名黑名单中，但 `lora_alpha=32` 验证通过
- Registry 已更新为 RUNNING，cron 监控已注册（每 8 分钟检查）

---
