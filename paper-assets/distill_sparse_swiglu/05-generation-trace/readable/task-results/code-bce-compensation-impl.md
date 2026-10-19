# code bce compensation impl

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_bce_compensation_impl_20260515T171038_result.json`
- **Structured JSON:** [`796e44e17616cc645860.json`](../../sessions/79/796e44e17616cc645860.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

### 产出报告

**新增/修改文件：**
- `src/predictor.py` — 新增 `CompensationHead`、`CompensationNetwork` 类；`PredictorWrapper` 新增 `comp_network`/`use_compensation` 属性，patched forward 支持 compensation 推理
- `src/losses.py` — 新增 `CompensationLoss`（MSE on sparse+comp vs dense）
- `src/train.py` — 新增 `bce_comp` loss type、`train_bce_comp()` 函数、4 个 CLI 参数（`--predictor_checkpoint`, `--comp_mode`, `--comp_bottleneck`, `--comp_loss_weight`）
- `src/evaluate.py` — 新增 `--comp_checkpoint`/`--comp_bottleneck` 参数，自动检测主 checkpoint 中的 compensation 网络并报告 with/without compensation PPL

**Compensation Network 参数量（Llama 3.1 8B, bottleneck=256）：**
- 每层：2,101,504 params（4096→256→4096）
- 总计：67,248,128 params（32 layers）
- bf16 大小：128.3 MB

**Dry-run 结果：**
- Staged mode（冻结 predictor）：2 steps 通过，comp_loss 从 0.0081 降到 0.0075
- Joint mode（联合训练）：2 steps 通过，bce_loss + comp_loss 正常记录

**使用示例：**
```bash
# Staged: 冻结 BCE predictor，只训练 compensation
python src/train.py --loss_type bce_comp --comp_mode staged \
  --predictor_checkpoint checkpoints/mvp_bce_s42/predictor_bce.pt \
  --num_steps 500 --batch_size 4 --gpu 0

# Joint: 联合训练 predictor + compensation
python src/train.py --loss_type bce_comp --comp_mode joint \
  --num_steps 1000 --batch_size 4 --gpu 0

# 评估（自动检测 checkpoint 中的 compensation）
python src/evaluate.py --checkpoint checkpoints/predictor_bce_comp.pt --gpu 0
```

---
