## Dry-run 验证结果

| 环境 | 配置 | 启动 | step 5000 | metrics.jsonl | 报错 |
|------|------|------|-----------|---------------|------|
| Cheetah Run | baseline | ✅ | ✅ | ✅ | 无 |
| Cheetah Run | treatment (gate+dt1+subsample+H15) | ✅ | ✅ | ✅ | 无 |
| Cartpole Swingup | baseline | ✅ | ✅ | ✅ | 无 |
| Cartpole Swingup | treatment (gate+dt1+subsample+H15) | ✅ | ✅ | ✅ | 无 |

obs/action 维度：
- Cheetah Run: obs 17D, act 6D
- Cartpole Swingup: obs 5D, act 1D

验证日期: 2026-05-14