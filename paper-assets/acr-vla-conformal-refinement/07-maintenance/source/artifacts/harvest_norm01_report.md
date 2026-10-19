# ε=0.1 (norm01) obs_only Object 实验收割报告

**日期**: 2026-05-21
**扫描范围**: bjb1-32546, bjb1-18228, bjb2-28827, bjb2-40593 四台服务器

## 收割结果

**修正 1 条 registry**:
- `eval-obs-only-object-norm01-seed60`: killed → success, SR=0.15 (从 bjb2-28827 JSON 恢复)

**无法恢复的实验** (无 JSON 或进程确认死亡):
- seed42-r2, seed46 (original), seed46-bjb2, seed46-r2, seed47-bjb2, seed47-r2, seed51-r2, seed52-r2, seed61

**仍在运行/准备中**: seed66, seed67 (RUNNING on bjb1-18228); seed76, seed77 (PREPARING on bjb1-32546, n_rollouts=20)

## obs_only Object norm01 — 全部有效 seeds (n=18)

| seed | SR | JSON path | server | registry exp_id | status |
|------|----|-----------|--------|-----------------|--------|
| 42 | 0.19 | logs/eval_object_obs_only_norm01_seed42.json | bjb2-28827 | eval-obs-only-object-norm01-seed42 | DEPLOYED/success |
| 44 | 0.16 | logs/eval_object_obs_only_norm01_seed44.json | bjb1-32546 | eval-obs-only-object-norm01-seed44 | DONE/success |
| 45 | 0.17 | logs/eval_object_obs_only_norm01_seed45_r2.json | bjb2-28827 | eval-obs-only-object-norm01-seed45-r2 | DONE/success |
| 46 | 0.18 | logs/eval_object_obs_only_norm01_seed46.json | bjb1-32546 | eval-obs-only-object-norm01-seed46-r3 | DONE/success |
| 47 | 0.17 | logs/eval_object_obs_only_norm01_seed47.json | bjb1-32546 | eval-obs-only-object-norm01-seed47 | DONE/success |
| 48 | 0.13 | (log only) | bjb2-28827 | eval-obs-only-object-norm01-seed48 | DONE/success |
| 49 | 0.16 | logs/eval_obs_only_object_norm01_seed49.json | bjb1-32546 | eval-obs-only-object-norm01-seed49 | DONE/success |
| 50 | 0.14 | logs/eval_obs_only_object_norm01_seed50.json | bjb1-18228 | eval-obs-only-object-norm01-seed50 | DONE/success |
| 51 | 0.11 | logs/eval_obs_only_object_norm01_seed51.json | bjb1-32546 | eval-obs-only-object-norm01-seed51 | DONE/success |
| 52 | 0.15 | logs/eval_obs_only_object_norm01_seed52.json | bjb1-32546 | eval-obs-only-object-norm01-seed52 | DONE/success |
| 53 | 0.19 | logs/eval_obs_only_object_norm01_seed53.json | bjb2-28827 | eval-obs-only-object-norm01-seed53 | DONE/success |
| 54 | 0.15 | logs/eval_obs_only_object_norm01_seed54.json | bjb2-28827 | eval-obs-only-object-norm01-seed54 | DONE/success |
| 57 | 0.19 | logs/eval_obs_only_object_norm01_seed57.json | bjb1-18228 | eval-obs-only-object-norm01-seed57 | DONE/success |
| 60 | 0.15 | logs/eval_obs_only_object_norm01_seed60.json | bjb2-28827 | eval-obs-only-object-norm01-seed60 | **HARVESTED** |
| 64 | 0.15 | logs/eval_obs_only_object_norm01_seed64.json | bjb1-32546 | eval-obs-only-object-norm01-seed64 | DONE/success |
| 65 | 0.15 | logs/eval_obs_only_object_norm01_seed65.json | bjb1-32546 | eval-obs-only-object-norm01-seed65 | DONE/success |
| 71 | 0.16 | logs/norm01_seed71.json | bjb2-28827 | eval-obs-only-object-norm01-seed71 | DONE/success |
| 74 | 0.13 | logs/norm01_seed74.json | bjb2-28827 | eval-obs-only-object-norm01-seed74 | DONE/success |

**注**: seed45 original (SR=0.14, bjb1-18228) 和 seed48 alt (SR=0.18, bjb1-18228 `eval_obs_only_norm01_seed48`) 为重复 seed 的独立运行，上表使用 r2/主条目作为 canonical。

## 统计汇总

| 指标 | 值 |
|------|----|
| n (unique seeds) | 18 |
| mean SR | **15.7%** |
| std | 2.2% |
| SEM | 0.5% |
| 95% CI | [14.7%, 16.7%] |
| min / max | 11% / 19% |

**vs ROADMAP ~15.0%**: 实际 mean=15.7%，略高于 ROADMAP 估计，一致。

## perdof Object norm01 — 附录 (n=7)

| seed | SR | registry exp_id |
|------|----|-----------------|
| 42 | 0.11 | eval-perdof-object-norm01-seed42 |
| 43 | 0.12 | eval-perdof-object-norm01-seed43 |
| 44 | 0.08 | eval-perdof-object-norm01-seed44 |
| 45 | 0.11 | eval-perdof-object-norm01-seed45 |
| 46 | 0.10 | eval-perdof-object-norm01-seed46-r2 |
| 47 | 0.14 | eval-perdof-object-norm01-seed47-bjb1 |
| 48 | 0.12 | eval-perdof-object-norm01-seed48 |

perdof mean = 11.1% ± 1.8%
