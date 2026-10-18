# code step3 5 pipeline prep

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_step3-5-pipeline-prep_20260522T145553_result.json`
- **Structured JSON:** [`2a0e5a892fce43ef20b6.json`](../../sessions/2a/2a0e5a892fce43ef20b6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇报：

## 汇报

### 1. 各脚本原数据加载方式
| 脚本 | 原来 | 变化 |
|------|------|------|
| Step 3 (MI) | 3 个函数: `load_local_clean_scores` + `load_api_clean_scores` + `merge_clean_scores` | → `clean, _ = load_all_scores()` |
| Confound | 3 个函数: `load_local_individual_asr` + `load_api_individual_asr` + `merge_asr` | → `load_all_scores()` + `load_pairs()` + 统一 ASR 计算 |
| Step 4 | 3 个函数: `load_mi_data` + `load_pairs` + `load_all_scores`（本地定义） | → 从 unified_data_loader 导入 |
| Step 5 | 与 Step 4 完全重复的 3 个函数 | → 从 unified_data_loader 导入 |

### 2. 完成项
- **统一加载器** `src/unified_data_loader.py` — 已创建并验证
  - 导出: `ALL_MODELS(15)`, `DATASETS`, `ATTACKS`, 所有路径常量
  - 函数: `load_all_scores()`, `load_pairs()`, `load_mi_data()`, `load_api_asr()`, `validate_coverage()`
  - 自动处理 checkpoint 嵌套格式 + individual JSON 格式
  - position_bias winner 反转统一处理
- **4 个脚本** — 已全部改用统一加载器，去除重复代码
- **Pipeline 启动脚本** `scripts/run_pipeline_15model.sh` — 已创建并设为可执行
- **目录结构** `individual_scores/` — 已就绪

### 3. 验证结果
- `loader OK` — import 验证通过
- 4 个脚本语法检查全部通过
- 当前数据: 8/15 模型 (6 local + haiku + gpt-4o partial)
- C(15,2)=105 pairs, C(15,3)=455 panels, 12 conditions 确认

### 4. Scoring 完成后操作步骤
```bash
# 1. 从本地 scp 9 个 API 模型的 scoring 结果
scp /path/to/individual_scores/*__*.json seetacloud-rtx6000:/root/cert_manip_resist_eval/artifacts/results/plan001/individual_scores/

# 2. 一键启动 pipeline
ssh seetacloud-rtx6000 'bash /root/cert_manip_resist_eval/scripts/run_pipeline_15model.sh'
```

缺 7 个 API 模型的数据 (claude-opus-4, claude-sonnet-4, gpt-5.5, gpt-4.1, gpt-4o-mini, gemini-2.5-pro, gemini-2.5-flash)，加上 gpt-4o 缺 arc_challenge 的 5 个攻击条件。数据到位后零配置启动。

---
