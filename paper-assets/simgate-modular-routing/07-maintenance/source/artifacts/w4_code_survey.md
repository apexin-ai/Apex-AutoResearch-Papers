# W4 Task-Type Positive Control: Code Survey & Modification Plan

## 1. Router Training Code Analysis

### 1.1 Main Training Script

**Location:** `/root/autodl-tmp/simgate-modular-routing/src/router_sft_train.py` (server)  
**Local copy:** `artifacts/router_sft_train.py` (slightly older version, less features)

### 1.2 Input Features

Prompt 由 `build_prompt()` 构造，格式：

```
<|im_start|>system
You are a routing classifier. Given the current observation and action history,
predict which reasoning modality will lead to a better outcome.<|im_end|>
<|im_start|>user
Observation: {observation}
Action history: {last 5 actions joined by " → "}<|im_end|>
```

**关键发现：prompt 中不包含 task_type。** 模型只能从 observation text 和 action history 推断应该用哪种 reasoning modality。

### 1.3 Model Architecture

- **Base model:** Qwen3-0.6B / 1.7B / 4B（通过 `--model_name` 指定，本地缓存在 `/root/autodl-tmp/models/Qwen/`）
- **Architecture:** `AutoModelForSequenceClassification` + LoRA
- **Classification head:** 2-way linear (`score` layer, modules_to_save=["score"])
- **LoRA config:** r=16, alpha=32, dropout=0.05, target_modules=["q_proj", "v_proj", "k_proj", "o_proj"]
- **Precision:** bf16

### 1.4 Training Configuration (plan-008-v4, 最新一轮)

| Parameter | Value |
|-----------|-------|
| epochs | 3 |
| batch_size | 4 |
| lr | 2e-5 |
| max_seq_len | 2048 |
| eval_split | 0.15 (episode-level stratified) |
| warmup_ratio | 0.1 |
| weight_decay | 0.01 |
| early_stopping_patience | 2 |
| metric_for_best_model | f1_macro |
| upsample_minority | true (WeightedRandomSampler) |
| gradient_accumulation_steps | 1 |

### 1.5 Data Loading

支持两种输入格式（通过 `--data_path` 或 `--data_dir`）：

**Format 1: labeled_steps.jsonl** (`results/plan_c/{task_type}/labeled_steps.jsonl`)
```json
{"task_type": "freeze", "episode_id": 0, "variation": 0, "step_idx": 0,
 "observation": "terminal 1 on agent...", "action_history": [],
 "label": "det-preferred", "signal_source": "death_asymmetry",
 "episode_score_internal": -100.0, "episode_score_det": 0.0, "score_gap": 100.0}
```

**Format 2: implicit_sft.jsonl** (`data/plan-004-implicit/implicit_sft.jsonl`)
```json
{"messages": [{"role": "system", "content": "..."}, {"role": "user", "content": "..."},
  {"role": "assistant", "content": "[SIMULATE] ..."}],
 "task_type": "chemistry-mix", "variation": 0, "step_idx": 0,
 "route_label": "deterministic"}
```

**Label mapping:** `RAW_LABEL_MAP` maps "det-preferred" → "deterministic", "internal-preferred" → "internal"  
**Split method:** Episode-level stratified split (sklearn train_test_split), stratified by majority label per episode

---

## 2. Training Data

### 2.1 Step-Level Data (plan_c, used by router SFT)

**Path:** `results/plan_c/{task_type}/labeled_steps.jsonl`  
**Total:** 2040 steps, 11 task types

| Task Type | Steps |
|-----------|-------|
| chemistry-mix | 240 |
| find-animal | 60 |
| find-non-living-thing | 510 |
| freeze | 180 |
| grow-fruit | 120 |
| identify-life-stages-1 | 180 |
| identify-life-stages-2 | 120 |
| inclined-plane-determine-angle | 120 |
| lifespan-longest-lived | 150 |
| lifespan-longest-lived-then-shortest-lived | 180 |
| measure-melting-point-unknown-substance | 180 |

