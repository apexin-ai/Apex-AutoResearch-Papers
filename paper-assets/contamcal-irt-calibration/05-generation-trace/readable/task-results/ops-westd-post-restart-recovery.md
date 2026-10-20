# ops westd post restart recovery

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd-post-restart-recovery_20260520T030357_result.json`
- **Structured JSON:** [`90a5a7f483ddac07a806.json`](../../sessions/90/90a5a7f483ddac07a806.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

lora_alpha=32，符合 C006。

```
westd-29999 服务器状态:
  可达: 是
  uptime: 222 天（无重启）
  GPU 状态: 1/4 空闲（GPU 0），3/4 占用
  磁盘: root 5% / data 77%
  缓存 symlink: 正常 → /root/autodl-tmp/.cache_migrated

实验恢复评估:
  Phi-4 s123 GSM8K eval:    ✅ 结果完整，无需重跑（d000+d100 均有 .done 标记）
  Qwen-14B d100_s123 retrain: 🔄 正在运行，1400/4159 (34%)，ETA ~2h16m
  Gemma-2 d100_s123 retrain:  🔄 正在运行，1437/4159 (35%)，ETA ~1h54m
  OLMo-2 s0 sweep:           🔄 d000 已完成，d005 正在训练 289/3177 (9%)，d025/d050/d100 待跑

需要重启的任务: 无
```

03:02 UTC 的 4 个 failed 标记是**误报**。实验已被重启（tmux 会话创建于今天 09:14-09:55 UTC），目前全部正常运行。GPU 0 空闲可用（Phi-4 eval 已完成）。

---
