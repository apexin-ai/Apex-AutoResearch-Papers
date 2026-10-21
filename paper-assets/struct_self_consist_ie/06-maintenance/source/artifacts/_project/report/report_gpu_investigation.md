# GPU 进程排查报告

**时间**: 2026-05-23 01:20 UTC

---

## 1. GPU 利用率与进程总览

### autodl-5090

| GPU | 利用率 | 显存占用 | 进程 |
|-----|--------|----------|------|
| 0 | 0% | 2/32607 MiB | 空闲 |
| 1 | 0% | 2/32607 MiB | 空闲 |
| 2 | 0% | 2/32607 MiB | 空闲 |
| 3 | **73%** | **29844/32607 MiB** | `exp_fewnerd_pretrained_n32_s42_v2` (PID 157469, vLLM) |

### autodl-5090-c

| GPU | 利用率 | 显存占用 | 进程 |
|-----|--------|----------|------|
| 0 | 0% | 0/32607 MiB | 空闲 |
| 1 | **87%** | **29901/32607 MiB** | `exp_fewnerd_pretrained_n16_s42_v2` (PID 452661, vLLM) |
| 2 | 0% | 0/32607 MiB | 空闲 |
| 3 | **84%** | **29785/32607 MiB** | `exp_fewnerd_pretrained_n32_s42` v1 残留 (PID 387768, vLLM) |

---

## 2. 未注册进程识别

### autodl-5090:cuda:3 → exp_fewnerd_pretrained_n32_s42_v2（已注册，正常）

- **身份**: registry 中 RUNNING 的实验，是合法进程
- **命令**: `python -u code/run_mvp_pilot.py --model_path /root/autodl-tmp/models/Qwen2.5-7B-Instruct --n_samples 32 --seed 42`
- **进度**: 55968/1204736 = **4.6%**，已运行 ~58 分钟
- **速度**: ~25 it/s
- **预计完成**: ~12.8 小时后 → **May 23 ~13:00 UTC**
- **状态**: ✅ 正常运行

### autodl-5090-c:cuda:1 → exp_fewnerd_pretrained_n16_s42_v2（Registry 未更新）

- **身份**: registry 中状态为 **PREPARING**，但实际已在运行
- **命令**: `python -u code/run_mvp_pilot.py --model_path /root/autodl-tmp/.hf_cache/Qwen2.5-7B-Instruct --n_samples 16 --seed 42`
- **进度**: 132960/602368 = **22%**，已运行 ~1h52m
- **速度**: ~22 it/s
- **预计完成**: ~5.9 小时后 → **May 23 ~07:15 UTC**
- **状态**: ⚠️ 正在运行但 registry 未更新到 RUNNING

### autodl-5090-c:cuda:3 → exp_fewnerd_pretrained_n32_s42 v1 残留（孤儿进程）

- **身份**: v1 实验的残留进程。Registry 中 v1 已标记为 DONE/failed（updated 15:49 UTC），但 **GPU 进程从未被 kill**
- **命令**: `python -u code/run_mvp_pilot.py --model_path /root/autodl-tmp/.hf_cache/Qwen2.5-7B-Instruct --n_samples 32 --seed 42`
- **进度**: 981920/1204736 = **81.5%**，已运行 ~13 小时
- **速度**: ~20 it/s
- **预计完成**: ~3.1 小时后 → **May 23 ~04:10 UTC**
- **状态**: ❌ **孤儿进程**。v1 因 UnicodeEncodeError 风险被标记为 failed，fix（errors='replace'）在 v1 启动后才部署，v1 进程使用旧代码，完成后大概率在 save 阶段崩溃

---

## 3. exp_fewnerd_pretrained_n32_s42_v2 进度

- **服务器**: autodl-5090 GPU 3（v2 主实例）
- **v2 进度**: 4.6%，预计 May 23 ~13:00 UTC 完成
- **v2 启动时间**: May 23 00:15 UTC
- **总 prompts**: 1,204,736（N=32, FewNERD pretrained baseline）

---

## 4. ANALYZING 实验状态

### exp_fewnerd_mf4_s123_v2
- **Registry**: ANALYZING, conclusion=success, server=autodl-5090 GPU cuda:2
- **残留进程**: 无（autodl-5090 GPU 2 空闲，0% 利用率）
- **状态**: ✅ 实验已完成执行，仅需结果分析

### exp_fewnerd_mf4_s456
- **Registry**: ANALYZING, conclusion=success, server=autodl-5090-c GPU cuda:2
- **残留进程**: 无（autodl-5090-c GPU 2 空闲，0% 利用率）
- **状态**: ✅ 实验已完成执行，仅需结果分析

---

## 5. 建议操作

| 优先级 | 操作 | 原因 |
|--------|------|------|
| **P0** | Kill autodl-5090-c PID 387495（及子进程 387768） | v1 孤儿进程，使用旧代码会在 save 时崩溃，白占 1 张 GPU。kill 后释放 cuda:3 |
| **P1** | 更新 registry: `exp_fewnerd_pretrained_n16_s42_v2` 状态 PREPARING → RUNNING，server=autodl-5090-c，gpu=cuda:1 | 实际已在运行但 registry 未反映 |
| **P2** | 分析 exp_fewnerd_mf4_s123_v2 和 exp_fewnerd_mf4_s456 的结果 | 长期处于 ANALYZING 状态，应完成分析并更新为 DONE |
