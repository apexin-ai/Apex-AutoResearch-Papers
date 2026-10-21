# prep eval script verify cqa1

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_eval_script_verify_cqa1_20260518T190331_result.json`
- **Structured JSON:** [`7b02295d0dde627b979d.json`](../../sessions/7b/7b02295d0dde627b979d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

### 1. Eval 脚本版本：**修复版** (offset-based ACIS hook)

确认点：
- Line 227: `state = {"offset": 0}` ✓
- Lines 234-238: `offset = state["offset"]` → `cam_mask = mask[:, offset:offset + n]` → `state["offset"] = offset + n` ✓
- Line 231: 只有 `if tokens.dim() != 3:` 的基本检查，没有旧版 `tokens.shape[1] != mask.shape[1]: return output` 的跳过逻辑 ✓

### 2. Checkpoint 路径格式

| 训练 | output_dir | 目录结构 |
|------|-----------|---------|
| baseline_control | `checkpoints/baseline_control/` | `step_{N:06d}/checkpoint.pt` + `latest/checkpoint.pt`（当前到 step_080000） |
| smart_compress_m96_seed43 | `checkpoints/smart_compress_m96_seed43/` | 单个滚动 `checkpoint.pt`（无 step 子目录） |

### 3. Eval 命令

**baseline_control_100k_v2 (cqa1:0)**:
```bash
cd /root/autodl-tmp/importance_margin_vla_compress && \
CUDA_VISIBLE_DEVICES=0 python eval_success_rate_libero.py \
    --checkpoint checkpoints/baseline_control/latest/checkpoint.pt \
    --config configs/baseline_control.yaml \
    --suite libero_object \
    --num_episodes 50 \
    --gpu 0 \
    --seed 42 \
    --mode baseline \
    --output eval_results/eval_baseline_control_100k_v2.json
```

**smart_compress_m96_seed43 (cqa1:2)**:
```bash
cd /root/autodl-tmp/importance_margin_vla_compress && \
CUDA_VISIBLE_DEVICES=2 python eval_success_rate_libero.py \
    --checkpoint checkpoints/smart_compress_m96_seed43/checkpoint.pt \
    --config configs/smart_compress_m96_seed43.yaml \
    --suite libero_object \
    --num_episodes 50 \
    --gpu 0 \
    --seed 42 \
    --mode baseline \
    --output eval_results/eval_smart_compress_m96_seed43.json
```

注意：`CUDA_VISIBLE_DEVICES=N` 后 `--gpu 0` 是正确的——进程视角下可见 GPU 编号为 0。

### 4. 备注

- baseline_control 的 `save_every=10000`，训练完成后最终 checkpoint 同时在 `step_100000/checkpoint.pt` 和 `latest/checkpoint.pt`
- smart_compress_m96_seed43 的 base config `save_every=1000`，但实际只保留滚动 `checkpoint.pt`（同 m96 seed42 模式），训练完成后直接用根目录的 `checkpoint.pt`
- 两个 eval 各跑 50 eps × 10 tasks = 500 episodes，libero_object max_steps=280

---
