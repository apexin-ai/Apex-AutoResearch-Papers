# MetaGPT + HumanEval 跨域验证方案

## 1. 目标

用 MetaGPT（层级 pipeline 架构）+ HumanEval（代码任务）验证 AG2 + GSM8K 上发现的 5 类通信功能 taxonomy 是否跨框架、跨任务域成立。最小验证规模：1 backbone × 1 topology × 50 tasks。

---

## 2. MetaGPT 消息格式分析

### 2.1 AG2 vs MetaGPT 消息模型对比

| 维度 | AG2 (GroupChat) | MetaGPT |
|------|----------------|---------|
| 通信模式 | 点对点 / 广播（peer-to-peer） | 发布-订阅（publish-subscribe） |
| 消息路由 | GroupChat manager 分发或直接对话 | Environment 消息池，角色按 `cause_by` 订阅 |
| 消息类 | `dict {"role", "content", "name"}` | `Message(role, content, cause_by, send_to, ...)` |
| 角色分化 | 同质（共享 LLM config + system prompt） | 异质（每个 Role 有独立 Action 链） |
| 拓扑结构 | round_robin / sequential / selector | 固定 pipeline（PM→Architect→Engineer→QA） |
| 轮次控制 | max_rounds 参数 | Action DAG 自然终止 |

### 2.2 MetaGPT Message 类关键字段

```python
class Message(BaseModel):
    id: str                    # 唯一消息 ID
    content: str               # 消息文本内容
    role: str                  # 发送者角色名（"ProductManager", "Engineer" 等）
    cause_by: str              # 触发此消息的 Action 类名（"WritePRD", "WriteCode" 等）
    send_to: set[str]          # 目标角色集合，空 = 广播
    sent_from: str             # 发送者角色名
    instruct_content: BaseModel # 结构化输出（可选）
```

### 2.3 关键差异对 taxonomy 的影响

1. **层级 vs 扁平**：MetaGPT 的 PM→Architect→Engineer→QA 是固定顺序，类似 AG2 sequential 但多角色。coordination 类消息可能更少（框架本身承担了协调），verification 集中在 QA 角色。

2. **Action-driven**：每个消息绑定一个 Action（WritePRD、WriteDesign、WriteCode、RunTests），消息功能与 Action 类型强相关。这可能导致 information_provision 和 reasoning_guidance 的边界更模糊。

3. **结构化输出**：MetaGPT 消息常包含结构化内容（JSON/Markdown），不像 AG2 纯自由文本。标注时需要处理。

---

## 3. Trace 提取方案

### 3.1 TracedEnvironment（推荐方案）

```python
# src/trace_collection_metagpt.py

from metagpt.environment import Environment
from metagpt.schema import Message
from datetime import datetime, timezone

class TracedEnvironment(Environment):
    """拦截 publish_message 记录完整消息 trace"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.message_trace: list[dict] = []
    
    def publish_message(self, message: Message, peekable: bool = True):
        self.message_trace.append({
            "sender": message.sent_from or message.role,
            "receiver": ",".join(message.send_to) if message.send_to else "all",
            "content": str(message.content),
            "cause_by": message.cause_by,
            "round": len(self.message_trace),
            "timestamp": datetime.now(timezone.utc).isoformat(),
        })
        return super().publish_message(message, peekable)
    
    def get_normalized_trace(self) -> list[dict]:
        """转换为与 AG2 相同的标准化消息格式"""
        return [
            {
                "sender": m["sender"],
                "receiver": m["receiver"],
                "content": m["content"],
                "round": m["round"],
                "timestamp": m["timestamp"],
            }
            for m in self.message_trace
        ]
```

### 3.2 自定义代码任务团队

不使用 MetaGPT 默认的 SoftwareCompany pipeline（太重，涉及文件系统操作），而是构建轻量级代码任务团队：

```python
from metagpt.roles import Role
from metagpt.actions import Action

class CodeSolver(Role):
    """编写代码解决 HumanEval 问题"""
    name: str = "CodeSolver"
    profile: str = "Code Solver"
    goal: str = "Write correct Python code to solve the given programming problem"
    
class CodeReviewer(Role):
    """审查代码正确性并提出修改建议"""
    name: str = "CodeReviewer" 
    profile: str = "Code Reviewer"
    goal: str = "Review code for correctness, edge cases, and logical errors"

class TestRunner(Role):
    """模拟测试执行，验证代码逻辑"""
    name: str = "TestRunner"
    profile: str = "Test Runner"
    goal: str = "Analyze code against test cases and report pass/fail"
```

