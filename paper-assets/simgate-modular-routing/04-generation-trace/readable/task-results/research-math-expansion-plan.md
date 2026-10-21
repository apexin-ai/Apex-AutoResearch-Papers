# research math expansion plan

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_math-expansion-plan_20260515T065859_result.json`
- **Structured JSON:** [`3c56431162d73d3d311b.json`](../../sessions/3c/3c56431162d73d3d311b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有信息收集完毕。以下是完整汇报：

---

## MATH Negative Contrast 实验调研报告

### 1. 代码状态

服务器上完整保留：
- `src/math_counterfactual.py` — 主 pipeline，含 `MathLLM`（vLLM API 模式）、`run_internal`、`run_code_interpreter`（多轮 ReAct）、`process_problem`、`load_math_problems`
- `src/code_sandbox.py` — `auto_print_last_expr` fix 已合并，正常工作
- `src/math_answer_utils.py` — 答案提取 + normalize + sympy 符号比较
- `src/analyze_math_pilot.py` — 分析脚本

模型 `/root/autodl-tmp/models/Qwen/Qwen2.5-7B-Instruct` 在位。

### 2. 已有数据

| 文件 | 行数 | offset | 状态 |
|------|------|--------|------|
| `pilot_50.jsonl` | 50 | 0 | 完整 |
| `math_200_fixed.jsonl` | 55 | 50 | 在 #56 crash |
| `dryrun.jsonl` | ~10 | — | 验证用，忽略 |
| `full_200_DIRTY_DO_NOT_USE.jsonl` | — | — | 脏数据，忽略 |

**可复用 105 题**（问题 index 0-104），两个文件格式完全一致（同 model、seed、sandbox 版本），直接拼接即可。

### 3. vLLM / GPU 评估

- **两块 RTX 5090 均空闲**（0 MiB），无 vLLM 进程运行
- MATH pipeline 默认用 **vLLM API server**（`localhost:8000`），需要先手动启动
- **Code sandbox 纯 CPU**（subprocess 跑 python3），不占 GPU
- 方案：在 cuda:1 启 vLLM server → MATH pipeline 通过 API 调用，不影响 cuda:0（留给 multi-model 实验）

启动命令：
```bash
CUDA_VISIBLE_DEVICES=1 python -m vllm.entrypoints.openai.api_server \
  --model /root/autodl-tmp/models/Qwen/Qwen2.5-7B-Instruct \
  --max-model-len 8192 --gpu-memory-utilization 0.85 --port 8000 &
```

### 4. vLLM 400 Error — 根因 + 修复

**根因**：`_generate_api` 无任何错误处理，直接 `resp.raise_for_status()`。在 code interpreter 多轮对话中，累积的 messages 超过 `max_model_len=4096` 导致 vLLM 返回 400。

**修复方案**（需改 `math_counterfactual.py`）：
1. 将 vLLM 的 `max-model-len` 提高到 **8192**（Qwen2.5-7B 支持 32K，8K 足够）
2. 在 `_generate_api` 中加 **retry + 异常捕获**：捕获 HTTPError 时跳过该问题（记为 error），而不是 crash 整个 pipeline

```python
def _generate_api(self, messages, temperature):
    payload = {...}
    for attempt in range(3):
        try:
            resp = requests.post(f"{self.api_url}/chat/completions", json=payload, timeout=120)
            resp.raise_for_status()
            return resp.json()["choices"][0]["message"]["content"].strip()
        except requests.exceptions.HTTPError:
            if attempt == 2:
                raise
            time.sleep(2)
```

3. 在 `main()` 的 for 循环中加 try/except 包裹 `process_problem`，失败时写入 error record 继续

### 5. 扩展方案

**目标**：200-300 总题（已有 105，需新跑 95-195 题）
**数据集**：2538 Level 4-5 题（data/math-raw/），远超需求

**续跑命令**（offset=105 继续）：
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
cd /root/autodl-tmp/simgate-modular-routing && \
python src/math_counterfactual.py \
  --n_problems 195 \
  --offset 105 \
  --output data/math-counterfactual/math_extend_195.jsonl \
  --model_path /root/autodl-tmp/models/Qwen/Qwen2.5-7B-Instruct \
  --api_url http://localhost:8000/v1 \
  --seed 42
```

**合并数据**：cat 三个 JSONL 文件 → 300 题完整数据集

### 6. 预估运行时间

- pilot-50：599s → 12s/题
- math-200-fixed 前 55 题：类似速率
- **195 题预估：~39 分钟**
- 加上 vLLM 启动时间（~2 min），**总计 ~41 分钟**

### 7. 已知风险

| 风险 | 严重性 | 缓解 |
|------|--------|------|
| vLLM 400（context overflow） | **高** | 提高 max_model_len 到 8192 + 加 retry/skip |
| pipeline crash 丢进度 | 中 | 已有 append 模式（逐条写入 JSONL），重启从断点手动续跑 |
| `answers_equal` 判断错误 | 低 | 已有 normalize + numeric + sympy 三级判定，pilot 验证过 |
| vLLM server OOM | 低 | 单卡 32GB，7B 模型 8K context 只需 ~18GB |

### 执行步骤建议

1. **修复** `_generate_api` 加 retry + try/except（防 crash）
2. **启动 vLLM** 在 cuda:1，`max-model-len=8192`
3. **跑 195 题** offset=105
4. **合并** 三个 JSONL → 300 题完整数据
5. **分析** 更新 CI 和统计

需要我现在开始实施修复和启动吗？

---
