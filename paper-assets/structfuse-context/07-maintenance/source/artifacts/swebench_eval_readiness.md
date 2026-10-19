# SWE-bench Lite 评估 Pipeline 就绪度报告

**日期**: 2026-05-14
**服务器**: bjb1-42106 (2× NVIDIA RTX PRO 6000 Blackwell, 98GB VRAM each)

---

## 检查项状态

| # | 检查项 | 状态 | 详情 |
|---|--------|------|------|
| 1 | SWE-bench 数据 | ✅ 通过 | Arrow 格式，dev=23, test=300 instances |
| 2 | HF 缓存 | ✅ 通过 | `load_dataset("princeton-nlp/SWE-bench_Lite")` 已缓存，无需网络 |
| 3 | 预 clone repos | ✅ 通过 | 12/12 repos 已 clone (~1.7GB 总计) |
| 4 | 评估脚本 | ✅ 通过 | `evaluation/eval_swebench.py` (20KB, ~550 行) |
| 5 | 训练模块依赖 | ✅ 通过 | `training/contrastive_model.py` 存在，脚本通过 sys.path 动态导入 |
| 6 | Python 依赖 | ✅ 通过 | torch, transformers, datasets, numpy, tqdm, peft, accelerate 均已安装 |
| 7 | 基座模型 | ✅ 通过 | Qwen2.5-Coder-3B 在 `/root/autodl-tmp/structfuse/models/Qwen/Qwen2.5-Coder-3B/` |
| 8 | Checkpoint (random_s42) | ✅ 通过 | `best_by_val_loss` + `best_by_recall_at_1` 均有 model.pt + tokenizer + config |
| 9 | Checkpoint (dataflow_aware_s42) | ⏳ 待训练 | 目前不存在，需等 M2 训练产出 |
| 10 | 磁盘空间 | ✅ 通过 | 90GB 可用 (250GB 总计, 65% 已用) |
| 11 | GPU | ✅ 通过 | 2× RTX PRO 6000 Blackwell (98GB) |

---

## Checkpoint 详情

**已有 (random_s42)**:
- 路径: `/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42/`
- 大小: 12GB (含 best_by_val_loss + best_by_recall_at_1)
- 配置: Qwen2.5-Coder-3B + LoRA (r=16), proj_dim=256, max_seq_length=2048

**待产出 (dataflow_aware_s42)**:
- 预期路径: `/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/dataflow_aware_s42/`
- 需要 `best_by_recall_at_1/model.pt` + `training_config.json`

---

## 评估命令模板

```bash
# 激活环境
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base

# 评估 random_s42 baseline (可立即执行)
cd /root/structfuse-context && python evaluation/eval_swebench.py \
    --checkpoint-path /root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42/best_by_recall_at_1 \
    --output-dir /root/autodl-tmp/structfuse/eval_results/swebench_random_s42_recall \
    --repo-cache-dir /root/autodl-tmp/swebench/repos/ \
    --swebench-split lite \
    --batch-size 16 \
    --max-seq-length 2048 \
    --top-k 1,3,5,10,20

# 评估 dataflow_aware_s42 (M2 训练完成后)
cd /root/structfuse-context && python evaluation/eval_swebench.py \
    --checkpoint-path /root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/dataflow_aware_s42/best_by_recall_at_1 \
    --output-dir /root/autodl-tmp/structfuse/eval_results/swebench_dataflow_s42_recall \
    --repo-cache-dir /root/autodl-tmp/swebench/repos/ \
    --swebench-split lite \
    --batch-size 16 \
    --max-seq-length 2048 \
    --top-k 1,3,5,10,20

# Dry-run 验证 pipeline 逻辑 (不需要 GPU)
cd /root/structfuse-context && python evaluation/eval_swebench.py \
    --checkpoint-path mock --dry-run --num-instances 5
```

---

## 预估评估时间

- **数据规模**: 300 test instances
- **每个 instance**: clone/checkout repo → 收集 .py 文件 → 编码 query → 批量编码候选文件 → cosine 排序
- **模型**: Qwen2.5-Coder-3B (LoRA), 约 3B 参数
- **GPU**: RTX PRO 6000 Blackwell (98GB VRAM), 单 GPU 足够
- **瓶颈**: 候选文件编码 (大 repo 如 django 有数千 .py 文件)
- **预估**: 每个 instance ~30-60s (含 git checkout + 文件收集 + batch encoding), 总计 **2.5-5 小时**
- 使用 `--repo-cache-dir` 可跳过网络 clone，节省约 30% 时间

---

## 缺失项和建议

1. **dataflow_aware_s42 checkpoint**: 唯一缺失项，等 M2 训练完成即可。random_s42 可先跑作为 baseline
2. **建议先跑 dry-run**: 用 `--dry-run --num-instances 5` 验证完整 pipeline 逻辑无 bug
3. **磁盘监控**: 评估过程中 git checkout 会在 workspace 产生临时文件，90GB 余量充足
