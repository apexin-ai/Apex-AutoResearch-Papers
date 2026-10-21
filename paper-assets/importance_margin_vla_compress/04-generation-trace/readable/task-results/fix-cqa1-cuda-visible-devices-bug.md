# fix cqa1 cuda visible devices bug

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_cqa1_cuda_visible_devices_bug_20260528T003320_result.json`
- **Structured JSON:** [`dc7f32eab165ef7c70a3.json`](../../sessions/dc/dc7f32eab165ef7c70a3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Process starting correctly, loading pi0.5 model. Here's the full diagnostic report.

---

## 诊断报告：cqa1-33015

### 1. GPU 分布实况（修复前）

| 物理 GPU | 显存占用 | 利用率 | 进程 |
|----------|---------|--------|------|
| **GPU 0** | 21125 MiB | 33% | PID 765078 (random_k05) **+ PID 801342 (random_k095)** |
| GPU 1 | 10543 MiB | 28% | PID 797637 (l2norm_k095) |
| GPU 2 | 4 MiB | 0% | **空闲** |
| GPU 3 | 3 MiB | 0% | **空闲** |

**Bug 根因：** `random_k095` 的命令中缺少 `CUDA_VISIBLE_DEVICES=3`，`--gpu 0` 直接映射到物理 GPU 0，与 `random_k05` 挤在同一张卡。

### 2. 各实验进度

| 实验 | PID | 实际 GPU | 进度 | 决定 |
|------|-----|---------|------|------|
| random_k05 s44 | 765078 | GPU 0 ✓ | **6/10 (60%)**, T5 刚完成，SR=59.3% | **保留** |
| l2norm_k095 s44 | 797637 | GPU 1 ✓ | **6/10 (60%+)**, T6 进行中，SR=96.7% | **保留** |
| random_k095 s44 | 801342 | GPU 0 ✗ | **4/10 (40%)**, T4 进行中，SR=77.0% | **已杀** |

### 3. 杀/留决定

- **random_k05 (60%)** — 保留。虽然之前与 random_k095 共享 GPU 0 拖慢速度，现在已独占，后续 4 个 task 会加速。
- **l2norm_k095 (60%+)** — 保留。GPU 1 独占运行正常，成绩极好 (96.7%)。
- **random_k095 (40%)** — **已杀。** <50% 阈值 + 在错误 GPU 上。

### 4. 重启结果

- 新实验：`eval_pi05_random_k095_long_seed44_strict_cqa1_v2`
- 新 PID：**894072**
- GPU：**cuda:3**（命令含 `CUDA_VISIBLE_DEVICES=3`）
- 状态：模型加载中，log 确认启动正常

### 5. 修复后 GPU 状态

| GPU | 状态 | 实验 |
|-----|------|------|
| 0 | 占用 | random_k05 s44 (60%, 独占) |
| 1 | 占用 | l2norm_k095 s44 (60%+) |
| **2** | **空闲** | **可部署** |
| 3 | 启动中 | random_k095 s44 v2 (重启) |

### 6. GPU 2 候补建议

从 ROADMAP s44 优先级：
1. **Random k=0.7 s44** — 待确认是否 pending
2. Attn k=0.85 s44 — 已在 westd-38929 运行
3. Attn k=0.5 s44 — 已在 westd-38929 运行

**GPU 2 空闲，等待指令部署。**

---
