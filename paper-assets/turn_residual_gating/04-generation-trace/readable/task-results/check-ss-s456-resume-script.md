# check ss s456 resume script

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_ss_s456_resume_script_20260523T114850_result.json`
- **Structured JSON:** [`55f8b8d034baee4e177e.json`](../../sessions/55/55f8b8d034baee4e177e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

信息已全部收集完毕。汇报如下：

---

### Resume 脚本确认

**脚本**: `scripts/d048_ss_s456_resume.sh`

**关键参数**:
- `--resume runs/d048_ss_s456/epoch_0` — 指向 epoch_0 checkpoint
- `--epochs 3` — 总 epoch 数仍写 3

**Checkpoint 存在性**: `runs/d048_ss_s456/epoch_0/` 存在，包含：
- `gate_params.pt` (3.4MB)
- `lora/` 目录

**Resume 逻辑** (`train_phase2_v8b.py:228-230`):
```python
_m = re.search(r'epoch_(\d+)', args.resume)
start_epoch = int(_m.group(1)) + 1 if _m else 1
```
从路径中提取 epoch 编号 0，`start_epoch = 0 + 1 = 1`。训练从 **epoch 1 开始**，跳过 epoch 0。

**预计训练量**: `--epochs 3` 意味着训练 epoch 1 和 epoch 2（共 2 个 epoch），**预计约 7 小时**。

---
