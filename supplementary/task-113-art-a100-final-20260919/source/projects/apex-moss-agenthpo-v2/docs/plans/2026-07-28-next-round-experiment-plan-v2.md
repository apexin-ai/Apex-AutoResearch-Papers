# MOSS 第二阶段实验计划 v2(2026-07-28)

> **状态**：历史方向稿，未执行。用户随后决定先单独验证 optimizer 的三层 benchmark
> 机制，不在同一阶段混入 Builder seed、`run_snippet` 或跨源泛化梯度；当前唯一待批准
> 协议为 `2026-07-28-three-tier-benchmark-qualification.md`。本文仅保留设计演进记录，
> 不得作为执行依据；未因本文发起模型调用。

---

## 1. 第一阶段已回答了什么

第一阶段(24M executor tokens,已全部消耗)关闭了一个问题、暴露了两个问题:

**已回答:harness 进化在 training benchmark 上的增益可独立复现。**

| lineage | seed | final harness | training 正式增益 | 训练资格线 +15 |
|---|---|---|---:|---|
| R0(旧) | v001 | v005 | +20.8 | 合格 |
| R1 | v001 | v007 | +8.3 | 不合格 |
| R2 | v001 | v002 | +16.7 | 合格 |

3 条独立 lineage 中 2 条越线(预注册 2/3 前提成立)。

**暴露的问题一:training 增益不迁移到 test benchmark。**

合格 lineage(R0/R2)在 12 道全新 test benchmark(BigCodeBench-Hard 不同编号,
零反馈)上平均增益 +1.39 点,bootstrap 95% CI [−4.17, +8.33] 跨 0。冻结判定
`inconclusive`——统计上既够不到泛化线也够不到过拟合线。但证据形态与 proposer
过拟合到 training benchmark 一致:增益系于单题交换得失、执行 tokens 为 v001 的
4–6 倍。

**暴露的问题二:第一阶段的 training/test 两层基准全部来自同一 benchmark 源
(BigCodeBench-Hard),只能检出"记住个别题目"这一层过拟合;无法区分 harness
是否学到的只是 BigCodeBench-Hard 的出题风格而非任务族通法。**

第二阶段针对这两个问题重新设计。

---

## 2. 第二阶段要回答的问题

| 编号 | 问题 | 用 MOSS 术语表述 |
|---|---|---|
| **Q1'** | 修复进化机制后,harness 能否在 test benchmark 上产生显著正增益? | 双轨循环 + 回归锁 + 反馈加密后,lineage final 在 test 上 gain > 0 且 CI 不跨 0? |
| **Q3'** | builder 初稿作为 seed 是否比通用 seed 的 evolvability 更高? | builder0-seeded lineage 的 test 终点 > v001-seeded lineage 的 test 终点? |
| **QG** | harness 学到的能力到底泛化到了什么层次? | 泛化梯度 T0–T4 上增益的衰减形态? |

Q1' 和 Q3' 共用同一批 lineage(一笔钱答两个问题)。QG 是第一阶段没有能力回答
的新维度,通过泛化梯度实现。

---

## 3. 核心改造一:双轨进化循环

### 3.1 第一阶段单轨循环的缺陷

```
proposer 看 training trace → 生成候选 harness → selector 只看 training 分数 → 接受
```

selector 只看 training benchmark,所以记题式修改在 selector 眼里和真泛化一样好。
第一阶段 R0/R2"training 合格、test ≈ 0"是该通路的实证。

### 3.2 双轨循环架构

```
proposer 消费 training trace → 生成候选 harness
    → [门禁 1] 合同/语法/smoke(不变)
    → [门禁 2] 回归锁:locked 任务不得退步(§4.1)
    → [门禁 3] training quick(proposer 可见结果)
    → [门禁 4] validation quick(proposer 不可见,仅 selector 用)
    → [selector] 接受条件:training ≥ best 且 validation ≥ best − ε
    → 重复至 training 满分或轮数上限
```

**关键规则**:

1. **proposer 永远看不到 validation 的成绩、trace 或失败原因。** 变异的信息源
   只有 training benchmark;
