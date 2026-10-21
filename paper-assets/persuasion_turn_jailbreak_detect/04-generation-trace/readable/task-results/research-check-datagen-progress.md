# research check datagen progress

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_check-datagen-progress_20260519T143452_result.json`
- **Structured JSON:** [`1cc16ad873c91d7e0a19.json`](../../sessions/1c/1cc16ad873c91d7e0a19.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 检查结果汇总

### exp16 (Llama Crescendo)

| 项目 | 状态 |
|------|------|
| **脚本** | 已创建 |
| **jailbreak 脚本** | `/root/persuasion_turn_jailbreak_detect/scripts/generate_crescendo_llama.py` (26KB) |
| **benign 脚本** | `/root/persuasion_turn_jailbreak_detect/scripts/generate_benign_llama.py` |
| **数据** | dry-run 已完成，仅 **2 条** jailbreak 对话 |
| **数据路径** | `data/llama_conversations/crescendo_jailbreak_llama.jsonl` (2 行, 36KB) |
| **进度文件** | `crescendo_jailbreak_llama.jsonl.progress` (59KB, 支持断点续传) |
| **dry-run** | 成功 (EXIT_CODE=0)，2 条对话耗时 2.1 min |
| **模型** | 已缓存在 `/root/autodl-tmp/hf_cache/meta-llama/Llama-3.1-8B-Instruct` |
| **tmux** | `llama_crescendo_dryrun` session 存在，dry-run 进程正在运行 |

脚本功能完整：8 个 playbook、30 个 harmful goals、断点续传、benign 模式。

### exp17 (Qwen expanded)

| 项目 | 状态 |
|------|------|
| **脚本** | **未创建** — 没有 `generate_crescendo_expanded*.py` |
| **数据目录** | **不存在** — 没有 `data/expanded_conversations/` |
| **进度** | 零 |

Worker 在创建 Qwen expanded 脚本之前就被中断了。

### 可复用 vs 需重做

**可直接复用：**
- `generate_crescendo_llama.py` — 完整可用，支持 resume
- `generate_benign_llama.py` — 完整可用
- Llama 模型缓存 — 无需重新下载
- 原始 `generate_crescendo.py`（Qwen vLLM 版）— 可参考其 playbook/goal 设计

**需要重做：**
1. Llama jailbreak 全量生成（目标 250 条，已完成 2 条 dry-run，脚本支持续传）
2. Llama benign 全量生成（0 条，脚本已就绪）
3. Qwen expanded 生成脚本（需从零编写）
4. Qwen expanded 数据生成（需脚本就绪后启动）

---