### 2.2 Implicit SFT Data (plan-004-implicit, used by plan-008 training)

**Path:** `data/plan-004-implicit/implicit_sft.jsonl`  
**Total:** 2040 samples  
**Label distribution:** 1830 deterministic (89.7%) / 210 internal (10.3%)

**每条记录包含 `task_type` 字段** — task-type augmented router 所需信息已存在于数据中。

### 2.3 Episode-Level Data (baseline, used by task_type_classifier.py)

**Path:** `results/baseline_245eps/episode_details.jsonl`  
**Total:** 980 lines (245 episodes × 4 conditions)  
**Fields:** condition, task_type, episode_idx, variation_idx, score, internal_final, det_final, oracle_label

---

## 3. Existing Results

### 3.1 Step-Level Router (现有 baseline)

| Checkpoint | Model | Balanced Acc | Accuracy |
|------------|-------|-------------|----------|
| plan-004-implicit | Qwen3-1.7B | **59.3%** | 65.4% |
| plan-004-v5 | Qwen3-1.7B | **79.1%** | 74.5% |

plan-004-v5 balanced acc 较高，但 internal F1 仍只有 0.42（precision=0.28, recall=0.85）。

### 3.2 Episode-Level Task-Type Classifier (已有代码)

**Script:** `guided_router/task_type_classifier.py`  
**结论（3-class, episode level）:** overall accuracy=61.2%, balanced accuracy=33.3%

⚠️ 注意：这个已有分析器用的是 **3-class** (det-pref / int-pref / no-pref) **episode-level** 数据。与 router SFT 的 **2-class** (deterministic / internal) **step-level** 设置不同，不能直接对比。

### 3.3 Death Risk Distribution

10/11 task types 有 death risk (internal_death_rate 0.45-0.56)，只有 find-non-living-thing 无 death risk (0.0)。  
→ **Task-type 是一个几乎完美的 binary indicator** for routing label。

---

## 4. Modification Plans

### Plan C（推荐，最简单最有说服力）

**独立 sklearn 脚本，task-type 作为唯一输入**

**新文件:** `src/task_type_positive_control.py`

**设计:**
- 从 `data/plan-004-implicit/implicit_sft.jsonl` 或 `results/plan_c/*/labeled_steps.jsonl` 加载 2040 步
- Input: task_type one-hot encoding (11维)
- Output: routing label (internal=0 / deterministic=1), 2-class
- Models: LogisticRegression, MLP (1-hidden-layer), DummyClassifier (majority baseline)
- Evaluation: episode-level stratified 5-fold CV + LOOCV（与现有 task_type_classifier.py 对齐）
- 关键指标: balanced_accuracy, per-class F1

**需要修改/新增的文件:**
1. `src/task_type_positive_control.py` — 新建，~120行

**具体代码结构:**
```python
# 1. 加载 step-level data (同 router_sft_train.py 的 load_labeled_data)
# 2. 构建 X = one-hot(task_type), y = label_id
# 3. Episode-level stratified 5-fold CV
# 4. Report: balanced_accuracy, confusion_matrix, per-task accuracy
# 5. 对比表: task-type-only vs step-level router (from checkpoints)
```

**训练命令:**
```bash
cd /root/autodl-tmp/simgate-modular-routing
python src/task_type_positive_control.py \
  --data_dir results/plan_c/ \
  --output_path artifacts/w4_task_type_positive_control.json
```

**预估训练时间:** <1 秒（sklearn，无 GPU）

**预期结果:** balanced accuracy ~90%+ (因为 10/11 tasks 全部映射到 deterministic, only find-non-living-thing → internal)

**论文叙事价值:** "Task type alone achieves ~90% balanced accuracy, demonstrating that routing signal is fundamentally a task-type-level property. The step-level router (56-59% bal. acc.) fails not because of insufficient model capacity, but because it cannot extract task-type information from step-level observations."

