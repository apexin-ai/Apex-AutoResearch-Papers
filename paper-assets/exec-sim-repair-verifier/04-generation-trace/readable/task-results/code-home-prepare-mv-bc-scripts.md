# code home prepare mv bc scripts

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_home-prepare-mv-bc-scripts_20260512T082727_result.json`
- **Structured JSON:** [`f2f55d380514a3b635cc.json`](../../sessions/f2/f2f55d380514a3b635cc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个脚本 dry-run 通过。

**环境确认：**
- Python 3.10.12, torch 2.10.0+cu128, peft 0.19.1
- Base model: `Qwen/Qwen3-4B`（HF cache 中可用）
- Checkpoint: `/home/sonny/exec-sim-repair-verifier/checkpoints/best/`（LoRA r=16, alpha=32）
- 数据: `/home/sonny/exec-sim-repair-verifier/data/test.jsonl`

**Dry-run 结果：** 两个脚本 `--help` 均正常输出，无 import 错误。

**预备提交命令（等 seed456/789/0 完成后执行）：**

```bash
# majority-voting (~3h)
cd /home/sonny/exec-sim-repair-verifier
nohup python3 eval_majority_voting.py \
  --base_model_path Qwen/Qwen3-4B \
  --checkpoint_path checkpoints/best \
  --data_dir data/ \
  --output eval_majority_voting.json \
  --K 3 --temperature 0.7 --gpu 0 \
  > logs/majority_voting.log 2>&1 &

# block-correlation (~1h)
nohup python3 eval_block_correlation.py \
  --base_model_path Qwen/Qwen3-4B \
  --checkpoint_path checkpoints/best \
  --data_dir data/ \
  --output eval_block_correlation.json \
  --gpu 0 \
  > logs/block_correlation.log 2>&1 &
```

注意：两个脚本都用 GPU 0，不能同时跑（模型约 8GB 显存）。建议先跑 block-correlation（~1h），再跑 majority-voting（~3h）。

---
