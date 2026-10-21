# ssh cwm data investigation

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_cwm-data-investigation_20260520T052748_result.json`
- **Structured JSON:** [`0734776c1f257e15859e.json`](../../sessions/07/0734776c1f257e15859e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data collected. Here's the complete report:

---

## 1. train_unified.py 数据加载代码 (lines 269-329)

```python
# Sanity check: render one example to verify template works
sample_target = "pass" if args.task == "cls" else "PASS: test completed successfully"
sample_text = _try_apply_chat_template(
    tokenizer,
    build_messages("def f(): return 1", "assert f() == 1", sample_target, task=args.task),
    tmpl_kw,
    tokenize=False,
    add_generation_prompt=False,
)
log.info(f"Sample formatted prompt (first 300 chars):\n{sample_text[:300]}")

# ── Data ──
if args.train_file:
    train_path = os.path.join(args.data_dir, args.train_file)
elif args.task == "cls":
    # Prefer repo-level swebench data if available
    repo_path = os.path.join(args.data_dir, "swebench_full", "swebench_train.jsonl")
    func_path = os.path.join(args.data_dir, "train.jsonl")
    train_path = repo_path if os.path.exists(repo_path) else func_path
else:
    train_path = os.path.join(args.data_dir, "cwm_train.jsonl")

if args.val_file:
    val_path = os.path.join(args.data_dir, args.val_file)
elif args.task == "cls":
    repo_path = os.path.join(args.data_dir, "swebench_full", "swebench_val.jsonl")
    func_path = os.path.join(args.data_dir, "val.jsonl")
    val_path = repo_path if os.path.exists(repo_path) else func_path
else:
    val_path = os.path.join(args.data_dir, "cwm_val.jsonl")

log.info(f"Train file: {train_path}")
log.info(f"Val file: {val_path}")
train_raw = load_jsonl(train_path)
val_raw = load_jsonl(val_path)
log.info(f"Loaded train={len(train_raw)}, val={len(val_raw)}")

train_ds = preprocess_split(tokenizer, train_raw, args.max_seq_length, "train", tmpl_kw, task=args.task)
val_ds = preprocess_split(tokenizer, val_raw, args.max_seq_length, "val", tmpl_kw, task=args.task)
```

**数据路径选择逻辑：**
- `--task cls` → 默认 `swebench_full/swebench_train.jsonl`（有则用），否则 `train.jsonl`
- `--task cwm` → 默认 `cwm_train.jsonl`
- `--train_file` / `--val_file` 可覆盖

---

## 2. cwm_train.jsonl 数据样本 (function-level 短格式)

**行数：15,290**

```
=== Sample 0 (label=1, mutation_type=original) ===
keys: [code, test, target, label, source, problem_id, mutation_type]
target (len=33): "PASS: test completed successfully"

=== Sample 1 (label=0, mutation_type=off_by_one) ===
target (len=22): "FAIL: AssertionError"

=== Sample 2 (label=0, mutation_type=operator_swap) ===
target (len=27): "FAIL: SyntaxError: expected ':'"
```

**关键：function-level CWM target 是短格式，仅一行 verdict。**

---

## 3. swebench_full/swebench_train.jsonl 数据样本 (repo-level 长格式)

**行数：70,748**

```
=== Sample 0 (label=1, source=swebench_verified, mutation_type=gold) ===
keys: [code, test, label, source, problem_id, mutation_type, error_message, execution_output, metadata]
code: git diff (sklearn/svm/base.py 修改)
execution_output (len=很长): "+ pytest -rA sklearn/svm/tests/test_svm.py\n===== test session starts ====\n...PASSED sklearn/svm/tests/test_svm.py::test_libsvm_parameters\nPASSED sklearn/svm/tests/test_svm.py::test_libsvm_iris\n..." (完整pytest输出)

=== Sample 1 (label=1, source=swebench_verified, mutation_type=mutation_operator_swap) ===
execution_output: 完整的 Django test runner 输出 (runtests.py --verbosity 2)
```

**关键：repo-level 的 execution_output 是完整 pytest/test runner 执行轨迹，数百到数千字符。**

---

## 4. train_unified.py 的 get_target + preprocess_split 函数

```python
def get_target(example, task):
    if task == "cls":
        return "pass" if example["label"] == 1 else "fail"
    if "target" in example:
        return example["target"]           # ← cwm_train.jsonl 走这里 (短格式)
    if "execution_output" in example:
        return example["execution_output"]  # ← swebench 走这里 (长格式)
    return None