2. **selector** 同时看 training 和 validation 的**标量分数**(不看 trace):
   - training 上必须有提升(驱动力);
   - validation 上不得低于当前最优 − ε(否决权);
   - 被否决的版本记入 archive 标记 `rejected`,proposer 下轮可见其 training
     trace 但不知被拒原因;
3. **validation 不参与停止规则**:何时停止进化只看 training 侧;
4. **test benchmark 全程零接触**:每条 lineage 冻结 final 后才运行一次。

**为什么不把 validation trace 也喂给 proposer?**

把 validation trace 喂给 proposer = 把 validation benchmark 并入 training
benchmark = 系统退回单轨循环。selector 失去独立于变异数据的否决信号,记题式修改
重新畅通无阻。test benchmark 终验仍然无偏(holdout 未见),但过拟合只能在
lineage 结束、预算花完后才被量出——双轨买的不是更准的测量,是**循环内的早期拦截**。

反向论点如实记录:并入 validation 使 proposer 反馈池从 ~16 题变 ~32 题,更大反馈
池本身有利于泛化。"更大反馈池 vs 独立过滤器"孰优是开放的实证问题;本方案基于
第一阶段单轨终局选过滤器,以 training 8→16 扩容补偿反馈池规模。预注册回退:
若 validation 否决率 ≈ 0(过滤器闲置),替代方案为并回反馈池 + 2σ 显著性门
(统计路线)。

---

## 4. 核心改造二:进化机制三项修复

### 4.1 回归锁(最高优先级)

**问题**:R1 逐任务矩阵显示 8 道 training 中 4 道恒过、另 4 道在版本间交换得失
("按下葫芦浮起瓢"),proposer 无回归保护。

**方案**:连续 ≥3 版通过的 training 任务标记 `locked`;候选版本在任一 locked 任务
上失败 → 在进入 validation 评估前直接拒绝。proposer 可看到哪些任务被 locked,
但不知拒绝机制存在。

**先例**:HarnessX 的 seesaw constraint(候选不得回归任何已解决任务)独立同构。
实现位置:`loop.py` 的接受逻辑,新增 `locked_tasks` 集合。

### 4.2 反馈加密(高优先级)

**问题**:8 道 training 中仅 4 道有区分度,单题 = 12.5 个百分点,一题的随机翻转
足以改变 proposer 的提案方向。

**方案**:training benchmark 从 8 题扩至 ~16 题(见 §5),单题权重 → 6.25%,
背题面翻倍。

### 4.3 自测执行通道(中优先级,可砍)

**问题**:v005–v007 的 harness 要求 executor 写 `__main__` assertions 自验,但
`_eval_one.py` 只运行 `test_solution.py`,assertions 从未执行。executor 花
303k tokens 在"写测试→嘴上说通过→实际没跑"的仪式上。

**方案**:新增 `run_snippet` 工具(沙箱:超时 10s、无网络、无文件写入);harness
可在流程中调用来验证中间假设,但不可修改 `solution.py` 或 `test_solution.py`。

**砍项优先级**:回归锁 > 反馈加密 > 自测通道。

---

## 5. 核心改造三:跨 benchmark 三层基准 + 泛化梯度

### 5.1 第一阶段的缺陷

三个数据池全部来自 BigCodeBench-Hard,只能检出"记住个别题目编号"这一层
过拟合。如果 harness 学到的是"BigCodeBench-Hard 的出题风格"(docstring 结构、
库偏好、测试模式),在同源的 validation 和 test 上照样表现好——归因链前提不成立。

### 5.2 三层基准重新设计(跨 benchmark 源)

| 基准层 | 来源 | 数量 | 进化循环中角色 |
|---|---|---|---|
| **training benchmark** | BigCodeBench-**Hard** | ~16 | proposer 唯一反馈源 |
| **validation benchmark** | BigCodeBench **非 Hard** | ~16–20 | selector 否决闸;标量分数可见,trace 永不进 proposer |
| **test benchmark** | BigCodeBench **非 Hard**(与 val 不重叠) | ~24 | 终验;零接触,lineage 冻结 final 后 3 遍正式 |

**为什么 validation 选非 Hard**:

- 与 training(Hard)来自同一 BigCodeBench 框架但**不同子集**,task family 形态
  一致(函数级实现 + 测试),但题目完全不同;
