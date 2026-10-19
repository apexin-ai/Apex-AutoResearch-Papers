# ssh a1 batchsize fix restart

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_a1_batchsize_fix_restart_20260520T001855_result.json`
- **Structured JSON:** [`b57c254aca031b141163.json`](../../sessions/b5/b57c254aca031b141163.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 产出总结

### 1. A1 实际 batch_size
**batch_size=32**（脚本默认值，命令行未覆盖）。不需要 kill 重启。

### 2. VRAM 13.4GB 的原因
A1 采用两阶段训练：
- **Phase 1** (step 0–5000): backbone 冻结，只训练 SDF decoder + EE extractor heads → VRAM 低是正常的
- **Phase 2** (step 5000+): 解冻 backbone 端到端训练 → VRAM 预计跳到 ~37GB+

当前 step=1061，仍在 Phase 1。

### 3. 训练状态
- Step: 1061/30000，运行 1h04m
- Loss: ~0.22–0.31（正常范围）
- lr: 2.50e-05（warmup 完成）
- 速度: ~3.5s/step

### 4. 默认值修复
| 脚本 | 修复前 | 修复后 |
|------|--------|--------|
| `train_a1_sdf_aux.py` | default=32 | ✅ 已经正确 |
| `train_a3_hook.py` L375 | default=2 | ✅ 改为 32 |

### 5. 不需要新 PID
A1 (PID 117519) 正常运行中，无需重启。

---
