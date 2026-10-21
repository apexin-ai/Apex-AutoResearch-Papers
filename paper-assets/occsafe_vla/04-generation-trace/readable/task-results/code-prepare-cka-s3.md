# code prepare cka s3

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prepare_cka_s3_20260525T120823_result.json`
- **Structured JSON:** [`c0c6261436bbd0cdc4bd.json`](../../sessions/c0/c0c6261436bbd0cdc4bd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部就绪。汇总：

### s3 训练配置确认
- **pretrained**: `/root/autodl-tmp/models/openvla-7b`（从头训练，非 resume）✓
- **occ_detach**: true ✓
- **occ_norm_type**: bn（finetune.py 默认值）✓
- **seed**: 由 `run_occ_detach.sh` 第一参数传入，run name "s3" 对应 seed 45

### s3 训练进度
- 当前 **~2962/50005 步**（~5.9%），速度 ~1.07 it/s
- 剩余 ~47043 步 → **~12.2 小时**
- 50K checkpoint 预计 **5月26日 ~08:15** 完成
- 10K checkpoint 尚未生成（首个 checkpoint 在 step 2500 或 10000）

### CKA 脚本修改
- 在 `cka_analysis.py:216` 插入了 summary 计算块
- JSON 现在输出格式：per-layer CKA 值 + `"summary"` 字段（含每个 condition 的 dinov2_mean/min_cka, siglip_mean/min_cka）
- `--help` dry-run 通过，参数解析正常

### run_command.sh
已保存到 `/root/autodl-tmp/analysis/cka_s3_verification/run_command.sh`，自动检测 50K checkpoint 路径，使用 `CUDA_VISIBLE_DEVICES=3`。50K checkpoint 就绪后直接执行：
```bash
bash /root/autodl-tmp/analysis/cka_s3_verification/run_command.sh
```

---
