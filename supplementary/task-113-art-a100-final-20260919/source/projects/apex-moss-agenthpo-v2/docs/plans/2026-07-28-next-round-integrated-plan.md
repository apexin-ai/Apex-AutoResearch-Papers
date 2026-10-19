# MOSS 下一轮实验整合方案(2026-07-28)

> **状态**:历史方向性设计。第一阶段已完成；原第二阶段“机制修复 + Builder seed
> 四谱系合并实验”已由
> `docs/plans/2026-07-28-three-tier-benchmark-qualification.md` 替代，不再执行。
> 新顺序为：先用两条逐字相同通用 seed lineage 完成 training/validation/test
> 三层迁移资格实验；通过 go gate 后，Builder evolvability 与 task-conditioned
> specialization 才分别另立协议。
> 整合来源:本轮全部实验数据与现象(`experiment-status-checkpoint.md`)、
> 三个用户追问的分析(`round3-design-directions.md`)、进化指标与抗过拟合设计
> (同文件 §3.1)、以及 GEPA/DGM/HarnessX 等外部最新工作的关键启发。
>
> **2026-07-28 更新:第一阶段已完成**(数据见 RESULTS.md 第五轮、
> `results/official/q1-confirmation-analysis.json`)。冻结判定:训练提升可复现
> (R0 +20.8、R2 +16.7,2/3 前提成立;R1 +8.3 不合格),external 迁移**不明确**
> (合格谱系平均 +1.39 点,bootstrap 95% CI [−4.17,+8.33] 跨 0)。R1-external 格按
> 预注册预算排序未运行,24M 已用 23.18M。本文重心随之移到第二阶段;
> §1.1 记录第一阶段终局及其对第二阶段设计的影响。

---

## 0. 用大白话先说结论

这份文档回答一个核心问题:**下一步怎么实验?**

简单说分三步:

1. **先把手头的活干完**(跑完 R2 复现 + 正式考试,关掉本轮的"进化能不能重复"这个问题);
2. **修好练习机制再重新练**(当前练习方式有三个毛病——学了新的忘旧的、练习反馈太粗、
   假装自测。修好之后,用两种不同的起点各练两遍,一笔钱同时回答"修好后还能练出来吗"
   和"好的初稿是不是更好的起点");
3. **用更严格的方法重答"不同题型要不要不同流程"**(必须先确认练习机制靠谱,否则
   比较的是两个不靠谱的东西)。

第 2 步里最大的改动是**借鉴 GEPA 的双轨进化**:练习时模型只看训练题的反馈来改进,
但系统在决定"这个新版本要不要留下来"时,偷偷用一批模型从未见过的验证题打个分。
如果新版本在验证题上变差了,即使训练题上变好了也不接受——这就像老师改卷子用两套题,
学生只能看到一套,另一套用来防背题。当前系统完全没有这个机制,所以学生可以肆无忌惮
地背题。

---

## 1. 本轮已经证明了什么、没证明什么

### 已证明(有正式数据支撑)

| 发现 | 证据 | 含义 |
|---|---|---|
| Harness 能显著改变固定模型的行为和训练成绩 | R0 train +20.8 点 | Harness 是有效的可优化对象 |
| 但训练提升不一定迁移到新题 | R0 val −3.3 点(灰区) | 存在过拟合风险 |
| 当前进化机制高度不稳定 | R1 v005→v007 峰值丢失;逐任务"按下葫芦浮起瓢" | 不是"越练越好",是"换着错" |
| "题型优势"是题池难度的假象 | Q2 配对 −6.7,CI 跨 0,`direction_refuted` | 对照组设计错误能产生方向相反的假信号 |
| Builder 能生成结构完整的 Harness,但不能生成好用的 | Q3 两族均低于 v001 | "能生成代码" ≠ "能生成有效工作流" |
| 评测门禁与反事实对照和算法本身同等重要 | R1/v003 伪下降、Q2 混淆、多次基础设施错误 | 合同/门禁必须是框架级能力 |

### 没证明(需要后续实验)

- ~~进化是否可独立重复(R2 未完成)~~ → **已关闭**:训练层面可复现(见 §1.1)
- 训练学到的东西能否迁移到新题(第一阶段判定"不明确",既没证成也没证伪)
- 修好机制后进化能否稳定且可迁移(机制还没修)
- Builder 初稿作为进化起点是否比通用起点更好(没测过 evolvability)
- 不同题型是否真的需要不同流程(Q2 需在公平条件下重做)

