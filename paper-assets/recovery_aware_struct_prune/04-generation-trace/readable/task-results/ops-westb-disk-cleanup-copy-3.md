# ops westb disk cleanup

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westb_disk_cleanup_20260519T101715_result.json`
- **Structured JSON:** [`06fb817e7a16339561cf.json`](../../sessions/06/06fb817e7a16339561cf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 磁盘状态汇报

### 分区概况

| 分区 | 总量 | 已用 | 可用 | 使用率 |
|------|------|------|------|--------|
| `/root/autodl-tmp` (数据盘) | 250G | 227G | **24G** | 91% |
| `/` (根分区) | 30G | 8.3G | 22G | 28% |

**注意**: 用户提到的 `/autodl-pub` 实际有 6.6T 可用，不紧张。真正紧张的是 `/root/autodl-tmp`。

### grpo_cka_only_20_seed123 训练状态

- 当前已用空间: **96K**（刚开始，尚无 checkpoint）
- 目录内仅有 `completions/` 子目录
- 预计完成后占用 ~12G（参考同类 grpo_cka_only_20 = 12G）
- 24G 可用 > 12G 预计需求，**暂时安全但余量不大**

### 各目录大小明细

**7B 模型目录 (10-15G 级)**:

| 目录 | 大小 | 说明 |
|------|------|------|
| `pruned_unstructured_20` | **15G** | unstructured pruning，清理候选 |
| `pruned_cka_only_20` | 12G | |
| `pruned_random_20` | 12G | |
| `pruned_rasp_20` | 12G | |
| `pruned_rasp_rlvr_20` | 12G | |
| `pruned_standard_20` | 12G | |
| `pruned_rasp_25` | 11G | |
| `pruned_standard_25` | 11G | |
| `grpo_cka_only_20` | 12G | |
| `grpo_rasp_25` | 11G | |
| `sft_cka_only_20` | 12G | |
| `sft_gradient_20` | 12G | |
| `sft_random_20` | 12G | |
| `sft_rasp_rlvr_20` | 12G | |
| `sft_rasp_25` | 11G | |
| `sft_standard_25` | 11G | |

**1.5B 模型目录 (2.8G 级)**: grpo/pruned/sft × {cka_only_20, rasp_20, standard_20}_1p5b — 各 2.8G，共 9 个 = ~25G

**其他**: models 3.4G, logs 20M, results 19M

### 清理建议（不执行，仅汇报）

| 优先级 | 目录 | 大小 | 理由 |
|--------|------|------|------|
| **P0** | `pruned_unstructured_20` | 15G | unstructured pruning control 实验，如已完成 eval 且结果已记录，可安全清理 |
| P1 | `grpo_random_20` | 220K | 仅 220K，清不清都无所谓 |

**用户提到的 `grpo_unstructured_20` 目录不存在**。仅有 `pruned_unstructured_20`。

### 结论

当前 24G 可用空间可以支撑 grpo_cka_only_20_seed123 完成训练（预计 ~12G），但训练后仅剩 ~12G。如果后续还有更多实验，建议清理 `pruned_unstructured_20`（释放 15G）。

---
