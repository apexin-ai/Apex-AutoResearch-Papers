# code d144 llama adapt

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d144-llama-adapt_20260519T131508_result.json`
- **Structured JSON:** [`27055117ab94652f759d.json`](../../sessions/27/27055117ab94652f759d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Here's the complete summary:

---

## 结果

### 1. 代码分析 — 无需修改

`train_grpo.py` 和 `eval_sta.py` 已经是模型无关的：
- 使用 `AutoModelForCausalLM` / `AutoTokenizer`（非 Qwen 硬编码）
- `chat_template_kwargs={"enable_thinking": False}` — Jinja2 对 LLaMA 模板静默忽略此参数（已验证）
- `strip_thinking()` — LLaMA 不生成 `&lt;think>` 标签，空操作
- Prompt 以 chat messages 格式传入 `apply_chat_template()`，LLaMA-3.2-3B base 模型自带 chat template

### 2. 新建 Config 文件（匹配 D134 参数）

**`configs/grpo_llama_exec_only.yaml`** — exec-only baseline
**`configs/grpo_llama_additive_bonus_b01.yaml`** — ISR β=0.1

两者均使用：
- `model_path: /root/autodl-tmp/models/Llama-3.2-3B`
- `data_path: data/train_500_seed42.jsonl`（遵守 C001）
- `batch_size=2, grad_accum=4`（effective 8，匹配 D134）
- `save_total_limit: 1`（遵守 C003）
- 500 steps, lr=1e-6, seed=42

### 3. 新建辅助脚本

**`scripts/setup_llama.sh`** — ModelScope 下载完成后：从 ms-cache 复制 safetensors 到主目录 + 验证模型加载 + 生成测试

### 4. Dry-run — 模型文件不完整，无法执行

- **问题**：`/root/autodl-tmp/models/Llama-3.2-3B/model-00001-of-00002.safetensors` 是之前 HuggingFace 下载的截断文件（4.97GB，实际需 ~6.06GB），加载报 `SafetensorError: incomplete metadata`
- **HF 恢复下载失败**：meta-llama/Llama-3.2-3B 是 gated model，当前未认证
- **ModelScope 下载进行中**：PID 391993 正在下载到 ms-cache，shard 1 ~17%, shard 2 ~57%，预计还需 **~2 小时**（~560kB/s）

### 5. 下载完成后执行

```bash
# Step 1: 复制模型文件
bash /root/solver-trace-ablation/scripts/setup_llama.sh

# Step 2: Dry-run (1 step)
export CUDA_VISIBLE_DEVICES=0
cd /root/solver-trace-ablation
python3 scripts/train_grpo.py --config configs/grpo_llama_exec_only.yaml --num_steps 1 --output_dir /tmp/llama_dryrun --no_wandb

# Step 3: 正式训练 (按需选择)
# exec-only:
python3 scripts/train_grpo.py --config configs/grpo_llama_exec_only.yaml
# ISR β=0.1:
python3 scripts/train_grpo.py --config configs/grpo_llama_additive_bonus_b01.yaml
```

### 6. 兼容性说明

| 项目 | 状态 |
|------|------|
| 模型加载 (Auto classes) | 兼容 |
| Chat template | LLaMA base 自带，格式正确 |
| `enable_thinking=False` | LLaMA 静默忽略，已验证 |
| pad_token | `<\|finetune_right_pad_id\|>` (id=128004)，已内置 |
| `trust_remote_code` | 非必需但无害 |
| Qwen 兼容性 | 未修改任何代码，Qwen 训练不受影响 |

---
