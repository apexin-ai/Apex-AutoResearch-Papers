# eval repobench r prep

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_repobench_r_prep_20260516T074605_result.json`
- **Structured JSON:** [`122eb1ee0012d5166b13.json`](../../sessions/12/122eb1ee0012d5166b13.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run 成功。脚本正常工作，模型加载、数据加载、检索评估、bootstrap CI 全部通过。

---

## 总结

### 1. Eval 脚本审查

**路径**: `/root/structfuse/evaluation/eval_repobench.py`

- **输入**: RepoBench-R gzipped pickle 文件（python/java × cff/cfr）
- **Checkpoint**: 需要含 `model.pt` + `training_config.json` + tokenizer 文件的目录
- **输出**: R@1, R@5, R@10, MRR + 95% bootstrap CI + per-difficulty (easy/hard) 分解
- **已支持多 seed**: `--batch-mode` 可批量评估同一目录下所有 checkpoint，输出 summary 对比表
- **CI 已内置**: `--n-bootstrap 1000` 默认就有 95% CI

### 2. Checkpoint 可用性 ✓

所有需要的 `best_by_val_loss` 均存在：
- `random_s42`, `random_s43`, `random_s44`
- `embedding_distance_s43`, `embedding_distance_s44`
- 额外还有 `dataflow_aware_s43`, `dataflow_aware_s44`

路径: `/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/{name}/best_by_val_loss/`

### 3. GPU 可行性

| GPU | 已用 | 剩余 | 结论 |
|-----|------|------|------|
| cuda:0 | 81 GiB / 98 GiB | ~17 GiB | 可行但紧张（训练进程 3 个） |
| cuda:1 | 54 GiB / 98 GiB | **~44 GiB** | **充裕，推荐用 cuda:1** |

Qwen2.5-Coder-3B + LoRA 推理约 6-8 GiB，**可以在 cuda:1 上与现有训练并行**，无需等待。

### 4. RepoBench-R 数据 ✓

`/root/autodl-tmp/structfuse/data/repobench/data/` 下 4 个文件全部就绪：
- `python_cff.gz`, `python_cfr.gz`, `java_cff.gz`, `java_cfr.gz`

### 5. 完整执行命令

每个 checkpoint 单独运行（用 `--gpu 1`）：

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/structfuse

# random seeds
for seed in 42 43 44; do
  python evaluation/eval_repobench.py \
    --checkpoint-path /root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s${seed}/best_by_val_loss \
    --language both --split both --gpu 1 --n-bootstrap 1000 \
    --output /root/autodl-tmp/structfuse/eval_results/repobench_random_s${seed}.json
done

# embedding_distance seeds
for seed in 43 44; do
  python evaluation/eval_repobench.py \
    --checkpoint-path /root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/embedding_distance_s${seed}/best_by_val_loss \
    --language both --split both --gpu 1 --n-bootstrap 1000 \
    --output /root/autodl-tmp/structfuse/eval_results/repobench_embed_dist_s${seed}.json
done

# dataflow_aware seeds (bonus)
for seed in 43 44; do
  python evaluation/eval_repobench.py \
    --checkpoint-path /root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/dataflow_aware_s${seed}/best_by_val_loss \
    --language both --split both --gpu 1 --n-bootstrap 1000 \
    --output /root/autodl-tmp/structfuse/eval_results/repobench_dataflow_s${seed}.json
done
```

或用 batch-mode 一次性跑全部：
```bash
python evaluation/eval_repobench.py \
  --checkpoint-path /root/autodl-tmp/structfuse/checkpoints/m2_full_qwen \
  --batch-mode --language both --split both --gpu 1 --n-bootstrap 1000 \
  --output /root/autodl-tmp/structfuse/eval_results/repobench_all.json
```

⚠️ **注意**: `--batch-mode` 的 `discover_checkpoints` 只搜一级子目录，而实际结构是二级（`random_s42/best_by_val_loss/`），所以需要逐个 checkpoint 跑或修改 discover 逻辑。

### 6. 缺失/需修改清单

| 项目 | 状态 |
|------|------|
| eval 脚本 | ✓ 就绪 |
| RepoBench 数据 | ✓ 就绪 |
| Checkpoint | ✓ 全部就绪 |
| 多 seed CI 报告 | ✓ 单 checkpoint 内 bootstrap CI 已支持；**跨 seed 聚合需手动计算 mean±std** |
| `--batch-mode` discover 深度 | ⚠️ 只搜一级目录，对 `best_by_val_loss` 二级结构无效——需逐个指定路径 |
| GPU 并行可行性 | ✓ cuda:1 有 44 GiB 空余，可立即并行 |
| 依赖 | ✓ 无额外依赖（dry-run 已验证） |

**结论：可以立即在 cuda:1 上启动 RepoBench-R 评估，无需等训练完成。**

---
