# ops anon repo push

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_anon-repo-push_20260523T131451_result.json`
- **Structured JSON:** [`029d4ee2541026f9dd77.json`](../../sessions/02/029d4ee2541026f9dd77.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**报告：**

| 项目 | 值 |
|------|-----|
| Repo URL | https://github.com/anonymous-nlp-2026/persuasion_turn_jailbreak_detect |
| 文件数量 | 579 |
| Commit hash | `74298e0` |
| 总大小 | 23M |
| Git author | Anonymous \&lt;anonymous@example.com\> |

**匿名化处理：**
- API key（`tum_XXB3sZI...`）→ `YOUR_API_KEY`（2个文件：`llm_judge_gpt41.py`, `llm_judge_gpt55.py`）
- `/root/autodl-tmp/hf_cache` → `./cache`
- `/root/persuasion_turn_jailbreak_detect` → `.`
- `/root/miniconda3/bin/python` → `python3`
- `hf-mirror.com` → `huggingface.co`
- 本地 DeBERTa snapshot 路径 → `microsoft/deberta-v3-base`
- 本地 RoBERTa/BERT 路径 → 标准 HuggingFace model name
- 删除了 `.bak`、`.disabled` 等无用文件
- 补拉了 `src/data/`（dataset.py, collator.py）因 rsync 排除了 `data/`

**未包含：** `paper/`、`data/`、`checkpoints/`、`docs/`、`figures/`、`artifacts/`（除 results JSON）

**未发现的敏感项：** 个人姓名（caoxiaoyu、周俊伟、张默涵、曹晓玉）均未出现在代码中，无需替换。

---
