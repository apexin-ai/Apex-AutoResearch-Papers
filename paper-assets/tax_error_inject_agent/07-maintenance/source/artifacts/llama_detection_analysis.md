## Detection 机制分析

### 1. Detection 定义

`injected_eval.py` 中 detection 通过 `detect_error_in_think()` 函数判定，对模型 `<think>` 输出应用 8 个正则 pattern：

```python
DETECTION_PATTERNS = [
    r"\b(?:wrong|error|mistake|incorrect|unexpected)\b",
    r"\b(?:strange|odd|confused|confusing|inconsistent)\b",
    r"(?:doesn'?t\s+match|doesn'?t\s+make\s+sense|not\s+right)",
    r"\b(?:something\s+(?:is\s+)?(?:off|wrong)|went\s+wrong)\b",
    r"\b(?:missing|lost|truncated|disappeared)\b",
    r"\b(?:should\s+have|need\s+to\s+redo|go\s+back|try\s+again)\b",   # ← Pattern 6
    r"\b(?:problem|issue|anomal)",
    r"\b(?:wait|hmm)\b.*\b(?:but|however|actually)\b",
]
```

任何 post-injection step 的 `<think>` 文本匹配上述任一 pattern，该 episode 即标记为 `detected=True`。

### 2. Detection 分布（报告值）

| Condition | Total Det | C1 | C4 | P1 | P2 |
|-----------|----------|----|----|----|----|
| Vanilla   | 10/47 (21.3%) | 2/12 | 3/11 | 2/12 | 3/12 |
| TaxEI     | 14/47 (29.8%) | 2/12 | 4/11 | 3/12 | 5/12 |
| Random    | 14/47 (29.8%) | 5/12 | 4/11 | 4/12 | 1/12 |

### 3. 关键发现：全部 Detection 是 "go back" 假阳性

**所有 38 个 detected episodes（三组共计）100% 仅匹配了 Pattern 6 中的 "go back" 子模式。** 没有任何一个匹配了 wrong/error/mistake/strange/missing/problem 等真正表达错误意识的 pattern。

具体数据：
- Vanilla: 10 detected episodes, 10/10 **仅匹配** "go back"（20 个 step-level matches）
- TaxEI: 14 detected episodes, 14/14 **仅匹配** "go back"（18 个 step-level matches）
- Random: 14 detected episodes, 14/14 **仅匹配** "go back"（24 个 step-level matches）

### 4. 典型 Examples

#### Example 1: Vanilla Ep0 — P1_step_order_swap

- **Task**: look_at_obj_in_light-AlarmClock-None-DeskLamp-308
- **Inject**: step 2, step order swap
- **Detection step**: 6
- **Think**: "I'm already holding the alarmclock. The desklamp was turned on earlier, so I'll **go back** to desk 1 to confirm the lamp is on and the 'hold the clock and turn on the lamp' goal is satisfied."
- **判定原因**: "go back" 是正常导航语言（返回灯所在位置完成任务），不是对错误的识别
- **结果**: 任务成功（7 steps）

#### Example 2: Vanilla Ep31 — C4_observation_masking

- **Task**: pick_cool_then_place_in_recep-Tomato-None-Microwave-10
- **Inject**: step 3, observation masking
- **Detection steps**: 11, 14, 23, 26, 36, 49（同一 episode 6 次触发）
- **Think**: 反复出现 "I should **go back** to the open fridge to locate the tomato"
- **判定原因**: 模型陷入循环，反复导航回冰箱，"go back" 是循环行为的副产物
- **结果**: 任务失败（50 steps，达到上限）

#### Example 3: Random Ep7 — C4_observation_masking

- **Task**: pick_and_place_simple-CellPhone-None-Drawer-219
- **Inject**: step 2, observation masking
- **Detection steps**: 8, 14, 20, 26, 32, 38, 44（7 次触发）
- **Think**: 反复 "I need to **go back** to the desk and place the phone in the drawer"
- **判定原因**: 同上，stuck in loop + 导航语言
- **结果**: 任务失败（50 steps）

