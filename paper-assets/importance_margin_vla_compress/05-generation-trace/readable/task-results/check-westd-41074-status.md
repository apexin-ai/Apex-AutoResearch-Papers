# check westd 41074 status

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_westd-41074-status_20260522T015415_result.json`
- **Structured JSON:** [`9c98a81d7dbc07928048.json`](../../sessions/9c/9c98a81d7dbc07928048.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### GPU 状态
| GPU | 显存占用 | 利用率 | 状态 |
|-----|---------|--------|------|
| cuda:0 | 0 / 98GB | 0% | **空闲可用** |
| cuda:1 | 3 / 98GB | 0% | **空闲可用** |
| cuda:2 | 28.6 / 98GB | 0% | 训练 M96 占用 |
| cuda:3 | 27.5 / 98GB | 0% | 训练 M64v6 占用 |

### 进程状态

| exp_id | PID状态 | GPU | SR(%) | 完成时间 | 备注 |
|--------|---------|-----|-------|---------|------|
| train_openvla_sc_m96_seed42 | 68539 ALIVE (1d22h) | cuda:2 | — | ETA ~10.4h | step 81250/100000, 0.5 sps |
| train_openvla_sc_m64_seed42_v6 | 59671 ALIVE (16h38m) | cuda:3 | — | ETA ~30.5h | step 34050/100000, 0.6 sps |
| eval_pi05_l2norm_k095_object_seed42_v2 | DONE | — | **98.2%** | 09:35 UTC+8 | 491/500, 成功 |
| eval_pi05_l2norm_k085_object_seed42_v4 | DONE | — | **98.0%** | 09:36 UTC+8 | 490/500, 成功 |
| eval_pi05_l2norm_k095_object_seed42 | 816380 DEAD | — | — | — | 崩溃: lerobot groot dataclass TypeError |
| eval_pi05_l2norm_k085_object_seed42_v3 | 816297 DEAD | — | — | — | 同上崩溃 |
| eval_openvla_sc_m64_50k_seed42 | 736865 DEAD | — | — | — | 崩溃: checkpoint 损坏 (zip archive) |
| PID 711846, 709434, 46032, 43102 | ALL DEAD | — | — | — | — |

### 关键发现

1. **cuda:0 和 cuda:1 空闲可用**

2. **已完成的 eval 结果**（来自 v4/v2 重试版本）:
   - Pi0.5 + L2norm k=0.95 → **SR 98.2%** (keep 243/256 tokens)
   - Pi0.5 + L2norm k=0.85 → **SR 98.0%** (keep 217/256 tokens)
   - Pi0.5 + Random k=0.925 → **SR 27.6%** (keep 236/256 tokens) — 对比 l2norm 差距极大

3. **失败原因**:
   - PID 816380/816297: `lerobot` 包升级后 `groot_n1.py` 的 dataclass 字段顺序冲突（`non-default argument 'backbone_cfg' follows default argument`）
   - PID 736865: M64 50k checkpoint 文件损坏（`checkpoint_step50000.pt` 不存在，只有 10k/20k/30k）— 当时训练还没到 50k

4. **训练进度**:
   - M96: 81.25% 完成，约 10.4h 后完成
   - M64v6: 34.05% 完成，约 30.5h 后完成（从 step 0 开始的全新训练）

---
