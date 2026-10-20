# ops fix duplicate eval gpu1

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fix-duplicate-eval-gpu1_20260521T122154_result.json`
- **Structured JSON:** [`1d2862020c81f7189ba8.json`](../../sessions/1d/1d2862020c81f7189ba8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

每个 dosage 恰好 1 个 monitor，新版（带 flock）已生效。

汇报：

```
kill 519410: done ✓
剩余 eval 进程: PID 519561, GPU 1 MMLU d000_s0, 正常运行
ARC eval: 未启动（monitor 脚本设计为 MMLU 完成后顺序启动 ARC，无需手动）
GSM8K: 脚本中无 GSM8K，安全

race condition 原因:
  - 两套 monitor 被重复启动（18:23 + 18:25），d000 有 1 个 monitor + 1 个外部触发（bare python vs /root/miniconda3/bin/python）
  - 脚本无锁机制，多实例同时检测到 .done 后各自启动 eval

d025 monitor: 1 个实例 (PID 521169, 新版带 flock)
d100 monitor: 1 个实例 (PID 521160, 新版带 flock)
d000 monitor: 1 个实例 (PID 512753, 旧版，正在执行 eval 不可重启)

修复措施:
  1. kill 519410 + 子进程 ✓
  2. kill 重复 d025/d100 monitor (512754, 512755) ✓
  3. 脚本加 flock 互斥锁 + eval_done 哨兵双重防护 ✓
  4. 用新脚本重启 d025/d100 monitor ✓
```

---
