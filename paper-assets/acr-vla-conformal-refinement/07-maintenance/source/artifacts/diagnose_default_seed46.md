# 诊断报告：eval-obs-only-object-default-seed46

**日期**: 2026-05-18  
**服务器**: bjb1-32546

## 结论：实验已成功完成，监控误报

### eval-obs-only-object-default-seed46

**状态**: ✅ 已正常完成  
**根因**: 监控系统 false negative，非实验失败

实验于 2026-05-18 08:10 正常结束，产出完整：
- `logs/eval_object_obs_only_default_seed46.json` — 完整 10 tasks × 10 rollouts
- `logs/eval_object_obs_only_default_seed46.log` — 11146 bytes，日志正常结束
- **结果**: overall_success_rate = 15.0% (15/100)

监控系统报"进程死亡5次"的原因：
1. 实验通过 `nohup` 直接启动，未经 agent-ml-research 任务系统，故 `~/runs/` 下无 cron log
2. `evaluate.py` 不写 sentinel 文件（sentinels 目录为空）
3. `evaluate.py` 不上报 W&B metrics
4. 进程结束后 PID 消失，监控误判为 crash

**不需要重试。数据已完整。**

---

### eval-obs-only-object-norm01-seed46

**状态**: ❌ 从未运行  
**根因**: 无任何痕迹（无 log、无 JSON、无 runs/ 记录、无 exit file）

该实验似乎从未成功启动过，或启动瞬间即失败未产生任何输出。

**需要重新提交**。建议通过 agent-ml-research 任务系统启动，确保有 sentinel 和 runs/ log：
```bash
CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py \
  --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 46 --K 10 \
  --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt \
  --max_correction_norm 0.1 \
  --output_file logs/eval_object_obs_only_norm01_seed46.json
```

---

### GPU 状态
GPU 3 当前空闲（2MiB, 0% utilization），可直接用于重跑 norm01-seed46。

### 对比成功实验
norm03-seed46 于 07:28 成功完成（17.0%, 同样通过 nohup 启动），log 结构与 default-seed46 完全一致。进一步确认 default-seed46 是正常完成。
