# code dcol roberta v6 prep

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_dcol_roberta_v6_prep_20260515T040134_result.json`
- **Structured JSON:** [`0e820bb20de4a3defd75.json`](../../sessions/0e/0e820bb20de4a3defd75.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

DCOL v6 准备完毕。汇报：

## DCOL v6 准备完成

### C001/C002 满足
已查阅 registry 中 dcol_deberta_001~005 全部 5 次失败记录，确认 v6 spec 不重复任何已知错误。

### 代码变更（`src/dcol_trainer_v6.py`）
基于 `dcol_trainer.py` 修改：
1. **模型**: RoBERTa-large（默认 `roberta-large`）
2. **LoRA target_modules**: `["query", "value"]`（RoBERTa 层名，非 DeBERTa 的 `query_proj/key_proj/value_proj`）
3. **lr**: 5e-5（v5 的 3e-4 的 1/6）
4. **lora_alpha**: 16（v5 一致）
5. **warmup_ratio**: 0.05
6. **新增 --bf16**: bf16 混合精度（`torch.amp.autocast`）
7. **新增 --max_grad_norm**: 梯度裁剪（默认 1.0）
8. **新增 NaN guard**: `NaNLossError` 异常，检测到 NaN/Inf 立即终止并写 results.json
9. **新增 Collapse guard**: step 500 时 acc<30% 触发 `CollapseGuardError` 终止
10. **新增 --max_steps**: 控制训练步数（dry-run 用）
11. **global_step 追踪**: 跨 epoch 全局步数计数

### Dry-run 结果
- 5 步训练成功，**无 NaN**
- 参数：357,250,291 总 / 1,890,547 可训练（0.53%）
- 数据集：180,000 条（比 v5 的 125k 更大）
- max_steps 停止正确触发

### 模型路径
`/root/autodl-tmp/models/roberta-large-ms/AI-ModelScope/roberta-large`

### 完整训练命令（等审批）
```bash
CUDA_VISIBLE_DEVICES=1 python3 src/dcol_trainer_v6.py \
  --data_dir data/ \
  --model_path /root/autodl-tmp/models/roberta-large-ms/AI-ModelScope/roberta-large \
  --features_path data/features_all.jsonl \
  --output_dir checkpoints/dcol_roberta_v6/ \
  --batch_size 32 --epochs 10 --lr 5e-5 --margin_lr 1e-4 \
  --use_lora --lora_r 16 --lora_alpha 16 \
  --seed 42 --bf16 --max_grad_norm 1.0 --gpu 0
```

**未提交训练**，等 Main Agent 审批。

---
