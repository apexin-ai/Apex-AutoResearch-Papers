# ops taxei rp eval launch

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_taxei-rp-eval-launch_20260516T060859_result.json`
- **Structured JSON:** [`ce0fab02f0218cb8b7ca.json`](../../sessions/ce/ce0fab02f0218cb8b7ca.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 4 个 tmux session 就位。报告如下：

---

## TaxEI-RP Eval ×4 启动报告

### 1. Checkpoint 路径

| Seed | Checkpoint |
|------|-----------|
| s42 | `/root/autodl-tmp/tax_error_inject_agent/output/v4-taxei-rp-s42/v0-20260516-101703/checkpoint-5415` |
| s0 | `/root/autodl-tmp/tax_error_inject_agent/output/v4-taxei-rp-s0/v0-20260516-101706/checkpoint-5415` |
| s123 | `/root/autodl-tmp/tax_error_inject_agent/output/v4-taxei-rp-s123/v0-20260516-101708/checkpoint-5415` |
| s1 | `/root/autodl-tmp/tax_error_inject_agent/output/v4-taxei-rp-s1/v0-20260516-101834/checkpoint-5415` |

所有 checkpoint 均含 `adapter_model.safetensors`。

### 2. Eval 命令

```bash
# s0 (GPU 1) — 已在运行
CUDA_VISIBLE_DEVICES=1 python eval/injected_eval.py \
  --model_path .../v4-taxei-rp-s0/.../checkpoint-5415 \
  --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B \
  --model_variant taxei --num_episodes 47 --seed 0 \
  --output eval_results/v4_taxei_rp_s0_injected.json

# s123 (GPU 2) — 已在运行
CUDA_VISIBLE_DEVICES=2 python eval/injected_eval.py \
  --model_path .../v4-taxei-rp-s123/.../checkpoint-5415 \
  --model_variant taxei --num_episodes 47 --seed 123 \
  --output eval_results/v4_taxei_rp_s123_injected.json

# s1 (GPU 3) — 已在运行
CUDA_VISIBLE_DEVICES=3 python eval/injected_eval.py \
  --model_path .../v4-taxei-rp-s1/.../checkpoint-5415 \
  --model_variant taxei --num_episodes 47 --seed 1 \
  --output eval_results/v4_taxei_rp_s1_injected.json

# s42 (GPU 0) — 等待 PID 239377 完成后自动启动
CUDA_VISIBLE_DEVICES=0 python eval/injected_eval.py \
  --model_path .../v4-taxei-rp-s42/.../checkpoint-5415 \
  --model_variant taxei --num_episodes 47 --seed 42 \
  --output eval_results/v4_taxei_rp_s42_injected.json
```

注：`--model_variant taxei-rp` 不被脚本接受（只允许 taxei/random/vanilla），改用 `taxei`。输出文件名中用 `taxei_rp` 区分。

### 3. PID 与 tmux session

| Session | Pane PID | Python PID | GPU | 状态 |
|---------|----------|------------|-----|------|
| `eval-rp-s0` | 240914 | 240920 | 1 | 运行中 (5/47) |
| `eval-rp-s123` | 241050 | 241056 | 2 | 运行中 (4/47) |
| `eval-rp-s1` | 241187 | 241193 | 3 | 运行中 (4/47) |
| `eval-rp-s42` | 241792 | — | 0 | 等待 GPU 0 释放 |

### 4. 初始输出正常
s0/s123/s1 均已通过模型加载并开始评估 episode，结果正常（有 OK 有 FAIL，注入类型各异）。

### 5. s0 训练已完成
PID 223049 不存在，训练已结束。

### 6. 异常
- **GPU 0 被占用**：`analyze_failure_modes_5seed.py --condition vanilla` (PID 239377) 仍在 GPU 0 上运行。s42 eval 的 tmux session 设置了自动等待——该进程结束后 s42 eval 将自动启动。
- 同时还有 `collect_trajectories_scaleup.py` (PID 238209) 在后台运行（CPU only，不影响 GPU）。

---
