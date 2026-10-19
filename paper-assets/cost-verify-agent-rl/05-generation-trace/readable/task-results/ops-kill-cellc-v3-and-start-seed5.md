# ops kill cellc v3 and start seed5

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_kill-cellc-v3-and-start-seed5_20260521T024238_result.json`
- **Structured JSON:** [`dd52b26e39fb476b70d2.json`](../../sessions/dd/dd52b26e39fb476b70d2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练已成功启动，模型正在加载（Qwen3 1.72B，safetensors checkpoint 已加载完成）。

**汇总：**

| 项目 | 状态 |
|------|------|
| **Cell C v3** | 已终止（PID 88226/94753 KILLED），registry → DONE(negative) |
| **Seed 5 训练** | PID **683267**，GPU 0,1 已占用（各 10795 MiB），模型加载中 |
| **GPU 状态** | GPU 0: 10795 MiB, GPU 1: 10795 MiB, GPU 2: 0 MiB, GPU 3: 0 MiB |
| **配置文件** | `_alfworld_exp029_seed5_episode.yaml` + `_alfworld_exp029_seed5_ood_final.yaml` 已就绪 |
| **Registry** | `exp029_seed5_episode` → RUNNING，spec 完整 |

W&B run 需等 vLLM 初始化完成后才会出现（通常 2-3 分钟）。

---
