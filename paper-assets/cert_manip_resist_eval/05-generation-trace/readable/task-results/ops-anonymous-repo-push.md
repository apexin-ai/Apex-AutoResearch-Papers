# ops anonymous repo push

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_anonymous-repo-push_20260525T084125_result.json`
- **Structured JSON:** [`38b7b5e28e432db48529.json`](../../sessions/38/38b7b5e28e432db48529.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 汇报

### (a) PAT 有效性
**有效** — fetch 和 push 均成功。

### (b) 推送时间戳
**2026-05-25**，force-push 到 `main` 分支，commit `efef31f`。

### (c) 仓库内容清单（79 文件）

| 目录 | 文件数 | 内容 |
|------|--------|------|
| `src/` | 11 | 核心库：attacks, config, correlation, eval_pipeline, judge_service, keff, panels, scaling, unified_data_loader, utils, __init__ |
| `scripts/` | 56 | 实验脚本 + 3 个 shell 脚本（run_all.py 为总入口） |
| `scoring/src/` | 6 | API 评分模块 |
| `scoring/scripts/` | 1 | API 批量评分脚本 |
| `data/` | 1 | README 占位 |
| 根目录 | 4 | README.md, requirements.txt, .gitignore, run_temperature_pilot.py |

### (d) 匿名性检查结果

| 检查项 | 结果 |
|--------|------|
| Git author/committer 为 `anonymous &lt;anonymous@anonymous.invalid>` | **PASS** |
| README/LICENSE/代码注释无真名、机构名 | **PASS** |
| 所有 `.py` docstring/comment 无身份泄露（@xxx.edu, university, institute, lab, author） | **PASS** |
| 无硬编码 API key（已替换为 `os.environ.get(...)`) | **PASS** |
| 无硬编码服务器路径 `/root/...`（已替换为相对路径） | **PASS** |
| requirements.txt 无身份信息 | **PASS** |
| .gitignore 已添加，无临时文件/缓存 | **PASS** |

仓库地址：`https://github.com/anonymous-nlp-2026-2/cert_manip_resist_eval`

---
