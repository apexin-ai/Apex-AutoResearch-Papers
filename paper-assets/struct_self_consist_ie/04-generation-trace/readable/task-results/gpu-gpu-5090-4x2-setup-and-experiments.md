# gpu gpu 5090 4x2 setup and experiments

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_gpu_gpu_5090_4x2_setup_and_experiments_20260514T120440_result.json`
- **Structured JSON:** [`daf904b2a33d7da7c478.json`](../../sessions/da/daf904b2a33d7da7c478.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

**环境**: gpu-5090-4x-2 已有完整环境（torch 2.10.0+cu128, vllm 0.18.1, transformers 4.57.1, 4× RTX 5090 32GB），代码/模型/数据已同步，无需额外安装。

**实验状态**:

| 实验 | GPU | 状态 | tmux session |
|------|-----|------|-------------|
| exp-001 seed=123 | cuda:0 | **已完成** | exp001_seed123 |
| exp-001 seed=456 | cuda:1 | 运行中 (~40%) | exp001_seed456 |
| exp-008 RE N=16 | cuda:2 | 运行中 (刚启动) | exp008_re_n16 |

**Registry**: `exp_001_n16_seed123`, `exp_001_n16_seed456`, `exp_008_re_n16` 均已更新为 RUNNING。

**注意**: 初次提交时 3 个 vLLM 实例同时初始化导致跨 GPU 内存竞争，seed456 和 exp008 失败。错开启动后解决。结果在 `output/exp001_n16_seed123/`（已生成 report.json），其余两个产出将分别在 `output/exp001_n16_seed456/` 和 `output/exp008_re_n16/`。

---