### 3.3 为什么用 3 角色而非 4 角色

MetaGPT 默认 4 角色（PM/Architect/Engineer/QA）中 PM 和 Architect 主要处理需求分析和架构设计，对 HumanEval 这种单函数问题来说是 overhead。3 角色（Solver/Reviewer/TestRunner）：
- 与 AG2 的 Solver/Checker 对应但更丰富
- 保留 MetaGPT 层级 pipeline 特征（Solver→Reviewer→TestRunner）
- 足够产生所有 5 类通信功能

---

## 4. HumanEval 评估方案

### 4.1 数据集

- 来源：`openai/human-eval`（164 题）或 `datasets` 库
- 采样：随机选 50 题（seed=42），覆盖不同难度
- 每题包含：function signature + docstring + canonical solution + test cases

### 4.2 Ground Truth 判定：代码执行 pass@1

与 GSM8K 的数值比较不同，HumanEval 需要**实际执行代码**并运行测试用例：

```python
import subprocess
import tempfile

def evaluate_humaneval(generated_code: str, test_code: str, timeout: int = 10) -> dict:
    """
    执行生成的代码 + 测试用例，判断 pass/fail
    
    Returns:
        {
            "is_correct": bool,      # 所有测试用例通过
            "error": str | None,     # 错误信息（如有）
            "execution_time": float  # 执行耗时（秒）
        }
    """
    full_code = generated_code + "\n\n" + test_code
    
    with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
        f.write(full_code)
        f.flush()
        
        try:
            result = subprocess.run(
                ["python3", f.name],
                capture_output=True, text=True,
                timeout=timeout
            )
            return {
                "is_correct": result.returncode == 0,
                "error": result.stderr if result.returncode != 0 else None,
                "execution_time": 0.0,  # 实际用 time.time() 包裹
            }
        except subprocess.TimeoutExpired:
            return {"is_correct": False, "error": "timeout", "execution_time": timeout}
```

### 4.3 答案提取

从多轮对话中提取最终代码：

```python
import re

def extract_code_answer(messages: list[dict]) -> str:
    """从消息历史中提取最后一个完整的 Python 代码块"""
    code_blocks = []
    for msg in reversed(messages):
        # 匹配 ```python ... ``` 或 ```...```
        blocks = re.findall(r'```(?:python)?\s*\n(.*?)```', msg["content"], re.DOTALL)
        if blocks:
            code_blocks = blocks
            break
    
    if not code_blocks:
        # fallback：提取 def 开头的代码段
        for msg in reversed(messages):
            match = re.search(r'(def \w+\(.*?\):.*?)(?=\n\S|\Z)', msg["content"], re.DOTALL)
            if match:
                return match.group(1)
    
    return code_blocks[-1] if code_blocks else ""
```

### 4.4 正确性标注适配

`correctness_annotation.py` 当前评估数学正确性。代码任务需要修改 prompt：

```python
CODE_CORRECTNESS_PROMPT = """You are evaluating the correctness of a message in a multi-agent 
code generation conversation.

Problem: {question}
Ground truth solution: {ground_truth}
Conversation so far: {context}
Target message: {target_message}

Evaluate the TARGET MESSAGE's contribution to solving the coding problem.
Categories:
- correct: Code logic, algorithm choice, and implementation are correct
- partially_correct: Some aspects correct but contains bugs or incomplete logic
- incorrect: Fundamental algorithmic or logical errors
- not_applicable: No code or technical reasoning content (pure coordination)

Return JSON: {{"correctness": "...", "confidence": 0.0-1.0, "reasoning": "..."}}
"""
```

---

## 5. 需要新增/修改的文件清单

### 5.1 新增文件

| 文件 | 说明 | 估计行数 |
|------|------|---------|
| `src/trace_collection_metagpt.py` | MetaGPT trace 收集器（TracedEnvironment + 团队配置 + HumanEval 加载） | ~350 |
| `configs/metagpt_humaneval.yaml` | MetaGPT + HumanEval 实验配置 | ~60 |
| `src/humaneval_utils.py` | HumanEval 数据加载 + 代码执行 + 答案提取 | ~150 |

### 5.2 需修改文件

