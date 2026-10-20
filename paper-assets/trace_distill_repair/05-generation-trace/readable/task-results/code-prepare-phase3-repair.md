# code prepare phase3 repair

**trace distill repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prepare_phase3_repair_20260514T194205_result.json`
- **Structured JSON:** [`6ca9d9bdf669f6df7115.json`](../../sessions/6c/6ca9d9bdf669f6df7115.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审查完成。以下是完整报告。

---

## Phase 3 审查报告

### 1. 代码文件清单

| 文件 | 用途 |
|------|------|
| `dtd_types.py` | 核心数据结构：`TraceEvent`, `TraceSegment`, `ScoredSegment`；提供 `serialize_event()`, `serialize_segment()` |
| `trace_collector.py` | 收集 buggy code 的 execution trace |
| `structural_segmenter.py` | 将 trace events 按 call_subtree / loop_iteration / exception_chain / basic_block 分段，最多 20 段 |
| `line_segmenter.py` | 基线方法：按固定窗口（window_size=5, stride=5）切分 trace events |
| `teacher_scorer.py` | Teacher LLM（deepseek-v4-flash）对 segment 打 keep/drop 标签 |
| `bugsinpy_setup.py` | BugsInPy 数据集管理：checkout buggy/fixed 代码，提供 45 个 candidate bugs |
| `run_phase2_scoring.py` | Phase 2 批量打分脚本：读取已有 segment 文件，调 teacher_scorer，输出 scores JSON |
| `mvp_pipeline.py` | **端到端 pipeline**（含 repair 逻辑）：4 条件 repair + 评估，有完整的 prompt 模板和 API client |
| `mvp_analysis.py` | MVP 结果分析：pass/kill 判定、win rate 计算、case study 选取 |
| `run_pipeline.py / v2 / v3` | 历史版本的 pipeline 运行脚本 |
| `run_new15.py` | batch 2（15 新实例）的 pipeline 脚本 |
| `run_phase2_3.py` | Phase 2+3 联合运行脚本 |

### 2. 数据文件位置和格式

| 数据 | 路径模式 | 格式 |
|------|---------|------|
| 原始 trace | `pipeline_output/{key}_trace.json` | `List[dict]`，每个 dict 含 event_type/function_name/filename/lineno/locals_snapshot/call_depth/timestamp/return_value/exception_info |
| Structural segments | `pipeline_output/{key}_structural_segments.json` | `List[dict]`，每个含 segment_type/start_idx/end_idx/metadata/token_estimate/events |
| Line segments | `pipeline_output/{key}_line_segments.json` | 同上，segment_type 为 `"line_window"` |
| Structural scores | `pipeline_output/phase2_structural_scores.json` | 4896 行，顶层含 mode/num_instances/results，results 下每个 instance 含 scores 数组（label/confidence/reasoning） |
| **Line scores** | **不存在** | Phase 2 line scoring **尚未执行** |
| Phase 1 summary | `pipeline_output/summary.json` | 全局 pipeline 摘要：event_counts、segmentation stats |

**关键发现**：
- 有效实例 38 个（trace 成功），但 `phase2_structural_scores.json` 排除了 fastapi_1/2/3/5 共 4 个，实际打分了 36 个
- **Line scores 缺失**：只有 `phase2_structural_scores.json`，没有 `phase2_line_scores.json`
- `mvp_results/` 目录为空，端到端 pipeline 未跑过

### 3. Phase 3 脚本需要的输入/输出

**输入**：
- `pipeline_output/{key}_trace.json` → full_trace condition
- `pipeline_output/{key}_structural_segments.json` → structural_filtered condition（需结合 scores 过滤）
- `pipeline_output/{key}_line_segments.json` → line_filtered condition（需结合 scores 过滤）
- `pipeline_output/phase2_structural_scores.json` → structural segment 的 keep/drop 标签
- `pipeline_output/phase2_line_scores.json` → **需要先运行 `python run_phase2_scoring.py --mode line`**
- `bugsinpy_workspace/instances/{key}/buggy/` → buggy source code
- `BugsInPySetup.CANDIDATE_BUGS` → instance descriptions（作为 issue_description）
- env var: `OPENROUTER_API_KEY`

**输出**：
- 每个 instance × 4 conditions 的 repair 结果 CSV
- 包含 instance_id, condition, repair_success, tokens_used, generated_fix, eval_method
- 分层分析：>2K token 子集按 structural segment count (≥5 vs <5) 报告 win rate

### 4. 已有可复用组件

| 组件 | 来源 | 可复用性 |
|------|------|---------|
| **REPAIR_PROMPT_TEMPLATE** | `mvp_pipeline.py` | 直接复用 |
| **TRACE_SECTION_TEMPLATE** | `mvp_pipeline.py` | 直接复用 |
| **OpenAI client 初始化** | `mvp_pipeline._get_repair_client()` | base_url + api_key 逻辑可提取 |
| **`_call_repair_llm()`** | `mvp_pipeline.py` | model=deepseek-v4-pro, temp=0.0, max_tokens=4096 |
| **`_build_repair_prompt()`** | `mvp_pipeline.py` | 组装 issue + code + trace_section |
| **`_evaluate_repair()`** | `mvp_pipeline.py` | exact_match → line_overlap → test_execution 三层评估 |
| **`_format_full_trace()`** | `mvp_pipeline.py` | 格式化完整 trace，带 8000 token 截断 |
| **`_format_filtered_trace()`** | `mvp_pipeline.py` | 格式化 ScoredSegment 列表 |
| **`load_segments()`** | `run_phase2_scoring.py` | JSON → TraceSegment 反序列化 |
| **`get_buggy_code()`** | `run_phase2_scoring.py` | 从 workspace 读 buggy source |
| **`discover_instances()`** | `run_phase2_scoring.py` | 扫描 pipeline_output 目录 |
| **`serialize_event()`** | `dtd_types.py` | TraceEvent → dict，处理 return_value 和 exception_info |
| **`EXCLUDED_INSTANCES`** | `run_phase2_scoring.py` | `{"fastapi_3", "fastapi_5"}` |
| **`ANNOTATIONS`** | `run_phase2_scoring.py` | 7 个实例标注（too_small/low_segment_count） |

### 5. 建议的 Phase 3 脚本结构

```python
# run_phase3_repair.py

