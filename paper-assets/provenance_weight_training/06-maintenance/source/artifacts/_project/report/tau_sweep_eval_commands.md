# τ Sweep Post-Hoc Eval 命令

**生成时间**: 2026-05-15T15:00 UTC
**状态**: 预验证通过，等待训练完成后执行

## 1. eval_perplexity.py 验证状态

| 项目 | 状态 |
|------|------|
| 脚本存在 | ✅ `/root/provenance_weight_training/eval_perplexity.py` |
| 依赖 (torch, transformers) | ✅ 已在 conda base 环境预装（tau_06 eval 已成功执行过） |
| 评估数据 | ✅ `data/human/eval_holdout.jsonl` (67,823 行, 237MB) |
| `final/` 目录创建逻辑 | ✅ `pretrain_weighted.py:400` — 训练完成后保存到 `{output_dir}/final` |

## 2. Checkpoint 路径（实际磁盘路径）

⚠️ **注意**: 实际目录名与 registry exp_id 不完全一致，以磁盘路径为准。

| 实验 (registry) | 实际 output_dir | eval checkpoint 路径 | GPU |
|---|---|---|---|
| tau_05_seed42 | `output/models/tau_0.5_seed42` | `output/models/tau_0.5_seed42/final` | cuda:1 |
| tau_07_seed42 | `output/models/tau_0.7_seed42` | `output/models/tau_0.7_seed42/final` | cuda:0 |
| tau_09_seed42 | `output/models/tau_09_seed42` | `output/models/tau_09_seed42/final` | cuda:3 |
| tau_095_seed42 | `output/models/tau_095_seed42` | `output/models/tau_095_seed42/final` | cuda:2 |

**当前训练进度** (截至 ~15:00 UTC):
- tau_0.5: step 4500/6103 (~74%)
- tau_0.7: step 3000/6103 (~49%)
- tau_0.9: step 2500/6103 (~41%)
- tau_0.95: step 2000/6103 (~33%)

## 3. 完整 Eval 命令

### 方案 A: 一次性评估全部 4 个（推荐）

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
cd /root/provenance_weight_training && \
python eval_perplexity.py \
  --checkpoints \
    output/models/tau_0.5_seed42/final \
    output/models/tau_0.7_seed42/final \
    output/models/tau_09_seed42/final \
    output/models/tau_095_seed42/final \
  --data_path data/human/eval_holdout.jsonl \
  --max_docs 5000 \
  --max_length 2048 \
  --output_path output/eval/posthoc_eval_tau_sweep.json
```

**预计耗时**: ~7-12 分钟（每个 checkpoint ~100-180 秒）

### 方案 B: 逐个评估（如需分批）

```bash
# tau=0.5
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
cd /root/provenance_weight_training && \
python eval_perplexity.py \
  --checkpoints output/models/tau_0.5_seed42/final \
  --data_path data/human/eval_holdout.jsonl \
  --max_docs 5000 \
  --output_path output/eval/posthoc_eval_tau_05_seed42.json

# tau=0.7
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
cd /root/provenance_weight_training && \
python eval_perplexity.py \
  --checkpoints output/models/tau_0.7_seed42/final \
  --data_path data/human/eval_holdout.jsonl \
  --max_docs 5000 \
  --output_path output/eval/posthoc_eval_tau_07_seed42.json

# tau=0.9
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
cd /root/provenance_weight_training && \
python eval_perplexity.py \
  --checkpoints output/models/tau_09_seed42/final \
  --data_path data/human/eval_holdout.jsonl \
  --max_docs 5000 \
  --output_path output/eval/posthoc_eval_tau_09_seed42.json

# tau=0.95
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
cd /root/provenance_weight_training && \
python eval_perplexity.py \
  --checkpoints output/models/tau_095_seed42/final \
  --data_path data/human/eval_holdout.jsonl \
  --max_docs 5000 \
  --output_path output/eval/posthoc_eval_tau_095_seed42.json
```

## 4. 预期输出格式

JSON 文件，每个 checkpoint 一个 entry:

```json
{
  "tau_0.5_seed42/final": {
    "loss": 2.87xx,
    "perplexity": 17.xxx,
    "num_tokens": 4077068,
    "elapsed_seconds": 1xx.x,
    "checkpoint": "output/models/tau_0.5_seed42/final"
  },
  ...
}
```

**关键指标**: `perplexity` (eval_ppl_holdout)、`loss` (eval_loss)
**参考 baseline**: τ=0.8 (adaptive_fix_seed42) PPL=17.650, τ=0.6 PPL=17.681

## 5. 参数一致性校验

与已完成的 tau_06 eval 对比，确保参数一致:

| 参数 | tau_06 eval (已验证) | τ sweep eval |
|------|---------------------|--------------|
| data_path | `data/human/eval_holdout.jsonl` | ✅ 相同 |
| max_docs | 5000 (默认) | ✅ 相同 |
| max_length | 2048 (默认) | ✅ 相同 |
| 评估 tokens | 4,077,068 | 预期相同 |
| 精度 | fp16 (torch.amp.autocast) | ✅ 脚本内置 |

## 6. 潜在问题预警

1. **目录名不一致**: tau_05 和 tau_07 实际目录含点号（`tau_0.5_seed42`, `tau_0.7_seed42`），而 tau_09/tau_095 不含点号。eval 命令已使用实际磁盘路径，不受影响。

2. **训练未完成时无 `final/` 目录**: 当前只有中间 checkpoint。必须等训练完成、`final/` 目录创建后再运行 eval。可用 `ls output/models/tau_*/final/ 2>/dev/null` 快速检查。

3. **GPU 占用**: 训练完成后 GPU 显存释放，eval 只需 1 张 GPU (~1.5GB for Qwen3-0.6B)，不会冲突。

4. **eval 和训练不要同时跑在同一 GPU**: 如果部分训练还未完成，eval 会自动用 `.cuda()`，默认 cuda:0。可设 `CUDA_VISIBLE_DEVICES=X` 指定空闲 GPU。