---

### Plan A（备选，LLM prompt augmentation）

**在 LLM prompt 中拼接 task_type**

**需要修改的文件:**
1. `src/router_sft_train.py` — 修改 `build_prompt()` 和 `RouterDataset.__getitem__()`

**具体改动:**

`build_prompt()` 修改前:
```python
def build_prompt(observation: str, action_history: List[str]) -> str:
    ...
    return (
        f"<|im_start|>system\n{SYSTEM_PROMPT}<|im_end|>\n"
        f"<|im_start|>user\n"
        f"Observation: {observation}\n"
        f"Action history: {history_summary}<|im_end|>"
    )
```

修改后:
```python
def build_prompt(observation: str, action_history: List[str], task_type: str = "") -> str:
    ...
    task_line = f"Task type: {task_type}\n" if task_type else ""
    return (
        f"<|im_start|>system\n{SYSTEM_PROMPT}<|im_end|>\n"
        f"<|im_start|>user\n"
        f"{task_line}"
        f"Observation: {observation}\n"
        f"Action history: {history_summary}<|im_end|>"
    )
```

`RouterDataset.__getitem__()` 修改:
```python
def __getitem__(self, idx):
    s = self.samples[idx]
    prompt = build_prompt(s["observation"], s["action_history"], s.get("task_type", ""))
    ...
```

新增 arg:
```python
p.add_argument("--include_task_type", action="store_true",
               help="Include task_type in prompt (positive control)")
```

**训练命令:**
```bash
python src/router_sft_train.py \
  --data_dir results/plan_c/ \
  --model_name /root/autodl-tmp/models/Qwen/Qwen3-0.6B \
  --output_dir checkpoints/w4-task-type-augmented-seed42 \
  --include_task_type \
  --upsample_minority \
  --seed 42
```

需要跑 4 seeds × 3 model sizes = 12 runs 以保持与 plan-008-v4 的对比一致性。

**预估训练时间:** ~3-5 min/run (0.6B), ~8-12 min/run (1.7B), ~20-30 min/run (4B)  
**总计:** ~4-6 小时 (12 runs)

**优点:** 直接与现有 router SFT baseline (plan-008-v4) 对比，same model same training procedure，仅差 prompt 中多一行 task_type  
**缺点:** 训练时间长，且结果对 paper narrative 不如 Plan C 简洁

---

### Plan B（不适用）

原方案"添加 task-type one-hot 到 feature layer"不适用，因为模型是 LLM-based sequence classifier，没有独立的 feature extraction 层。

---

## 5. 推荐方案

**先做 Plan C，再视需要做 Plan A。**

- Plan C (~120行 Python, <1秒运行) 足以证明 "task-type alone → ~90% bal. acc."
- 如果 reviewer 要求 "same model architecture" 对比，再补做 Plan A
- Plan C 的结果可以直接出一个表/图：

| Method | Input | Balanced Acc |
|--------|-------|-------------|
| Majority baseline | — | 50.0% |
| Step-level router (Qwen3-1.7B LoRA) | observation + action_history | 59.3% |
| Task-type only (LogisticRegression) | task_type one-hot | ~90%+ |
| Task-type only (majority per task) | task_type | ~90%+ |

---

## 6. Data Dependency Summary

| Data | Path | Samples | Labels |
|------|------|---------|--------|
| Step-level (plan_c) | `results/plan_c/*/labeled_steps.jsonl` | 2040 | det-preferred / internal-preferred |
| Step-level (implicit) | `data/plan-004-implicit/implicit_sft.jsonl` | 2040 | deterministic (1830) / internal (210) |
| Episode-level | `results/baseline_245eps/episode_details.jsonl` | 245 ep | det-pref / int-pref / no-pref |

所有数据中都包含 `task_type` 字段，无需额外数据采集。
