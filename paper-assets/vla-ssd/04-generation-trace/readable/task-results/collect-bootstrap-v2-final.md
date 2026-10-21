# collect bootstrap v2 final

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_collect_bootstrap_v2_final_20260523T062013_result.json`
- **Structured JSON:** [`4e58d3784eb3b924bce1.json`](../../sessions/4e/4e58d3784eb3b924bce1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

现在已有 19 个文件。还差 1 个：**tracvla_long/untrained** 正在 cuda1 上跑（刚开始 extraction 阶段）。nora_object 和 nora_long 不在本批次中。

## 状态汇总

- **完成**: 19/20 文件
- **运行中**: tracvla_long/untrained（cuda1，extraction 阶段 ~100/5000）
- **cuda0**: 已完成 (12:59)
- **不在批次内**: nora_object, nora_long

## 全量结果表（19 个已完成文件）

| arch | suite | cond | peak_r2 | peak_L | exit_r2 | delta | CI_lo | CI_hi | boot_mean | boot_std | sig? |
|------|-------|------|---------|--------|---------|-------|-------|-------|-----------|----------|------|
| **openvla** | goal | trained | 0.4556 | L1 | 0.3395 | 0.1160 | -0.2528 | -0.0117 | -0.1417 | 0.0647 | NO |
| openvla | goal | untrained | 0.4042 | L24 | 0.2565 | 0.1477 | -0.0617 | 0.0746 | -0.0025 | 0.0344 | NO |
| openvla | spatial | trained | 0.5782 | L15 | 0.5447 | 0.0335 | -0.0575 | 0.0487 | -0.0085 | 0.0275 | NO |
| openvla | spatial | untrained | 0.5660 | L10 | 0.4931 | 0.0729 | -0.0788 | 0.0604 | -0.0159 | 0.0372 | NO |
| openvla | object | trained | 0.5883 | L26 | 0.5332 | 0.0551 | -0.0310 | 0.0515 | 0.0056 | 0.0206 | NO |
| openvla | object | untrained | 0.5749 | L26 | 0.5381 | 0.0369 | -0.0359 | 0.0532 | 0.0034 | 0.0235 | NO |
| openvla | long | trained | 0.5050 | L23 | 0.4294 | 0.0757 | -0.0539 | 0.0595 | -0.0052 | 0.0292 | NO |
| openvla | long | untrained | 0.5181 | L24 | 0.5027 | 0.0154 | -0.0655 | 0.0285 | -0.0257 | 0.0250 | NO |
| **tracvla** | goal | trained | 0.5399 | L13 | 0.2065 | 0.3334 | 0.0546 | 0.3416 | 0.1671 | 0.0733 | **YES** |
| tracvla | goal | untrained | 0.5048 | L11 | 0.4403 | 0.0645 | -0.1873 | -0.0039 | -0.0864 | 0.0480 | NO |
| tracvla | spatial | trained | 0.6871 | L13 | 0.5315 | 0.1557 | 0.0115 | 0.1498 | 0.0752 | 0.0358 | **YES** |
| tracvla | spatial | untrained | 0.6120 | L4 | 0.5643 | 0.0477 | -0.8003 | -0.5788 | -0.7005 | 0.0569 | NO |
| tracvla | object | trained | 0.6315 | L13 | 0.2692 | 0.3623 | 0.0377 | 0.3674 | 0.1752 | 0.0843 | **YES** |
| tracvla | object | untrained | 0.6274 | L17 | 0.6184 | 0.0090 | -0.0648 | 0.0217 | -0.0191 | 0.0222 | NO |
| tracvla | long | trained | 0.5897 | L13 | 0.2319 | 0.3579 | 0.0302 | 0.3363 | 0.1564 | 0.0805 | **YES** |
| **nora** | goal | trained | 0.4489 | L8 | -0.0062 | 0.4551 | 0.9960 | 1.8478 | 1.3478 | 0.2116 | **YES** |
| nora | goal | untrained | 0.4203 | L5 | 0.3397 | 0.0806 | -0.0624 | 0.0856 | 0.0035 | 0.0454 | NO |
| nora | spatial | trained | 0.5763 | L20 | 0.2683 | 0.3080 | 0.0624 | 0.4450 | 0.2351 | 0.1020 | **YES** |
| nora | spatial | untrained | 0.5125 | L4 | 0.4240 | 0.0885 | -0.0468 | 0.0610 | 0.0030 | 0.0287 | NO |

## 关键发现

**Significant (CI_lo > 0) 全部是 trained 条件**：
- tracvla trained: goal/spatial/object/long 全部显著（4/4）
- nora trained: goal/spatial 显著（2/2）
- openvla: 0/4 显著

**所有 untrained 条件均不显著**（0/9 完成的 untrained 文件显著）。

**注意异常值**：
- `nora goal trained`: bootstrap_mean=1.3478, CI=[0.996, 1.8478] — 远超 delta=0.4551，数值异常大
- `tracvla spatial untrained`: CI=[-0.8003, -0.5788] — bootstrap_mean=-0.7005，极端负值

还差 **tracvla_long/untrained**（预计 ~30-40 分钟完成）。

---
