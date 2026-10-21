# check bootstrap v3 cron exit 2

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_bootstrap_v3_cron_exit_2_20260523T071751_result.json`
- **Structured JSON:** [`36d291db46ed78e0c208.json`](../../sessions/36/36d291db46ed78e0c208.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**状态汇报：**

**进程正常运行中**，Cron 报告是误报。两个 GPU 各自在跑：

- **cuda:0** — 完成 `openvla/goal/trained`，当前正在跑 `openvla/goal/untrained`（extraction 完成，RidgeCV fitting 中）
- **cuda:1** — 完成 `tracvla/goal/trained`，当前正在跑 `tracvla/goal/untrained`（extraction 850/5000）

**完成进度：2/20 JSON**（每条件含 extraction + 1000 次 bootstrap，每个约 20-30 分钟）

**已完成结果：**

| 条件 | peak_layer | peak_R² | exit_R² | delta | 95% CI | boot_mean |
|------|-----------|---------|---------|-------|--------|-----------|
| openvla/goal/trained | L1 | 0.418 | 0.331 | 0.086 | [-0.056, 0.106] | 0.017 |
| tracvla/goal/trained | L13 | 0.540 | 0.207 | 0.333 | [0.207, 0.451] | 0.316 |

注意点：
- **TracVLA trained** delta=0.333 显著（CI 不含 0），晚期层大幅衰减（L28-L30 甚至为负）
- **OpenVLA trained** delta=0.086 不显著（CI 含 0），各层 R² 相对平坦

按当前速度，预计全部 20 个条件还需 **~9-10 小时**。

---
