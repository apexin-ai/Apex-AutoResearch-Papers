# diagnose urgent gpu status check

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_urgent_gpu_status_check_20260521T042114_result.json`
- **Structured JSON:** [`ff5c9154e28ade2e1396.json`](../../sessions/ff/ff5c9154e28ade2e1396.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇总

| 项目 | 状态 | 详情 |
|------|------|------|
| **cuda:0 (Object)** | ALIVE | PID 513523 · Phase 2 R² probing · L0-L8 done, ~L12-13 now · ~14min/层, 预计还需 ~4.5h |
| **cuda:1 (NORA Goal v2)** | ALIVE | PID 526944 · Phase 2 R² probing · L0 done · ~25min/层, 刚开始 |
| **Phi-3-Vision download** | ⚠️ 挣扎中 | PID 521338 · 584MB/~8GB · 11/21 files · HF 大文件反复 ReadTimeout，正在重试 |
| **NORA Spatial ckpt** | ❌ 失败 | 447MB/~5GB · ChunkedEncodingError: 仅下载 197MB/4.76GB 后断连 · **进程已死** |
| **OFT ckpt (Long)** | 进行中 ~95% | PID 522184 (aria2c) · 15GB · model 1-3 完成, model-4 + action_head + lora adapter 还在下 |
| **LIBERO-Long data** | ✅ 完成 | 10 个 hdf5 文件 |

### Phase 2 中间结果（目前产出的 R² 值）

**Object (OpenVLA, cuda:0)**:
| Layer | img_mean R² | last_pre R² |
|-------|------------|------------|
| L0 | 0.6952 | 0.5710 |
| L8 | 0.6727 | 0.6753 |

**NORA Goal v2 (cuda:1)**:
| Layer | img_mean R² | last_pre R² |
|-------|------------|------------|
| L0 | 0.6081 | 0.5864 |

### 需要处理的问题

1. **NORA Spatial 下载需要重启** — 进程已死，只下了元数据文件，主模型 safetensors 断连。建议用 `HF_HUB_DISABLE_XET=1` 重新启动，或改用 ModelScope 下载。

2. **Phi-3-Vision 下载极慢** — HF 代理反复超时。如果持续失败，应 kill 后改用 ModelScope（`microsoft/Phi-3-vision-128k-instruct` 在 ModelScope 有镜像）。

3. **两个实验 GPU util 0%** — 正常，Phase 2 的 sklearn MLP probing 是 CPU-bound 操作，GPU 内存占用但不做计算。

---
