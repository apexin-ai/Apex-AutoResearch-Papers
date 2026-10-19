# ssh diagnose baseline s1 exit

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_diagnose_baseline_s1_exit_20260520T143115_result.json`
- **Structured JSON:** [`9571787fb966545f4159.json`](../../sessions/95/9571787fb966545f4159.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结论

**conclusion = failed**

| 项目 | 详情 |
|------|------|
| **退出原因** | **磁盘满**。数据盘 `/root/autodl-tmp/` 350G 已用 100%（剩余 272K）。在 step 16000 保存 checkpoint 时 `torch.save(optimizer.state_dict())` 写入失败 |
| **最终 step** | **15999**（53%），loss=0.0055，lr=1.31e-05 |
| **最新完整 checkpoint** | **14000**（`tmp_16000` 是写到一半的残留，11G） |
| **错误** | `RuntimeError: PytorchStreamWriter failed writing file data/1387: file write failed` |

### 恢复建议
1. 清理 `tmp_16000`（11G 废数据）
2. 清理数据盘上不再需要的文件腾出空间（每个 checkpoint 约 11G，剩余 14000 steps 还需 ~7 个 checkpoint）
3. 从 checkpoint 14000 恢复训练

---
