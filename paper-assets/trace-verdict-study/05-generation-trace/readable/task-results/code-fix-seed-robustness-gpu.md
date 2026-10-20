# code fix seed robustness gpu

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix_seed_robustness_gpu_20260515T124609_result.json`
- **Structured JSON:** [`1452bf6a8b83e6630802.json`](../../sessions/14/1452bf6a8b83e6630802.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修复完成。改动摘要：

1. **CVD 隔离**：训练/评估前 `export CUDA_VISIBLE_DEVICES=$GPU`，命令内部统一 `--gpu 0`（CVD 后只见一张卡）
2. **GPU 可用性检查**：启动时查 `nvidia-smi --id=$GPU` 已用显存，> 1000 MiB 则报错退出
3. **默认值改为 1**：`GPU=1`，避免默认撞 cuda:0
4. **顶部注释**：说明 GPU 参数须与 registry 分配一致
5. **aggregate_seeds.py**：无 GPU 硬编码，无需修改

---
