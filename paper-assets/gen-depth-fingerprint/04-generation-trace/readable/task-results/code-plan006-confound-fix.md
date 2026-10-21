# code plan006 confound fix

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan006-confound-fix_20260515T232416_result.json`
- **Structured JSON:** [`f528524ca7f901fa594f.json`](../../sessions/f5/f528524ca7f901fa594f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

速率约 18 行/分钟，总计 ~4975 行，预计 **~4.5 小时**完成。

**已完成：**
1. 进程 246021（旧 plan-006）已停
2. `paraphrastic_chains.py` 参数已修改：`repetition_penalty=1.3→1.0`，`max_new_tokens=200→256`，与 `generate_chain.py` 完全对齐
3. 旧数据已备份（`*_old_rp13.*`）
4. 新实验已启动（PID 256127，nohup 后台），registry `plan-006-confound-fix` 状态 RUNNING

**后续监控：**
- 日志：`tail /tmp/plan006_confound_fix.log`
- 进度：`wc -l data/pythia-2.8b-paraphrase/generations_shard0.jsonl`（目标 ~4975 行）
- 跑完后 evaluate phase 会自动输出 `results/plan006_paraphrastic_comparison.json`，包含 Spearman correlation 和 F1 对比

---
