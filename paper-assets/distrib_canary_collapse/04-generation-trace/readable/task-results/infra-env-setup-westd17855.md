# infra env setup westd17855

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_env_setup_westd17855_20260518T154535_result.json`
- **Structured JSON:** [`08c2adc45265a93792c8.json`](../../sessions/08/08c2adc45265a93792c8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全面状态已收集。生成最终报告。

---

## westd-17855 环境搭建状态报告

### 1. 硬件环境
| 项目 | 状态 |
|------|------|
| GPU | 6× NVIDIA RTX PRO 6000 Blackwell (98GB VRAM each) |
| 磁盘 | 350GB，已用 11GB (3%)，剩余 340GB |
| Python | 3.12 (Miniconda3 base) |
| PyTorch | 2.8.0+cu128，CUDA ✅ |

### 2. 目录结构 ✅
```
/root/autodl-tmp/distrib_canary_collapse/
├── analysis/          (detrending_utils.py)
├── artifacts/
├── configs/
├── data/              (c4_5k, wikitext103, wikitext103_5k, dryrun_tiny)
├── docs/
├── figures/
├── logs/
├── mmct/              (__init__.py, consensus_test.py, methods.py, null_distribution.py, run_mmct.py)
├── results/
├── scripts/           (change_point_analysis.py, change_point_supplement.py, gen_single_method_table.py, transfer_entropy_analysis.py)
├── iterative_train.py
├── metrics.py
├── prepare_data.py
└── prepare_c4*.py (5 variants)
```

### 3. Python 依赖 ✅
transformers 5.8.1, datasets 4.8.5, scipy, statsmodels, accelerate, mauve-text, nltk — 全部 import 通过

### 4. 数据 ✅
| 数据集 | 大小 | 来源 |
|--------|------|------|
| c4_5k | 14MB | 从 westd-19828 SCP 传输 |
| wikitext103 | 503MB | 从 westd-19828 SCP 传输 |
| wikitext103_5k | 503MB | 本地 `prepare_data.py` 生成（716K train, 1.5K eval, 5K prompts）|

### 5. Dry-run 测试 ✅（部分）
- 模型加载：✅ pythia-410m 正常加载
- 文本生成：✅ 10 条 synthetic data 生成并保存
- 指标计算：⏳ 等待 gpt2-large 下载完成（MAUVE 指标依赖）
- 训练步骤：⏳ 尚未到达（等 metrics 完成）

**pipeline 核心流程（加载→生成→保存）已验证可用。**

### 6. 模型缓存
| 模型 | 大小 | 状态 |
|------|------|------|
| EleutherAI/pythia-410m | ~860MB | ✅ 已缓存 |
| EleutherAI/pythia-1.4b | ~2.8GB | ⏳ 下载中 (~2.4GB/2.8GB, 86%) |
| gpt2-large | ~3.1GB | ⏳ 下载中 (~2.4GB/3.1GB, 77%) — MAUVE 依赖 |
| EleutherAI/pythia-6.9b | ~14GB | ⏳ 排队中（cache_all_models.sh 按序下载）|
| gpt2-medium | ~1.4GB | ⏳ 排队中 |
| facebook/opt-350m | ~700MB | ⏳ 排队中 |

**后台进程：**
- PID 4100: `cache_all_models.sh` — 自动按序缓存 5 个模型
- PID 6113: dryrun 进程（等待 gpt2-large 完成后继续）

### 7. 与 westd-19828 对比

| 对比项 | westd-19828 | westd-17855 |
|--------|------------|------------|
| GPU | 6× RTX PRO 6000 | 6× RTX PRO 6000 |
| 代码 | ✅ 完整 | ✅ 已同步 |
| 数据 | ✅ 完整 | ✅ 完整 |
| 依赖 | ✅ | ✅ |
| 模型缓存 | ✅ 完整 | ⏳ pythia-410m 完成，其余下载中 |
| HF Mirror | ✅ | ✅ (hf-mirror.com) |

### 注意事项
1. 模型下载正在后台自动进行，无需干预。pythia-6.9b (~14GB) 将在当前下载完成后开始，预计总计还需 ~30-40 分钟。
2. gpt2-large 不在用户指定的缓存列表中，但被 MAUVE 指标自动依赖。已在 dryrun 过程中触发下载。
3. 环境变量 `HF_ENDPOINT=https://hf-mirror.com` 和 `HF_HOME=/root/autodl-tmp/.hf_cache` 已配置在 `.bashrc` 中。

---
