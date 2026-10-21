# CRM Training Data Coverage: LIBERO-10 / LIBERO-Goal

## CRM 训练数据
CRM v3 norm checkpoint 训练使用的 precomputed cache (`/root/autodl-tmp/crm_cache_v5/`) 仅包含:
- **LIBERO-Object** (10 tasks)
- **LIBERO-Spatial** (10 tasks)
- 合计 20 tasks

## 新 Benchmark 覆盖情况

### LIBERO-10 (CLI: `--benchmark long`, 内部映射: `libero_10`)
- 10 tasks，长序列操作任务
- **不在 CRM 训练集中** — CRM eval 需要 zero-shot transfer

### LIBERO-Goal (CLI: `--benchmark goal`, 内部映射: `libero_goal`)
- 10 tasks，相同初始状态不同目标
- **不在 CRM 训练集中** — CRM eval 需要 zero-shot transfer

## 结论
- **VLA-only baseline**: 可直接评估，不依赖 CRM → 已部署 6 个实验
- **CRM eval (obs_only/perdof)**: 现有 checkpoint 未在 Goal/10 上训练。需要:
  1. 先收集 VLA-only baseline 数据
  2. 决定是 (a) 用现有 CRM zero-shot 测试泛化性，还是 (b) 在新 suite 上重新 precompute + retrain CRM
  3. 推荐先跑 zero-shot CRM eval，若效果差再考虑 retrain

## 部署状态 (2026-05-19 16:40 UTC)
| exp_id | benchmark | seed | server | GPU |
|--------|-----------|------|--------|-----|
| eval-vla-only-long-seed42 | LIBERO-10 | 42 | bjb1-32546 | cuda:0 |
| eval-vla-only-long-seed43 | LIBERO-10 | 43 | bjb1-32546 | cuda:2 |
| eval-vla-only-long-seed44 | LIBERO-10 | 44 | bjb1-32546 | cuda:3 |
| eval-vla-only-goal-seed42 | LIBERO-Goal | 42 | bjb1-32546 | cuda:4 |
| eval-vla-only-goal-seed43 | LIBERO-Goal | 43 | bjb1-32546 | cuda:5 |
| eval-vla-only-goal-seed44 | LIBERO-Goal | 44 | bjb2-28827 | cuda:0 |
