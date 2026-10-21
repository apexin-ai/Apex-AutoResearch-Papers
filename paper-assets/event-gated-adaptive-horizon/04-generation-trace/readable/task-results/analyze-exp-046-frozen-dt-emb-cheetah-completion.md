# analyze exp 046 frozen dt emb cheetah completion

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_exp_046_frozen_dt_emb_cheetah_completion_20260522T182723_result.json`
- **Structured JSON:** [`6ecc98326459f7a23687.json`](../../sessions/6e/6ecc98326459f7a23687.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Cron 不在当前 session 中，无需删除。

---

## exp_046_frozen_dt_emb_cheetah 结果汇报

**状态**: 正常完成，224K env steps (目标 210K)，exit_code=0

**Eval return trajectory**:
```
5K:8.3 → 15K:110 → 35K:160 → 95K:181 → 105K:206 → 115K:46 → 145K:207 → 155K:161 → 215K:150.5
```
波动大但无灾难性崩溃，peak=207.4 (145K)，final=150.5

**ve_ratio trajectory**:
```
全程 0.0-0.4，peak=0.4 (115K-135K)，final=0.1
零 CIVO alerts
```

**NVE (≥35K diagnostic window)**:
- **Peak NVE = 1.35** (45K) — **低于 1.5 阈值**
- Final NVE = 0.17
- 对比 exp_010b (trained dt_emb, same config): NVE=70.64 → frozen dt_emb 降低 ~52×

**Conclusion: SUCCESS**

Frozen dt_emb 在 Cheetah Run（CIVO 更严重的环境）上也有效阻止了 CIVO。跨环境验证通过：
- Walker: exp_042 NVE=0.194, exp_015b NVE=0.47
- **Cheetah: exp_046 NVE=1.35** (即便 trained dt_emb 在 Cheetah 上 NVE 高达 70.64)

---
