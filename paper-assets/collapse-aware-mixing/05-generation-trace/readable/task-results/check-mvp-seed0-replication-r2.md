# check mvp seed0 replication r2

**collapse aware mixing** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_mvp_seed0_replication_r2_20260514T024249_result.json`
- **Structured JSON:** [`90e228fa806eb33c491c.json`](../../sessions/90/90e228fa806eb33c491c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
STATUS: RUNNING
CURRENT_STAGE: G0_eval (checkpoint 6/6 final_model, generating 500K tokens — started 10:35 UTC)
```

**G0 checkpoint holdout metrics (5/6 complete):**

| Checkpoint | eff_rank | ppl | unigram_H | coverage |
|---|---|---|---|---|
| ckpt-76 | 679.7 | 13.53 | 6.893 | 0.4675 |
| ckpt-152 | 677.8 | 13.34 | 6.917 | 0.4704 |
| ckpt-228 | 677.0 | 13.28 | 6.925 | 0.4652 |
| ckpt-304 | 676.9 | 13.27 | 6.944 | 0.4700 |
| ckpt-305 | 676.9 | 13.27 | 6.943 | 0.4658 |
| final | *(computing)* | | | |

G0 final eff_rank≈676.9，与 v7 的 676.96 几乎一致。G1/G2 尚未开始，无法判断 seed robustness。

**重要问题：有两个相同的 pilot_pipeline.py 进程同时运行，共享同一 GPU 和输出目录：**
- PID 122563 (tmux session, 08:45 启动)
- PID 123063 (后台, 08:46 启动, 通过 env_init.sh 启动)

两者写入同一个 `/root/autodl-tmp/output_seed0/` 和同一个 log 文件。这意味着：
1. GPU 资源被平分，实验速度减半
2. 输出文件可能被相互覆盖/混淆
3. v7 跑了 ~15h，按当前速度可能需要 ~30h

**建议**：kill 掉其中一个进程（推荐 kill PID 123063，保留 tmux 中的 122563），然后让实验继续。否则结果可能不可靠，且耗时翻倍。是否执行？

---
