# d064 Final Status — westd-16980

**检查时间**: 2026-05-20 07:18 (服务器时间)

## 文件状态

| 文件 | 行数 | 大小 | 状态 | JSON 验证 |
|------|------|------|------|-----------|
| d064_llama_docred_beam4_unconstrained_16980.jsonl | 998/998 | 8.5MB | ✅ 完成 (03:30) | ✅ OK |
| d064_llama_docred_beam4_constrained_16980.jsonl | 998/998 | 8.5MB | ✅ 完成 (04:17) | ✅ OK |
| d064_llama_docred_greedy_unconstrained_w5.jsonl | 909/998 | 8.1MB | 🔄 运行中 (91.1%) | — |
| d064_llama_docred_greedy_constrained_w5.jsonl | 726/998 | 6.5MB | 🔄 运行中 (72.7%) | — |

## 运行中任务预估

| 任务 | 开始时间 | 已用时 | 速率 | 剩余 | 预计完成 |
|------|----------|--------|------|------|----------|
| greedy_unconstrained_w5 | 03:47 | 3h31m | ~4.3 行/分 | 89 行 | ~07:39 (~20分钟后) |
| greedy_constrained_w5 | 04:18 | 3h00m | ~4.0 行/分 | 272 行 | ~08:26 (~68分钟后) |

## GPU 状态

| GPU | 型号 | 显存使用 | 利用率 | 进程 PID |
|-----|------|----------|--------|----------|
| GPU0 | NVIDIA RTX PRO 6000 Blackwell | 18275/97887 MiB | 90% | 663864 |
| GPU1 | NVIDIA RTX PRO 6000 Blackwell | 18275/97887 MiB | 86% | 665503 |

## 日志文件

| 日志 | 大小 | 最后修改 |
|------|------|----------|
| d064_beam4_unc_16980.log | 140KB | 03:30 |
| d064_beam4_con_16980.log | 136KB | 04:17 |
| d064_greedy_unc_w5.log | 120KB | 07:18 (活跃) |
| d064_greedy_con_w5.log | 97KB | 07:18 (活跃) |

## 异常

无异常。两个 beam4 任务已正常完成（998行，JSON 首尾行验证通过）。两个 greedy w5 任务（Option C）正在正常推进中，GPU 利用率健康，预计全部完成时间约 08:30。
