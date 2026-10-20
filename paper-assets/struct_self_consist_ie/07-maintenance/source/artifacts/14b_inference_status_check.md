# 14B 推理任务状态检查

**检查时间**: 2026-05-20 22:37 UTC
**服务器**: autodl-5090-c

## 任务架构

三个 shell 脚本各自在固定 GPU 上循环运行 N∈{1,2,4,8,16}：
- `run_14b_fewnerd.sh` → GPU 0 (CUDA_VISIBLE_DEVICES=0)
- `run_14b_conll.sh` → GPU 1 (CUDA_VISIBLE_DEVICES=1)
- `run_14b_scierc.sh` → GPU 3 (CUDA_VISIBLE_DEVICES=3)

模型: `checkpoints/qwen25-14b-fewnerd-merged-final`，T=1.0，seed=42，collect_logprobs

## 进程状态

| 任务 | 原始 PID | 当前状态 | 当前运行 N 值 | 进度 |
|------|---------|---------|-------------|------|
| FewNERD | 201001 | **运行中** (GPU 0, 98%) | N=1 | 4886/37648 (13%), ~1547 toks/s, 预计剩余 ~55min (仅 N=1) |
| CoNLL | 201712 (已结束) | **运行中** (GPU 1, 12%) | N=2 | 1460/6906 (21%), ~3117 toks/s |
| SciERC | 203156 (已结束) | **运行中** (GPU 3, 99%) | N=16 | 347/551 (63%), 即将完成 |

**注意**: 原始 PID 201712/203156 是第一轮 N=1 的 python 进程，已结束。Shell 脚本启动了新进程继续后续 N 值。
当前活跃 VLLM 引擎: PID 201291 (GPU 0), PID 206376 (GPU 1), PID 205675 (GPU 3)。GPU 2 空闲。

## 已完成输出

| 目录 | 状态 | report.json | samples.jsonl |
|------|------|-------------|--------------|
| scierc_n1 | ✅ 完成 | 1.5KB | 1.2MB |
| scierc_n2 | ✅ 完成 | 1.5KB | (有) |
| scierc_n4 | ✅ 完成 | 1.7KB | (有) |
| scierc_n8 | ✅ 完成 | 1.7KB | 3.9MB |
| scierc_n16 | ⏳ 运行中 (~63%) | - | - |
| conll2003_n1 | ✅ 完成 | 1.6KB | 9.9MB |
| conll2003_n2 | ⏳ 运行中 (~21%) | - | - |
| fewnerd_n1 | ⏳ 运行中 (~13%) | - | - |

## 预估完成时间

| 任务 | 当前 N | 当前 N 剩余时间 | 全部 N 完成预估 |
|------|--------|----------------|---------------|
| SciERC | N=16 | ~几分钟 | **即将全部完成** |
| CoNLL | N=2 | ~5min | ~2-3h (N=4/8/16 逐步变长) |
| FewNERD | N=1 | ~55min | **20-30h+** (37648 实例/N，N=1 已需 ~1h) |

## 已完成结果摘要

### SciERC (551 instances, NER)

| N | greedy_F1 | oracle_F1 | oracle_headroom | fleiss_kappa | soft_jaccard | verdict |
|---|-----------|-----------|-----------------|-------------|-------------|---------|
| 1 | 0.0041 | 0.0063 | 0.0022 | 1.0 (trivial) | 1.0 (trivial) | FAIL |
| 2 | 0.0041 | 0.0063 | 0.0022 | 0.685 | 0.847 | FAIL |
| 4 | 0.0041 | 0.0063 | 0.0022 | 0.620 | 0.810 | FAIL |
| 8 | 0.0041 | 0.0147 | 0.0106 | 0.660 | 0.813 | FAIL |

Signal metrics (N=4, full set):
- Fleiss vs F1: ρ=-0.133 (p=0.002) — **显著但方向相反**
- SoftJaccard vs F1: ρ=-0.127 (p=0.003) — **显著但方向相反**
- structural_beats_surface: True (N=2,4), False (N=8)
- rho_advantage: 0.0064 (N=4)

Logprob baseline (full set): ρ ∈ [-0.077, -0.049], AUROC ∈ [0.20, 0.31]

**核心问题**: 99%+ 样本 F1=0，greedy F1 仅 0.41%。模型在 SciERC 上几乎完全失败。

### CoNLL2003 (3453 instances, NER, N=1 only)

| N | greedy_F1 | oracle_F1 | oracle_headroom | fleiss_kappa | soft_jaccard | verdict |
|---|-----------|-----------|-----------------|-------------|-------------|---------|
| 1 | 0.046 | 0.042 | -0.004 | 1.0 (trivial) | 1.0 (trivial) | FAIL |

- 95% 样本 F1=0
- oracle_F1 < greedy_F1 (负 headroom，异常)
- Logprob: ρ=-0.052 (p=0.007), AUROC=0.436

**核心问题**: F1 仅 4.6%，同样几乎完全失败。

### FewNERD

尚无完成结果（N=1 进行中，13%）。

## 关键警告

1. **模型在 SciERC/CoNLL 上 NER F1 极低** (0.4%-4.6%)，99%/95% 样本 F1=0
2. 所有已完成 report 均建议 "re-running at T=0.7"
3. SciERC consistency signal (Fleiss/SJ) 与 F1 的相关性**为负** — 一致性高的样本反而 F1 更低
4. CoNLL oracle_headroom 为负，说明多样本采样无法改善（N=1 时 trivial）
5. 模型是在 FewNERD 上训练的，跨数据集泛化能力可能很差 — 等 FewNERD 结果出来后对比确认
