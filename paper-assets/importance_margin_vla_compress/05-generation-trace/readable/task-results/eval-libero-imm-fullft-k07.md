# eval libero imm fullft k07

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_libero_imm_fullft_k07_20260517T015417_result.json`
- **Structured JSON:** [`fe3af5da762a03f4fb5b.json`](../../sessions/fe/fe3af5da762a03f4fb5b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

**已完成：**
1. **Checkpoint 传输** — cqa1 → westd rsync 成功（879MB，通过 key-based SSH）
2. **Config 创建** — `configs/libero_imm_twostage_fullft_k07.yaml`（k_ratio=0.7, Full FT, lora.rank=0）
3. **Eval 启动** — `eval_imm_k07_object` 在 westd GPU 0 上运行中
   - Mode: `acis_prune`
   - Suite: `libero_object`（10 tasks × 50 episodes = 500 total）
   - 已开始执行 episodes

**预估耗时：** ~40-50 分钟（每 episode ~5s × 500）

**监控命令：**
```
tail -f ~/runs/importance_margin_vla_compress/eval_imm_k07_object.log
```

结果将写入 `eval_results/eval_imm_k07_object_acis_prune.json`。完成后我会更新 registry metrics。

---
