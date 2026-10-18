# diagnose train openvla sc m64 seed42 v4

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_train_openvla_sc_m64_seed42_v4_20260521T080939_result.json`
- **Structured JSON:** [`238f5bd0bafa9af94ebc.json`](../../sessions/23/238f5bd0bafa9af94ebc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全貌清楚了。现在整理完整的诊断报告。

## 诊断结果

**磁盘：`/dev/md0` 250GB，清理前 100% 满（204KB 可用），清理后 93%（19GB 可用）**

### 空间占用排行

| 路径 | 大小 | 说明 |
|------|------|------|
| `checkpoints/openvla_sc_m128` | 38GB | M128 实验 checkpoint（2个×19GB） |
| `checkpoints/openvla_sc_m96_seed42` | 38GB | M96 实验 checkpoint（2个×19GB） |
| `.hf_cache/datasets/parquet/` | 66GB | 2份33GB parquet cache（可能重复） |
| `.hf_cache/lerobot/hub/` | 33GB | LIBERO 数据集 cache（训练使用） |
| `openvla-libero-object` | 15GB | **M64 训练需要的 base model，不能删** |
| `openvla-oft-libero-object` | 15GB | OFT 版模型（其他实验用） |
| `models/` | 12GB | RoboFlamingo/CLIP/xvla 模型 |
| `miniconda3` (root分区) | 12GB | conda 环境 |
| `pi05_libero_finetuned` | 7GB | Pi0.5 微调模型 |
| `libero_data` | 7GB | LIBERO 数据 |

### 已清理

| 项目 | 大小 | 状态 |
|------|------|------|
| `checkpoints/openvla_sc_m64_seed42/` | **19GB** | 已删除（v4崩溃的checkpoint） |
| `checkpoints/openvla_vtc_m128_seed42/` | 0 | 已删除（空目录） |
| `__pycache__` | ~152KB | 已删除 |

### 核心问题

**每个 checkpoint 是 19GB，不是预期的 500MB-1GB。** 原因是 `save_checkpoint()` 保存了完整 `model.state_dict()`（整个 OpenVLA 7B ~14GB），而实际只有 VTC compressor 是 trainable 的。冻结的 7B 参数每次都被重复保存。

100K steps 每 10K 保存 = 10 个 step checkpoint + 1 个 latest = 11 × 19GB = **209GB**。即使清空全盘也放不下。

```json
{"root_cause":"save_checkpoint saves full 7B model.state_dict() (14GB) + optimizer for every checkpoint, but only VTC compressor (~400M params) is trainable. Each ckpt = 19GB instead of expected <1GB. 250GB disk was 100% full with 94GB checkpoints + 100GB HF cache + 30GB models.","freed_gb":19,"available_gb_after":19,"safe_to_restart":false,"recommendations":["【必须】修改 save_checkpoint：step checkpoint 只保存 compressor.state_dict()（~500MB），不保存完整 model.state_dict()；仅 checkpoint.pt (latest) 保存完整状态用于 resume","【建议】删除 M128+M96 checkpoints（76GB）如果实验已完成评估","【建议】检查 .hf_cache/datasets/parquet/ 两份33GB cache 是否重复，删一份可释放33GB","【建议】添加 max_keep_ckpt=3 参数，自动删除旧 step checkpoint","【可选】openvla-oft-libero-object（15GB）和 models/OpenFlamingo（6.4GB）如不再使用可删除"]}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "root_cause": "save_checkpoint saves full 7B model.state_dict() (14GB) + optimizer for every checkpoint, but only VTC compressor (~400M params) is trainable. Each ckpt = 19GB instead of expected <1GB. 250GB disk was 100% full with 94GB checkpoints + 100GB HF cache + 30GB models.",
    "freed_gb": 19,
    "available_gb_after": 19,
    "safe_to_restart": false,
    "recommendations": [
      "【必须】修改 save_checkpoint：step checkpoint 只保存 compressor.state_dict()（~500MB），不保存完整 model.state_dict()；仅 checkpoint.pt (latest) 保存完整状态用于 resume",
      "【建议】删除 M128+M96 checkpoints（76GB）如果实验已完成评估",
      "【建议】检查 .hf_cache/datasets/parquet/ 两份33GB cache 是否重复，删一份可释放33GB",
      "【建议】添加 max_keep_ckpt=3 参数，自动删除旧 step checkpoint",
      "【可选】openvla-oft-libero-object（15GB）和 models/OpenFlamingo（6.4GB）如不再使用可删除"
    ]
  }
}
```

</details>

---
