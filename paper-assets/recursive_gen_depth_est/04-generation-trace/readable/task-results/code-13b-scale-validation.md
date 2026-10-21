# code 13b scale validation

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_13b_scale_validation_20260517T084540_result.json`
- **Structured JSON:** [`6543db205c48b5710c9a.json`](../../sessions/65/6543db205c48b5710c9a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

plan_014 已执行完毕。

**已完成：**
- `scripts/qwen25_14b_scale_validation.py` — 697 行全 pipeline 脚本（d0-d3 生成 → 19 特征自引用提取 → RF/LR 5-fold CV）
- `scripts/run_qwen25_14b_scale_validation.sh` — shell wrapper（环境设置 + 模型下载）
- Registry: `qwen25_14b_scale_001` 状态 RUNNING
- tmux session: `qwen25_14b_scale`

**运行参数：**
- Qwen2.5-14B FP16（无量化），cuda:0
- 5000 samples/depth × 4 depths (d0-d3)
- LoRA r=16, alpha=32, q/k/v_proj, 3 epochs, lr=2e-4, gradient_checkpointing
- 自引用特征提取（Qwen2.5-14B 计算自身生成文本的 surprisal）
- RF (n=200) + LR, 5-fold CV

**预计耗时：** 模型下载 ~30min + pipeline ~15-18h。日志：`logs/qwen25_14b_scale_validation.log`

---
