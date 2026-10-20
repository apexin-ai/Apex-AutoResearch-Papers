# WNUT-17 数据质量诊断报告 (exp_003)

## 概要

**根因：训练数据空实例比例过高（63.8%），导致模型过度倾向于预测"无实体"。**

这不是数据转换 bug，而是训练数据构造策略问题叠加 WNUT-17 固有难度。

---

## 方向 1：数据格式转换检查

### 转换脚本 (convert_wnut17.py)
- BIO→span 转换逻辑正确，与标准 BIO 解码一致
- Entity type mapping 正确：6 types (corporation, creative-work, group, location, person, product)
- Char offset 计算正确（基于 space-joined tokens）
- 脚本内含 validation：检查 text[start:end] == entity_text

### 数据格式
- test.json: JSONL 格式，1287 行，`load_uie_jsonl()` 正常加载
- train.json: JSONL 格式，3394 行

### Prompt 模板差异（次要问题）
训练与推理 prompt 有轻微不一致：
- **训练**: `Output format: {"entities": [...], "relations": [...], "events": []}` + `For relations, head is the subject entity...`
- **推理**: `Output format: {"entities": [{"text": "...", "type": "...", "start": <int>, "end": <int>}], ...}`（无 relations 说明行）

影响有限，因为模型理解核心指令，且 XGrammar 约束解码保证输出格式。

**结论：数据转换本身无 bug。**

---

## 方向 2：Greedy 输出抽查

### F1=0 实例分类（共 355 个，金标非空）

| 类别 | 数量 | 占比 | 说明 |
|------|------|------|------|
| 模型输出为空 | 260 | 73.2% | **主要失败模式** |
| Span 边界不匹配 | 49 | 13.8% | 模型预测了实体但位置偏移 |
| Type 不匹配 | 46 | 13.0% | 位置正确但类型错误 |

### 典型案例

**模型输出空（260 例）：**
- `"( Source : ANI )"` → gold: ANI (group), pred: 空
- `"Watch What Else is Making News"` → gold: What Else is Making News (creative-work), pred: 空
- `"Wow , / r / news totally kicked..."` → gold: /r/news (group), /r/politics (group), pred: 空
- `"they changed all the topics to Zlatan"` → gold: Zlatan (product), pred: 空
- `"Bhangra is Punjabi"` → gold: Bhangra (person), Punjabi (location), pred: 空

**Span 边界错误（49 例）：**
- gold `Gurez sector` (33-45) → pred `Gurez` (33-38)：漏标 "sector"
- gold `Rajesh Kalia` (164-176) → pred `Colonel Rajesh Kalia` (156-176)：多标 title
- gold `Chad` (6-10) → pred `Rip Chad` (2-10)

**Type 错误（46 例）：**
- gold `Zlatan` = product → pred `Zlatan` = person（合理歧义）
- 部分 WNUT-17 金标本身有争议（如 `Bhangra` 标为 person 而非 creative-work）

---

## 方向 3：Gold Empty 实例处理

### 数据分布

| | 训练集 | 测试集 |
|---|---|---|
| 总实例数 | 3394 | 1287 |
| 空实体实例 | 2166 (63.8%) | 598 (46.5%) |
| 有实体实例 | 1228 (36.2%) | 689 (53.5%) |

### 评估处理

report.json 中 `n_gold_empty_filtered: 598` 表明评估代码**正确过滤**了 gold empty 实例：
- "full" 集 n=689（排除 gold empty）
- "conditional" 集 n=334（进一步排除 greedy F1=0 的）

### 模型在 gold empty 实例上的行为
- 598 个 gold empty 实例中，579 个模型也输出空（96.8%）
- 仅 19 个产生了假阳性预测

**结论：gold empty 处理正确，不是 bug。但 63.8% 训练 empty 率导致模型习得过强的"空输出"先验。**

---

## 方向 4：Train/Eval Loss vs 推理 F1 差距

### 训练日志

| Epoch | Train Loss | Eval Loss |
|-------|-----------|-----------|
| ~1 | 0.2080 | 0.0880 |
| ~2 | 0.0470 | 0.0857 |
| ~3 | 0.0300 | **0.0772** (最佳) |
| ~4 | 0.0240 | 0.0788 |
| ~5 | 0.0210 | 0.0896 (回升) |

- 模型用最终 checkpoint（epoch 5, step 1065），但 epoch 3 的 eval loss 最低
- Eval loss 在 epoch 5 回升 → 轻微过拟合
- 训练使用 LoRA（87M trainable / 8.3B total = 1.05%），5 epochs，batch 16

### 关键问题
- **训练的 eval set = dev set**（1009 实例），与 test set（1287 实例）是不同数据切分
- 模型确实是在 WNUT-17 上训练的（非 SciERC zero-shot）
- Eval loss 低（0.077-0.089）但推理 F1 仅 0.525 → loss 被大量空实例拉低（空实例 loss 很小，只需输出 `{"entities": [], ...}`）

---

## Logprob 反向相关解释

| 子集 | Mean Logprob | 说明 |
|------|-------------|------|
| 空预测（n=260） | **-0.007** | 极高置信 |
| 非空预测 F1=0（n=95） | -0.054 | 中等置信 |
| 非空预测 F1>0（n=334） | -0.046 | 中等置信 |

**机制**：模型预测空输出时置信度最高（logprob 接近 0），因为训练数据中 63.8% 是空实例。在 gold 非空的 689 实例中：
- 高 logprob → 很可能是空预测 → F1=0 → **负相关 (rho = -0.41)**
- 在 conditional 集（F1>0, n=334）中，logprob rho = +0.35 → 模型对非空预测的置信度确实有区分力

### SJ 高但 rho 低的原因
- 155 个实例：16 个 sample 全部为空 → SJ = 1.0 但 F1 = 0
- 这些高一致性 + 零 F1 的点拉平了整体相关性
- Conditional 集 SJ rho = 0.288，显著高于 full 集的 0.089

---

## 根因判断

**主因：训练数据空实例过多（63.8%）— 数据构造策略问题，非转换 bug。**

| 因素 | 类别 | 影响程度 |
|------|------|---------|
| 训练集 63.8% 空实例 | 数据策略 | **致命** — 导致 73% 的 F1=0 |
| WNUT-17 社交媒体噪声 | 方法边界 | 中等 — 导致 27% 的 F1=0 |
| Prompt 模板微小差异 | 次要 bug | 轻微 |
| Epoch 5 轻微过拟合 | 训练策略 | 轻微 |

---

## 修复建议

### P0：降低训练空实例比例
将空实例从 63.8% 下采样到 ≤25%（保留 ~400 个空实例 + 1228 个有实体 = 空占比 24.6%），重新训练。这是最直接的修复。

### P1：使用 best checkpoint
训练时加 `save_best_model=True`（按 eval_loss），或手动使用 epoch 3 的 checkpoint（step 600, eval_loss=0.077）而非最终的 epoch 5。

### P2：评估指标选择
对于 WNUT-17 这类 high-empty-rate 数据集，使用 conditional 指标（排除 F1=0）作为主信号，full 指标仅作参考。当前 conditional SJ rho = 0.288, logprob rho = 0.350 表明方法在非空预测上有效。

### P3：金标质量 review
WNUT-17 存在标注噪声（如 `Bhangra` = person, `Zlatan` = product），但这是数据集固有问题，非我方可控。
