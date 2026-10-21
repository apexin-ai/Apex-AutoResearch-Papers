# ops d134 emergency disk cleanup and restart

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_d134-emergency-disk-cleanup-and-restart_20260518T182011_result.json`
- **Structured JSON:** [`5b57aca0c772d166c535.json`](../../sessions/5b/5b57aca0c772d166c535.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
清理前磁盘: 208G/250G (42G free)
清理后磁盘:  41G/250G (210G free, freed 167G)

各项清理详情:
  ISR s47-s51:        已是 16-17M，无需清理（之前已清过）
  Random s47:         已是 17M，无需清理（之前已清过）
  Random s48:         已删除整个目录（崩溃残留）
  Random s49:         -16G（删除整个目录）
  sweep_isr_b005 s43: -16G → 16M
  sweep_isr_b005 s44: -16G → 16M
  sweep_random_b005 s43: -16G → 16M
  sweep_random_b005 s44: -16G → 16M
  plan002_additive_b01_s45_1000: -16G → 16M
  d129_1.7b_isr_b01 s43/s44: -26G → 32M
  d129_1.7b_isr_b03 s43/s44: -26G → 33M
  d129_1.7b_random_b01 s43/s44: -26G → 32M

s48 重启状态: running, PID 131128, step 2/500, GPU0 81410 MiB
Pipeline 自动清理: 已加入（每个 seed classify 完成后自动清理 checkpoint + safetensors + optimizer + rng_state + scheduler）
Pipeline 脚本: /root/autodl-tmp/d134_random_pipeline_v2.sh
Pipeline 队列: Random s48 → s49 → s50 → s51
```

---
