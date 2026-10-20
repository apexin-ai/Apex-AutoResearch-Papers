# exp_086 Orphan Process Cleanup Report (v2)

**Date**: 2026-05-25  
**Server**: westd-19154 (cuda:0)  
**Experiment**: exp_086_frozen_dt_emb_cheetah_s0

## 情况判定：B（最坏情况）

| PID | 角色 | 预期操作 | 实际状态 |
|-----|------|----------|----------|
| 37174 | 旧进程 (started 00:49:33) | KILL | 存活 → 已 kill |
| 37520 | 新进程 (started 00:51:21) | KEEP | 已死（被之前 Worker 误杀） |

## 执行操作

1. **确认进程状态**：`ps -p 37174,37520` 仅返回 37174，确认 37520 已被误杀
2. **Kill 37174 及父进程 37173**：成功
3. **清空 logdir**：`rm -rf logdir/exp_086_frozen_dt_emb_cheetah_s0/` — 旧进程产生的数据不可信
4. **数据完整性检查**：跳过（情况 B，数据来源为旧进程，直接清空）

## Registry 更新

- `conclusion` → `killed`
- `status` → `DONE`

## 需要重新提交

**是。** logdir 已清空，实验需要从头重跑。原始命令：

```bash
python -u dreamer.py --configs defaults dmc_proprio \
  --task dmc_cheetah_run \
  --logdir logdir/exp_086_frozen_dt_emb_cheetah_s0 \
  --steps 105000 --seed 0 --compile False --device cuda:0 \
  --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 \
  --imag_horizon 8 --dt_emb_freeze True
```
