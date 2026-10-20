# code anonymous repo push

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_anonymous_repo_push_20260523T132336_result.json`
- **Structured JSON:** [`be0166e94f4e80ec6f1d.json`](../../sessions/be/be0166e94f4e80ec6f1d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。汇报：

| 项目 | 结果 |
|------|------|
| **Repo URL** | https://github.com/anonymous-nlp-2026/struct_self_consist_ie |
| **文件数** | 330 |
| **Commit 数** | 1 (`Anonymous submission for review`) |
| **Git author** | `Anonymous &lt;anonymous@example.com>` |
| **匿名化检查** | CLEAN — 无 `caoxiaoyu`、`qq.com`、`/root/`、`autodl`、机构名等泄露 |

包含内容：
- `code/` — 核心模块（sampling, consistency, evaluation, unified_metrics, data_utils）+ 全部分析脚本（200+ 文件）
- `scripts/` — 实验后处理脚本
- `configs/` — train/export/lora 配置（路径已替换为 `./models/` 等通用路径）
- `experiments/` — 跨任务 pilot（FewRel RE, HumanEval code）
- `examples/` — DeepSpeed 配置
- 顶层 `.py`/`.sh` — 实验启动脚本
- `README.md` — 去身份化的复现说明
- `.gitignore` — 排除数据/checkpoint/日志

---
