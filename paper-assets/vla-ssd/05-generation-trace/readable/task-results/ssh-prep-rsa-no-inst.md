# ssh prep rsa no inst

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_prep-rsa-no-inst_20260515T210801_result.json`
- **Structured JSON:** [`ac9a9575ede817d9f286.json`](../../sessions/ac/ac9a9575ede817d9f286.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已读完全部代码。以下是预检结果。

---

## 预检结果

### 1. h5 格式兼容性 ✅

`run_no_inst_extraction.sh` 调用同一个 `scripts/extract_features.py`，仅 `--task_instruction ""` 不同。输出结构完全一致：`demo_X/last_preaction`，shape `(T, 33, 4096)`。RSA 脚本无需适配数据格式。

### 2. RSA 脚本问题 ❌ — 路径硬编码不支持 no-inst

`load_vla_features()` 第 59 行：
```python
def load_vla_features(model_type, task, demo_ids, layer):
    path = FEAT_ROOT / f"{model_type}_libero_goal" / f"{task}.h5"
```

`model_type` 只接受 `"trained"` / `"untrained"`，路径拼为 `trained_libero_goal/`。无法指向 `trained_libero_goal_no_inst/`。

### 3. 已有 RSA 结果可复用 ✅

`rsa_results.json` 包含 with-inst 全部数据：
- trained peak RSA = **0.4876** (layer 14)
- untrained peak RSA = **0.4846**
- DINO RSA = **0.388**
- G1 delta = 0.003 (FAIL), G2 = 4/33 (FAIL)

with-inst 和 DINO 结果无需重跑。

### 4. 缺失功能：bootstrap CI

D025 gate 要求 "bootstrap CI excludes 0"，当前脚本**没有 bootstrap**。

### 5. 提取进度

- `trained_libero_goal_no_inst/`: 1/10 tasks 完成
- `untrained_libero_goal_no_inst/`: 3/10 tasks 完成

---

## 修改方案（4 处改动 + 1 个新命令）

### 改动 1：`load_vla_features` 加 suffix 参数（第 59 行）

```python
# 原：
def load_vla_features(model_type, task, demo_ids, layer):
    path = FEAT_ROOT / f"{model_type}_libero_goal" / f"{task}.h5"

# 改为：
def load_vla_features(model_type, task, demo_ids, layer, suffix=""):
    path = FEAT_ROOT / f"{model_type}_libero_goal{suffix}" / f"{task}.h5"
```

### 改动 2：argparse 加 `--feat_suffix`（约第 186 行，`--skip_cka` 后面）

```python
parser.add_argument("--feat_suffix", type=str, default="",
                    help="Suffix for feature dirs (e.g. '_no_inst')")
```

### 改动 3：调用处传 suffix（约第 253-254 行）

```python
# 原：
tf = load_vla_features("trained", task, demo_ids, layer)
uf = load_vla_features("untrained", task, demo_ids, layer)

# 改为：
tf = load_vla_features("trained", task, demo_ids, layer, suffix=args.feat_suffix)
uf = load_vla_features("untrained", task, demo_ids, layer, suffix=args.feat_suffix)
```

### 改动 4：输出路径含 suffix（约第 346 行）

```python
# 原：
out_path = OUT_DIR / "rsa_results.json"

# 改为：
out_path = OUT_DIR / f"rsa_results{args.feat_suffix}.json"
```

---

## 提取完成后的执行命令

```bash
# Step 1: 跑 no-inst RSA（CKA 可跳过，省时间）
cd /root/vla-ssd
python rsa_analysis.py --feat_suffix _no_inst --skip_cka
# → 输出 /root/autodl-tmp/vla-ssd/results/rsa/rsa_results_no_inst.json

# Step 2: D025 gate 判定（python one-liner）
python -c "
import json
with open('/root/autodl-tmp/vla-ssd/results/rsa/rsa_results.json') as f:
    wi = json.load(f)
with open('/root/autodl-tmp/vla-ssd/results/rsa/rsa_results_no_inst.json') as f:
    ni = json.load(f)

wi_peak = max(v['trained_rsa'] for v in wi['per_layer'].values())
ni_peak = max(v['trained_rsa'] for v in ni['per_layer'].values())
dino_rsa = wi['per_layer']['layer_0']['dino_rsa']
delta = wi_peak - ni_peak

print(f'with-inst RSA (trained peak): {wi_peak:.4f}')
print(f'no-inst RSA (trained peak):   {ni_peak:.4f}')
print(f'DINO RSA:                     {dino_rsa:.4f}')
print(f'Delta (with - no):            {delta:+.4f}')
print(f'Delta > 0.10:                 {delta > 0.10}')
print(f'no-inst ≤ DINO + 0.05:        {ni_peak <= dino_rsa + 0.05}')
print(f'FAIL check (no-inst ≥ with-inst - 0.05): {ni_peak >= wi_peak - 0.05}')
"
```

### Bootstrap CI（需额外实现）

当前脚本无 bootstrap。建议在 Step 2 中加入，对 no-inst 的 per-task RSA 做 1000 次 bootstrap resample，计算 delta 的 95% CI。这可以写成独立的 D025 gate 脚本，而不是塞进 `rsa_analysis.py`。是否需要我现在写出 bootstrap 的具体代码？

---
