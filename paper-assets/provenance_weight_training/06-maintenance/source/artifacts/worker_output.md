## Grid-b 训练进度 (2026-05-14 21:38 检查)

**硬件**: 4× NVIDIA RTX PRO 6000 Blackwell Server Edition, 每卡占用 ~46.5GB 显存
**总步数**: 6103 steps（200M tokens, batch=4, grad_accum=4, seq_len=2048）

> **注意**: cuda:0 实际运行的是 grid_b2_0_seed42（单个 b=2.0 实验），非之前描述的 grid_b_seed42_batch 批量实验。

### cuda:0 - grid_b2_0_seed42 (PID 93300)
- 当前: b=2.0, step 4167/6103 (68.3%)
- 速率: ~2.13 sec/step
- 预估剩余: **~1h 9min**
- Checkpoints: 3500, 4000
- 状态: ✅ 正常，无 error

### cuda:1 - grid_b2_0_seed123 (PID 88027)
- 当前: b=2.0, step 5097/6103 (83.5%)
- 速率: ~2.15 sec/step
- 预估剩余: **~36min**
- Checkpoints: 4500, 5000
- 状态: ✅ 正常，无 error

### cuda:2 - grid_b3_0_seed123 (PID 90134)
- 当前: b=3.0, step 4802/6103 (78.7%)
- 速率: ~2.14 sec/step
- 预估剩余: **~46min**
- Checkpoints: 4000, 4500
- 状态: ✅ 正常，无 error

### cuda:3 - grid_b5_0_seed123 (PID 94717)
- 当前: b=5.0, step 3619/6103 (59.3%)
- 速率: ~2.25 sec/step
- 预估剩余: **~1h 33min**
- Checkpoints: 3000, 3500
- 状态: ✅ 正常，无 error

### 完成时间预估
| 实验 | 预计完成时间 |
|------|------------|
| grid_b2_0_seed123 | ~22:15 |
| grid_b3_0_seed123 | ~22:25 |
| grid_b2_0_seed42 | ~22:50 |
| grid_b5_0_seed123 | ~23:10 |

所有 4 个实验均正常运行，预计今晚 23:10 前全部完成。
