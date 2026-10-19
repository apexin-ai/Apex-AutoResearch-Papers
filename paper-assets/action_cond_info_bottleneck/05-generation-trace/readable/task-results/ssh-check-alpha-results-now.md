# ssh check alpha results now

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check-alpha-results-now_20260517T041325_result.json`
- **Structured JSON:** [`3de6ffe78df67b474495.json`](../../sessions/3d/3de6ffe78df67b474495.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
=== ALPHA 0.0 SPATIAL ===
NOT READY
=== ALPHA 0.0 PROGRESS ===
0
=== ALPHA 0.3 SPATIAL ===
NOT READY
=== ALPHA 0.3 PROGRESS ===
0
=== PROCESSES ===
   PID     ELAPSED COMMAND
837180    01:15:52 python3 -u scripts/eval_acib.py --checkpoint_dir /root/acib/outputs/acib_v7_contrastive --checkpoint_step 20000 --base_model lerobot/smolvla_libero --suites libero_spatial libero_object libero_goal libero_10 --n_episodes 50 --gpu 0 --seed 42 --out_dir /root/autodl-tmp/v7_alpha_sweep/alpha_0.0 --scoring_alpha 0.0
872669       54:07 python3 -u scripts/eval_acib.py --checkpoint_dir /root/acib/outputs/acib_v7_contrastive --checkpoint_step 20000 --base_model lerobot/smolvla_libero --suites libero_spatial --n_episodes 50 --gpu 0 --seed 42 --out_dir /root/autodl-tmp/v7_alpha_sweep/alpha_0.3 --scoring_alpha 0.3
```

两个进程都活着，都在 GPU 0 上跑。alpha=0.0 跑了 1h15m（4 suites），alpha=0.3 跑了 54m（仅 spatial）。两者的 libero_spatial eval_info.json 都还没产出，进度目录数为 0——还在跑第一个 suite 的 episodes。

---
