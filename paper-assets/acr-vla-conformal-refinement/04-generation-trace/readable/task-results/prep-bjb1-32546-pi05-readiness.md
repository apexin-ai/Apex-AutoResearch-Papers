# prep bjb1 32546 pi05 readiness

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_bjb1-32546-pi05-readiness_20260526T033800_result.json`
- **Structured JSON:** [`222febe33ccc8fe2d9f5.json`](../../sessions/22/222febe33ccc8fe2d9f5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

LIBERO 和 PyTorch 都就绪。现在写报告。

---

## bjb1-32546 π0.5 CRM K=2 Long 实验就绪检查报告

### 依赖状态

| # | 依赖项 | 状态 | 详情 |
|---|--------|------|------|
| 1 | π0.5 模型权重 | ✅ 就绪 | `/root/autodl-tmp/models/pi05_libero_finetuned/model.safetensors` (7.0GB) |
| 2 | π0.5 CRM checkpoint | ✅ 就绪 | `/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt` (2.5MB, 2026-05-25) |
| 3 | Long precompute 数据 | ⚠️ 不存在，但**评估不需要** | `crm_cache_pi05_2048/` 整个目录不存在。但 `evaluate.py` 跑的是**在线 LIBERO 环境 rollout**，不读 precompute 数据。Precompute 数据仅用于 CRM 训练。 |
| 4 | 代码 | ✅ 存在 | `src/evaluate.py` 存在 (36KB, 2026-05-26 更新)。**无 .git 目录**，无法确认是否最新版本。 |
| 5 | LIBERO 环境 | ✅ 就绪 | libero 已安装 (conda python3.12) |
| 6 | PyTorch + CUDA | ✅ 就绪 | torch=2.10.0+cu128, CUDA=True, 6 GPU |
| 7 | 磁盘空间 | ✅ 充足 | 根分区 20GB 可用 (34% 已用)，数据盘 151GB 可用 (40% 已用) |

### 问题项

**1. 无 Git 仓库** — 代码目录 `/root/acr-vla-conformal-refinement/` 没有 `.git`，无法确认代码版本是否与 bjb1-18228 一致。建议在 SmolVLA 实验完成后用 `rsync` 或 `git clone` 同步最新代码。

**2. `crm_cache_pi05_2048/long/` 不存在** — 虽然评估命令不需要，但如果后续需要在 bjb1-32546 上做 CRM 训练，需要从 bjb1-18228 传输：
```bash
# 仅 long/ 子目录: 2.5GB，传输约 1-3 分钟（内网）
scp -r connect.bjb1.seetacloud.com:/root/autodl-tmp/crm_cache_pi05_2048/long/ /root/autodl-tmp/crm_cache_pi05_2048/long/

# 全部 4 个 benchmark: 5.9GB
scp -r connect.bjb1.seetacloud.com:/root/autodl-tmp/crm_cache_pi05_2048/ /root/autodl-tmp/crm_cache_pi05_2048/
```

### 结论

**bjb1-32546 基本具备运行条件。** 模型、CRM checkpoint、LIBERO 环境、PyTorch 全部就绪。唯一不确定项是代码版本——建议在 SmolVLA 完成后先同步代码再启动实验。

参考运行命令（6 GPU 可并行跑 6 个 seed）：
```bash
CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --model pi05 --mode crm_obs_only --K 2 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt --obs_dim 2048 --unified_obs_dim 2088 --benchmark long --seed 42 --n_rollouts 20 --output_file logs/eval_long_crm_obs_only_norm0.05_seed42_pi05_K2.json
```

---