### 1.1 第一阶段终局(2026-07-28)及其对第二阶段的影响

**结果(冻结判定,数据在 RESULTS.md 第五轮)**:

| 谱系 | 训练提升(正式 3 遍) | 越 +15 线? | 全新考试相对 v001 |
|---|---:|---|---:|
| R0(旧) | +20.8 点 | 是 | +2.8 点 |
| R1 | +8.3 点 | 否 | (低优先级,预算前熔断未考) |
| R2 | +16.7 点 | 是 | 0 点 |

- **训练可复现成立**(2/3):三条独立谱系里两条把训练成绩练过了预设线,
  "进化能提高训练分"不再是单次运气;
- **迁移不明确**:合格两条在从未见过的 12 道新题上平均只比没练过的 v001 高
  1.39 点,置信区间跨 0,既够不到 +5 的"真学会了"线,也够不到 −5 的
  "背题背坏了"线;
- **老毛病重现**:R0 的增益全部来自一道题(241)多过了一次;R2 是一道题
  (241)多过、另一道(502)反而丢了,净 0——还是"换着错",不是稳定累积;
  且两者考试花的 tokens 是 v001 的 4.1/6.4 倍;
- **quick 单遍噪声再次实锤**:R2 quick 100% → 正式 91.7%,R1 quick 75% →
  正式 83.3%,单遍反馈上下浮动近 10 点。

**对第二阶段设计的三点影响**:

1. **双轨进化的必要性从"推测"升级为"实证"**:现在的接受规则只看训练分,
   R0/R2 都被判"训练合格",但迁移均≈0——正是"背题版本畅通无阻"的形态。
   val 否决闸(§2.2)针对的就是这个通路。
2. **考试尺子必须加长**:12 道题、单题一遍 = ±8.3 点,置信区间宽达 12.5 点,
   测不出 ±5 以内的效应。第二阶段 holdout 扩到 **~24 题**(reserve 余量 +
   本轮 external 12 题可复用为候选,机械抽取),单题影响减半、区间宽度约减 30%。
3. **quick 单遍不可作为接受依据的孤证**:v001 基线在新一轮 val 上的参照分
   将用 2 遍均值定标(仅基线定标一次,不改逐版本 quick 的单遍协议),
   给 ε 容忍带一个有数据依据的取值。

---

## 2. 核心机制改造:GEPA 启发的双轨进化

### 2.1 外部研究的关键启发

最相关的工作(2026-07-28 已核实到机制细节):

- **GEPA**(Genetic-Pareto prompt optimization,ICLR 2026 Oral):用训练集驱动变异
  (reflector 只看训练失败),用验证集驱动**选择**(Pareto 前沿淘汰);验证集的成绩
  和内容永远不给 reflector 看。在小数据(<200 例)时推荐 50/50 split。**变异对象
  仅限提示词**,不含工具与控制流。
- **Gated Semantic Quality-Diversity harness evolution**(arXiv 2607.13683):
  目前最接近"GEPA 思想迁移到 harness 层"的工作。变异对象是**完整 harness**
  (prompt/知识注入/runtime 控制流/config 四类杠杆、13 个编辑面,保护 kernel 不可改);
  多次引用 GEPA,采纳其"多样性保留优于贪心爬山"的结论,但把 per-task Pareto 换成
  **按 pathology 语义分格的 archive**。关键差异:**没有 validation 层**——变异和
  选择都在 training benchmark 上,抗过拟合改用配对 2σ 显著性门 + pathology 键控
  archive,外加一个只考一次的 sealed test(+9~+15.5 pp,retention 86–147%)。
  另一重要实证:在冻结模型上,可归因增益集中于 runtime/config 编辑,**纯提示词
  编辑大多无效**——支持 MOSS 把控制流纳入变异面的选择。
- **HarnessX / AEGIS**(arXiv 2606.14249):harness 本体论最完整(8 个生命周期
  hook × 9 个行为维度),trace 驱动变异 + 确定性接受门,其 "seesaw constraint"
  (**候选不得回归任何已解决任务**)与本方案的回归锁(§3.1)独立同构。无可见的
  train/val 分离,未引用 GEPA,泛化纪律存疑(报告了 post-peak degradation)。
