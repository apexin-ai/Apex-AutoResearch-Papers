# 剩余训练存活状态检查

**检查时间**: 2026-05-23 ~14:00 UTC

## 训练状态

| exp_id | server | gpu | status | last_step | notes |
|--------|--------|-----|--------|-----------|-------|
| train_pi05_a1_obj_s2_l01 | westd-35807 | cuda:3 | **DEAD** | 7999 (27%) | 磁盘满，step 8000 存 checkpoint 时 `OSError: [Errno 28] No space left on device` |
| train_pi05_a1_obj_s0_l005 | westd-45947 | cuda:0 | **ALIVE** | ~8067 (27%) | 正常运行，~4.62s/it，loss~0.02，ETA ~28h |
| train_pi05_a1_obj_s0_l01 | westd-45947 | cuda:1 | **ALIVE** | ~8070 (27%) | 正常运行，~4.62s/it，loss~0.02，ETA ~28h |

## GPU 空闲情况

| server | gpu | memory_used | utilization | 状态 |
|--------|-----|-------------|-------------|------|
| westd-35807 | cuda:0 | 0 MiB / 97887 MiB | 0% | **空闲** |
| westd-35807 | cuda:1 | 0 MiB / 97887 MiB | 0% | **空闲** |
| westd-35807 | cuda:2 | 0 MiB / 97887 MiB | 0% | **空闲** |
| westd-35807 | cuda:3 | 0 MiB / 97887 MiB | 0% | **空闲** |
| westd-45947 | cuda:0 | 27097 MiB / 97887 MiB | 100% | 训练中 (s0_l005) |
| westd-45947 | cuda:1 | 27097 MiB / 97887 MiB | 100% | 训练中 (s0_l01) |

## 磁盘状态

| server | 总容量 | 已用 | 可用 | 使用率 |
|--------|--------|------|------|--------|
| westd-35807 | 350G | 350G | 8K | **100%** |
| westd-45947 | 250G | 176G | 75G | 71% |

## 关键发现

1. **westd-35807 全部 4 张 GPU 空闲** — s2_l01 也挂了（磁盘满），加上之前已知的 s1_l005/s1_l01/s2_l005 共 4 个训练全部死亡
2. **westd-35807 磁盘 100% 满** — 这是 s2_l01 崩溃的直接原因，也可能影响了其他 3 个训练。重启训练前必须先清理磁盘
3. **westd-45947 两个训练健康运行** — step ~8070/30000，进度 27%，预计还需 ~28 小时完成
4. westd-45947 磁盘 71%，step 8000 checkpoint 已成功保存，但后续 checkpoint 需关注空间
