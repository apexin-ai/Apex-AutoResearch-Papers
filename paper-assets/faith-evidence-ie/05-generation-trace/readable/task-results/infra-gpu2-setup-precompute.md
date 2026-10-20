# infra gpu2 setup precompute

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_gpu2-setup-precompute_20260514T070013_result.json`
- **Structured JSON:** [`275b3dbee82ff631cad0.json`](../../sessions/27/275b3dbee82ff631cad0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

NLI 预计算正在运行，速度约 490 samples/s。38180 个样本预计 ~80 秒完成。

汇总：

| 步骤 | 状态 |
|------|------|
| 环境探测 | 4x RTX 5090, conda base, torch 2.10.0+cu128 |
| 依赖安装 | 全部已预装，无需额外安装 |
| 代码部署 | `docred_processor.py`, `ced_reward.py`, `ced_signal_validation.py` + 所有 `__init__.py` |
| DocRED 数据 | train 3053 docs (38180 relations), dev 998 docs |
| DeBERTa 模型 | `cross-encoder/nli-deberta-v3-base` 已缓存 |
| NLI 预计算 | **RUNNING** on cuda:0, ~490 samples/s, exp_id=`precompute_nli_train` |

输出将保存到 `/root/autodl-tmp/data/docred/train_nli_cache.json`。日志在 `~/runs/faith-evidence-ie/precompute_nli_train.log`。

---
