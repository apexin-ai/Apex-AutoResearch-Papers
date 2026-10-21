# code exp wiki v2 fix and submit

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_wiki_v2_fix_and_submit_20260517T114130_result.json`
- **Structured JSON:** [`4dce7b517807c479034e.json`](../../sessions/4d/4dce7b517807c479034e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验都在正常运行 depth 1 生成阶段。

**完成总结：**

| 任务 | 状态 |
|------|------|
| 修复 `run_pipeline.py` skip-if-exists 逻辑 | ✓ 添加 model_name 参数、mismatch 检测、metadata 嵌入 |
| Git commit | ✓ `0b10b43` |
| 数据目录准备 | ✓ `data/exp_wiki_pythia/` 和 `data/exp_wiki_olmo/` 各 5000 行 depth_0.jsonl |
| exp_wiki_pythia_v2 (cuda:2) | ✓ 运行中，Pythia-1.4B continuation |
| exp_wiki_olmo_v2 (cuda:3) | ✓ 运行中，OLMo-1B-hf continuation |
| Registry 更新 | ✓ 两个实验 RUNNING，spec 含 data_path/model_name/seed/git_commit |

---
