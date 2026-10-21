# infra P0 disk cleanup and resume occ

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_P0_disk_cleanup_and_resume_occ_20260521T044117_result.json`
- **Structured JSON:** [`078b95e86e2fa2cb79f0.json`](../../sessions/07/078b95e86e2fa2cb79f0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。汇报如下：

---

## 第 1 步：清理
- 清理前: 350G/350G (100%)
- 清理后: 66G/350G (19%)，释放 284G
- 保留 checkpoint:
  - s0: `occ_s0/...-42500_chkpt`
  - s1: `occ_s1/...-17500_chkpt`
  - s2: `occ_s2/...-42500_chkpt`

## 第 2 步：轮转脚本
- PID: 71055
- 状态: running

## 第 3 步：训练恢复
- occ_s0: wrapper PID 71392, python PID 71469, cuda:0
- occ_s1: wrapper PID 72538, python PID 72614, cuda:1
- occ_s2: wrapper PID 73694, python PID 73770, cuda:2

## 第 4 步：验证
- GPU 占用: GPU0=62203MiB/99%, GPU1=62203MiB/44%(刚启动), GPU2=62165MiB/99%, GPU3=0MiB(未使用)
- 磁盘: 66G/350G (19%)
- 参数验证: 三个进程 cmdline 均包含 `--num_images_in_input 2`, `--use_proprio True`, `--occ_detach false`, `--use_occ_head True` ✓
- 速度: s0=~1.09 it/s (step 76), s1=~1.09 it/s (step 45), s2=~1.05 it/s (step 12, 刚启动在加速)
- OCC loss: s0=0.0086, s1=0.0140, s2=0.0111 (resume 后首个 step)
- **注意**：用的是 `conda activate occsafe` 而非任务描述中写的 base（base 环境缺少 draccus 等依赖）
- 问题: 无

---
