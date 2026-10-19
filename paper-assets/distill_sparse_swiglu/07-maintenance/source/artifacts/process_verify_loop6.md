# Process Verification Report — Loop 6
**Timestamp**: 2026-05-16 ~13:21 UTC  
**Server**: westd-34887

---

## 1. bce_isocompute_v3_s42

| 项目 | 状态 |
|------|------|
| PID | 205598 (wrapper 205597) ✅ 存活 |
| 运行时间 | 42:35 |
| GPU | cuda:1 (CUDA_VISIBLE_DEVICES=1), 82% util, 90947/97887 MiB |
| 当前步数 | **2400/2700** |
| 速度 | 1.05 s/step |
| 预计剩余 | 300 × 1.05s ≈ **5.3 min** |
| 最新 loss | 0.6359 (bce=0.6349, reg=0.0011) |
| sparsity | 0.511 (稳定) |
| lr | 3.25e-05 (cosine 末段) |

**状态**: RUNNING，即将完成。训练正常，loss 收敛良好。

---

## 2. bench_mistral_kl50_s42

| 项目 | 状态 |
|------|------|
| 原始 PID 207957 | ❌ 不存在 |
| 实际 PID | **207962** (wrapper 207961) ✅ 存活 |
| 运行时间 | ~10 min (启动 13:11) |
| GPU | cuda:0, 100% util, 64635/97887 MiB |
| Registry 标记 | DONE(killed) — **错误** |

**评测进度**:
- ✅ wikitext2 — 完成
- ✅ arc_challenge — 完成
- ✅ winogrande — 完成
- 🔄 **mmlu** — loglikelihood requests 3425/58702 (~6%), 37.8 it/s
- ⏳ gsm8k — 未开始

**MMLU 预计剩余**: ~55277 items / 37.8 it/s ≈ 24 min，加上 gsm8k 预计总共还需 **~30-40 min**。

**状态**: RUNNING。Registry 标记 DONE(killed) 有误，PID 不一致是因为 207957 可能是 submit wrapper PID，实际 python 进程是 207962。

---

## 3. bench_dense

| 项目 | 状态 |
|------|------|
| PID 207789 | ❌ 不存在（进程已死） |
| Registry 标记 | PREPARING — **错误** |
| 日志 | `/root/runs/distill_sparse_swiglu/bench_dense.log` |

**失败原因**: 参数解析错误，立即崩溃（EXIT_CODE=2）
```
benchmark_eval.py: error: argument --sparsity_mode: invalid choice: 'dense' 
(choose from 'per_token', 'teal_global')
```

脚本不接受 `--sparsity_mode dense`，应使用 `--dense` 标志。

**状态**: FAILED（参数错误），需修正命令后重新提交。

---

## GPU 使用情况

| GPU | Utilization | Memory |
|-----|-------------|--------|
| cuda:0 | 100% | 64635 / 97887 MiB (66%) — bench_mistral_kl50_s42 |
| cuda:1 | 82% | 90947 / 97887 MiB (93%) — bce_isocompute_v3_s42 |

---

## 建议的 Registry 更新

| 实验 | 当前标记 | 建议动作 |
|------|----------|----------|
| bce_isocompute_v3_s42 | RUNNING | 无变化，~5 min 后完成 |
| bench_mistral_kl50_s42 | DONE(killed) | → **RUNNING**, PID 更新为 207962，预计 ~30-40 min 完成 |
| bench_dense | PREPARING | → **FAILED** (arg parse error)，修正命令后重新提交：使用 `--dense` 而非 `--sparsity_mode dense` |

## bench_dense 重新提交建议

当前 cuda:0 被 bench_mistral 占用，等它完成后再提交 bench_dense 到 cuda:0。或者 bce_isocompute_v3_s42 即将完成（~5 min），届时可用 cuda:1。
