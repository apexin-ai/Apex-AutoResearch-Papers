# ops deploy cross seed 14b

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_deploy-cross-seed-14b_20260522T201139_result.json`
- **Structured JSON:** [`f6255d92bec6849ee15c.json`](../../sessions/f6/f6255d92bec6849ee15c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 个实验全部部署完毕，汇总：

| 实验 | 服务器 | GPU | tmux session | PID | 状态 |
|------|--------|-----|-------------|-----|------|
| t10_a050_s43 | westd-19828 | cuda:1 | `14b_t10_a050_s43` | 821294 | Loading model |
| t10_a075_s43 | westd-17855 | cuda:2 | `14b_t10_a075_s43` | 717612 | Loading model |
| t10_a060_s43 | westd-17855 | cuda:3 | `14b_t10_a060_s43` | 717753 | Loading model |

**操作记录**:
- 已 kill PID 714525（17855 cuda:3 上的 `t10_a075_s42_fp32_14b --start_gen 10` 超 spec 进程，原始 gen_0-9 完整保留）
- 3 个实验均正在加载 `EleutherAI/pythia-1.4b-deduped`，GPU 显存将在模型加载到 GPU 后占用

**⚠️ 磁盘风险**: westd-17855 仅剩 27G，2 个实验预计各 ~11G，完成时可能触及磁盘上限。建议中期检查 `df -h`。

---