- 如果 harness 利用了 Hard 特有的复杂度模式或出题偏好,在非 Hard 上会露馅
  → selector 拦截;
- 如果 harness 学到了"函数级实现"这个 task family 的通法,在非 Hard 上也
  应该有效 → selector 放行;
- 格式差异足够小,不会因为格式不兼容导致误杀合理版本。

**前置检查**:v001 在非 Hard 上不能饱和(接近 100% 则无区分度)。需先跑 canary:
从 BigCodeBench 非 Hard 随机抽 5 道,v001 单遍,落在 30–80% 才可用。

### 5.3 泛化梯度(T0–T4):精确定位 harness 学到了什么层次

不再用单一 test benchmark 做二元判定("泛化了/没泛化"),而是在终验时让 final
harness 在**五个递增距离**上分别跑分,画出泛化衰减曲线:

| 级别 | 与 training benchmark 的差异维度 | 具体数据源 | 掉分说明过拟合到… |
|---|---|---|---|
| **T0** | 仅题目不同(同源同难度同格式) | BigCodeBench-Hard 不同编号 | 个别题目特征(记题) |
| **T1** | 难度不同(同源同格式) | BigCodeBench 非 Hard | Hard 特有的难度模式 |
| **T2** | benchmark 源不同(同为函数级实现) | LiveCodeBench / CodeContests 函数题 | BigCodeBench 的出题风格 |
| **T3** | 信息结构不同(同为实现,可见测试量不同) | `tddgen`(全测试可见)格式题 | "部分信息"这种特定信息形态 |
| **T4** | task family 不同(代码但从实现变修 bug) | `bugfix` 族 / SWE-bench 单函数级 | 任务族本身 |

**解读规则**:

- T0 掉分 → 最低级过拟合(记题),修 proposer 即可
- T1 掉分 → benchmark 难度层过拟合,harness 策略强绑 Hard 难度
- T2 掉分 → benchmark 风格层过拟合,harness 利用了 BigCodeBench 惯例
- T3 掉分 → 信息结构层,harness 策略依赖"测试不完整"这个条件——这是
  task-conditioned 的能力边界,不是失败
- T4 掉分 → task family 层——**预期中的衰减**,证明 harness 确实是
  task-conditioned 的

```
泛化衰减曲线(示意):

harness 增益
    ↑
+15 |  ██
    |  ██  ██
+10 |  ██  ██
    |  ██  ██  ██
 +5 |  ██  ██  ██
    |  ██  ██  ██  ░░
  0 |--██--██--██--░░--░░---
    |              ░░  ░░
 -5 |
    +--T0--T1--T2--T3--T4→ 距离

理想形态:T0–T2 保持正增益(通法),T3–T4 开始衰减(task-conditioned 边界)
```

**分期策略**:

- **第二阶段必做**:T0 + T1(数据现成或仅需导入 BigCodeBench 非 Hard)
- **第二阶段尽力做**:T2(需导入 LiveCodeBench + 格式适配)
- **第三阶段**:T3 + T4(需生成新格式题目或适配 SWE-bench)

即使只有 T0+T1 两级,也比第一阶段的单一 test 信息量大一倍:能区分"记题"和
"Hard 风格过拟合"。

---

## 6. 实验矩阵

### 6.1 lineage 设计

4 条独立 lineage,共用修复后的双轨进化循环和同一冻结三层基准:

| lineage | seed | 回答 |
|---|---|---|
| A1 | 通用 v001(逐字) | Q1' 可复现性证据 #1 |
| A2 | 通用 v001(逐字) | Q1' 可复现性证据 #2 |
| B1 | builder0(仅凭 family card 生成,过门禁第一版,不挑) | Q3' evolvability 证据 #1 |
| B2 | builder0(同上,独立进化) | Q3' evolvability 证据 #2 |

4 条 lineage 之间禁止共享 trace、提案或任何进化中间产物。

### 6.2 每条 lineage 的进化流程

```
seed(v001 或 builder0)
  → proposer 消费 training trace → 候选 harness
  → [回归锁] locked 任务检查
  → [training quick] ~16 题单遍(proposer 可见)
  → [validation quick] ~16–20 题单遍(proposer 不可见)
  → [selector] training ≥ best ∧ validation ≥ best − ε → 接受/拒绝
  → archive.jsonl 记录(含 val_score、rejected_reason)
  → 重复至 training 满分或轮数上限(≤7 版)
```