- **Darwin Gödel Machine**(arXiv 2505.22954):完整源码级自改进 + archive 谱系
  管理,但选择分数与搜索反馈来自同一 benchmark——正是本方案要堵的单轨通路。

**设计定位**:把 GEPA 的数据角色纪律(train 变异 / val 选择)完整迁移到
harness 源码层的工作,**截至检索日尚未出现**;本方案的双轨循环是这一组合的首次
落地。领域内对"选择侧抗过拟合"存在两条路线——数据路线(GEPA:validation 层)
与统计路线(2607.13683:train 上的显著性门)——本方案取数据路线为主、ε 容忍带
吸收统计路线的思想;回归锁与 test-once 纪律均有独立先例(seesaw、sealed test),
不是孤立发明。

### 2.2 对 MOSS 的翻译:双轨进化架构

**当前架构(单轨)**:

```
Proposer 看到 train 失败 → 生成新版本 → 只要 train 分不降就接受
```

问题:没有任何机制惩罚"在训练题上背题但在新题上变差"的版本。

**改造后架构(双轨)**:

```
Proposer 看到 train 失败 trace → 生成新版本候选
                                     ↓
                              [门禁 1] 合同/语法/smoke(不变)
                                     ↓
                              [门禁 2] train quick(不变,Proposer 可见结果)
                                     ↓
                              [门禁 3] val quick(新增——Proposer 不可见)
                                     ↓
                              [选择器] 接受/拒绝(综合 train+val)
```

**关键规则**:

1. **Proposer 永远看不到 val 的成绩、trace 或失败原因。** 它只看 train 的反馈来
   生成新版本——这和 GEPA 的 reflector 只看 train 一样。
2. **选择器**(loop.py 里的接受/拒绝逻辑)看 train **和** val 的成绩,但只看分数,
   不看 trace。选择规则:
   - **必要条件**:train 恒过题不得退步(回归保护,见 §3.1);
   - **接受条件**:train score ≥ 当前最优 **且** val score ≥ 当前最优 − ε(ε 为
     预设容忍带,抵消单次噪声);
   - 不满足接受条件的版本:记录到 archive 但标记为 `rejected`,Proposer 下轮
     仍能看到它的 train trace(但不知道它被拒的原因是 val 退步)。
3. **val 不参与停止规则。** 何时停止进化仍然只看 train 侧(达到满分或轮数上限),
   决不允许"看一眼 val 分数决定要不要再练一轮"——那等于把 val 变成第二个 train。
4. **最终评判仍然用完全独立的 holdout。** val 在进化中扮演"防背题的安全网",
   本身也可能产生微弱泄漏(选择偏差);真正定胜负的 holdout 全程零接触,在进化
   完成后才运行一次。

**这与原约束"进化只能看 train"的关系**:原约束的本意是防止 Proposer 利用 val 信息
来针对性背题。双轨架构严格保持这一点——Proposer 仍然**只看 train**;val 只被
loop 层的选择器用于淘汰,Proposer 对此完全不知情。这是一个精确的区分:
**生成用 train,筛选用 val,评判用 holdout**——三层数据各司其职。

### 2.3 数据 split 设计

当前可用题目(以 tddgen_hidden 为例):

| 池 | 数量 | 当前用途 |
|---|---:|---|
| old train | 8 | 进化反馈 |
| old val | 10 | 正式评测 |
| q1_external canary | 4 | 难度校准 |
| q1_external val | 12 | 外部泛化评测 |
| reserve | 34 | 未使用 |

改造后(50/50 原则,参照 GEPA 在小数据量下的推荐):

| 池 | 数量 | 来源 | 用途 |
|---|---:|---|---|
| **train** | ~16 | old train 8 + reserve 抽 8 | Proposer 唯一反馈源 |
| **val**(选择门禁) | ~16 | old val 10 + reserve 抽 6 | 选择器可见分数;Proposer 不可见 |
| **holdout**(最终评判) | **~24**(§1.1 影响 2) | reserve 余 ~20 + q1_external 16 中机械抽取 | 全程零接触;进化完成后运行一次 |

