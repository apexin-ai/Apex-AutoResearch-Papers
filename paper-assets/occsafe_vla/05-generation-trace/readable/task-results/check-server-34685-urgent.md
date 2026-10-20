# check server 34685 urgent

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_server-34685-urgent_20260527T040938_result.json`
- **Structured JSON:** [`14c1c123f83bcd6335ba.json`](../../sessions/14/14c1c123f83bcd6335ba.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

原始结果汇总：

**GPU 利用率 (nvidia-smi)**
```
79 %, 62203 MiB
80 %, 62203 MiB
71 %, 62203 MiB
81 %, 63037 MiB
```

**Checkpoints (`/root/autodl-tmp/checkpoints/`)**
- 无 `checkpoint_50000.pt` 文件
- 最新目录：`mvp_occ_s4` (10:59), `ablation_occ_detach_s4` (10:58), `detach_ln_v2_s1` (10:13), `detach_ln_s4` (10:11)

**训练进程 (4个)**
| GPU | 实验 | 参数 |
|-----|------|------|
| 0 | `detach_ln_s4` | occ_detach=true, occ_norm_type=ln, seed=46 |
| 1 | `detach_ln_v2_s1` | occ_detach=true, occ_norm_type=ln, seed=43 |
| 2 | `ablation_occ_detach_s4` | occ_detach=true, seed=46 |
| 3 | `mvp_occ_s4` | occ_detach=false, seed=46 |

4 张 GPU 全部在跑，利用率 71-81%，max_steps=50005，尚未产出 checkpoint_50000.pt。`tmux` 和 `date` 不在 read_only 白名单无法执行。

---
