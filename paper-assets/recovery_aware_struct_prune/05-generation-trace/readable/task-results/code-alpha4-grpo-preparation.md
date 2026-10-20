# code alpha4 grpo preparation

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_alpha4_grpo_preparation_20260521T155844_result.json`
- **Structured JSON:** [`47d29887a7e664c861ec.json`](../../sessions/47/47d29887a7e664c861ec.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有输入文件确认存在。总结如下：

---

**⚠️ 模型修正**: 服务器上没有 Qwen2.5-7B-Instruct，实际模型是 `/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B`。脚本已用正确路径。

**Pipeline 脚本**: `westd-29022:/root/recovery_aware_struct_prune/scripts/run_alpha4_pipeline.sh`

**启动命令**:
```bash
bash scripts/run_alpha4_pipeline.sh 0   # 在 GPU 0 上运行
```

**4 步流水线**:

| Step | 操作 | 预估时间 | GPU |
|------|------|---------|-----|
| 1 | Prune (α=4.0, 20%) | ~5-10 min | 1×GPU |
| 2 | SFT warmup (2 epochs, lr=2e-5, bs=1, grad_accum=8) | ~30-45 min | 1×GPU |
| 3 | GRPO 100 steps (v5: dapo, β=0.01, temp=0.4, adamw_8bit) | ~2-3 hrs | 1×GPU |
| 4 | GSM8K eval (N=1319, greedy) | ~20-30 min | 1×GPU |

**总预估时间**: ~3.5-4.5 小时，1 张 GPU

**无需修改现有代码** — α 参数已在 `prune.py` 中支持，GRPO v5 的 `--max_steps` 参数也已就绪。

**所有输入路径已验证存在**:
- 模型: `/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B` ✓
- Importance scores: `results/importance_scores.pt` ✓
- CKA scores: `results/cka_scores.pt` ✓

**输出路径** (均在数据盘 `/root/autodl-tmp/`):
- Pruned: `pruned_alpha4_20/`
- SFT: `sft_alpha4_20/`
- GRPO: `grpo_alpha4_20/`
- Eval: `results/eval_grpo_alpha4_20.json`

脚本内置了每步的 skip 逻辑（检测已有输出），可安全中断后重跑。

---
