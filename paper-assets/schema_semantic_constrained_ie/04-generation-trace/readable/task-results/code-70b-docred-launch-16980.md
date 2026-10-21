# code 70b docred launch 16980

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_70b_docred_launch_16980_20260518T124003_result.json`
- **Structured JSON:** [`1eb2db44fe5e549b96fc.json`](../../sessions/1e/1eb2db44fe5e549b96fc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 GPU 都在满负载运行。

**汇报：**

| 实验 | exp_id | GPU | PID | 日志 |
|------|--------|-----|-----|------|
| DocRED unconstrained | `70b_docred_unconstrained` | cuda:0 | 556552 | `~/runs/schema_semantic_constrained_ie/70b_docred_unconstrained.log` |
| DocRED constrained (full_s1) | `70b_docred_constrained` | cuda:1 | 556631 | `~/runs/schema_semantic_constrained_ie/70b_docred_constrained.log` |

**环境修复：**
- 模型从 westd-21461 scp 完成（38GB，9 个 shard）
- transformers 从 4.57.6 升级到 5.8.1（4.57.6 的 autoawq 兼容性问题）
- 安装 gptqmodel 7.0.0（transformers 5.8.1 的 AWQ 后端要求）
- Marlin fp16 CUDA 扩展已编译缓存

**模型加载正常：** 每张 GPU 占用约 39GB 显存，利用率 ~88%。

**补充说明：** 用户给的命令缺少 `--data_path data/docred/dev.json` 和 `--constraints_path data/docred/ontology_constraints_docred.json`，已自动补上。

**预估运行时间：** DocRED dev 集 998 篇文档，文档长度远大于 SciERC 句子，70B 模型单文档推理较慢，预计 8-15 小时。constrained 模式因额外约束计算会更慢。

---
