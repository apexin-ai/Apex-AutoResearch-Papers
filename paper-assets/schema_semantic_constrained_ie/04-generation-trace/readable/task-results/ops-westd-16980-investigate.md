# ops westd 16980 investigate

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd-16980-investigate_20260516T060950_result.json`
- **Structured JSON:** [`135020b20bc48f63c43a.json`](../../sessions/13/135020b20bc48f63c43a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有关键数据已收集。汇总报告：

```
## w6_mistral_scierc_constrained 排查结果
- 根因: 进程已正常完成（551/551, success=551, fail=0），但 exit sentinel 未写入
  - tmux session 已不存在（可能 session 退出后被自动清理）
  - /tmp/agent-ml-exit/w6_mistral_scierc_constrained.exit 不存在
  - 日志最后更新 14:05，实际全部跑完
  - 非 xgrammar 问题，非 OOM，非 crash
- 日志关键行:
  [551/551] NIPS_2016_80_abs_sent3: OK E=3 R=2 2.4s
  Done: 551 new samples, success=551, fail=0 (skipped 0 already processed)
  Output: outputs/w6_mistral_scierc_constrained.jsonl
- GPU 状态: cuda:0 空闲（当前被 w7_qwen_ft_grammar PID 337075 占用 ~15GB），cuda:1 被 w5 eval 占用
- 修复方案: 无需修复。进程已成功完成，只是 cron 监控因缺少 sentinel 误报。
  可手动补写: echo "0|2026-05-16T14:05:00Z" > /tmp/agent-ml-exit/w6_mistral_scierc_constrained.exit
- Metrics (from violation_report + F1 计算):
  - ET%: 0.00 (constrained decoding生效)
  - RV%: 0.00
  - DR%: 13.36
  - E-F1: 55.38 (P=51.02, R=60.55)
  - R-F1: 5.50 (P=4.38, R=7.39)
  - parse_fail_rate: 0.00%
  - total_samples: 551

## w5_qwen_docred_lora_constrained_eval 进度
- 进程状态: 运行中 (PID 321568, 100% CPU, GPU 1 占用 17.4GB, 82% util)
- 完成度: 688/998 (68.9%)
- 日志最新行: [656/998] Brazil–Pakistan relations: FAIL E=0 R=0 76.3s
- 已运行: ~4h16m (从 09:54 开始)
- 预估剩余: ~2h (按平均速度)
- tmux session: w5_qwen_docred_lora_constrained_eval (active)
```

---