### 6.3 终验

每条 lineage 冻结 final 后:

1. **主判定**:final 在 test benchmark(~24 题非 Hard)上 3 遍正式;
2. **泛化梯度**:final 在 T0–T4 每级各取一组题(每级 ≥8 题)单遍;
3. **v001 基线**:在所有级别上 3 遍,作为增益计算的分母。

---

## 7. 判定标准

### 7.1 主指标(唯一定胜负)

`test_gain = test_score(final) − test_score(v001)`

每条 lineage 3 遍,task-paired bootstrap(固定 seed)。

### 7.2 Q1' 判定

| A1 和 A2 结果 | 结论 |
|---|---|
| 两条均 training ≥ +15 且 test gain 显著 > 0 | 修复后进化可复现且可迁移 |
| 两条均 training ≥ +15 但 test ≈ 0 | 可复现但仍过拟合(双轨不够) |
| training 前提不满足 | 机制修复不够,需进一步迭代 |

### 7.3 Q3' 判定

| B 组 vs A 组 | 结论 |
|---|---|
| B 组 test 终点均值 > A 组(超过组内波动) | builder seed 的 evolvability 优势成立 |
| B 组 training 涨而 test 不涨 | builder 初稿更易诱导过拟合(负结论) |
| 无显著差异 | seed 不影响进化结果 |

### 7.4 QG 判定(泛化梯度)

不做二元判定,报告 T0–T4 上的增益衰减曲线形态:

- **理想**:T0–T2 正增益,T3–T4 衰减 → harness 学到了函数级实现的通法
- **中性**:T0 正增益,T1 开始衰减 → 只学到了 BigCodeBench-Hard 特有策略
- **最差**:T0 就 ≈ 0 → 双轨循环仍未解决记题问题

### 7.5 诊断指标(仅描述,不参与判定)

| 指标 | 含义 |
|---|---|
| `training_gain − test_gain` | 总过拟合量 |
| `validation_gain − test_gain` | 选择侧过拟合量(validation 被选择压力污染的程度) |
| validation 否决率 | 双轨过滤器是否真正起作用 |
| 逐任务翻转率 | 回归锁的效果 |
| tokens/task 相对 v001 | 成本膨胀 |
| retention = test_gain / training_gain | 与 QD-harness 论文对标的迁移效率 |

---

## 8. 防过拟合手段全览

| 手段 | 防的是哪层过拟合 | 机制 |
|---|---|---|
| 三层数据分离(train/val/test 互不相交) | 记题 | proposer 不见 val/test |
| 跨 benchmark 源(Hard vs 非 Hard) | benchmark 风格 | val/test 与 training 来自不同子集 |
| 回归锁 | 策略震荡(换着错) | locked 任务回归即拒 |
| training 扩容 8→16 | 反馈粒度不足 | 单题权重 12.5% → 6.25% |
| validation 否决闸 | 记题式修改通过 selector | val 分不降才接受 |
| ε 容忍带 | 单次噪声误杀 | v001 在 val 上 2 遍定标 |
| test 只考一次 | 选择侧泄漏 | 终验零接触 |
| 泛化梯度 T0–T4 | 所有层次(归因而非拦截) | 终验画出衰减曲线 |

---

## 9. 代码变更清单

| 文件 | 变更 | 类型 |
|---|---|---|
| `loop.py` | 新增 `locked_tasks` + 回归锁检查 | 修改 |
| `loop.py` | 新增 validation quick 步骤(training quick 之后、accept 之前) | 修改 |
| `loop.py` | selector:training ≥ best ∧ validation ≥ best − ε | 修改 |
| `proposer.py` | 验证 validation trace 不进入 prompt(应已如此) | 验证 |
| `_eval_one.py` | 新增 `run_snippet` 工具(沙箱化) | 修改 |
| `eval.py` | 支持对 validation 池评估但结果不写入 proposer 可见路径 | 修改 |
| `archive.jsonl` | 新增 `val_score`、`rejected_reason` 字段 | 格式扩展 |
| `config.py` | 新增 `EVOLUTION_VAL_TOLERANCE`(ε) | 新增 |
| 导入脚本 | BigCodeBench 非 Hard 题目导入 + tddgen_hidden 格式转换 | 新增 |
| 导入脚本 | LiveCodeBench 导入 + 格式适配(T2 级,尽力做) | 新增 |

