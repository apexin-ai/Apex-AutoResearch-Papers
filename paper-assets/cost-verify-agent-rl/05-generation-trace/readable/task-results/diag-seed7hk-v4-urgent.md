# diag seed7hk v4 urgent

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_seed7hk_v4_urgent_20260523T230915_result.json`
- **Structured JSON:** [`2e27fe2f26afa80b5b6c.json`](../../sessions/2e/2e27fe2f26afa80b5b6c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

### seed7hk eval v4
**状态：正在运行中（seed=0/3）**

- 07:06 启动，当前在第 1 轮 eval (seed=0)
- 模型 `qwen_exp029_seed7_high_kl_step5_hf` **加载成功**（config 修复生效）
- wandb run: `evalvar-seed7hk-s0-fix` (ID: mmsm7ira)
- 数据 tokenization 完成 (8810 items + 341 items)，正在 eval rollout 阶段
- PID 84851 仍存活，TaskRunner (PID 86914) 88% CPU 活跃

旧的 3 轮 (seed7hk_s0/s1/s2) 全部 crash：`ValueError: Unsupported model: /root/autodl-tmp/checkpoints/exp029_seed7_high_kl_step5_hf`。v4 修复了这个问题。

### GPU
| GPU | Util | VRAM |
|-----|------|------|
| 0 | 0% | 8133 / 97887 MiB |

GPU 利用率 0% 可能是 ALFWorld 环境交互的 CPU-bound 阶段，模型已加载到 VRAM (8.1GB)。仅 1 张 GPU 可见。

### seed200
无活跃进程。checkpoint 存在于 `/root/autodl-tmp/checkpoints/qwen_exp029_seed200_step5_hf`。

### 注意
有 6 个旧的 orphan `ray::TaskRunner` 进程 (PID 48255/52397/55911/70926/74563/78173，02:40-05:55 启动) 仍在运行，来自之前失败的 eval。占用约 17GB+ 内存。v4 eval 完成后建议清理。

---