def load_structural_scores(path) -> Dict[str, List[dict]]:
    """读 phase2_structural_scores.json，返回 {instance_key: [score_dicts]}"""

def load_line_scores(path) -> Dict[str, List[dict]]:
    """读 phase2_line_scores.json，同上"""

def build_trace_context(instance_key, condition, scores, segments, events) -> str:
    """
    根据 condition 构建 trace 文本：
    - no_trace: 返回 ""
    - full_trace: serialize 全部 events（用 serialize_event）
    - structural_filtered: 用 scores 中 label="keep" 过滤 segments，serialize
    - line_filtered: 同上
    """

def call_repair_llm(client, model, prompt) -> str:
    """调 deepseek-v4-pro，temp=0.0，max_tokens=4096"""

def evaluate_repair(generated_fix, fixed_code, test_command, buggy_dir, buggy_file) -> dict:
    """exact_match → line_overlap → test_execution"""

def compute_token_count(instance_key, events) -> int:
    """计算该实例 full trace 的 token 数，用于 >2K 子集判定"""

def count_structural_segments(instance_key, summary) -> int:
    """从 summary.json 获取 structural segment 数量，用于分层（≥5 vs <5）"""

def run_all(instances, conditions, output_path):
    """主循环：38 instances × 4 conditions = 152 次调用，写 CSV"""

def analyze_results(csv_path):
    """计算 overall win rate + >2K 子集分层 win rate"""
```

### 6. 注意事项和风险点

1. **Phase 2 line scoring 未完成**：`phase2_line_scores.json` 不存在。必须先运行 `python run_phase2_scoring.py --mode line` 才能启动 Phase 3 的 line_filtered condition。line segments 数量远大于 structural（如 youtube-dl_1 有 13449 个 line segments vs 20 个 structural），API 调用量和耗时会非常大。

2. **Structural scores 排除范围不一致**：task 说排除 fastapi_3/5（2 个），但 phase2_structural_scores 实际排除了 fastapi_1/2/3/5（4 个）。Phase 3 需要明确：是 38 个还是 36 个有效实例？

3. **Python 环境**：`python3` 不在 PATH 中，需用 `/root/miniconda3/bin/python3`，或先 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`。

4. **Trace 序列化必须用 `serialize_event()`**：函数处理了 return_value 的 `repr()` 和 exception_info 的 dict 化。手动构造会丢失这些转换。

5. **`_format_filtered_trace()` 的输入是 `ScoredSegment` 列表**，但 Phase 3 从 JSON 读入的是 dict。需要将 scores JSON 中 label="keep" 的 segment 重新反序列化为 `TraceSegment`（复用 `load_segments()` 中的逻辑），再包装为 `ScoredSegment`，或者直接用 raw dict 构建 text（绕过 dataclass）。

6. **Line scoring 的 segment 数量极大**：如 youtube-dl_1 有 13449 个 line windows。即使用 teacher_scorer 的 max_concurrent=5，API 调用量约 55K+ 次（38 instances × 平均 1450 segments）。需要考虑截断策略（如 `--max-segments`）。

7. **评估方法**：`_evaluate_repair()` 优先用 test execution（需要正确的 test_command 和 buggy_dir），Phase 3 脚本需要确保 bugsinpy_workspace 中的 instance 目录完整且可执行测试。

8. **Token 计算**：`estimate_tokens()` 用 `len(text) // 4` 作粗略估计。>2K token 子集的判定基于这个粗略值，需要明确是基于 full trace token count 还是 structural filtered token count。

---
