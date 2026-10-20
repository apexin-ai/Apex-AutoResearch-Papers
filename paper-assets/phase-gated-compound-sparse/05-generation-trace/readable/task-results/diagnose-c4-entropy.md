# diagnose c4 entropy

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_c4_entropy_20260514T083804_result.json`
- **Structured JSON:** [`98affe28d54a468dc66e.json`](../../sessions/98/98affe28d54a468dc66e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验**实际上已经成功完成**，不是失败。

日志显示：
- 15:17:01 开始，加载模型到 `cuda:0`
- 处理了全部 30/30 problems
- 16:26:16 正常结束，总耗时 69.1 分钟
- 结果已保存到 `c4_entropy_results.json`（1.7MB）

Summary 表也完整输出了所有 8 个配置（4 sparsity × 2 masking strategy）的 Entropy/Gini/CV 指标。

```json
{"root_cause":"实验实际已成功完成（30/30 problems, 69.1 min）。监控系统误判为失败——可能因为：(1) 脚本不在预期路径 /root/autodl-tmp/pacs/scripts/（该目录不存在），submit_training_job 未生成 ~/runs/ 下的 c4_entropy 日志，导致 sentinel 检测失败；(2) 使用了 cuda:0 而非预期的 cuda:1","error_type":"infrastructure","fix_steps":["无需修复——实验已成功，结果在 /root/autodl-tmp/pacs/results/c4_attention_entropy/c4_entropy_results.json","如需重跑，需确认脚本实际路径（/root/autodl-tmp/pacs/scripts/ 目录不存在）","更新监控配置以匹配实际日志路径"],"can_auto_fix":false,"partial_results":"有完整结果（30/30 problems）"}
```

关键数据摘要：
- **importance pruning** 一致性地 **降低** entropy（Ent Δ ≈ -0.04 ~ -0.05），说明重要 head 被保留后注意力更集中
- **random pruning** 一致性地 **增加** entropy（Ent Δ ≈ +0.13 ~ +0.23），且随 sparsity 增大效果更强
- 这直接支持 C4 claim：importance-based pruning 保持了 KV importance discrimination

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "root_cause": "实验实际已成功完成（30/30 problems, 69.1 min）。监控系统误判为失败——可能因为：(1) 脚本不在预期路径 /root/autodl-tmp/pacs/scripts/（该目录不存在），submit_training_job 未生成 ~/runs/ 下的 c4_entropy 日志，导致 sentinel 检测失败；(2) 使用了 cuda:0 而非预期的 cuda:1",
    "error_type": "infrastructure",
    "fix_steps": [
      "无需修复——实验已成功，结果在 /root/autodl-tmp/pacs/results/c4_attention_entropy/c4_entropy_results.json",
      "如需重跑，需确认脚本实际路径（/root/autodl-tmp/pacs/scripts/ 目录不存在）",
      "更新监控配置以匹配实际日志路径"
    ],
    "can_auto_fix": false,
    "partial_results": "有完整结果（30/30 problems）"
  }
}
```

</details>

---
