# ssh full gpu scan deploy 8 idle v2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_full-gpu-scan-deploy-8-idle-v2_20260517T105959_result.json`
- **Structured JSON:** [`dad7b83392712407e096.json`](../../sessions/da/dad7b83392712407e096.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

bjb1-18228 cuda:1 也已正常运行。汇总如下：

---

```
=== GPU 扫描结果 ===

bjb1-18228 (4 GPU):
  cuda:0 — 占用: PID 474319, obs_only ε=0.1 seed45 (May16)
  cuda:1 — 占用: PID 612853, obs_only ε=0.3 seed47 (今天 19:00, 刚启动)
  cuda:2 — 占用: PID 587763, obs_only ε=0.1 seed46 (今天 14:51)
  cuda:3 — 占用: PID 588037, obs_only ε=0.1 seed47 (今天 14:51)

bjb1-32546 (6 GPU):
  cuda:0 — 占用: PID 421086, perdof ε=0.3 seed44 (今天 18:58) ← P1#1
  cuda:1 — 占用: PID 414819, perdof ε=0.1 seed47_r2 (今天 18:22)
  cuda:2 — 占用: PID 416568, obs_only ε=0.3 seed46 (今天 18:27)
  cuda:3 — 占用: PID 422357, obs_only default seed46 (今天 18:59) ← P1#2
  cuda:4 — 占用: PID 393646, perdof ε=0.1 seed46 (今天 14:51)
  cuda:5 — 占用: PID 423767, perdof default seed46 (今天 18:59) ← P1#3

bjb2-28827 (6 GPU):
  cuda:0 — 占用: PID 224628, scalar seed45 (May16)
  cuda:1 — 占用: PID 222830, perdof ε=0.2 seed45 (May16)
  cuda:2 — 空闲 (1 MiB) → 已部署
  cuda:3 — 占用: PID 242264, obs_only default seed45 (May16)
  cuda:4 — 占用: PID 389051, perdof ε=0.2 seed46 (今天 18:36)
  cuda:5 — 占用: PID 326081, perdof ε=0.2 seed44 (今天 08:36)

bjb2-40593 (1 GPU):
  cuda:0 — 占用: PID 388460, perdof ε=0.1 seed47 (今天 17:56)

空闲 GPU 总数: 1 (部署前)
空闲 GPU 列表: [bjb2-28827:cuda2]

=== Kill 重复实验 ===
PID 387642 已不存在，无需 kill。

=== 已发现优先级实验已被部署 ===
P1#1 perdof ε=0.3 seed44 → bjb1-32546 cuda:0 (PID 421086) ✓
P1#2 obs_only default seed46 → bjb1-32546 cuda:3 (PID 422357) ✓
P1#3 perdof default seed46 → bjb1-32546 cuda:5 (PID 423767) ✓
P1#4 obs_only ε=0.3 seed47 → bjb1-18228 cuda:1 (PID 612853) ✓

=== 本次部署结果 ===
P1#5 perdof ε=0.3 seed46 → bjb2-28827 cuda:2, PID=394433 ✓

=== 验证 ===
perdof ε=0.3 seed46 (PID 394433):
  日志: CRM loaded, 10 tasks loaded
  GPU: 11324 MiB, 99% utilization ✓

=== 未部署（GPU 不够）===
- P2#6: VLA-only seed46
- P2#7: VLA-only seed47
- P2#8: argmin seed48
```

**总结**：17 张 GPU 现已全部占满。P1 #1-4 在本轮扫描前已被其他 session 部署，本次新部署了 P1 #5（perdof ε=0.3 seed46）到 bjb2-28827 唯一的空闲 cuda:2。P2 的 3 个 baseline 实验需等现有实验完成后才能部署。

---
