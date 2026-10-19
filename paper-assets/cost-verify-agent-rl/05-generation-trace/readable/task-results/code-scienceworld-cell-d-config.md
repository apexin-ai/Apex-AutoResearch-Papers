# code scienceworld cell d config

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_scienceworld_cell_d_config_20260524T042701_result.json`
- **Structured JSON:** [`2402bed3710ebe853818.json`](../../sessions/24/2402bed3710ebe853818.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。产出汇总：

### 创建的文件

| 文件 | 路径 |
|------|------|
| Cell D GRPO 配置 | `/root/cost-verify-agent-rl/RAGEN/config/_scienceworld_cell_d_grpo.yaml` |
| SFT 训练脚本 | `/root/cost-verify-agent-rl/scripts/run_scienceworld_sft_v2.sh` |
| Cell D 启动脚本 | `/root/cost-verify-agent-rl/scripts/run_scienceworld_cell_d.sh` |
| 数据生成脚本（从 westd 复制） | `/root/cost-verify-agent-rl/generate_scienceworld_sft.py` |

### Cell D 配置关键参数
- `context_window_mode: "full"` + `max_context_window: -1`（episode-level）
- `n_gpus_per_node: 1`，`CUDA_VISIBLE_DEVICES: "0"`
- `model_path: /root/autodl-tmp/checkpoints/scienceworld_sft_v2/final`
- `total_training_steps: 15`，`save_freq: 5`，`test_freq: 5`
- `env_tags: ScienceWorldSG`（全部 30 task types）
- `seed.train: 42`
- `train: env_groups=8, group_size=8`（64 samples/step）
- `kl_loss_coef: 0.01`，`lr: 1e-6`（与 Cell A 一致）

### SFT 训练参数
- Base model: `/root/autodl-tmp/models/Qwen/Qwen3-1___7B/` ✓ 已确认存在
- lr=2e-5, epochs=3, batch=2, grad_accum=8, max_seq=16384
- 输出: `scienceworld_sft_v2/final/`

### 需注意
1. **SFT 数据尚不存在**：`/root/autodl-tmp/expert_sft/scienceworld_sft_train.jsonl` 不在 bjb1 上。需先运行 `python generate_scienceworld_sft.py` 生成（需要 `scienceworld` 包）
2. **SFT checkpoint 尚不存在**：Cell D 依赖 SFT 完成后的 checkpoint，启动脚本有 pre-flight 检查会拦截
3. **执行顺序**：生成 SFT 数据 → 运行 SFT 训练 → 启动 Cell D GRPO

---
