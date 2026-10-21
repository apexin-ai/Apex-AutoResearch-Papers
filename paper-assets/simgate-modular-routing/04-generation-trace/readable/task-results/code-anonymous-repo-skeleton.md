# code anonymous repo skeleton

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_anonymous-repo-skeleton_20260522T024213_result.json`
- **Structured JSON:** [`d290562dfb155dfb2b45.json`](../../sessions/d2/d290562dfb155dfb2b45.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

No identifying information found — the only GitHub links are public dataset references (ScienceWorld, ALFWorld, MATH), which are appropriate.

匿名代码仓库骨架已创建完毕，位于 `artifacts/anonymous_code/`，共 22 个文件：

```
anonymous_code/
├── README.md                              # 论文标题、环境配置、复现步骤（无作者/机构）
├── requirements.txt                       # 核心依赖（torch, transformers, peft, scienceworld 等）
├── configs/
│   └── default.yaml                       # 实验超参配置（11 tasks, counterfactual, router training）
├── data/
│   └── README.md                          # 数据获取说明（ScienceWorld Apache 2.0, ALFWorld MIT, MATH MIT）
└── src/
    ├── counterfactual_analysis.py         # Algorithm 1: 反事实标注（fork-and-lookahead）
    ├── daf_computation.py                 # DAF 计算 + 10000 次 bootstrap CI
    ├── death_decomposition.py             # Death decomposition 分析（Table 3 核心证据）
    ├── scienceworld_utils.py              # ScienceWorld 环境封装（创建/fork/重放）
    ├── llm_agent.py                       # ReAct LLM agent（支持 vLLM API / 本地推理）
    ├── alfworld_counterfactual.py         # ALFWorld 反事实扩展（Table 4）
    ├── math_counterfactual.py             # MATH 反事实扩展（Table 4）
    ├── code_sandbox.py                    # MATH code interpreter 沙箱
    ├── math_answer_utils.py               # 数学答案提取与 sympy 等价比较
    ├── guided_router/
    │   ├── __init__.py
    │   ├── config.py                      # 11 task 的 death risk 配置（来自反事实数据）
    │   ├── router.py                      # Decomposition-Guided Router（oracle/learned）
    │   ├── eval_episode.py                # Episode-level balanced accuracy 评估
    │   └── loto_eval.py                   # Leave-One-Task-Out 11-fold 评估
    └── router_training/
        ├── __init__.py
        ├── data_loader.py                 # 数据加载、stratified/LOTO 切分、RouterDataset
        ├── router_sft.py                  # Classification head LoRA SFT
        ├── generative_router_sft.py       # Generative implicit router LoRA SFT
        └── format_implicit_data.py        # 标注数据 → [SIMULATE] chat 格式转换
```

匿名性检查通过：无作者名、机构、服务器地址、W&B 链接、硬编码绝对路径。

---
