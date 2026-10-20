# diagnose gpu collision westd 20260526

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_gpu_collision_westd_20260526_20260525T233120_result.json`
- **Structured JSON:** [`59d95f290cc2d02879ca.json`](../../sessions/59/59d95f290cc2d02879ca.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态汇总

### bjb1-45299 (2x 98GB GPU)

| 实验 | PID | 状态 | Step | Eval Return | GPU | 显存 | FPS |
|------|-----|------|------|-------------|-----|------|-----|
| exp_092_cheetah_no_dt_emb_s1 | 313538 | **alive** (Rl) | 25000/105K | 99.0 | cuda:0 | 3257 MiB | 9.9 |
| exp_093_cheetah_no_dt_emb_s2 | 313815 | **alive** (Rl) | 25000/105K | 64.6 | cuda:1 | 2742 MiB | 9.9 |

GPU 总占用: GPU0 = 3801/97887 MiB (4%), GPU1 = 2751/97887 MiB (3%)。运行 ~39 分钟。

### westd-19154 (2x 98GB GPU)

| 实验 | PID | 状态 | Step | Eval Return | GPU | 显存 | FPS |
|------|-----|------|------|-------------|-----|------|-----|
| exp_094_cheetah_008d_s3 | 53576→53581 | **alive** | 25000/105K | 139.4 | cuda:1 | 3223 MiB | 9.8 |
| exp_095_cheetah_no_dt_emb_s3 | 54119→54124 | **alive** | 20000/105K | — | cuda:1 | 3223 MiB | 9.9 |
| exp_096_cheetah_008a_s0 | 54457→54462 | **alive** | 25000/105K | 119.8 | cuda:0 | 4637 MiB | 13.0 |

GPU 总占用: GPU0 = 4656/97887 MiB (5%), GPU1 = 6480/97887 MiB (7%)。

### cuda:1 冲突分析 (westd)

**结论：没有实际冲突，不需要 kill 任何进程。**

- exp_094 和 exp_095 确实都在 cuda:1 上运行，但 98GB 显存下两个进程合计仅 6.4GB (6.6%)
- GPU 利用率 66%，FPS 均正常 (~9.9)，无 OOM 风险
- exp_095 比 exp_094 晚启动约 6 分钟，step 落后 5000（20K vs 25K），训练正常推进中

### 要点

- 5 个实验全部存活，正常训练
- 进度都在 20K-25K / 105K 之间（约 20-24% 完成）
- 显存占用极低（均 <5GB/进程），98GB GPU 完全充裕
- exp_096 的 FPS 最高（13.0），因为 cuda:0 上只有它一个进程
- 性能最好的是 exp_094（eval 139.4），其次 exp_096（119.8），exp_093 目前最弱（64.6）

---
