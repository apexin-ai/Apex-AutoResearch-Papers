# ops final eval prep

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_final_eval_prep_20260524T043016_result.json`
- **Structured JSON:** [`cc4a8d49332c3ae23f76.json`](../../sessions/cc/cc4a8d49332c3ae23f76.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文档已写入 `artifacts/eval_commands_d012_final.md`。

## 检查结果汇总

| 检查项 | 状态 | 备注 |
|--------|------|------|
| eval 脚本 (两台) | ✅ | `eval_pi05_safelibero.py` 和 `serve_policy.py` 均存在 |
| Checkpoint 结构 | ✅ | 每 2000 步保存，`30000/` 会在训练结束时生成 |
| Mid-eval JSON | ⚠️ | s0 (westd-45947) 已有 2 个 JSON；**s1/s2 无 mid-eval 结果**（训练在 mid-eval 前因磁盘满崩溃） |
| 磁盘空间 | ✅ | 45947: 75GB free, 35807: 225GB free |
| 输出目录 | ❌ | `d012_final/` 尚未创建，eval 前需 `mkdir -p` |

## 关键发现：训练时间修正

原预估严重偏早：

| | 原预估 | 实际预估 | 差异 |
|--|--------|----------|------|
| westd-45947 s0 | 10:20 UTC | **~18:00 UTC** | +7.7h |
| westd-35807 s1/s2 | 13:30 UTC | **~21:30 UTC** | +8h |

原因：s1/s2 在 step ~22000 时因 westd-35807 磁盘满崩溃，从 22000 恢复后延迟了约 8 小时。s0 也比预估慢（可能原预估基于更早的速度）。

---
