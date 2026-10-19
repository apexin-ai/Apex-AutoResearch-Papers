# ssh full gpu scan and deploy all idle

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_full-gpu-scan-and-deploy-all-idle_20260517T105546_result.json`
- **Structured JSON:** [`72a92e3ca0aff33cc580.json`](../../sessions/72/72a92e3ca0aff33cc580.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过，5 个实验均已成功加载环境并开始评估。

```
=== GPU 扫描结果 ===
bjb1-18228 (4 GPU):
  GPU 0: 1942 MiB, 23% → obs_only norm01 seed45
  GPU 1: 1 MiB, 0%    → 空闲
  GPU 2: 4268 MiB, 21% → obs_only norm01 seed46
  GPU 3: 4735 MiB, 20% → obs_only norm01 seed47

bjb1-32546 (6 GPU):
  GPU 0: 2 MiB, 0%     → 空闲
  GPU 1: 5665 MiB, 22% → perdof norm01 seed47_r2
  GPU 2: 5665 MiB, 22% → obs_only norm03 seed46
  GPU 3: 2 MiB, 0%     → 空闲
  GPU 4: 4736 MiB, 21% → perdof norm01 seed46
  GPU 5: 2 MiB, 0%     → 空闲

bjb2-28827 (6 GPU):
  GPU 0: 2410 MiB, 18% → scalar seed45 + tmux spatial
  GPU 1: 1941 MiB, 18% → perdof norm02 seed45
  GPU 2: 1 MiB, 0%     → 空闲 (just killed)
  GPU 3: 2410 MiB, 18% → obs_only default seed45
  GPU 4: 5186 MiB       → perdof norm02 seed46
  GPU 5: 2875 MiB, 17% → perdof norm02 seed44

bjb2-40593 (1 GPU):
  GPU 0: 5628 MiB, 11% → perdof norm01 seed47

空闲 GPU: bjb1-18228:1, bjb1-32546:0/3/5, bjb2-28827:2 (共 5 张)

=== 部署结果 ===
killed: bjb2-28827 PID 387642 (duplicate obs_only ε=0.2 seed46) ✓

deployed:
1. perdof ε=0.3 seed44   → bjb1-32546 cuda:0, PID=421084
2. obs_only default seed46 → bjb1-32546 cuda:3, PID=422355
3. perdof default seed46   → bjb1-32546 cuda:5, PID=423765
4. obs_only ε=0.3 seed47  → bjb1-18228 cuda:1, PID=612851
5. perdof ε=0.3 seed46    → bjb2-28827 cuda:2, PID=392854

未部署（无空闲 GPU）:
- VLA-only seed46

=== 验证 ===
全部 5 个实验确认启动成功:
  "[eval] Loading LIBERO object environments..."
  "[eval] 10 tasks loaded."
```

现在 17 张 GPU 全部满载运行。

---