不改动:`eval.py` 防作弊/哈希校验、`builder.py`、`harness_source.py`、判分入口。

---

## 10. 预算估算

| 项目 | tokens(悲观) | tokens(乐观) |
|---|---:|---:|
| 4 lineage 进化(每条 ~16 training + ~16 val,≤7 版) | 32M | 20M |
| 4 lineage test 终验(~24 题 × 3 遍) | 20M | 12M |
| v001 基线(所有级别 × 3 遍 + val 定标 2 遍) | 6M | 4M |
| 泛化梯度 T0–T4(每级 ≥8 题,final + v001 各 1 遍) | 8M | 5M |
| 门禁、canary、隔离余量 | 4M | 3M |
| **合计** | **~70M** | **~44M** |

若只批 2 条 lineage(A1+B1)且泛化梯度只做 T0+T1:约减 40–45%,
悲观 ~40M / 乐观 ~25M。

---

## 11. 分期执行顺序

### 阶段 0:前置验证(零正式 token)

1. 导入 BigCodeBench 非 Hard 题目(~990 道),转为 `tddgen_hidden` 格式;
2. 随机抽 5 道 canary,v001 单遍:确认基线落在 30–80%(不饱和、有区分度);
3. 如果饱和:回退到同源不同题设计(T0 替代 T1 作 validation),仍比第一阶段强;
4. sha256 机械冻结 training / validation / test 三个池,在首次 proposer 调用前
   落盘并 commit。

### 阶段 1:进化(预算主体)

按决策价值排序启动 lineage:A1 → B1 → A2 → B2。预算不足时从尾部砍(A1+B1
即可得初步 Q1'/Q3')。

### 阶段 2:终验 + 泛化梯度

所有 lineage 冻结 final 后:
- 主判定:test benchmark 3 遍正式;
- 泛化梯度:T0+T1(必做),T2(尽力做);
- 机械分析:套用冻结判定线 + 画泛化衰减曲线。

### 阶段 3(更后,依赖第二阶段)

- T3+T4 级别的泛化梯度扩展;
- Q2':同题双呈现配对,回答"不同 task family 是否真的需要不同 harness"。

---

## 12. 风险与回退

| 风险 | 后果 | 回退 |
|---|---|---|
| v001 在非 Hard 上饱和(≈100%) | validation 无区分度 | 回退到同源不同题(Hard)作 validation;或用 LiveCodeBench |
| 双轨否决率过高(大量版本被拦) | 进化停滞 | 放宽 ε 或回退单轨 + 2σ 显著性门 |
| 双轨否决率 ≈ 0(过滤器闲置) | 等效单轨 | 把 validation 并回反馈池 + 2σ 门(统计路线) |
| 预算超限 | lineage 不完整 | 按 A1 > B1 > A2 > B2 排序砍尾 |
| builder0 在新 training 上门禁不过 | B 组无法启动 | builder 重新生成一次(仍只看 family card) |
| LiveCodeBench 格式适配失败 | T2 级无数据 | T2 降级为"已知风险",只报告 T0+T1 |
| `run_snippet` 沙箱逃逸 | 安全风险 | 不启用此工具,仅做回归锁 + 反馈加密 |

---

## 13. 相关工作定位

