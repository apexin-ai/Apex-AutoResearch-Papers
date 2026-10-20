# code occ dryrun mini

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_occ_dryrun_mini_20260520T101527_result.json`
- **Structured JSON:** [`972e3cf67e3bb71cea5a.json`](../../sessions/97/972e3cf67e3bb71cea5a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

清理完毕。下面是 **dry-run 完整结果**：

---

## Occ 训练 Mini Dry-Run 结果

### Loss 曲线（20 步）

| Step | loss_value | action_l1 | next_action_l1 | occ_loss |
|------|-----------|-----------|----------------|----------|
| 0 | 0.7695 | 0.6250 | 0.7930 | 0.1195 |
| 5 | 0.9375 | 1.3438 | 0.8789 | 0.0910 |
| 10 | 0.6289 | 0.6094 | 0.6289 | 0.0695 |
| 15 | 0.4707 | 0.4648 | 0.4707 | 0.0589 |
| 19 | 0.5664 | 0.5547 | 0.5664 | 0.0542 |

### 验证结论

1. **occ_loss**: 非零、非 NaN，从 0.1195 单调下降到 0.0542（-55%），FocalLoss 工作正常
2. **action_loss**: 正常范围（初始 spike 后收敛到 ~0.5），与无 occ head 的 vanilla 训练行为一致
3. **标签非零**: dummy 数据 ~15% occupied，occ_loss 非零确认标签被正确加载和使用
4. **无 NaN、无 OOM**: 20 步零错误完成
5. **VRAM 共存**: 提取进程 10 × 557MiB = 5.6GB + dry-run ~62GB，cuda:3 总 97.9GB 足够
6. **occ_detach=false**: 梯度回传到 vision encoder 正常（DDP grad stride warning 是已知无害警告）
7. **occ_index.json 加载成功**: 日志确认 "Loaded occ index: 10 tasks"
8. **occ_head 参数**: 1,213,313（1.2M），相对 action_head 151M 很轻量

### 注意事项
- 使用的是 dummy 随机 occ 数据（提取进程仍在运行，真实 HDF5 被锁定）
- 真实数据可用后需要重新验证 occ_loss 的绝对值范围
- print 语句已回滚，finetune.py 恢复原状

---