| 文件 | 修改内容 | 估计改动 |
|------|---------|---------|
| `src/correctness_annotation.py` | 增加 `task_type` 分支，代码任务用不同 prompt | +30 行 |
| `src/local_impact.py` | neutralize placeholder 增加代码角色模板 | +10 行 |
| `src/analysis.py` | 增加跨框架对比分析（AG2 vs MetaGPT taxonomy 分布 χ²） | +80 行 |
| `src/utils.py` | 增加 `extract_code_answer()` | +30 行 |

### 5.3 无需修改

| 文件 | 原因 |
|------|------|
| `src/functional_annotation.py` | taxonomy 定义和标注 prompt 与任务域无关，直接复用 |
| `src/local_impact.py`（核心逻辑） | 消除实验逻辑与任务域无关，只要输入是标准 JSONL |

### 5.4 总工作量估计

| 阶段 | 时间 |
|------|------|
| trace_collection_metagpt.py 开发 + 调试 | 4-6h |
| humaneval_utils.py 开发 | 2h |
| correctness / analysis 适配 | 2h |
| 50 tasks trace 收集（GPU 时间） | 3-4h |
| 标注 + 消除实验（GPU 时间） | 6-8h |
| 分析 + 结果整理 | 2h |
| **总计** | **~20h（2-3 天）** |

---

## 6. 最小验证实验配置

### 6.1 实验矩阵

| 维度 | 值 |
|------|-----|
| 框架 | MetaGPT |
| Backbone | Qwen2.5-7B-Instruct（port 8000，与 AG2 实验一致） |
| 拓扑 | hierarchical pipeline（Solver→Reviewer→TestRunner） |
| 任务 | HumanEval 50 题（从 164 题随机采样，seed=42） |
| Max rounds | 6（与 AG2 一致） |
| Temperature | 0（确定性解码，与 AG2 一致） |

### 6.2 配置文件

```yaml
# configs/metagpt_humaneval.yaml
framework: metagpt
task:
  dataset: humaneval
  num_tasks: 50
  seed: 42
  
model:
  name: Qwen2.5-7B-Instruct
  base_url: http://localhost:8000/v1
  temperature: 0
  max_tokens: 2048

team:
  roles:
    - name: CodeSolver
      profile: "Code Solver"
      system_prompt: |
        You are a skilled Python programmer. Given a function signature and docstring, 
        write a correct implementation. Think step by step about edge cases.
    - name: CodeReviewer
      profile: "Code Reviewer"  
      system_prompt: |
        You are a code reviewer. Check the provided code for correctness, edge cases, 
        and logical errors. If you find issues, suggest specific fixes.
    - name: TestRunner
      profile: "Test Runner"
      system_prompt: |
        You are a test analyst. Given code and test cases, mentally trace through the 
        execution and report whether the code would pass or fail each test. Be precise.
  max_rounds: 6
  topology: hierarchical  # Solver → Reviewer → TestRunner → Solver (iterative)

evaluation:
  method: code_execution  # vs "numeric_comparison" for GSM8K
  timeout: 10  # seconds per test execution
  metric: pass_at_1

ablation:
  method: remove  # same as AG2
  neutralize_placeholders:
    CodeSolver: "Let me write some code for this."
    CodeReviewer: "I'll review the code."
    TestRunner: "I'll check the tests."
    default: "Acknowledged."
  
annotation:
  model_a: Qwen2.5-7B-Instruct  # port 8000
  model_b: Llama-3.1-8B-Instruct  # port 8001
  embedding: all-MiniLM-L6-v2

output:
  trace_dir: data/metagpt_humaneval/traces/
  impact_dir: data/metagpt_humaneval/impact/
  annotation_dir: data/metagpt_humaneval/annotations/
  analysis_dir: data/metagpt_humaneval/analysis/
```

### 6.3 验证成功标准

| 指标 | 阈值 | 说明 |
|------|------|------|
| 消息总量 | ≥ 200 | 50 tasks × avg 4+ msgs/task |
| 5 类全部出现 | 每类 ≥ 5 条 | taxonomy 在代码域也有表达 |
| 跨模型标注 κ | ≥ 0.35 | 略低于 GSM8K 的 0.60 可接受（新域） |
| function_type × action_level χ² | p < 0.05 | 功能类型与影响存在统计关联 |
| 跨框架分布比较 | 报告即可 | 不要求分布完全一致，差异本身是发现 |

---

## 7. 潜在风险和 Fallback 方案

### 7.1 风险矩阵

