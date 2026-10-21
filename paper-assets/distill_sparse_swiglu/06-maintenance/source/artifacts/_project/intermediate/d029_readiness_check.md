# D029 Benchmark Readiness Check
**Date**: 2026-05-16 | **Server**: westd-34887

## 1. Script
- ✅ `src/benchmark_eval.py` — 16,308 bytes, last modified 11:32 today

## 2. Checkpoints

| Checkpoint | File | Size | Status |
|---|---|---|---|
| KL 50% (mvp_kl_norm_v2_s42) | `predictor_kl_normalized.pt` | 145M | ✅ |
| KL 30% (kl_sparsity30_s42_v3) | `predictor_kl_normalized.pt` | 145M | ✅ |
| KL 70% (kl_sparsity70_s42) | `predictor_kl_normalized.pt` | 145M | ✅ |
| Mistral KL 50% (mistral_kl_s42) | `predictor_kl_normalized.pt` | 145M | ✅ |
| STE (ste_baseline_s42) | `predictor_kl_normalized.pt` | 145M | ✅ |
| BCE iso v2 (bce_isocompute_v2_s42) | `predictor_bce.pt` | 145M | ✅ |

全部 6 个 checkpoint 存在，大小均为 145M (>100MB)。

## 3. STE Checkpoint 文件名
STE checkpoint 确认使用 `predictor_kl_normalized.pt`（非 `predictor_ste.pt`），与命令行一致。

## 4. Model Directories
- ✅ `/root/autodl-tmp/models/llama-3.1-8b/`
- ✅ `/root/autodl-tmp/models/mistral-7b/`

## 5. Results Output Directory
- ✅ `results/benchmark/` 存在，已有 8 个子目录

## 6. Disk Space
| Mount | Size | Used | Avail | Use% |
|---|---|---|---|---|
| `/root/` (overlay) | 30G | 17G | 14G | 55% |
| `/root/autodl-tmp/` | 250G | 43G | 208G | 17% |

空间充足。

## 7. benchmark_eval.py 参数验证
- ✅ `--dense` — 存在 (action=store_true)
- ✅ `--baseline_mode` — 存在 (teal_vanilla, teal_greedy, wina, wina_greedy, rsparse)
- ✅ `--allocation` — 存在 (default=global_topk, 支持 uniform)
- ✅ `--sparsity_target`, `--gpu`, `--exp_id` 等参数齐全

## 8. BCE v3 状态

- **PID 205598** 仍在运行，已运行 ~11 分钟
- 命令: `python -u src/train.py ... --num_steps 2700 --output_dir checkpoints/bce_isocompute_v3_s42`
- `checkpoints/bce_isocompute_v3_s42/` 目录存在但**为空**（尚未产生 checkpoint）

### bench_bce_iso50_s42 建议
**先用 v2 checkpoint 跑 benchmark**。理由：
1. v3 刚开始训练 11 分钟，2700 steps 预计还需数小时
2. v2 checkpoint 已就绪 (145M, predictor_bce.pt)
3. v3 完成后可单独重跑此一条 benchmark 替换结果，成本极低

## 总结

| 项目 | 状态 |
|---|---|
| 脚本 | ✅ Ready |
| 6 个 checkpoint | ✅ 全部就绪 |
| 模型目录 | ✅ Ready |
| 输出目录 | ✅ Ready |
| 磁盘空间 | ✅ 充足 |
| 参数兼容性 | ✅ 全部确认 |
| BCE v3 | ⏳ 训练中，建议先用 v2 |

**结论: D029 benchmark 批次可以立即开始执行。**