| MOSS 组件 | 最接近的外部工作 | 本方案的区别 |
|---|---|---|
| 双轨循环(train 变异 / val 选择) | GEPA:reflector 只看 train,Pareto 选择看 val | GEPA 变异对象是提示词;MOSS 变异完整 harness 源码;GEPA 的 train/val 分离**无消融实验支撑**,本方案基于第一阶段单轨终局作为本地实证 |
| 回归锁 | HarnessX seesaw constraint | 独立同构;HarnessX 无可见的 train/val 分离 |
| 泛化梯度 T0–T4 | 无直接先例 | 新贡献:从二元"泛化了/没泛化"到多级归因 |
| 完整 harness 进化 | QD-harness(2607.13683):4 类杠杆 × 13 编辑面 | QD-harness 变异和选择都在 training 上(无 val 层),抗过拟合走统计路线(2σ 门);本方案走数据路线(val 否决) |
| sealed test 只考一次 | QD-harness sealed test / GEPA held-out | 已有先例;本方案在此基础上扩展为梯度 |
| builder seed evolvability | HarnessX 可组合模块初始化 | 本方案用 A/B 对照量化 seed 对进化的影响 |

**定位总结**:把 GEPA 的数据角色纪律完整迁移到 harness 源码层 + 跨 benchmark
泛化梯度,截至检索日尚无同时具备这两点的工作。

---

## 14. 历史决策菜单（已作废）

> 下列选项已被“先做两条相同通用 seed 的 optimizer 资格实验”取代，不再等待拍板。

| # | 问题 | 推荐 |
|---|---|---|
| 1 | 双轨循环:是否采纳? | 采纳(第一阶段终局是本地实证) |
| 2 | 三项修复:全要 / 砍 `run_snippet` / 只要回归锁? | 全要;预算紧则砍 `run_snippet` |
| 3 | lineage 数量:4 条 / 2 条(A1+B1)? | 4 条;预算紧则 2 条 |
| 4 | 预算上限:给一个具体数字 | 悲观 ~70M / 乐观 ~44M / 最小 ~25M |
| 5 | 泛化梯度:T0+T1 必做,T2 是否尝试? | 尽力做 T2 |
| 6 | 是否先跑非 Hard canary 验证 v001 基线? | 是(零成本前置检查) |

---

## 附录 A:MOSS 术语对照

| MOSS 术语 | 本方案对应 | 角色 |
|---|---|---|
| training benchmark | BigCodeBench-Hard ~16 题 | proposer 唯一反馈源;selector 的提升条件 |
| validation benchmark | BigCodeBench 非 Hard ~16–20 题 | selector 否决闸;标量分数可见,trace 不进 proposer |
| test benchmark | BigCodeBench 非 Hard ~24 题(与 val 不重叠) | 终验;零接触,final 冻结后 3 遍 |
| 泛化梯度 T0–T4 | 五级递增距离的 benchmark 组 | 终验画衰减曲线,精确归因过拟合层次 |
| lineage | A1/A2/B1/B2 | 从固定 seed 独立进化的 harness 谱系 |
| seed | v001 或 builder0 | lineage 起点 harness |
| proposer | Sonnet via TokenRouter | 消费 training trace,生成候选 harness |
| selector | loop.py 双轨接受逻辑 | training 提升 ∧ validation 不退步 → 接受 |
| executor | Haiku via TokenRouter(冻结) | 使用 harness 解题的固定模型 |
| archive | archive.jsonl | 完整进化历史,含被拒版本和 val_score |

## 附录 B:参考文献

- GEPA: [arXiv:2507.19457](https://arxiv.org/abs/2507.19457), ICLR 2026 Oral
- QD-harness: [arXiv:2607.13683](https://arxiv.org/abs/2607.13683) (2026)
- HarnessX / AEGIS: [arXiv:2606.14249](https://arxiv.org/abs/2606.14249) (2026)
- Darwin Gödel Machine: [arXiv:2505.22954](https://arxiv.org/abs/2505.22954) (2025)
- BigCodeBench: [bigcode-bench.github.io](https://bigcode-bench.github.io/)

## 附录 C:本文档与已有文档的关系

| 文档 | 状态 |
|---|---|
| `2026-07-28-next-round-integrated-plan.md`(v1) | 历史方向稿 |
| `2026-07-27-hidden-final-verification-round.md` | 第一阶段冻结协议 |
| `2026-07-28-q1-confirmation-resumption.md` | 第一阶段恢复指引(已完成) |
| `experiment-status-checkpoint.md` | 第一阶段数据源 |
| `RESULTS.md` | 第一阶段正式结果 |
| `2026-07-28-three-tier-benchmark-qualification.md` | **当前唯一待批准协议** |
| 本文档(v2) | **历史方向稿，已被替代** |