| 风险 | 概率 | 影响 | 缓解 |
|------|------|------|------|
| MetaGPT API 不稳定 / 版本变更 | 中 | 高 | 锁定 metagpt==0.8.1，保存 wheel 到数据盘 |
| HumanEval 代码执行安全问题 | 低 | 高 | subprocess + timeout + tmpfile，禁止网络访问 |
| Qwen 7B 代码能力不足（pass@1 太低） | 中 | 中 | 下文 Fallback A |
| 某类 taxonomy 在代码任务中不出现 | 中 | 中 | 下文 Fallback B |
| 消息轮次太少（pipeline 一次过） | 高 | 高 | 下文 Fallback C |
| MetaGPT 层级结构导致 coordination 几乎不出现 | 高 | 低 | 这本身是一个发现：框架结构影响功能分布 |

### 7.2 Fallback 方案

**Fallback A: 代码能力不足**
- Qwen 7B HumanEval pass@1 预估 ~40-50%。如果低于 20%（大量失败导致消息没有有效推理内容）：
- → 换用 Qwen2.5-14B-Instruct 或 Qwen2.5-Coder-7B-Instruct（代码特化模型）
- → 或降低任务难度：只选 HumanEval Easy 子集

**Fallback B: 某类 taxonomy 缺失**
- 如果 acknowledgment 在代码任务中几乎不出现（角色分化导致没有"同意"的场景）：
- → 这是合法的发现——"功能分布受任务域调制"
- → 论文中作为 finding 报告，而非 taxonomy 失败

**Fallback C: 消息轮次不足**
- MetaGPT pipeline 默认是单 pass（每个角色只说一次），总消息数可能只有 3 条/task
- → 必须启用迭代模式：Solver→Reviewer→TestRunner→**Solver**（revision loop）
- → 设置 `max_rounds=6` 确保至少 2 轮迭代
- → 如果 MetaGPT 不原生支持迭代，手动实现循环：

```python
async def iterative_solve(team, task, max_iterations=2):
    """强制多轮迭代，确保消息量足够"""
    for i in range(max_iterations):
        await team.run(n_round=3)  # 每轮 3 个角色各说一次
        # 检查 TestRunner 是否判定通过
        last_msg = team.env.message_trace[-1]
        if "all tests pass" in last_msg["content"].lower():
            break
    return team.env.get_normalized_trace()
```

**Fallback D: MetaGPT 集成太复杂**
- 如果 MetaGPT API 变动太大、无法稳定提取 trace：
- → 退守方案：用 AG2 搭建 hierarchical topology（3 角色固定顺序）+ HumanEval
- → 仍然证明"跨任务域"泛化，只是少了"跨框架"论点
- → 论文中标注为 limitation，留作 future work

---

## 8. 论文叙事价值

### 8.1 最佳结果（5 类全部出现，分布不同）

> "Our five-category taxonomy emerges consistently across both math reasoning (GSM8K) and code generation (HumanEval) tasks, and across both peer-to-peer (AG2) and hierarchical pipeline (MetaGPT) frameworks. However, the **distribution** of function types is modulated by both task domain and framework architecture: verification messages are 2.3× more frequent in code tasks, while coordination messages are significantly reduced under MetaGPT's structured pipeline (p < 0.01)."

### 8.2 可接受结果（4/5 类出现）

> "Four of five function types appear in both domains. The absence of [acknowledgment] in hierarchical pipelines suggests that this function type is an artifact of peer-to-peer negotiation dynamics rather than a universal communication primitive."

### 8.3 最差可接受结果（分布差异显著但 taxonomy 仍有解释力）

> "While the relative prevalence of function types differs significantly across domains (χ² = XX, p < 0.001), the taxonomy's discriminative power for predicting message impact remains significant in both settings (code: AUC = 0.XX, math: AUC = 0.XX), confirming its utility as a framework-agnostic analytical tool."

---

## 9. 执行计划

```
Day 1 (上午): 实现 trace_collection_metagpt.py + humaneval_utils.py
Day 1 (下午): 本地测试 5 题，验证 trace 格式 + 代码执行
Day 2 (上午): 修改 correctness_annotation.py，部署到服务器
Day 2 (下午): 运行 50 题 trace 收集（~3-4h GPU）
Day 3 (上午): 运行标注 + 消除实验（~6-8h GPU，可 nohup）
Day 3 (下午): 运行 analysis.py，整理跨框架对比结果
```

前置条件：AG2 全规模实验已完成。MetaGPT 实验不阻塞论文主体写作。
