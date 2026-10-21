# ssh modify prune and prepare floor ablation

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_modify_prune_and_prepare_floor_ablation_20260523T060311_result.json`
- **Structured JSON:** [`9a20eed8ed802ba70093.json`](../../sessions/9a/9a20eed8ed802ba70093.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

### 任务 1：prune.py 修改 ✅
- **Line 170**: 添加 `--floor_ratio` 参数（default=0.4）
- **Line 285**: `n_mlp_groups * 0.4` → `n_mlp_groups * args.floor_ratio`
- **Line 309**: `intermediate_size * 0.4` → `intermediate_size * args.floor_ratio`
- **Line 453**: metadata 中记录 `floor_ratio`
- `--help` 输出已验证

### 任务 2：7B 模型路径 ✅
`/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B`

### 任务 3：CKA-only 所需参数 ✅
- `--cka_path results/cka_scores.pt`（不需要 `--importance_path`）
- 不需要 `--alpha`

### 任务 5：Pipeline 脚本 ✅
`scripts/run_floor_ablation.sh` — 通用脚本，接受 floor_ratio 和 gpu_id 参数。

**3 个 floor 值的调用命令**：
```bash
# floor=0.3 (GPU 0)
nohup bash scripts/run_floor_ablation.sh 0.3 0 > /root/autodl-tmp/recovery_aware_struct_prune/logs/floor_0.3.out 2>&1 &

# floor=0.5 (GPU 0)
nohup bash scripts/run_floor_ablation.sh 0.5 0 > /root/autodl-tmp/recovery_aware_struct_prune/logs/floor_0.5.out 2>&1 &

# floor=0.6 (GPU 0)
nohup bash scripts/run_floor_ablation.sh 0.6 0 > /root/autodl-tmp/recovery_aware_struct_prune/logs/floor_0.6.out 2>&1 &
```

每个 pipeline 串行执行 4 步（Prune → SFT 2ep → GRPO 100步 → GSM8K eval），每步有 SKIP 机制支持断点续跑。

---