### 5. "go back" 频率分析

| Condition | Pre-injection steps | "go back" rate | Post-injection steps | "go back" rate |
|-----------|----:|------:|----:|------:|
| LLaMA Vanilla | 173 | 0.6% (1) | 955 | 2.1% (20) |
| LLaMA TaxEI | 173 | 0.6% (1) | 912 | 2.0% (18) |
| LLaMA Random | 173 | 0.0% (0) | 862 | 2.8% (24) |
| Qwen TaxEI | — | — | 1250 total | **0.0% (0)** |

Post-injection "go back" 频率（2-3%）略高于 pre-injection（0-0.6%），但这是因为注入打断了正常流程后，模型需要导航回之前位置继续任务——是 **行为层面的正常响应**，不是错误意识。

### 6. Qwen 对比

#### Qwen detection=0% 的根本原因：无 think 输出

`recovery.py` 第 227 行：
```python
text = self.tokenizer.apply_chat_template(
    messages, tokenize=False, add_generation_prompt=True,
    enable_thinking=False,  # ← 关键：禁用 Qwen3 native thinking
)
```

- **Qwen3-8B**: `enable_thinking=False` 触发 Qwen3 的 `/no_think` 模式，模型不生成 `<think>` 标签，直接输出 action。`parse_response()` 提取 think_snippet 永远为空字符串。
- **LLaMA-3.1-8B**: `enable_thinking` 参数被 LLaMA tokenizer 忽略（非 Qwen 特有）。LLaMA 看到 prompt 中 "Think step by step in `<think></think>` tags" 的指令，忠实地生成 `<think>` 内容 → 给 detection heuristic 提供了匹配文本。

**验证**: Qwen 全部 1250 个 trajectory steps 的 think_snippet 均为空字符串（100%）。

#### 同一 episode 对比（Episode 0: AlarmClock-DeskLamp-308, P1_step_order_swap）

| | LLaMA Vanilla | Qwen TaxEI |
|---|---|---|
| Success | True (7 steps) | True (5 steps) |
| Detection | True (step 6) | False |
| Think content | 每步有完整推理文本 | 全部为空 |
| Post-injection behavior | 导航搜索 → 找到 → "go back" 到灯 | 直接导航到目标 |

### 7. 结论

**Detection 指标不可信，不应作为论文 contribution。** 具体原因：

1. **LLaMA 的 detection 全部是假阳性**：38/38 detected episodes 仅因 "go back"（正常 ALFWorld 导航用语）触发 Pattern 6，没有一个包含 wrong/error/strange/missing 等真正表达错误意识的词汇。模型在 `<think>` 中从未表达 "我注意到出错了"。

2. **Qwen detection=0% 是评估 artifact**：Qwen3 的 `enable_thinking=False` 导致无 think 输出，detection heuristic 无文本可匹配。这不代表 Qwen "不能检测错误"，只是没有可分析的推理 trace。

3. **LLaMA vs Qwen 的 detection 差异完全由输出格式决定**：LLaMA 产生 `<think>` 文本 → 有词可匹配；Qwen 不产生 → 无词可匹配。与错误检测能力无关。

4. **"go back" 在 Pattern 6 中是过于宽泛的匹配词**：在 ALFWorld 这种需要空间导航的环境中，"go back to X" 是极其常见的正常导航表述，不应作为错误检测信号。

### 8. 建议

- **从论文中移除 detection_rate 指标**，或明确标注为 unreliable heuristic
- 如果要保留 detection 分析，需要：
  - 从 Pattern 6 中移除 "go back"
  - 对 Qwen 启用 `enable_thinking=True` 以获得可比较的 think trace
  - 人工标注一个 gold standard detection 集来验证 heuristic 质量
- 论文的核心贡献应聚焦于 **recovery rate**（任务成功率），这是一个不依赖 think 文本的客观指标
