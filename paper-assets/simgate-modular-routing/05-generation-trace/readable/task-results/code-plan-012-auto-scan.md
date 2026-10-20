# code plan 012 auto scan

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan-012-auto-scan_20260513T233117_result.json`
- **Structured JSON:** [`ab57864c5e4363ac9e56.json`](../../sessions/ab/ab57864c5e4363ac9e56.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本已经完全支持自动扫描，无需修改。

**确认结果：**

1. **数据输入方式**：`--data_dirs` 接受逗号分隔的目录列表（line 467, 477）
2. **自动扫描**：`load_episodes()` 遍历每个 data_dir，用 `os.listdir()` 扫描所有子目录，检查是否有 `episodes.jsonl`（line 84-86）
3. **自动合并**：使用 `defaultdict(list)`（line 79），同一 task_name 在多个目录中出现时自动合并所有 episodes
4. **容错**：目录不存在时跳过并打印 WARN（line 82-83）

**plan_c 当前数据**：已有 4 个 task 完成 —— `find-non-living-thing`, `find-animal`, `grow-fruit`, `identify-life-stages-1`

**plan-001b 完成后的运行命令**：
```bash
python src/death_decomposition.py --data_dirs results/prescreening,results/mvp,results/research,results/plan_c --output results/decomposition_final/death_decomposition_report.json --paper_table results/decomposition_final/paper_table1_data.json
```

不需要改代码，脚本已具备全部所需功能。

---
