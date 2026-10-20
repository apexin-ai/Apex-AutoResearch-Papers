# ops 14b global scan v2

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_14b-global-scan-v2_20260522T200908_result.json`
- **Structured JSON:** [`50c82c4b5b763547419e.json`](../../sessions/50/50c82c4b5b763547419e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 1.4B 实验状态汇总

### 完成的实验

| Cell | Server | gen_10 | Analysis | Status |
|------|--------|--------|----------|--------|
| scale/14b_c4_s42_fp32 | 17855 | Done | Yes | **Complete** |
| scale/14b_a050_s42_fp32 | 19828 | Done | Yes | **Complete** |
| t10_a050_s42_fp32_14b | 19828 | Done | Yes | **Complete** |
| t10_a060_s42_fp32_14b | 17855 | Done | Yes | **Complete** |
| t10_a075_s42_fp32_14b | 17855 | Done | Yes | **Complete** |

### 运行中的实验

| Cell | Server:GPU | 当前 gen | 目标 gen | Step | 预估 |
|------|-----------|---------|---------|------|------|
| t10_a045_s42_fp32_14b | 17855:GPU4 | gen 6 训练中 | 10 | 4457/5000 (89%) | ~4 gen 剩余 |
| t15_a050_s42_fp32_14b | 17855:GPU0 | gen 10 训练中 | 15 | — | ~5 gen 剩余 |
| t15_a060_s42_fp32_14b | 17855:GPU1 | gen 10 训练中 | 15 | — | ~5 gen 剩余 |
| t15_a045_s42_fp32_14b | 17855:GPU5 | gen 8 训练中 | 15 | — | ~7 gen 剩余 |
| t10_a075_s42 restart | 17855:GPU3 | gen 10 生成合成数据 | 10 | synth gen | 即将完成 |
| t15_a075_s42_fp32 | 19828:GPU0 | gen 6 训练中 | 15 | 4646/5000 (93%) | ~9 gen 剩余 |

### 异常

| Cell | Server | 问题 |
|------|--------|------|
| t10_a050_s42_fp32_14b | 17855 | 目录存在但 **无任何 gen metrics**（已在 19828 完成，可能是废弃目录） |

### 空闲 GPU

| Server | GPU | 显存 | 状态 |
|--------|-----|------|------|
| **17855** | GPU 2 | 0 / 98 GB | **空闲** |
| **19828** | GPU 1 | 0 / 98 GB | **空闲**（t10_a050 tmux 会话残留但进程已结束） |

---
