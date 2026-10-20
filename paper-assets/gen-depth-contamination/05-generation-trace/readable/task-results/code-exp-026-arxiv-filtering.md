# code exp 026 arxiv filtering

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_026_arxiv_filtering_20260518T102036_result.json`
- **Structured JSON:** [`a78e1c8e39c8ccf7fccf.json`](../../sessions/a7/a78e1c8e39c8ccf7fccf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练正常运行中：
- **GPU 0/1/2**: 各 ~8115 MiB, ~80% 利用率，OOM 问题已解决
- **GPU 3**: 5741 MiB (exp_027，未受影响)
- **binary** (275 steps): ~35% 完成，~2.5 it/s
- **no_filter / graduated** (825 steps): ~10% 完成，~2.5 it/s

训练速度 ~2.5 it/s：
- binary: 275 steps, 预计 ~2 分钟完成训练 + eval
- no_filter/graduated: 825 steps, 预计 ~5.5 分钟完成训练 + eval
- 每个 strategy 5 seeds，总计约 binary ~10 min, no_filter/graduated ~28 min

**汇报：**

| 项目 | 详情 |
|------|------|
| 数据路径 | `/root/autodl-tmp/gen-depth-contamination/data/exp_024_arxiv/` (depth_0-5.jsonl, 2200 docs/depth) |
| 模型 | `/root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-1___5B/` (Qwen2.5-1.5B base) |
| 脚本 | `scripts/exp026_arxiv_filtering.py` + `scripts/run_exp026.sh` |
| LoRA | rank=4, alpha=8, targets=q_proj+v_proj (544,768 trainable / 1.54B total, 0.04%) |
| Strategies | no_filter (13200 docs, GPU 0), binary depth 0-1 (4400 docs, GPU 1), graduated α=0.9^d (13200 docs, GPU 2) |
| Seeds | 42, 123, 456, 789, 1024 |
| Launcher PID | 31749 |
| 日志 | `logs/exp_026_arxiv_filtering.log` |
| 预计完成 | ~30 分钟 |
| Registry | exp_026_arxiv_filtering → RUNNING |

---
