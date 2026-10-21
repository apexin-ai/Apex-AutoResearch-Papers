# progress check all servers 20260527

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_progress_check_all_servers_20260527_20260527T101705_result.json`
- **Structured JSON:** [`cb6ab22b6dd6a4f3d105.json`](../../sessions/cb/cb6ab22b6dd6a4f3d105.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

快照已写入 `artifacts/progress_snapshot_20260527.md`。

**汇总：**

| 状态 | 数量 | 详情 |
|------|------|------|
| ✅ 已完成 | 2 | pi05_random_k095 (SR=60.6%), openvla_attn_k05_goal (SR=42.8%) |
| ❌ 崩溃 | 1 | pi05_l2norm_k085_w41 — 网络不通无法加载 tokenizer，需 `HF_HUB_OFFLINE=1` 重启 |
| 🔄 运行中 | 9 | ETA 18:35 ~ 23:15 UTC，全部在 deadline 前 |

**需要立即处理：** westd-41074:GPU3 的 `pi05_l2norm_k085_long_w41` 崩溃了，启动时访问 `google/paligemma-3b-pt-224` tokenizer 网络不通。需要设 `HF_HUB_OFFLINE=1` 确保 tokenizer 已缓存后重启。

**重点关注：**
- pi05_random_k09 前3个task累计SR=32%，k=0.9异常正在复现
- cqa1 上的 pi05_l2norm_k085 前6个task SR=89.7%，表现极好
- westd-38929:GPU0 的 random_k095_long 最晚完成 (~23:15 UTC)，但不影响 deadline

---