def preprocess_split(tokenizer, data, max_len, name, tmpl_kw, task="cwm"):
    out = {"input_ids": [], "labels": [], "attention_mask": []}
    n_trunc = 0
    n_skip = 0
    for ex in data:
        target = get_target(ex, task)
        if target is None:
            n_skip += 1
            continue
        tok, trunc = tokenize_example(
            tokenizer, ex["code"], ex["test"], target, max_len, tmpl_kw, task=task,
        )
        for k in out:
            out[k].append(tok[k])
        n_trunc += int(trunc)
    if n_skip:
        log.warning(f"{name}: skipped {n_skip}/{len(data)} examples with no target or execution_output")
    pct = n_trunc / len(data) * 100 if data else 0
    log.info(f"{name}: {n_trunc}/{len(data)} truncated ({pct:.1f}%)")
    return Dataset.from_dict(out)
```

**CWM prompt template:**
```
System: "You are a code execution simulator. Given a code snippet and a test case, predict the execution result."
User: "## Code\n{code}\n\n## Test\n{test}\n\nWhat is the execution result?"
```

---

## 5. train_repo_cwm.py 的数据加载和 target 处理

```python
# Header comment:
# Input: data/swebench_full/{swebench_train,swebench_val}.jsonl
# fields: code (git diff), test (test name), label, execution_output (generation target)

SYSTEM_PROMPT = (
    "You are a code execution simulator. Given a code patch (git diff) and a test name, "
    "predict the execution result when the test is run against the patched code."
)

def build_messages(code, test, target=None):
    user_msg = f"## Patch (git diff)\n{code}\n\n## Test\n{test}\n\nWhat is the execution result?"
    ...

def preprocess_split(tokenizer, data, max_len, name, tmpl_kw):
    for ex in data:
        target = ex.get("execution_output", ex.get("target", ""))
        # ← 优先用 execution_output (长格式完整执行轨迹)
        tok, trunc = tokenize_example(tokenizer, ex["code"], ex["test"], target, max_len, tmpl_kw)
        ...
        out["class_label"].append(ex["label"])  # 带 class_label 用于加权 loss
    ...

# defaults:
# --data_dir  /home/sonny/exec-sim-repair-verifier/data/swebench_full
# --max_seq_length 2048
```

**关键区别 vs train_unified.py：**
- train_repo_cwm.py 有 **WeightedCausalLMTrainer** (样本加权 loss，按 class 频率)
- prompt 用 "Patch (git diff)" 而非 "Code"
- 直接读 `execution_output`，无 get_target 的 task 分支

---

## 6. Qwen CWM s123-v4 训练日志

```
2026-05-20 09:30:05 Loading tokenizer: /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B/
2026-05-20 09:30:05 Chat template kwargs: {'enable_thinking': False}
2026-05-20 09:30:07 Loaded train=70748, val=9335          ← swebench 数据
2026-05-20 09:30:07 Class weights: fail=1.7009, pass=0.2991
2026-05-20 09:34:53 train: 3192/70748 truncated (4.5%)
2026-05-20 09:36:02 val: 1883/9335 truncated (20.2%)
2026-05-20 09:36:04 Loading model: /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B/
2026-05-20 09:36:04 Attention: sdpa
2026-05-20 09:36:11 Starting training...
trainable params: 15,335,424 || all params: 8,206,070,784 || trainable%: 0.1869
Total steps: 6633, ~12s/it

{'loss': 24.4882, 'epoch': 0.02}   ← step 50
{'loss': 18.5001, 'epoch': 0.05}   ← step 100
{'eval_loss': 0.3030, 'epoch': 0.23} ← step 600 后 eval

训练正在进行中，已达约 step 600 (9%)。
```

**注意：日志中没有出现 "Train file" / "Val file" 行 — 说明用的是 train_repo_cwm.py（没有这个日志），不是 train_unified.py（有这个日志）。**

---

## 7. Qwen CWM s42 eval 输出 (qwen3_8b_cwm_repo_s42_ckpt400_seq4096)

```json
Sample 0: problem_id=pydata__xarray-6992, label=1, pred=1, correct=1, truncated=false
  gen_text (LONG): "+ pytest -rA xarray/tests/test_dataset.py\n===== test session starts ====\n...collected 1864 items\n...xarray/tests/test_dataset.py ......[100%]\n..."
  unparseable: true   ← 长执行轨迹，无法解析为简单verdict

