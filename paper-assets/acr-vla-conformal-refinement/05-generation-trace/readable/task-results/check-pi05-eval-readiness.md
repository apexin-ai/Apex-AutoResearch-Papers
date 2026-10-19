# check pi05 eval readiness

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_pi05-eval-readiness_20260524T145907_result.json`
- **Structured JSON:** [`4a2988e549d5a2f882b2.json`](../../sessions/4a/4a2988e549d5a2f882b2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部检查完成。以下是 π0.5 eval 部署准备情况报告。

---

## π0.5 Eval 部署就绪清单

### 1. Eval 脚本适配 — ✅ 就绪

`/root/acr-vla-conformal-refinement/src/evaluate.py` 完整支持 π0.5：
- `--model pi05` 已在 choices 中
- π0.5 feature dim=2048 有显式校验（L614-618），CRM 模式需传 `--obs_dim 2048`
- `_pad_obs` + `--unified_obs_dim` 支持多 VLA 维度统一
- π0.5 chunk replay 已修复（`predict_action()` 路径），解决了之前 0% SR 的 bug

### 2. π0.5 模型权重 — ✅ 就绪

`/root/autodl-tmp/models/pi05_libero_finetuned/model.safetensors` (7.5GB) 存在

### 3. CRM Checkpoint — ❌ 阻塞

- **现有**: `crm_smolvla_3suite_v1/crm_best.pt` (obs_dim=960) — SmolVLA 的，**不兼容** π0.5 (需 obs_dim=2048)
- **π0.5 CRM**: 服务器上不存在。训练预计 5/25 ~04:00 UTC 完成后，需要知道 checkpoint 产出位置并同步到此服务器

### 4. Precomputed Features — ℹ️ 不阻塞 eval

- `crm_cache_pi05/object/` 仅完成 shard 0 (7251/72507=10%)，spatial/goal 完全缺失
- 但 **precomputed features 仅用于 CRM 训练**（train_crm.py），eval 使用 live inference，不需要这些数据

### 5. 方法映射

| 用户方法名 | evaluate.py 参数 | 需要 CRM ckpt |
|-----------|-----------------|-------------|
| `vla_only` | `--mode vla_only --baseline_mode single` | ❌ 不需要 |
| `k2mean` | `--mode vla_only --baseline_mode mean --K 2` | ❌ 不需要 |
| `reconvla` | `--mode reconvla` | ❌ 不需要 |
| `crm` | `--mode acr_vla --obs_dim 2048 --checkpoint &lt;pi05_crm_best.pt>` | ✅ 需要 |
| `adaptive` | `--mode adaptive_conformal_crm --obs_dim 2048 --checkpoint &lt;pi05_crm_best.pt>` | ✅ 需要 |

### 6. 30 个实验矩阵

**可立即启动 (18/30):**

| # | suite | seed | method | 命令 |
|---|-------|------|--------|------|
| 1 | object | 42 | vla_only | `python evaluate.py --benchmark object --mode vla_only --model pi05 --seed 42 --n_rollouts 20` |
| 2 | object | 43 | vla_only | 同上 `--seed 43` |
| 3 | spatial | 42 | vla_only | `--benchmark spatial --seed 42` |
| 4 | spatial | 43 | vla_only | `--benchmark spatial --seed 43` |
| 5 | goal | 42 | vla_only | `--benchmark goal --seed 42` |
| 6 | goal | 43 | vla_only | `--benchmark goal --seed 43` |
| 7 | object | 42 | k2mean | `python evaluate.py --benchmark object --mode vla_only --baseline_mode mean --K 2 --model pi05 --seed 42 --n_rollouts 20` |
| 8-12 | ... | ... | k2mean | 同上，替换 benchmark/seed |
| 13 | object | 42 | reconvla | `python evaluate.py --benchmark object --mode reconvla --model pi05 --seed 42 --n_rollouts 20` |
| 14-18 | ... | ... | reconvla | 同上，替换 benchmark/seed |

**阻塞中 (12/30) — 等待 π0.5 CRM checkpoint:**

| # | suite | seed | method | 命令模板 |
|---|-------|------|--------|---------|
| 19-24 | object/spatial/goal × s42/s43 | crm | `python evaluate.py --benchmark {suite} --mode acr_vla --model pi05 --obs_dim 2048 --checkpoint {PI05_CRM_CKPT} --seed {seed} --n_rollouts 20` |
| 25-30 | object/spatial/goal × s42/s43 | adaptive | `python evaluate.py --benchmark {suite} --mode adaptive_conformal_crm --model pi05 --obs_dim 2048 --checkpoint {PI05_CRM_CKPT} --seed {seed} --n_rollouts 20` |

### 7. GPU 时间估算

| 方法 | 每次 inference | 每 run 推理次数 | 预估时长/run |
|------|-------------|-------------|------------|
| vla_only (K=1) | ~1.5s | ~5,600 (280步/10步×10任务×20rollouts) | ~2.5h |
| k2mean (K=2) | ~3s | ~5,600 | ~3h |
| reconvla (K=10) | ~15s | ~5,600 | ~4h |
| crm (K=10) | ~15s + CRM | ~5,600 | ~4.5h |
| adaptive (K=2/10) | ~3-15s | ~5,600 | ~3.5h |

**总计**: ~30 runs × ~3.5h avg = **~105 GPU-hours**。每个 eval 需 1 GPU ≥24GB VRAM。

### 8. 行动建议

1. **立即可做**: 启动 18 个不依赖 CRM 的 eval（vla_only/k2mean/reconvla）
2. **待确认**: π0.5 CRM 训练的 checkpoint 输出路径——训练完成后需同步到 `/root/autodl-tmp/checkpoints/crm_pi05_3suite/crm_best.pt`
3. **注意**: 之前 `eval_pi05_baseline_object_seed42_r2.json` 全 10 任务 0% SR 是已修复的 chunk replay bug，当前代码已修复

---
