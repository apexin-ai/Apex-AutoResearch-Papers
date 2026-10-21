# infra westd 14391 env setup

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_westd-14391-env-setup_20260522T163849_result.json`
- **Structured JSON:** [`b446f442c6e4307dc7bc.json`](../../sessions/b4/b446f442c6e4307dc7bc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

环境搭建完成。汇报：

| 项目 | 状态 |
|------|------|
| **镜像** | 非预置镜像，conda 环境 (miniconda3) |
| **Python** | 3.12.3 (conda base) |
| **PyTorch** | 2.11.0+cu130, CUDA=True |
| **GPU** | 1× NVIDIA RTX PRO 6000 Blackwell (94GB VRAM) |
| **vLLM** | 0.21.0 |
| **transformers** | 5.9.0 |
| **z3-solver** | 4.15.4 |
| **scipy** | 1.17.1 |
| **scikit-learn** | 1.8.0 |
| **磁盘** | 根分区 19GB 可用, 数据盘 250GB 可用 |
| **项目代码** | `/root/autodl-tmp/symb_invariant_consensus/` (符号链接至 `/root/symb_invariant_consensus/`) |
| **sica 模块** | import OK |
| **数据文件** | folio_full.json, proofwriter_full.json 等已就位 |
| **env_activate** | resources.yaml 已更新 |

服务器就绪，可以跑 multi-seed 实验。

---
