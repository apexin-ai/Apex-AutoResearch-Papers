# GPU 状态 + 多种子实验汇总 (2026-05-23 20:30 UTC)

## GPU 状态

### westd-16639 (4× RTX PRO 6000 Blackwell, 98GB each)
| GPU | 显存占用 | Util% | 进程 | 实验 | 状态 |
|-----|---------|-------|------|------|------|
| cuda:0 | 88275/97887 MiB | 97% | PID 744822: vLLM LLaMA-8B (port 8009) → PID 745727: llama8b_pw_seed789 | exp-multi-seed-llama-pw-seed789 | 运行中 (383/600) |
| cuda:1 | 88263/97887 MiB | 97% | PID 684239: vLLM LLaMA-8B (port 8006) → PID 761487: llama8b_pw_seed456 | exp-multi-seed-llama-pw-seed456 | 运行中 (178/600) |
| cuda:2 | 90169/97887 MiB | 97% | PID 739631: vLLM Qwen2.5-14B (port 8007) → PID 740846: qwen25_pw_seed789 | exp-multi-seed-qwen25-pw-seed789 | 运行中 (441/600) |
| cuda:3 | 0/97887 MiB | 0% | — | — | **空闲** |

**备注:** PID 681007 (旧 idle vLLM Qwen2.5-14B) 已被 kill，cuda:3 已释放。

### westd-14391 (1× RTX PRO 6000 Blackwell, 98GB)
| GPU | 显存占用 | Util% | 进程 | 实验 | 状态 |
|-----|---------|-------|------|------|------|
| cuda:0 | 88229/97887 MiB | 0%* | PID 9284: vLLM LLaMA-8B (port 8000) → PID 46221: llama8b_pw_seed123 | llama8b_pw_seed123 | 运行中 (461/600) |

*GPU util 瞬时读数为 0%，但日志显示 20:32:30 仍有活跃请求。实验正常运行中。

**⚠️ 关键发现:** LLaMA-8B PW seed42 已完成 (n=600)。seed123 仍在跑但 **16639 上已有完整的 seed123 结果 (n=600)**，该实验冗余。

### westd-30973 (3× RTX PRO 6000 Blackwell, 98GB each)
| GPU | 显存占用 | Util% | 进程 | 实验 | 状态 |
|-----|---------|-------|------|------|------|
| cuda:0 | 88249/97887 MiB | 97% | PID 3232: vLLM Qwen2.5-14B (port 8000) → PID 6058: qwen25_pw_seed789_v3 | exp-multi-seed-qwen25-pw-seed789-v3 | 运行中 (332/600) |
| cuda:1 | 88275/97887 MiB | 97% | PID 3658: vLLM LLaMA-8B (port 8001) → PID 6027: llama8b_pw_seed789_v2 | exp-multi-seed-llama-pw-seed789-v2 | 运行中 (320/600) |
| cuda:2 | 88275/97887 MiB | 97% | PID 4812: vLLM LLaMA-8B (port 8002) → PID 6097: llama8b_pw_seed456_v2 | exp-multi-seed-llama-pw-seed456-v2 | 运行中 (326/600) |

## 需要清理的进程

| 服务器 | PID | 原因 |
|--------|-----|------|
| westd-14391 | 46221 (实验) + 9284 (vLLM) | llama8b_pw_seed123 已在 16639 完成 (n=600)，此实验冗余。kill 后可释放 1 张 GPU |

## 重复实验警告

以下实验在多台服务器上同时运行（不同版本）：

| 实验 | westd-16639 进度 | westd-30973 进度 | 说明 |
|------|-----------------|-----------------|------|
| llama8b_pw_seed789 | 383/600 | 320/600 (v2) | 16639 领先 |
| llama8b_pw_seed456 | 178/600 | 326/600 (v2) | 30973 领先 |
| qwen25_pw_seed789 | 441/600 | 332/600 (v3) | 16639 领先 |

如果 v2/v3 是有意的新版本运行，可考虑 kill 16639 上的旧版本以释放 GPU。反之亦然。

## 空闲 GPU

| 服务器 | GPU | 可用显存 | 建议 |
|--------|-----|---------|------|
| westd-16639 | cuda:3 | 98GB | 可启动 Qwen2.5 seed456 resume (从 478/600 继续) |

## 多种子实验结果

### LLaMA-3.1-8B × ProofWriter-600
| Seed | n | SC% | SICA% | Δ(pp) | 状态 | 服务器 | 输出路径 |
|------|---|-----|-------|-------|------|--------|---------|
| 42 | 600 | 72.33 | 66.67 | -5.67 | ✅ 完成 | westd-14391 | llama8b_pw_seed42 |
| 123 | 600 | 71.33 | 64.17 | -7.17 | ✅ 完成 | westd-16639 | llama8b_pw_seed123 |
| 456 | 178 | 72.47 | 66.85 | -5.62 | ⏳ 运行中 | westd-16639 | llama8b_pw_seed456 |
| 456 v2 | 326 | 73.31 | 68.40 | -4.91 | ⏳ 运行中 | westd-30973 | llama8b_pw_seed456_v2 |
| 789 | 383 | 73.89 | 67.89 | -6.01 | ⏳ 运行中 | westd-16639 | llama8b_pw_seed789 |
| 789 v2 | 320 | 69.06 | 66.56 | -2.50 | ⏳ 运行中 | westd-30973 | llama8b_pw_seed789_v2 |

**已完成种子 (seed42, seed123) 平均:** SC=71.83%, SICA=65.42%, Δ=-6.42pp

### Qwen2.5-14B × ProofWriter-600
| Seed | n | SC% | SICA% | Δ(pp) | 状态 | 服务器 | 输出路径 |
|------|---|-----|-------|-------|------|--------|---------|
| 123 | 600 | 72.33 | 71.17 | -1.17 | ✅ 完成 | westd-16639 | qwen25_pw_seed123 |
| 456 | 478 | 73.43 | 72.38 | -1.05 | ⏸️ 暂停 | westd-16639 | qwen25_pw_seed456 |
| 789 | 441 | 73.24 | 71.88 | -1.36 | ⏳ 运行中 | westd-16639 | qwen25_pw_seed789 |
| 789 v3 | 332 | 72.29 | 71.69 | -0.60 | ⏳ 运行中 | westd-30973 | qwen25_pw_seed789_v3 |

**已完成种子 (seed123) 初步:** SC=72.33%, SICA=71.17%, Δ=-1.17pp  
**Qwen2.5 的 Δ 显著小于 LLaMA (-1.x vs -5~7pp)**

## 未完成实验清单

| 实验 | 当前进度 | 预计剩余时间 | 服务器 |
|------|---------|------------|--------|
| llama8b_pw_seed456 | 178/600 (30%) | ~8h | 16639 cuda:1 |
| llama8b_pw_seed456_v2 | 326/600 (54%) | ~5h | 30973 cuda:2 |
| llama8b_pw_seed789 | 383/600 (64%) | ~4h | 16639 cuda:0 |
| llama8b_pw_seed789_v2 | 320/600 (53%) | ~5h | 30973 cuda:1 |
| qwen25_pw_seed456 | 478/600 (80%) | 需 resume | **未运行** |
| qwen25_pw_seed789 | 441/600 (74%) | ~3h | 16639 cuda:2 |
| qwen25_pw_seed789_v3 | 332/600 (55%) | ~5h | 30973 cuda:0 |
| llama8b_pw_seed123 (14391) | 461/600 (77%) | 冗余，建议 kill | 14391 cuda:0 |
