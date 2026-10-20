# data plan005 multi attack gen

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data_plan005-multi-attack-gen_20260517T170605_result.json`
- **Structured JSON:** [`4790f7bd67bd7cc676d3.json`](../../sessions/47/4790f7bd67bd7cc676d3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

生成进行中，进度稳定。当前状态：

**FITD:** 12/80, ETA ~84min  
**DD:** ~8/80, ETA ~95min

两个进程在后台自动运行，输出即时保存到 JSONL 文件。即使出现单条错误也会跳过继续。如果需要检查最终结果，可以等约 90 分钟后运行：

```bash
# 查进度
tail -3 /root/persuasion_turn_jailbreak_detect/logs/gen_fitd_full.log
tail -3 /root/persuasion_turn_jailbreak_detect/logs/gen_dd_full.log

# 查已生成条数
wc -l /root/persuasion_turn_jailbreak_detect/data/generated/fitd_all.jsonl
wc -l /root/persuasion_turn_jailbreak_detect/data/generated/deceptive_delight_all.jsonl
```

质量已通过 5 条样本验证：
- 无 `&lt;think>` 泄漏
- 无重复内容（similarity check + repetition_penalty）
- 策略标注符合 playbook 设计
- 对话递进自然

完成后我会运行 Step 5/6 的验证和报告。需要我现在检查还是稍后？

---
