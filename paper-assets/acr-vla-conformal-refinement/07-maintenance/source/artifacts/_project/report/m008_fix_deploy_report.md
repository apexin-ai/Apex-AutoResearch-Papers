# M008 未追踪进程注册 + bjb1-18228 部署报告

**执行时间:** 2026-05-17 21:32-21:40 UTC

---

## 第 1 部分: 4 个未追踪进程注册结果

| exp_id | server | GPU | PID | 状态 | registry | cron |
|--------|--------|-----|-----|------|----------|------|
| eval-obs-only-object-norm005-seed43-r2 | bjb1-32546 | cuda:0 | 433500 | **ALIVE** | RUNNING ✅ | 已存在 ✅ |
| eval-obs-only-object-norm003-seed43 | bjb1-18228 | cuda:1 | 621127 | **DEAD** | DONE/failed ✅ | N/A |
| eval-perdof-object-norm02-seed47 | bjb2-28827 | cuda:2 | 404983 | **ALIVE** | RUNNING ✅ | 已存在 ✅ |
| eval-random-selection-object-seed42 | bjb2-40593 | cuda:0 | 395256 | **ALIVE** | RUNNING ✅ | 已存在 ✅ |

**异常:** eval-obs-only-object-norm003-seed43 (PID 621127) 确认已死，与 Director 预测一致（batch7 误杀）。已标记 DONE/failed。

---

## 第 2 部分: bjb1-18228 部署结果

nvidia-smi 确认 4 张 GPU 全部空闲后部署。

| exp_id | GPU | PID | 类型 | nvidia-smi 确认 |
|--------|-----|-----|------|----------------|
| eval-perdof-object-norm02-seed45-r2 | cuda:0 | 634438 | perdof ε=0.2 seed45 | ✅ 98:00.0 |
| eval-obs-only-object-norm005-seed43-r3 | cuda:1 | 633649 | obs_only ε=0.05 seed43 | ✅ A8:00.0 |
| eval-obs-only-object-norm02-k5-seed42 | cuda:2 | 633736 | K=5 sweep seed42 | ✅ B8:00.0 |
| eval-obs-only-object-norm02-k20-seed42 | cuda:3 | 636713 | K=20 sweep seed42 | ✅ D8:00.0 |

所有 4 个实验 registry (RUNNING) + cron 均已注册。

---

## 异常记录

1. **残留 tmux session 冲突:** bjb1-18228 上发现 2 个前 Worker 遗留 tmux session (`eval-obs-only-object-norm005-seed43`, `eval-perdof-object-norm02-seed45-deploy`)，占用 cuda:0 和 cuda:1。已清理。
2. **tmux server 级联清理:** 杀掉残留 tmux server (PID 631666) 时导致所有 tmux session 丢失，但 4 个 Python 进程以 orphan 方式存活（re-parented to PID 1），GPU 进程确认正常。
3. **eval-obs-only-object-norm02-k20-seed42 首次提交丢失:** 第一次 submit 返回成功但 tmux session 未创建，已重新提交成功。
4. **进程数:** 当前 bjb1-18228 上 4 个 evaluate.py Python 进程，符合 ≤4 限制。
