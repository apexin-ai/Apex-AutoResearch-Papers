# code eval checkpoint full context

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_eval_checkpoint_full_context_20260517T081157_result.json`
- **Structured JSON:** [`114efc0060151ffea069.json`](../../sessions/11/114efc0060151ffea069.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 调研结论与产出

### 1. RAGEN eval 机制调研

**选择方案 B（独立脚本）**，原因：
- RAGEN 有 `ragen/eval.py` 独立入口，但它用 Hydra 绑定 `config_name=base`，默认 CoordSokoban 环境，覆盖为 ALFWorld 需要大量 Hydra overrides 且调试困难
- 已有 `scripts/eval_checkpoint.py` 提供了完整的 ALFWorld standalone eval 基础设施（FSDP 转换、env 初始化、action parsing、metrics 收集）
- 关键变化：将 single-turn + `HISTORY_LENGTH=5` 替换为 **multi-turn messages 匹配 RAGEN `context_window_mode=full`**

**Multi-turn 格式**（匹配 `ctx_manager._build_infer_multi_turn_messages`）：
- `system`: `"You're a helpful assistant. {env_instruction}"`
- `user`: `"\nTurn 1:\nState:\n{obs}\n..."` 
- `assistant`: model response
- `user`: `"Reward:\n{reward}\n\nTurn 2:\nState:\n..."` 
- ... 完整对话历史

### 2. 脚本

**路径**: `/root/cost-verify-agent-rl/scripts/eval_checkpoint_full_context.py` (379 行)

### 3. 验证结果

- 语法检查: OK
- `--help`: OK
- `--dry_run --run_dir`: 正确发现 exp029 的 3 个 checkpoint (step 5, 10, 15)
- `--dry_run --ckpt_path`: 正确解析单个 checkpoint

### 4. 使用说明

```bash
# 环境激活
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/cost-verify-agent-rl

# 单个 checkpoint（FSDP 自动转换）
python scripts/eval_checkpoint_full_context.py \
    --ckpt_path /root/autodl-tmp/checkpoints/hsweep-h2/global_step_10 \
    --num_episodes 32 --gpu 0

# 批量：一个 run 下所有 checkpoint
python scripts/eval_checkpoint_full_context.py \
    --run_dir /root/autodl-tmp/checkpoints/hsweep-h2/ \
    --num_episodes 32 --gpu 0

# 先预览发现了哪些 checkpoint
python scripts/eval_checkpoint_full_context.py \
    --run_dir /root/autodl-tmp/checkpoints/hsweep-h2/ --dry_run

# 输出在 /root/autodl-tmp/eval_results/full_context/
# 每个 checkpoint 一个 JSON + batch 汇总 JSON
```

### 5. 限制

- 必须在 base conda env 中运行（依赖 RAGEN、vllm、alfworld）
- FSDP → HF 转换需要 ~8GB CPU 内存和 ~30s
- 每个 checkpoint eval 后必须重新加载模型（不同权重）
- `max_model_len=20480` 匹配 hsweep 训练配置；若 full-context 对话超长，最旧的 turn 会被自动截断（`truncate_messages`）
- hsweep checkpoint 目录尚未创建（训练未开始），脚本已验证可正确处理 exp029 的现有 FSDP checkpoint

---
