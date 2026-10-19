# qwen14b_teal30_uniform_gsm8k 状态报告

**检查时间**: 2026-05-19
**服务器**: westd-34887 cuda:1

## 进程状态
- PID 133906: **存活** (Ss+, etime=50:07)
- 子进程 PID 133911 在 GPU 1 上运行

## 日志关键信息
- Sparsity 计算完成，model-level: **0.293**（目标 0.30）
- 各层 sparsity 范围: 0.281–0.301，分布均匀
- lm-eval loglikelihood 阶段已完成 (1319/1319)
- **generate_until 阶段进行中**: 15% (193/1319)，~15.2 s/it
- 无 error/warning（仅有 max_new_tokens/max_length 的 info 提示，不影响结果）

## 预计完成时间
- 剩余 1126 samples × 15.2s ≈ **4h 46min**
- 预计完成: ~今晚

## GPU 使用
| PID | 显存 | 备注 |
|-----|------|------|
| 129225 | 63254 MiB | cuda:0 上其他实验 |
| 133911 | 37268 MiB | 本实验 (cuda:1) |

## 结论
实验正常运行中，无异常。等待 generate_until 完成后检查 exact_match 分数。
