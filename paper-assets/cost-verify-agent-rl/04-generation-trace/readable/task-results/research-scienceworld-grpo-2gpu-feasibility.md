# research scienceworld grpo 2gpu feasibility

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_scienceworld_grpo_2gpu_feasibility_20260520T042011_result.json`
- **Structured JSON:** [`4cb646276ca8c34dcf78.json`](../../sessions/4c/4cb646276ca8c34dcf78.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### 可行性：完全可行

1.7B Qwen3 (bf16 ~3.4GB) 在 2×96GB GPU 上内存极其充裕。即使 Cell C 的 full-context rollout（max 20480 tokens，16 env_groups × 8 group_size），单卡 48GB vLLM 预算也绑绑有余。

### Config 修改（相对原 4-GPU 版本）

| 参数 | Cell A 原值 → 新值 | Cell C 原值 → 新值 |
|------|-------------------|-------------------|
| `CUDA_VISIBLE_DEVICES` | "0,1,2,3" → "0,1" | "0,1,2,3" → "0,1" |
| `n_gpus_per_node` | 4 → 2 | 4 → 2 |
| `gpu_memory_utilization` | 0.4 → 0.5 | 0.35 → 0.5 |
| `model_path` | `.../global_step_448/huggingface` → `.../scienceworld_sft/huggingface` (bjb1 路径) | 同左 |
| `ppo_mini_batch_size` | 16（不变） | 16（不变） |
| 所有超参 | 不变 | 不变 |

`ppo_mini_batch_size` 保持 16：2 GPU × micro_batch=1 = 2/step → 8 次 gradient accumulation（原 4 次），数学等价，只是每 step 稍慢。

### 已创建文件

- `westd-47453:/root/cost-verify-agent-rl/RAGEN/config/_scienceworld_cell_a_2gpu.yaml`
- `westd-47453:/root/cost-verify-agent-rl/RAGEN/config/_scienceworld_cell_c_2gpu.yaml`

### 注意事项

- 运行前需将 config 同步到 bjb1-17606（git push + pull 或 scp）
- bjb1 上 SFT checkpoint 已就位：`/root/autodl-tmp/checkpoints/scienceworld_sft/huggingface/`
- 建议 dry-run 验证模型加载 + vLLM 初始化（需要时告知我执行）

---
