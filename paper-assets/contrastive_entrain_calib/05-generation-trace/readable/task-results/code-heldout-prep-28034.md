# code heldout prep 28034

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_heldout-prep-28034_20260523T035439_result.json`
- **Structured JSON:** [`94c655cbfbd388eaae69.json`](../../sessions/94/94c655cbfbd388eaae69.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部就绪。验证结果：

| 项目 | 状态 |
|------|------|
| 训练脚本 `run_exp004_heldout.py` | ✅ 已写入 28034 |
| `train_split.jsonl` | ✅ 292 行 |
| `eval_split.jsonl` | ✅ 70 行（从 29046 SCP 过来） |
| 合计 | 362 行 = calibration_v2_1_expanded 总量 ✓ |
| 模型 Qwen3-8B | ✅ `/root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B/` |
| 输出目录 | ✅ `/root/contrastive_entrain_calib/outputs/exp004_heldout/` 已创建可写 |
| GPU 设置 | ✅ `CUDA_VISIBLE_DEVICES="1"` (line 11) |
| 超参 | ✅ seed=42, r=64, alpha=128, 7 modules, lr=5e-5, warmup=200, 8000 steps, grad_accum=16, λ_l2=0.1, save_steps=500 |

**脚本修改点（相对 29046 原版）：**
- 添加 `os.environ["CUDA_VISIBLE_DEVICES"] = "1"` (line 11，在 `import torch` 之前)
- `--output-dir` 默认值从 `/root/autodl-tmp/...` 改为 `/root/contrastive_entrain_calib/outputs/exp004_heldout/`
- `device = torch.device("cuda:0")` 保持不变（CUDA_VISIBLE_DEVICES=1 会将物理 GPU 1 映射为进程内的 cuda:0）

---