- 分配按 `sha256(task_id)` 机械执行,在任何第二阶段模型调用前冻结;
- 每个池互不相交;
- canary 4 道只做难度校准,不进任何池的正式分数。

### 2.4 为什么不直接把 val 的 trace 也喂给 Proposer

用户提出过"在 val 上也一同做进化"的思路,即让 Proposer 同时看到 train 和 val 的
失败原因。这个做法**理论上最大化了 Proposer 的信息量**,但有两个已观察到的风险:

1. **R0 的教训**:当 Proposer 能看到所有反馈时,它自然会把**所有**失败的局部特征
   写进 Harness——R1/v004 已经在 8 道 train 上做到了点名 120/458/1057。如果再加
   16 道 val 的 trace,背题面翻倍,而且 val 不再能检测过拟合。
2. **勘误与修正论证(2026-07-28,经用户质疑核实)**:本节旧版曾称"GEPA 的实证
   结论是 reflector 只看 train 子集时 held-out 泛化更好"——**经查证 GEPA 论文与
   官方 FAQ 均无此消融实验**,分离只是其结构性设计选择("Without a separate
   valset, GEPA will tend to overfit the training data"是断言而非实证),特此勘误。
   用户的反驳也成立:val trace 进 proposer **不会污染 holdout 测量**——holdout
   全程未见,终验仍然无偏。正确的论证在循环动力学而不在测量:
   - 让 proposer 看 val trace,等价于把 validation benchmark 并入 training
     benchmark——系统退回**单轨循环**,selector 失去独立于变异数据的否决信号;
   - 记题式修改在"变异所依据的同一题池"上必然涨分,单轨 selector 会**奖励**
     而不是**过滤**这类修改;过拟合只能在终点被 holdout 量出,而那时预算已花完。
     第一阶段单轨终局(R0/R2 train 合格、test≈0)就是这个形态的本地实证;
   - 如实记录反向论点:并入 val 使反馈池从 16 题变 32 题,单纯从数据量角度
     **有利于**泛化。"更大反馈池 vs 独立过滤器"孰优是开放的实证问题;本方案
     基于第一阶段证据选过滤器,并以 train 8→16 扩容补偿反馈池规模。若第二阶段
     出现"validation 否决率≈0(过滤器闲置)",预注册的替代方案是把 val 并回
     反馈池、改用 2σ 显著性门(统计路线,见 §2.1)。

因此我们的设计选择是:**把 val 信息限制在"分数"层面用于筛选,不暴露"怎么错的"
给 Proposer。** 如果未来发现这个选择过于保守(比如 Proposer 在 train 上已经饱和
但 val 仍有明确可修的系统性失败),可以考虑受控地暴露 val 的**聚合统计**(如
"val 上数值计算类题目通过率低于字符串类"),但永不暴露单题 trace。这是一个可以
在后续轮次升级的旋钮,不是现在就需要决定的。

**val 筛选本身会不会被"运气"骗过?(选择过拟合的三道防线)**

只用 val 做选择并不能做到零泄漏——每次接受/拒绝决策都向谱系泄漏约 1 比特的
val 信息,且固定的小 val 集存在"某种 harness 风格恰好对上这批题"的系统性拟合
风险。设计上的三道防线:

1. **val 是否决权,不是目标函数**:接受的驱动力必须来自 train 提升,val 只能
   拦截、不能当选。一个版本不可能*因为* val 运气好而胜出,只可能*侥幸漏网*——
   而漏网的背题版本会在终点被 holdout 如实量出(`overfit_gap`)。
2. **ε 容忍带对齐单题噪声**:单题翻转不该决定生死;ε 取值以 v001 基线定标的
   波动为依据(§1.1 影响 3)。
3. **holdout 兜底**:val 在进化中允许被轻度污染,最终结论只认全程零接触的
   holdout。三层数据各堵一个洞:val 防变异侧背题,holdout 防选择侧背题。

进化论式的直觉("每代都要过 val 闸,运气不可遗传,方法才可遗传")对**采样噪声**
成立,但对**固定题集的口味偏好**不成立——后者每代都在,只有 holdout 能检出。
若第二阶段观察到"val 涨、holdout 不涨"的漂移,升级旋钮是按题轮换 val 子集
(GEPA minibatch 式)或 Pareto 按题保留,预注册为后续选项、本轮不启用。

---

## 3. 进化机制三项修复(第二阶段)

### 3.1 修复一:回归保护(最高优先级)

**问题**:R1 矩阵显示 4/8 恒过题在各版本间随机丢失又恢复,Proposer 没有"别把学会的
东西忘了"的约束。

**方案**:

- 将恒过题(连续 ≥3 个版本通过的题)标记为"锁定通过";
- 新版本如果在任一锁定题上失败,**直接拒绝**(不进 val 评估、不消耗预算);
- Proposer 可以看到哪些题被锁定(以便避免修改影响它们的策略部分),但不知道
  拒绝机制的存在——它只会发现"又一次生成了相同版本号"(archive 里同一版本号
  对应多次尝试,只有通过的那次留下来)。
- 实现位置:`loop.py` 的 `accept_or_reject` 函数,新增 `locked_tasks` 集合。

**GEPA 对标**:GEPA 的 Pareto 前沿本质上也是回归保护——一个 prompt 只要在某一个
验证样例上是最好的就会被保留,防止新一代把所有特长都丢掉。

### 3.2 修复二:反馈粒度加密(高优先级)

**问题**:8 道 train 中只有 4 道有区分度,单题 = 12.5 个百分点,一题的随机翻转就能
把进化引向完全不同的方向。

**方案**:

- train 从 8 题扩到 ~16 题(见 §2.3),单题权重从 12.5% 降到 6.25%;
- quick 评估仍为单遍(不改为 2 遍——在双轨架构下,val 的筛选作用已大幅降低
  单次 train 噪声对接受决策的影响);
- 扩容后的 train 在首次模型调用前冻结。

### 3.3 修复三:自测执行通道(中优先级)

**问题**:v005–v007 的 Harness 要求模型写 `__main__` assertions 自验,但系统只运行
`test_solution.py`,assertions 从未执行。模型花 303k tokens 在"写测试→嘴上说通过→
实际没跑"的仪式上。

**方案**:

- 新增受沙箱约束的 `run_snippet` 工具:模型可以提交一段 Python 代码片段,
  系统在隔离环境中执行并返回 stdout/stderr(超时 10s,无网络,无文件写入);
- Harness 可以在流程中使用此工具来验证中间假设;
- 工具合同:运行结果只返回给当前步骤,不修改 `solution.py` 或 `test_solution.py`;
- 实现位置:`_eval_one.py` 的工具注册,新增 `run_snippet` handler。

**砍项优先级**:回归保护 > 反馈加密 > 自测通道。前两项直击已证实的进化不稳定;
第三项治的是成本污染,不修也不影响正确性,只是浪费钱。

---

## 4. 三阶段执行计划

### 第一阶段:完成本轮(**已完成,2026-07-28**)

**目标**:关闭 Q1"进化是否可重复"。**已按冻结协议全部执行完毕**,实际走向:

| 步骤 | 计划 | 实际 |
|---|---|---|
| 1 | R2 恢复进化至多 v007 | R2 在 v002 quick 8/8 后按冻结规则提前停止,formal train 91.7%(+16.7,合格) |
| 2 | 正式矩阵按决策价值排序 | 前 5 格完成;R1-external 在 1.5× 预留门前熔断未跑(预注册结果,非删格) |
| 3 | 机械分析 | `decision_complete=true`,判定 **inconclusive**;RESULTS.md 第五轮已落盘 |

**实际消耗**:全轮累计 23.18M / 24M,余 0.82M。判定分支落在预注册的第三支:
训练前提 2/3 成立,external 效应 +1.39 点、CI 跨 0 → **"训练专化可复现,
迁移效果未识别"**。结果细节与对第二阶段的影响见 §1.1。

### 第二阶段:修机制 + 起点对比(**已被三层资格实验替代,不执行**)

> 本节保留为设计演进记录。它同时改变 selector 与 seed，无法在 optimizer 尚未证明
> test-benchmark transfer 时解释 Builder 差异。当前唯一后续协议见
> `2026-07-28-three-tier-benchmark-qualification.md`。

**目标**:一笔钱同时回答两个问题——
- Q1':"修好机制后,进化是否可重复且可迁移?"
- Q3':"Builder 初稿作为起点,是否让进化更快更高?"

**设计**:

4 条独立谱系,共用修复后的进化机制(§3)和同一冻结 train/val/holdout:

| 谱系 | 起点(seed) | 目的 |
|---|---|---|
| A1 | 通用 v001(逐字) | Q1' 可重复性证据 #1 |
| A2 | 通用 v001(逐字) | Q1' 可重复性证据 #2 |
| B1 | Builder 初稿(取已通过门禁的第一版,不挑) | Q3' 起点价值证据 #1 |
| B2 | Builder 初稿(同上,独立进化) | Q3' 起点价值证据 #2 |

**进化流程(每条谱系相同)**:

```
v001/builder0 → [Proposer 看 train trace] → 候选版本
    → [门禁 1] 合同/语法/smoke
    → [门禁 2] 锁定题回归检查
    → [门禁 3] train quick (Proposer 可见)
    → [门禁 4] val quick (Proposer 不可见,仅选择器用)
    → [选择器] 接受/拒绝
    → 重复至 train 满分或轮数上限
```

**评判(进化完成后)**:

每条谱系的 final 在 holdout(~24 题,§1.1 影响 2)上跑 3 遍正式。

| 指标 | 角色 | 判定用? |
|---|---|---|
| `holdout_final − holdout_baseline` | 主指标:定胜负的唯一数据 | 是 |
| `overfit_gap = train_gain − holdout_gain` | 过拟合直接量 | 辅助解读 |
| 爬升速度(轮数、tokens) | 次指标:效率 | 仅描述 |
| 逐任务翻转率 | 次指标:稳定性 | 仅描述 |
| val quick 的筛选拒绝率 | 机制诊断:双轨是否起作用 | 仅描述 |

**Q1' 判定**:A1 和 A2 两条谱系均满足 train gain ≥ +15 **且** holdout gain 显著为正
→ "修复后进化可重复且可迁移";只满足前者 → "可重复但仍过拟合";不满足前者
→ "机制修复不够,需进一步迭代"。

**Q3' 判定**:B 组 holdout 终点均值 > A 组 holdout 终点均值(超过组内波动)
→ "好起点成立";B 组 train 涨而 holdout 不涨 → "Builder 初稿更易诱导背题"(负结论);
无显著差异 → "起点不影响进化结果"。

**防过拟合手段汇总**:

1. 三层数据分离:train(生成)、val(筛选)、holdout(评判),互不相交;
2. 回归保护:锁定题不得退步;
3. 训练扩容:8→16 题,背题难度翻倍;
4. 停止规则只依赖 train,holdout 零接触直到 final;
5. 每谱系只考一次 holdout,不做逐版本 holdout 曲线;
6. Proposer 永不见 val trace,选择器只见 val 分数。

**预算粗估**:

| 项目 | tokens |
|---|---:|
| 4 谱系进化(每条 ~16 题 train + ~16 题 val,≤7 版) | 4 × 8M = 32M |
| 4 谱系 holdout 正式(每条 ~24 题 × 3 遍) | 4 × 5M = 20M |
| baseline holdout(v001 × ~24 题 × 3 遍 + val 定标 2 遍) | 5M |
| 门禁、canary、隔离余量 | 3M |
| **合计** | **~60M(悲观)** |

悲观口径假设进化复杂度与 R1 相当且 holdout 单价按 R2 external 实测(~6 倍 v001)。
两个重要的下调因素:回归保护会拦掉无效版本(R1 有 3/6 版是无效交换),双轨拒绝
会缩短谱系;乐观口径 ~35M。若预算只批 2 条谱系(A1+B1),约减 40%。
正式方案需细化后给出精确预算与熔断线。

### 第三阶段:Q2' 同题双呈现配对(更后,依赖第二阶段)

**目标**:回答"不同题型是否真的需要不同流程",唯一变量必须是题型。

**前置条件**:第二阶段证明进化机制可靠,两侧谱系均满足训练前提。

**设计**:

- 同一底层函数生成两种呈现:stub 变体(从头实现)与 AST 变异 bug 变体(修复缺陷);
- 只保留两种变体都通过质量门禁的题(保证底层难度天然同分布);
- 两条谱系各看本方呈现的 train 进化;
- 考试时每道题的两种呈现都考、两个 harness 都考;
- 主指标:task-paired difference-in-differences(交互项)。

**预算**:届时另批,依赖第二阶段结论。

---

## 5. 进化机制改造的代码变更清单

仅列出最小必要改动(第二阶段实现时的实施指引):

| 文件 | 变更 | 类型 |
|---|---|---|
| `loop.py` | 新增 `locked_tasks` 集合 + 接受前检查锁定题回归 | 修改 |
| `loop.py` | 新增 val quick 评估步骤(在 train quick 之后、accept 之前) | 修改 |
| `loop.py` | 选择器逻辑:train ≥ best **且** val ≥ best − ε | 修改 |
| `proposer.py` | 确保 val 成绩和 trace 不进入 prompt(只传 train 侧 trace) | 验证(应已如此) |
| `_eval_one.py` | 新增 `run_snippet` 工具 handler(沙箱化) | 修改 |
| `eval.py` | 支持对 val 池评估但不写入 proposer-visible 的结果路径 | 修改 |
| `archive.jsonl` | 新增 `val_score` 和 `rejected_reason` 字段 | 格式扩展 |
| `config.py` | 新增 `EVOLUTION_VAL_TOLERANCE`(ε 参数) | 新增 |

不改动:`eval.py` 的防作弊/哈希校验、`builder.py`、`harness_source.py`、判分入口。

---

## 6. 风险与回退

| 风险 | 后果 | 回退 |
|---|---|---|
| 双轨选择导致进化速度极慢(大量版本被 val 拒绝) | 轮数上限内训练分不升 | 放宽 ε 或回退到单轨(记录"双轨过于保守"作为结论) |
| 训练扩容后恒过题占比仍高 | 区分度不足 | 用 canary 预先筛选高区分度题,替换恒过题 |
| 预算超限 | 谱系不完整 | 按决策价值排序谱系:A1 > B1 > A2 > B2(前两条即可得初步 Q1'/Q3') |
| Builder 初稿在新 train 上门禁不过 | B 组无法启动 | 允许 builder 重新生成一次(仍只看 family card,不看题目) |
| `run_snippet` 沙箱逃逸 | 安全风险 | 用 `subprocess` + `seccomp` 或 Docker;首轮不启用此工具也可 |
| R2 本轮失败(进化不可重复) | 第二阶段仍然值得做 | 第二阶段本身就是修机制后的重试,R2 失败反而加速进入第二阶段 |

---

## 7. 与外部工作的对照表

| MOSS 组件 | 对应外部概念 | 参考 |
|---|---|---|
| Proposer(Sonnet 诊断失败出新版) | GEPA reflector / DGM self-edit | GEPA: train feedback → mutation |
| loop.py 选择器(新增) | GEPA Pareto 前沿选择 | 用 val 分数筛选,不暴露 val trace |
| 回归保护(锁定恒过题) | GEPA 多样性保留 / 精英保留 | 确保旧能力不退化 |
| train/val/holdout 三层分离 | GEPA train/val + 独立 test | 生成/筛选/评判各用不同数据 |
| Builder 初稿 | HarnessX 可组合模块初始化 | 结构化起点 vs 空白起点 |
| `run_snippet` 工具 | DGM 的自我测试能力 | 让 agent 能验证中间假设 |
| archive.jsonl 谱系管理 | DGM 变体 archive | 完整进化历史,含被拒版本 |

---

## 8. 历史决策点（已由三层资格方案取代）

> 下列第 2–5 项不再是当前决策菜单，仅保留设计演进记录。当前待批准项、100M
> 保守授权与两条通用 seed gate 见
> `2026-07-28-three-tier-benchmark-qualification.md`。

### 已决定/已完成

1. ~~恢复第一阶段~~ — **已完成**(2026-07-28,判定 `inconclusive`,见 §1.1);
   24M 预算余 0.82M,不足以支撑任何新正式格,第二阶段必须新授权。

### 原第二阶段启动前决定（已作废）

2. **双轨进化(§2)**:是否采纳"val 用于选择、不给 Proposer 看"的设计?
   第一阶段终局强化了它的必要性(训练合格但迁移≈0,正是单轨的盲区)。

3. **三项修复的取舍**(§3):全要 / 砍 `run_snippet` / 只要回归保护?
   推荐全要,但如果预算紧张,`run_snippet` 可以后补。

4. **第二阶段预算授权**:悲观 ~60M、乐观 ~35M(4 谱系 + 24 题 holdout);
   若只批 2 谱系约减 40%。需要你给一个上限数字,正式方案按它细化熔断线。

5. **谱系数量**:推荐 4 条(2×v001 + 2×builder);如果预算只够 2 条,
   优先 1×v001 + 1×builder(最小可回答 Q1'+Q3' 的设计)。

### 可以以后决定

6. **Q2' 第三阶段**:依赖第二阶段结论,现在只需知道你认可方向(同题双呈现)。

---

## 附录 A0:旧方案术语对照（新定义以三层资格方案 §1 为准）

| MOSS 术语 | 第一阶段实际对应 | 第二阶段对应 | 角色 |
|---|---|---|---|
| training benchmark | `tddgen_hidden/train` 8 题 | 扩至 ~16 题 | proposer 唯一反馈源;selector 的提升条件 |
| validation benchmark | **不存在(单轨循环的架构空缺)** | 新增 ~16 题 | selector 的否决闸;仅标量分数,trace 永不进 proposer |
| test benchmark | `q1_external/val` 12 题(仓库命名"val"易混淆) | 扩至 ~24 题 | 终验唯一判定数据;每 lineage 冻结 final 后 3 遍,零反馈 |
| lineage | R0/R1/R2 | A1/A2/B1/B2 | 从固定 seed 独立进化的 harness 谱系 |
| seed | v001(逐字) | v001 或 builder0 | 谱系起点 harness |
| selector | loop.py 接受逻辑(旧:只看 train) | 双轨:train 提升 ∧ val ≥ best − ε | 版本存留决策 |

**三层基准的过拟合归因链**:候选 train↑ 但被 val 否决 → proposer 过拟合到
training benchmark(循环内拦截);final 的 val↑ 而 test≈0(`val_gain − test_gain`)
→ 谱系经选择压力过拟合到 validation benchmark;test 显著↑ → 只支持迁移到新的
benchmark sample，不能单独声称 Task-level transfer。
第一阶段没有 validation 层,第一种过拟合无阻进入 final——R0/R2"train 合格、
test 零增益"即该通路的实证。

## 附录 A:参考文献

- GEPA (Genetic-Pareto prompt optimization): [arXiv:2507.19457](https://arxiv.org/abs/2507.19457), ICLR 2026 Oral
- Self-Evolving Agent Harnesses via Gated Semantic Quality-Diversity: [arXiv:2607.13683](https://arxiv.org/abs/2607.13683) (2026)
- HarnessX / AEGIS: [arXiv:2606.14249](https://arxiv.org/abs/2606.14249) (2026)
- Darwin Gödel Machine: [arXiv:2505.22954](https://arxiv.org/abs/2505.22954) (Zhang, Hu, Lu, Lange, Clune 2025)
- MOSS (Self-Evolution through Source-Level Rewriting): [arXiv:2605.22794](https://arxiv.org/abs/2605.22794) (2026)
- DSPy/MIPRO: [dspy.ai](https://dspy.ai)
- GEPA FAQ (split ratios): [gepa-ai.github.io/gepa/guides/faq](https://gepa-ai.github.io/gepa/guides/faq/)

## 附录 B:本文档与已有文档的关系

| 文档 | 状态 | 与本文档的关系 |
|---|---|---|
| `2026-07-27-hidden-final-verification-round.md` | 冻结 | 本轮协议本体,本文不修改 |
| `2026-07-28-q1-confirmation-resumption.md` | 已批准执行 | 第一阶段恢复的具体操作指引 |
| `2026-07-28-round3-design-directions.md` | 被本文整合 | 三问分析 + 指标设计已合并至本文 §1–§4 |
| `experiment-status-checkpoint.md` | 数据来源 | 本文所有数据引用均可追溯至此 |
| `2026-07-28-three-tier-benchmark-qualification.md` | **待批准** | 先行的 optimizer 迁移资格协议；替代本文原第二阶段 |
| 本文档 | **历史方向文档** | 第一阶段终局与设计演进记录；原第二阶段不再执行 |
