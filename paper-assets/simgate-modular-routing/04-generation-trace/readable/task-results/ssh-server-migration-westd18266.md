# ssh server migration westd18266

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_server-migration-westd18266_20260518T060123_result.json`
- **Structured JSON:** [`510e0be52dc59f975bea.json`](../../sessions/51/510e0be52dc59f975bea.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 迁移汇报

| 项目 | 状态 |
|------|------|
| **GPU** | 4× RTX PRO 6000 Blackwell, SM 12.0, Driver 580.95.05, CUDA 13.0, 每卡 ~96GB |
| **代码迁移** | 完整 (729 files, src/, crafter_pilot/, 全部脚本) |
| **模型迁移** | 完整 (Qwen2.5-7B-Instruct, 15.2GB) |
| **数据迁移** | 完整 (results/ 下所有实验 JSON: backbone_72b, reflexion_baseline, retry_dose_response) |
| **Python 环境** | Python 3.12.3, vLLM 0.21.0, torch 2.11.0, transformers 5.8.1, crafter 1.8.3, scienceworld 1.2.3 |
| **dry-run** | 通过。10 个 task × 1 episode × 5 steps 全部正常完成 |
| **额外安装** | Java JRE (ScienceWorld 依赖), scienceworld 包 |
| **注意事项** | Blackwell GPU 需要 `VLLM_USE_FLASHINFER_SAMPLER=0` |

全量实验未启动，环境已就绪。

---
