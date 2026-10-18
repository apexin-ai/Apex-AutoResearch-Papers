# code 1 3b correct download

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_1_3b-correct-download_20260518T101539_result.json`
- **Structured JSON:** [`8b117a22ee7441c1de54.json`](../../sessions/8b/8b117a22ee7441c1de54.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

下载持续进行中。当前状态汇报：

**已确认的正确 repo 名称格式**：`m-a-p/1.3B-100B-{variant}`
- 用户列表中的修正：
  - `GatedDeltaNet-pure-baseline` → 实际为 `GatedDeltaNet-pure`
  - `GatedDeltaNet-New-hybrid-24-1` → 实际为 `GatedDeltaNet-hybrid-24-1`
  - `HGRN2-pure-baseline` → 实际为 `HGRN2-pure`

**下载速度**：~600 KB/s (0.6 MB/s)

**当前进度**：正在下载第 1/13 个模型 (GatedDeltaNet-pure)，已下载 ~122MB / ~5.3GB

**已完成的 3 个模型**（之前正确下载的）：
| 模型 | 大小 |
|------|------|
| 1.3B-100B-GatedDeltaNet-hybrid-3-1 | 5.3G |
| 1.3B-100B-RetNet-pure | 4.9G |
| transformer_1.3B_baseline | 4.3G |

**预计总时间**：~30 小时（13 个模型 × ~5GB × 600KB/s 速度）

**磁盘**：44G/250G 已用 (18%)，剩余 207G 足够（~65GB 新增）

下载在 `screen -r download` 中运行，不会因 SSH 断开而中断。需要我定期检查进度还是等完成后再汇报？

---
