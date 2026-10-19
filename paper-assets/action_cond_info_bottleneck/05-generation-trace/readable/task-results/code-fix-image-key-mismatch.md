# code fix image key mismatch

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix_image_key_mismatch_20260515T223351_result.json`
- **Structured JSON:** [`077103c352166c29d4b6.json`](../../sessions/07/077103c352166c29d4b6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务完成。总结：

## 改动列表

### `/root/acib/scripts/train_acib.py`

1. **L31** — 添加 `HF_HUB_OFFLINE=1` 环境变量，避免联网卡住

2. **L51-80** — 新增 `IMAGE_KEY_MAP`、`remap_image_keys()`、`tokenize_batch()` 三个组件：
   - `IMAGE_KEY_MAP`: 映射 `observation.images.image` → `camera1`, `image2` → `camera2`
   - `remap_image_keys()`: 在 batch dict 中重命名 key
   - `tokenize_batch()`: 用 SmolVLM2 tokenizer 将 `task` 文本转为 `observation.language.tokens` + `attention_mask`（bool 类型）

3. **L160-177** — 重写 `build_dataloader()`：
   - 读取数据集 fps，自动计算 `delta_timestamps` 生成 50 步 action chunks
   - 修复旧版缺少 `--data_root` 传递和无 action chunks 的问题

4. **L205-207** — `train()` 中策略构建后提取 tokenizer

5. **L244-248** — 训练循环中添加 batch 预处理流水线：`remap_image_keys` → `tokenize_batch` → `to(device)`

6. **L278-294** — 修复 logging 中的 loss_dict key（`"total"` → `total_loss.item()`，`"task"` → `loss_dict.get("loss", 0)`，`"consistency"` → `"acib_consistency"`，`"ib"` → `"acib_ib"`）

## Dry-run 结果

```
Step 1/5 | loss=0.1089 task=0.0964 ib=0.7916 β=0.0000 | 0.4 steps/s
Step 2/5 | loss=1.3536 task=1.3451 ib=0.8577 β=0.0000 | 0.7 steps/s
Step 3/5 | loss=1.9895 task=1.9821 ib=0.5655 β=0.0000 | 0.9 steps/s
Step 4/5 | loss=1.0051 task=1.0017 ib=0.6973 β=0.0000 | 1.0 steps/s
Step 5/5 | loss=4.9914 task=4.9886 ib=0.6490 β=0.0000 | 1.1 steps/s
Training complete: 5 steps in 0.0h
```

Loss 值正常（非 NaN/Inf），β=0 因在 warmup 阶段。~1.1 steps/s on batch_size=2。

## 补充说明
- 模型 config 注册了 camera3 但 `empty_cameras=0`，原始训练也不用 camera3（`train_config.json` 的 `rename_map` 只映射 2 个相机）
- 数据集 state dim=8 vs 模型 config state dim=6，`prepare_state` 只做 padding 不截断，不影响 forward 但正式训练前需确认
- 当前未加 state/action 的 MEAN_STD normalization（原始训练有 normalizer preprocessor），正式训练需要补上

---
