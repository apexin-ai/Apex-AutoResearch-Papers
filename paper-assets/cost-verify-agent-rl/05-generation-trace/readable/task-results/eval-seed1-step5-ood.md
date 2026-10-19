# eval seed1 step5 ood

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_seed1_step5_ood_20260521T222538_result.json`
- **Structured JSON:** [`2aa97f6f4b6478cbe360.json`](../../sessions/2a/2aa97f6f4b6478cbe360.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**Seed 1 step 5 checkpoint 不存在。**

搜索结果：

| 服务器 | 路径搜索范围 | global_step_5 |
|--------|-------------|---------------|
| westd-47453 | `/root/autodl-tmp/` 全盘 | exp029-seed8, intervention-c-hard-cap |
| bjb1-17606 | `/root/autodl-tmp/` + `/root/` | exp029-seed7-high-kl |

`exp029_episode_level`（seed 1）在两台服务器上均无任何 checkpoint 残留。`exp029_seed3` 目录在 westd 上存在但为空。registry 中也无该实验条目。

**可用的 step 5 checkpoint（可替代做同期对照）：**
- **Seed 8 step 5**（westd）— 已有 OOD eval 结果 11.94%（这是崩溃 seed，已完成）
- **Seed 7 (high-kl) step 5**（bjb1）— 另一个崩溃 seed
- **Intervention-C step 5**（westd）— hard-cap 干预实验

没有任何 stable seed 的 step 5 checkpoint 可用。Stable seeds（3/5/6）的最早 checkpoint 分别是 step 15、step 10、step 15。

**阻塞原因：Seed 1 checkpoint 不存在，无法执行此 eval。** 如需 stable seed 早期对照，最接近的选项是 Seed 5 step 10（westd 上有 HF 格式）。

---
