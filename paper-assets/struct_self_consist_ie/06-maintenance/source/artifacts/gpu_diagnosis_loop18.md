# GPU 进程诊断 - Loop 18

检查时间: 2026-05-21 ~04:55 UTC

## autodl-5090

| GPU | 实验 | PID | 存活 | GPU利用率 | 显存占用 |
|-----|------|-----|------|-----------|----------|
| cuda:0 | exp_fewnerd_mf4v2_s42_v3 | 70770 | ❌ 死亡 | 0% | 2/32607 MiB |
| cuda:1 | exp_fewnerd_5epoch_s42 | 63198 | ❌ 死亡 | 0% | 2/32607 MiB |
| cuda:2 | exp_fewnerd_5epoch_s123 | 63337 | ❌ 死亡 | 0% | 2/32607 MiB |
| cuda:3 | (无任务) | — | — | 0% | 2/32607 MiB |

所有 3 个 PID 不存在，4 张 GPU 全部空闲。

## autodl-5090-c

| GPU | 实验 | PID | 存活 | GPU利用率 | 显存占用 |
|-----|------|-----|------|-----------|----------|
| cuda:0 | exp_fewnerd_5epoch_s456 | 353730 | ✅ 存活 | 85% | 30645/32607 MiB |
| cuda:1 | exp_fewnerd_mf4v2_s123_v3 | 357390 (python: 357394) | ✅ 存活 | 86% | 30215/32607 MiB |
| cuda:2 | exp_fewnerd_mf4v2_s456_v3 | 357658 (python: 357662) | ✅ 存活 | 92% | 30165/32607 MiB |
| cuda:3 | e2_pretrained_fewnerd_s42 (额外) | 346388 | ✅ 存活 | 80% | 30295/32607 MiB |

运行时间: s456(5epoch) 2h06m, mf4v2_s123_v3 1h10m, mf4v2_s456_v3 1h10m, e2_pretrained 2h42m。

## 磁盘

- 5090: 88% used, 31GB available (250G total)
- 5090-c: 72% used, 101GB available (350G total)

## 结论

- 存活: 3/6（全部在 autodl-5090-c）
- 死亡: 3/6 — exp_fewnerd_mf4v2_s42_v3, exp_fewnerd_5epoch_s42, exp_fewnerd_5epoch_s123（全部在 autodl-5090）
- 空闲GPU: autodl-5090 全部 4 张 GPU 空闲（cuda:0~3）
- 额外发现: autodl-5090-c cuda:3 有一个额外实验 e2_pretrained_fewnerd_s42 在运行
- 磁盘警告: autodl-5090 磁盘 88%，接近满，需关注
