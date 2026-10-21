# exp028c Step 10 Val Check

**时间**: 2026-05-16 15:50 UTC+8
**进程**: PID 824675, 存活, 已运行 10h12m
**当前精确进度**: Step 10 已完成（checkpoint 保存于 14:15），正在执行 step 11-15
**Val episodes**: 16（满足 C003 要求）

## Val 指标对比（16 episodes）

| 指标 | Step 0 (初始) | Step 5 | Step 10 |
|------|:---:|:---:|:---:|
| **success** | **6.25%** (1/16) | **6.25%** (1/16) | **0%** (0/16) |
| pass@1 | 6.25% | 6.25% | 0% |
| action_is_valid | 0.7449 | 0.965 | 0.9363 |
| action_is_effective | 0.95 | 1.0 | 0.9963 |
| num_actions | 44.94 | 49.44 | 49.81 |
| manager_invalid_action | 0.05 | — | 0.00375 |
| reward/mean | 0.1186 (@759) | 0.5183 (@791) | 0.0 (@800) |

## Train 指标

| 指标 | Step 5 | Step 10 | 趋势 |
|------|:---:|:---:|:---:|
| **success** | 9.375% | **18.75%** | ↑ 2× |
| pass@8 | 37.5% | **50%** | ↑ |
| action_is_valid | 0.8960 | 0.9067 | ↑ |
| action_is_effective | 0.9850 | 0.9842 | ≈ |
| actor/entropy | 0.2364 | 0.2149 | ↓ |
| actor/kl_loss | 0.8240 | 0.1974 | ↓↓ |
| actor/pg_loss | 0.00479 | 0.00591 | ↑ |
| actor/ppo_kl | 0.01409 | 0.01883 | ↑ |
| actor/grad_norm | 13.085 | 9.885 | ↓ |
| critic/score/mean | 0.4769 | 0.9783 | ↑ |
| batch_size | 6144 | 5888 | ↓ |

## 关键发现

**Step 10 val success = 0%，从 6.25% 跌至零。** 这是一个严重的红灯信号。

Train-val 分歧明显：
- Train success 从 9.375% → 18.75%（翻倍增长）
- Val success 从 6.25% → 0%（完全归零）
- Val reward/mean 从 0.5183 → 0.0

可能原因：
1. **策略过拟合训练分布** — train pass@8=50% 但 val pass@1=0%，模型在训练任务上学到了模式但无法泛化
2. **Entropy 持续下降** (0.2364→0.2149) — 策略在收窄，可能锁定到训练集特有的动作模式
3. **Val action_is_valid 仍高** (0.9363) 但 success=0% — 模型生成的动作格式正确但策略完全无效

注意：val action_is_valid 从 step 0 的 0.7449 大幅提升到 step 5 的 0.965，说明模型学会了格式。但 success 没有同步提升，现在还崩了。

## 时间线预估

- Step 5 → Step 10: ~4h11m（10:04 → 14:15）
- 预计 Step 15 val: ~18:30
