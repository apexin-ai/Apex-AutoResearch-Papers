# ssh gpu status all servers

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_gpu_status_all_servers_20260521T205833_result.json`
- **Structured JSON:** [`5c1d4c38bbe7056276e3.json`](../../sessions/5c/5c1d4c38bbe7056276e3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总结果：

---

## autodl-5090

| GPU | 显存占用 | 利用率 | 状态 |
|-----|---------|--------|------|
| 0 | 2MiB / 32607MiB | 0% | **空闲** |
| 1 | 2MiB / 32607MiB | 0% | **空闲** |
| 2 | 2MiB / 32607MiB | 0% | **空闲** |
| 3 | 2MiB / 32607MiB | 0% | **空闲** |

- **运行中实验**: 无。仅有一个残留 tmux session `exp_001_n16_seed456`（May 15 创建），无活跃 python 子进程。
- **磁盘**: 250GB 总量，25GB 可用（91% 已用）⚠️ 偏紧
- **5-epoch 模型**: ✅ 存在，`checkpoints/qwen3-8b-fewnerd-5epoch-merged/`，~15.3GB，时间戳 May 22 01:55

**确认：4 张 GPU 全空闲，handoff 信息属实。**

---

## autodl-5090-c

| GPU | 显存占用 | 利用率 | 进程 |
|-----|---------|--------|------|
| 0 | 0MiB / 32607MiB | 0% | **空闲** |
| 1 | 30206MiB / 32607MiB | 84% | VLLM PID 357933 |
| 2 | 30156MiB / 32607MiB | 88% | VLLM PID 358101 |
| 3 | 30286MiB / 32607MiB | 78% | VLLM PID 346917 |

**运行中实验（3 个）:**

| 实验 | PID | GPU | seed | 模型 | 启动时间 |
|------|-----|-----|------|------|---------|
| `exp_fewnerd_mf4v2_s123_v3` | 357394 | cuda:1 | 123 | qwen3-8b-fewnerd-exp021-merged | 03:44 |
| `exp_fewnerd_mf4v2_s456_v3` | 357662 | cuda:2 | 456 | qwen3-8b-fewnerd-exp021-merged | 03:44 |
| `exp_e2_pretrained_fewnerd_s42` | 346388 | cuda:3 | 42 | Qwen2.5-7B-Instruct (pretrained) | 02:12 |

**vs 预期对比:**
- ✅ `exp_fewnerd_mf4v2_s456_v3` (PID 357658 tmux / 357662 python, cuda:2) — 在跑
- ❌ `exp_fewnerd_5epoch_s456` (PID 353730, cuda:0) — **未找到**，GPU 0 空闲。该实验已结束或被 kill
- ➕ `exp_fewnerd_mf4v2_s123_v3` (cuda:1) — handoff 未提及的额外实验
- ✅ `exp_e2_pretrained_fewnerd_s42` — 仍在跑（PID 346388, cuda:3, seed 42）。注意 tmux session 名为 `exp_e2_pretrained_fewnerd_s456` 但实际执行的是 seed 42 的命令

- **磁盘**: 350GB 总量，101GB 可用（72%）
- **5-epoch 模型**: 此服务器也有一份副本

---

## autodl-5090-b

**❌ 不在服务器注册表中。** 可用服务器列表：autodl-5090, autodl-5090-c, bjb1-21071, bjb2-11496, westb-25965。T-ablation 实验（exp_fewnerd_t05_s456、exp_fewnerd_t12_s456）无法确认状态。可能需要检查 bjb 系列服务器是否就是 "autodl-5090-b"，或该实例已关机/重建导致 SSH 配置丢失。

---
