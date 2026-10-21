# GPU & 实验状态报告

**时间**: 2026-05-21 11:20 UTC

---

## autodl-5090 (4x RTX 5090)

### GPU 状态
| GPU | Util | VRAM Used | VRAM Total |
|-----|------|-----------|------------|
| 0 | 97% | 31518 MiB | 32607 MiB |
| 1 | 97% | 31518 MiB | 32607 MiB |
| 2 | 100% | 31518 MiB | 32607 MiB |
| 3 | 100% | 31518 MiB | 32607 MiB |

### 活跃实验
| 实验 | PID | GPU | 进度 | 状态 |
|------|-----|-----|------|------|
| **32B FewNERD N=8 s42** | 978391 | cuda:0-3 (TP=4) | 92% (34513/37648) | RUNNING |

- 模型: `qwen25-32b-fewnerd-merged`, T=1.0, --collect_logprobs
- 速度: ~3940 toks/s input, ~1947 toks/s output
- 预计剩余: ~3-5 分钟
- 输出目录: `output/exp_32b_fewnerd_n8_s42/` (空，尚未写入)

---

## autodl-5090-b (4x RTX 5090)

### GPU 状态
| GPU | Util | VRAM Used | VRAM Total |
|-----|------|-----------|------------|
| 0 | 91% | 30276 MiB | 32607 MiB |
| 1 | 86% | 30270 MiB | 32607 MiB |
| 2 | 0% | 2 MiB | 32607 MiB |
| 3 | 0% | 2 MiB | 32607 MiB |

### GPU 冲突检查
- 旧 PIDs (296744, 296880, 297143, 297409): **全部已退出**
- 新 PIDs 305836 (cuda:2), 305838 (cuda:3): **已退出** -- GPU 2/3 空闲
- **无 GPU 冲突** -- 仅 GPU 0 和 GPU 1 各跑一个实验

### 活跃实验
| 实验 | PID | GPU | 进度 | 状态 |
|------|-----|-----|------|------|
| fewnerd_t05_s456 | 305832 | cuda:0 | 5% (16720/301184) | RUNNING |
| fewnerd_t12_s456 | 305834 | cuda:1 | 5% (15208/301184) | RUNNING |

- 模型: `qwen3-8b-fewnerd-exp021-merged`, N=8, --collect_logprobs
- 速度: ~6490/5940 toks/s input
- 预计剩余: ~1.5-2 小时

### 已完成实验
| 实验 | 输出目录 | 结果 |
|------|----------|------|
| scierc_t05_s123 | `output/scierc_t05_s123/` | report.json + samples.jsonl |
| scierc_t12_s123 | `output/scierc_t12_s123/` | report.json + samples.jsonl |

#### SciERC T=0.5 s123 结果
- greedy_f1: **0.6651**, oracle_f1: **0.7428**, oracle_headroom: **0.0777**
- fleiss_kappa_mean: 0.5872, soft_jaccard_mean: 0.8417
- rho_SJ_F1 (full): **0.3215** (p<1e-14), rho_FK_F1: 0.2953
- logprob_baseline AUROC (full): 0.5843
- structural_beats_surface: **true**, rho_advantage: 0.026
- verdict: **MARGINAL**

#### SciERC T=1.2 s123 结果
- greedy_f1: **0.6643**, oracle_f1: **0.7879**, oracle_headroom: **0.1236**
- fleiss_kappa_mean: 0.3394, soft_jaccard_mean: 0.6416
- rho_SJ_F1 (full): **0.3464** (p<1e-16), rho_FK_F1: 0.2226
- logprob_baseline AUROC (full): 0.5738
- structural_beats_surface: **true**, rho_advantage: **0.124**
- verdict: **MARGINAL**

---

## autodl-5090-c (4x RTX 5090)

### GPU 状态
| GPU | Util | VRAM Used | VRAM Total |
|-----|------|-----------|------------|
| 0 | 99% | 31365 MiB | 32607 MiB |
| 1 | 0% | 0 MiB | 32607 MiB |
| 2 | 90% | 29869 MiB | 32607 MiB |
| 3 | 90% | 30117 MiB | 32607 MiB |

### 活跃实验
| 实验 | PID | GPU | 状态 |
|------|-----|-----|------|
| **14B FewNERD** (final) | 252310 | cuda:0 | RUNNING |
| **FewNERD 7B N=16 s42** | 264875 | cuda:2 | RUNNING |
| **CoNLL N=16 s42** | 269975 | cuda:3 | RUNNING |
| probe_groupkfold.py | 270904, 271213 | CPU | RUNNING (scierc 300/551) |

- 14B: `qwen25-14b-fewnerd-merged-final`, N=8, T=1.0, s42, --enforce_eager
- 7B: `qwen25-7b-fewnerd-merged`, N=16, T=1.0, s42
- CoNLL: `qwen3-8b-conll2003-merged`, N=16, T=1.0, s42

### 已完成实验
| 实验 | 原 PID | GPU | 输出目录 |
|------|--------|-----|----------|
| **SciERC T=0.8 s123** | 269240 | cuda:1 | `output/scierc_t08_s123/` |

#### SciERC T=0.8 s123 结果
- greedy_f1: **0.6623**, oracle_f1: **0.7725**, oracle_headroom: **0.1102**
- fleiss_kappa_mean: 0.4513, soft_jaccard_mean: 0.7502
- rho_SJ_F1 (full): **0.3822** (p<1e-19), rho_FK_F1: 0.2980
- logprob_baseline AUROC (full): 0.5963
- structural_beats_surface: **true**, rho_advantage: **0.084**
- verdict: **MARGINAL**

### Probe GroupKFold 中间结果

#### CoNLL
- groupkfold_auroc_mean: **0.8849** (std 0.046)
- stratifiedkfold_auroc_mean: 0.9796
- delta (groupkfold - stratified): **-0.095**
- interpretation: **HIGH** -- probe > MV, info exists in representation, prompt interface fails

#### FewNERD
- groupkfold_auroc_mean: **0.6513** (std 0.039)
- stratifiedkfold_auroc_mean: 0.9872
- delta: **-0.336**
- interpretation: **MODERATE** -- partial info in representation

(SciERC 处理中，300/551 完成)

---

## 汇总

| 服务器 | 空闲 GPU | 活跃实验数 | 备注 |
|--------|---------|-----------|------|
| 5090 | 0/4 | 1 (32B TP=4) | 即将完成 (~3-5min)，完成后 4 GPU 全部释放 |
| 5090-b | 2/4 (GPU 2,3) | 2 | GPU 2/3 空闲可调度 |
| 5090-c | 1/4 (GPU 1) | 3 + 1 CPU | GPU 1 空闲可调度 |

### SciERC 温度扫描对比 (seed=123, N=8)

| T | greedy_f1 | oracle_f1 | headroom | rho_SJ_F1 | rho_advantage | kappa |
|---|-----------|-----------|----------|-----------|---------------|-------|
| 0.5 | 0.6651 | 0.7428 | 0.078 | 0.322 | 0.026 | 0.587 |
| 0.8 | 0.6623 | 0.7725 | 0.110 | **0.382** | 0.084 | 0.451 |
| 1.2 | 0.6643 | 0.7879 | 0.124 | 0.346 | **0.124** | 0.339 |

**观察**: T=0.8 在 rho_SJ_F1 上达到最高 (0.382)，T=1.2 headroom 最大但 kappa 最低。T=0.8 是 structural signal 和 diversity 的最佳平衡点。
