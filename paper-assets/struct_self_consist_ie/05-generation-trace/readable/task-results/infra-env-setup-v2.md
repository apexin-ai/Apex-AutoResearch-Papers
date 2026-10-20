# infra env setup v2

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_env_setup_v2_20260514T050925_result.json`
- **Structured JSON:** [`749d6b55a0e2c5becb74.json`](../../sessions/74/749d6b55a0e2c5becb74.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

环境搭建完成。汇总：

| 项目 | 版本/信息 |
|------|----------|
| Python | 3.12.3 (conda base) |
| CUDA | 12.8 (driver 595.58.03) |
| PyTorch | 2.10.0+cu128 |
| vLLM | 0.18.1 |
| Transformers | 4.57.1 |
| Accelerate | 1.11.0 |
| Datasets | 4.0.0 |
| SciPy | 1.17.1 |
| LLaMA Factory | 0.9.4 |
| GPU | 4× RTX 5090 32GB |

所有依赖就绪，`env.sh` 已写入 `/root/autodl-tmp/struct_self_consist_ie/env.sh`，后续命令 `source env.sh` 即可激活完整环境。

---
