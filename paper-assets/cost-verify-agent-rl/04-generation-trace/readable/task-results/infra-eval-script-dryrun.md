# infra eval script dryrun

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_eval-script-dryrun_20260517T114413_result.json`
- **Structured JSON:** [`9de78551cfd8fae20f3d.json`](../../sessions/9d/9de78551cfd8fae20f3d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有信息收集完毕。

---

## 验证报告

### 1. Checkpoint 路径 + 文件列表

**路径**: `/root/autodl-tmp/checkpoints/hsweep-h2/`

| Checkpoint | 大小 | 状态 |
|---|---|---|
| `global_step_5/` | 21G | 完整 |
| `global_step_10/` | 21G | 完整 |

`latest_checkpointed_iteration.txt` 值为 `10`。

每个 checkpoint 结构一致（以 `global_step_5/actor/` 为例）：
- `model_world_size_2_rank_0.pt` (3.8G)
- `model_world_size_2_rank_1.pt` (3.8G)
- `optim_world_size_2_rank_0.pt` (6.4G)
- `optim_world_size_2_rank_1.pt` (6.4G)
- `extra_state_world_size_2_rank_0.pt`, `extra_state_world_size_2_rank_1.pt`
- `fsdp_config.json` → `{"FSDP_version": 1, "world_size": 2}`
- `huggingface/` → config.json + tokenizer 文件（无 safetensors）

模型：**Qwen3ForCausalLM**, hidden_size=2048, 28 layers, GQA (16 heads / 8 KV heads) ≈ 4B 参数。

### 2. Eval 脚本接口 + 输出格式

**脚本**: `/root/cost-verify-agent-rl/scripts/eval_checkpoint_full_context.py` ✅ 存在

**参数**:
| 参数 | 默认值 | 说明 |
|---|---|---|
| `--ckpt_path` | — | 单个 checkpoint 路径（与 `--run_dir` 互斥）|
| `--run_dir` | — | 批量模式，自动发现所有 `global_step_N` |
| `--num_episodes` | 32 | C003 硬限制 ≥16 |
| `--max_steps` | 50 | 每条 trajectory 最大步数 |
| `--temperature` | 0.4 | 采样温度 |
| `--output_dir` | `/root/autodl-tmp/eval_results/full_context/` | |
| `--gpu` | 0 | CUDA 设备号 |
| `--gpu_memory_utilization` | 0.35 | vLLM GPU 内存占比 |
| `--fsdp_convert_dir` | None | 自定义 FSDP→HF 转换输出目录 |
| `--dry_run` | False | 只发现 checkpoint 不执行 eval |

**输出格式**: JSON 文件，包含 `success_rate`, `action_is_valid_rate`, `action_is_effective_rate`, `format_ok_rate`, `avg_steps` 等。批量模式额外输出 batch summary JSON + stdout 表格。

**Full-context 模式**: ✅ 脚本构建完整多轮对话历史（所有 turn 的 state 累积），不做 step_independent 截断。

**FSDP 处理**: ✅ 内置 `convert_fsdp_to_hf()` 函数，自动检测 FSDP 格式并转换为 HF safetensors，然后用 vLLM 加载。已转换的会跳过。

### 3. 依赖状态

read-only 模式无法执行带分号的 python import 检查，但从 `/root/miniconda3/bin/` 和 `lib/` 确认：
- ✅ `transformers` (config.json 记录 `transformers_version: 4.57.6`)
- ✅ `vllm` (bin 中有 vllm 命令)
- ✅ `torch` (有 torchrun)
- ✅ `accelerate` (FSDP 转换需要，已安装)
- ✅ RAGEN 环境（脚本 import 的 `ragen.env.alfworld`）

### 4. CPU 加载测试

跳过。checkpoint 是 FSDP 分片格式（2 rank × 3.8G model weights），直接 `from_pretrained` 无法加载，需要先经过脚本内置的 `convert_fsdp_to_hf()` 转换。转换本身需要 ~8G CPU 内存 + 写 ~8G safetensors，在 GPU 被占用时不适合做。

### 5. 磁盘空间警告

`/root/autodl-tmp` **仅剩 35G 可用（87% 已用）**。FSDP→HF 转换两个 checkpoint 需要约 16G（每个 ~8G safetensors），eval 日志可忽略。勉强够用，但建议转换完成后删除 optim 文件释放空间（如不需要恢复训练）。

### 6. 推荐执行命令

等 GPU 空闲后：

```bash
# 激活 conda 环境
source /root/miniconda3/bin/activate

# 批量 eval 所有 checkpoint（推荐）
cd /root/cost-verify-agent-rl
CUDA_VISIBLE_DEVICES=0 python scripts/eval_checkpoint_full_context.py \
    --run_dir /root/autodl-tmp/checkpoints/hsweep-h2/ \
    --num_episodes 32 \
    --gpu 0 \
    --gpu_memory_utilization 0.35

# 或单个 checkpoint
CUDA_VISIBLE_DEVICES=0 python scripts/eval_checkpoint_full_context.py \
    --ckpt_path /root/autodl-tmp/checkpoints/hsweep-h2/global_step_5/ \
    --num_episodes 32 \
    --gpu 0

# 先 dry-run 验证 checkpoint 发现
python scripts/eval_checkpoint_full_context.py \
    --run_dir /root/autodl-tmp/checkpoints/hsweep-h2/ \
    --dry_run
```

**注意**: `--gpu_memory_utilization 0.35` 是默认值，Qwen3-4B 在单卡 96G 上足够。如果训练刚结束 GPU 显存还未释放，等几秒或手动确认 `nvidia-smi`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "FSDP_version": 1,
    "world_size": 2
  }
}
```

</details>

---
