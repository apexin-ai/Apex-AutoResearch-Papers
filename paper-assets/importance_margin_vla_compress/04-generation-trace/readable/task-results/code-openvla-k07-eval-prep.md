# code openvla k07 eval prep

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_openvla_k07_eval_prep_20260517T212735_result.json`
- **Structured JSON:** [`bc03f86637d63dd155e3.json`](../../sessions/bc/bc03f86637d63dd155e3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

### Dry-run 验证通过

- 模型加载正常（GPU 15.1GB）
- Pruning hook 正确：**256 → 179 vision tokens** (`int(256 * 0.7) = 179`)
- Task 1 完成无报错，Task 2 正常启动
- 输出文件自动命名为 `openvla_random_prune_k07_object.json`

### k=0.7 全量启动命令

k=0.5 完成后在 GPU 0 执行：

```bash
cd /root/autodl-tmp/importance_margin_vla_compress && \
source /root/miniconda3/bin/activate && \
nohup python -u eval_openvla_libero.py \
    --mode random_prune \
    --k_ratio 0.7 \
    --suite libero_object \
    --num_episodes 50 \
    --seed 7 \
    > eval_results/openvla_random_prune_k07_object.log 2>&1 &
```

脚本已硬编码 `CUDA_VISIBLE_DEVICES="0"`，无需额外指定 GPU。

### 当前 k=0.5 进度

Task 5/10，约 50% 完成，预计还需 ~2.5 小时（按 1.9 eps/min）。

---