Sample 1: problem_id=django__django-14315, label=1, pred=1, correct=1, truncated=false
  gen_text (LONG): "+ ./tests/runtests.py --verbosity 2 --settings=test_sqlite...\ntest_accent ... ok\ntest_basic ... ok\n..."
  unparseable: true

Sample 2: problem_id=pytest-dev__pytest-7490, label=0, pred=0, correct=1, truncated=false
  gen_text (LONG): "+ pytest -rA src/_pytest/skipping.py\n...FAILURES...AssertionError..."
  unparseable: false  ← 这条能解析，因为有明确 FAILURE
```

**Qwen s42 生成完整执行轨迹（长格式），大量 unparseable=true。**

---

## 8. DeepSeek CWM s42 eval 输出 (deepseek_cwm_repo_s42_seq4096)

```json
Sample 0: problem_id=pydata__xarray-6992, label=1, pred=1, correct=1, truncated=false
  gen_text (SHORT): "PASS: test_to_and_from_iris_dask (xarray.tests.test_dataarray.TestIrisConversion)"
  unparseable: false

Sample 1: problem_id=astropy__astropy-7336, label=1, pred=1, correct=1
  gen_text (SHORT): "PASS: test_kwarg_wrong_unit (astropy.units.tests.test_quantity_decorator.QuantityDecoratorTests)"
  unparseable: false

Sample 2: problem_id=django__django-12406, label=1, pred=1, correct=1
  gen_text (SHORT): "PASS: test_recleaning_model_form_instance (model_forms.tests.ModelFormBasicTests)"
  unparseable: false
```

**DeepSeek s42 生成短格式 verdict（"PASS: test_name"），全部 unparseable=false。这与训练数据的长格式 execution_output 完全不同。**

---

## 9. DeepSeek CWM s123 eval 输出 (deepseek_cwm_repo_s123_seq4096)

```json
Sample 0: problem_id=pydata__xarray-6992, label=1, pred=1, correct=1, truncated=false
  gen_text (LONG): "+ pytest -rA xarray/tests/test_dataset.py\n===== test session starts ====\n...collected 3389 items\n...xarray/tests/test_dataset.py .........FF..F..."
  unparseable: true

Sample 1: problem_id=django__django-14315, label=1, pred=1, correct=1, truncated=false
  gen_text (LONG): "+ ./tests/runtests.py --verbosity 2 ...\ntest_nopass ... FAIL\ntest_passfile ... FAIL\n..."
  unparseable: true

Sample 2: problem_id=pytest-dev__pytest-7490, label=0, pred=0, correct=1, truncated=false
  gen_text (LONG): "+ pytest -rA --durations 0\n...ERROR: testbed/src/_pytest/skipping.py\n...AttributeError..."
  unparseable: false
```

**DeepSeek s123 生成长执行轨迹，与 Qwen s42 类似，unparseable 率高。**

---

## 关键发现汇总

| 维度 | 值 |
|------|-----|
| cwm_train.jsonl (func-level) | 15,290 行，target 短格式 ("PASS: test completed" / "FAIL: Error") |
| swebench_train.jsonl (repo-level) | 70,748 行，execution_output 长格式（完整 pytest 输出） |
| train_unified.py CWM 默认数据 | `cwm_train.jsonl`（短格式 target） |
| train_repo_cwm.py 数据 | `swebench_full/swebench_train.jsonl`（长格式 execution_output） |
| Qwen s123-v4 训练数据 | 70,748 train + 9,335 val（swebench 长格式，用 train_repo_cwm.py） |
| **DeepSeek s42 eval 生成** | **短格式 verdict** ("PASS: test_name")，unparseable=false |
| **DeepSeek s123 eval 生成** | **长执行轨迹**，unparseable=true 居多 |
| **Qwen s42 eval 生成** | **长执行轨迹**，unparseable=true 居多 |

**核心发现：DeepSeek s42 是唯一生成短格式输出的模型/种子组合 — 尽管训练数据都是长格式 execution_output。这可能是 seed=42 训练配置不同（用了不同的训练脚本或数据），或者模型自发学会了摘要式输出。**

---
