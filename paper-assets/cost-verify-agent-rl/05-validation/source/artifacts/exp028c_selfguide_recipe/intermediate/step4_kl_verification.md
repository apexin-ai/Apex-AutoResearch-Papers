# exp028c step_4 kl_loss 验证报告

## W&B 查询信息
- Run ID: 4yu6qz1m
- Run name: exp028c-alfworld-selfguide-recipe
- Entity/Project: xiaoyucorynne-/cost-verify-agent-rl
- Run state: running (截至查询时)

## W&B 原始数据（全部 5 steps）

| step | actor/kl_loss | actor/ppo_kl | actor/pg_loss | actor/entropy_loss | actor/grad_norm | actor/kl_coef |
|------|-------------|------------|-------------|------------------|----------------|--------------|
| 1    | 0.012797    | 0.019207   | 0.008277    | 0.271309         | 16.881833      | 0.01         |
| 2    | 0.170613    | 0.017287   | 0.007009    | 0.245078         | 17.303639      | 0.01         |
| 3    | 0.111844    | 0.019441   | 0.004700    | 0.248123         | 12.569769      | 0.01         |
| 4    | 0.031226    | 0.015264   | 0.005596    | 0.238121         | 14.531632      | 0.01         |
| 5    | 0.824006    | 0.014086   | 0.004794    | 0.239676         | 13.084765      | 0.01         |

## 与 registry 对比

### step 2
- Registry: kl_loss=0.1706, pg_loss=0.007
- W&B: kl_loss=0.170613, pg_loss=0.007009
- **结论：✅ 一致（四舍五入）**

### step 3
- Registry: kl_loss=0.1118
- W&B: kl_loss=0.111844
- **结论：✅ 一致（四舍五入）**

### step 4（核心验证目标）
- Registry: kl_loss=0.031, ppo_kl=0.015
- W&B: kl_loss=0.031226, ppo_kl=0.015264
- **结论：✅ kl_loss=0.031 确实是 actor/kl_loss 的真实值，不是 ppo_kl 的误录**

## 分析

Reviewer 的怀疑可以理解——step 4 的 kl_loss (0.031) 相比 step 3 (0.112) 下降了 72%，看起来异常。但 W&B 数据明确显示：

1. actor/kl_loss = 0.031226（registry 记录 0.031 正确）
2. actor/ppo_kl = 0.015264（registry 记录 0.015 正确）
3. 两者是不同的值，不存在误录

kl_loss 的波动轨迹：0.013 → 0.171 → 0.112 → 0.031 → 0.824，非单调变化，step 4 的低值是真实的训练动态。

## 需要修正的 step

**无。** 所有已记录的 step (2/3/4) 的值均与 W&B 一致。
