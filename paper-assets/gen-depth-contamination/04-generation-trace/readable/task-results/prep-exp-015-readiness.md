# prep exp 015 readiness

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_exp-015-readiness_20260515T043726_result.json`
- **Structured JSON:** [`e2785a29ebd6b35e08c5.json`](../../sessions/e2/e2785a29ebd6b35e08c5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有检查完成。以下是就绪状态报告：

---

## exp-015 Neural Probe 重跑就绪状态报告

### ✅ 就绪项

| 项目 | 状态 |
|------|------|
| **脚本** | `scripts/run_exp015_neural_probe.py` v2 存在（May 14 更新，550 行） |
| **Bootstrap CI** | `bootstrap_auc_ci()` L188，doc-level resampling，默认 1000 次 |
| **Permutation test** | `permutation_test_auc()` L231，默认 500 次 |
| **Per-fold VRAM logging** | `torch.cuda.max_memory_allocated()` 在每个 fold 循环内（L282-284） |
| **OOM batch adaptation** | `extract_embeddings()` 自动减半 batch_size |
| **内存优化** | Phase 2 提取所有 embedding → free LLM → Phase 3 训练 MLP |
| **数据 Pythia** | `data_exp001_pythia/` — 6 depth files + features.csv (~37MB) |
| **数据 OLMo** | `data_exp002_olmo/` — 6 depth files + features.csv (~42MB) |
| **数据 Qwen-cont** | `data_exp017_qwen_cont/` — 6 depth files + features.csv (~44MB) |
| **模型缓存** | Qwen2.5-1.5B-Instruct 已缓存（`model.safetensors` 等完整文件在默认路径） |
| **依赖** | torch=2.10.0+cu128, transformers=4.57.6, sklearn=1.8.0, cuda=True |
| **GPU** | RTX 4090D 24GB，独占后足够（Qwen-cont 单跑 ~9GB） |
| **输出路径** | 无冲突（已有的 `exp015_neural_probe_results.json` 是旧 v1 单数据集结果，会被覆盖） |

### ⚠️ 注意项

1. **现有结果文件是 v1 旧版**：`exp015_neural_probe_results.json` 仅含 Qwen-cont 单数据集，无 bootstrap CI / permutation test / VRAM logging。重跑会覆盖。
2. **脚本默认只跑 Qwen-cont**：`--data_dir` 和 `--label` 默认值只有 Qwen-cont 一个数据集，需要命令行显式指定 3 个。
3. **GPU 当前被占**：exp-006 正在使用 ~15GB 显存（15183/24564 MiB），需等其完成释放。

### ❌ 缺失项

无。所有必要组件就绪。

### 推荐启动命令

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
cd /root/autodl-tmp/gen-depth-contamination && \
python scripts/run_exp015_neural_probe.py \
  --data_dir \
    /root/autodl-tmp/gen-depth-contamination/data_exp001_pythia \
    /root/autodl-tmp/gen-depth-contamination/data_exp002_olmo \
    /root/autodl-tmp/gen-depth-contamination/data_exp017_qwen_cont \
  --label Pythia OLMo Qwen-cont \
  --output /root/autodl-tmp/gen-depth-contamination/artifacts/exp015_neural_probe_results.json \
  --embed_batch_size 16 \
  --bootstrap_resamples 1000 \
  --permutation_resamples 500
```

模型会为 3 个数据集依次提取 embedding，然后释放 LLM 显存，再训练 3 个 MLP probe。预计总耗时 30-60 分钟，峰值显存 ~9-10GB（独占 24GB 无压力）。

---
