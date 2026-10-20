# code trajectory pipeline design

**error type pref optim** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_trajectory-pipeline-design_20260514T094752_result.json`
- **Structured JSON:** [`f5bc375053f0e77a968a.json`](../../sessions/f5/f5bc375053f0e77a968a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 4 个脚本 dry-run 通过。汇总：

## Phase A 数据采集 Pipeline 部署完成

**服务器路径**: `/root/error_type_pref_optim/`

| 脚本 | 大小 | 功能 | Dry-run |
|------|------|------|---------|
| `generate_trajectories.py` | 10,243B | Qwen3-8B 在 ALFWorld 生成 ~200 条轨迹 | **PASS** |
| `classify_errors.py` | 12,548B | 零样本 LLM 错误分类 (action/verification/planning) | **PASS** |
| `measure_correction_horizon.py` | 14,184B | 每个失败步 N=10 次纠正续写，测量 correction horizon | **PASS** |
| `analyze_correction_spans.py` | 11,093B | 统计分析 + Mann-Whitney U + 可视化 | **PASS** |

**执行顺序**:
```
generate_trajectories.py → classify_errors.py → measure_correction_horizon.py → analyze_correction_spans.py
```

**数据流**:
```
data/trajectories.jsonl → data/classified_trajectories.jsonl → data/correction_measured_trajectories.jsonl → data/correction_analysis_summary.json + PDF plots
```

**ETO 仓库结构概述** (脚本设计参考):
- `ETO/eval_agent/envs/alfworld_env.py` — ALFWorld 环境交互接口 (parse_action, process_ob, step)
- `ETO/eval_agent/tasks/alfworld.py` — 任务加载 (train/dev/test splits: 3321/140/134)
- `ETO/eval_agent/prompt/` — ICL 指令和示例 (conversation 格式)
- `ETO/eval_agent/data/alfworld/base_config.yaml` — 环境配置
- 模型路径: `/root/error_type_pref_optim/models/Qwen3-8B` (ModelScope 下载中)

**注意**: Qwen3-8B 模型仍在通过 ModelScope 下载中（上次检查时 `._____temp/` 目录存在 `.incomplete` 文件），模型下载完成后即可执行 pipeline。

---
