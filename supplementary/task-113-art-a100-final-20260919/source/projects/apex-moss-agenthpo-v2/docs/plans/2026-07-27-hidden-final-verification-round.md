# 第二轮:隐藏终验协议(Hidden Final Verification)—— 决策就绪设计

> 状态：历史冻结协议，已执行并终局（2026-07-27）；V1 manifest + 本文已于提交 `ca584f0` 冻结，V1 canary
> 4/5 落带后成为正式协议。正式池过滤后 38 题，已按预注册下限缩为每族 8/10；
> bugfix 变异 12/19 合格，已触发 `specgen_hidden` V0 回退；正式池冻结提交 `c4525ec`。
> 前序:`2026-07-27-task-conditioned-harness-builder-pilot.md`(判定线与三问框架继续沿用)、
> `PROGRESS.md` 两条 2026-07-27 记录、`RESULTS.md`(旧四格 + BigCodeBench-Hard canary 全部饱和)。

---

## 0. 一段话说清楚本轮改什么

上一轮的诊断很明确:**不是题不够难,而是信息给多了**——Harness 能读完整测试、反复运行、
按失败迭代,把 BigCodeBench-Hard 的一次生成难题降级成了"测试全可见的交互修复题",
haiku-4-5 因此 5/5。本轮只做一个最小干预:**把大部分测试藏起来,只在终验时使用**。
任务文件布局、工具、计分入口、模型、判定线全部不动;先用同一批 5 道已冻结的题做
受控 canary(同题、只变信息边界),落进 50–80% 带内再扩正式题库。

---

## 1. 任务形态:推荐与拒绝理由(设计问题 1)

**推荐:方案 A —— 公开规格 + 少量可见测试 + 隐藏终验,单文件形态不变。**

每题仍是一个目录:`solution.py`(stub,含签名 + docstring + 示例)+ `test_solution.py`
(**可见子集**,官方套件的前 k 个测试方法)+ `_hidden/test_hidden.py`(**完整官方套件**,
harness 全程不可见,仅评分器终验使用)。judge 语义:隐藏套件全绿才算过。

**拒绝方案 B(多文件真实仓库级 bug 修复)**,理由:
1. 它同时改变文件布局、可编辑白名单、快照/恢复逻辑、工具语义和 family card 五个变量,
   而已确认的病因只有"测试全可见"一个。一轮引入两个自变量,canary 结果无法归因。
2. 防作弊面骤增(多文件哈希、conftest 注入、import 遮蔽),`_eval_one.py` 需要重写而非扩展,
   与"eval.py 唯一计分入口 + 最小改动"的约束冲突。
3. 真实仓库题(SWE-bench/BugsInPy)依赖环境重、确定性差,违反"本地确定性运行"约束。

**拒绝方案 C(A+B 结合)**:继承 B 的全部问题。

**保留的升级路径**:若方案 A 在 V0 档(零可见测试,见 §3)canary 仍 5/5,说明单函数形态对
haiku-4-5 彻底饱和,那时仓库级才是必要的下一步——到时回方案模式重新设计,本文附录 B 已
预留多文件防作弊合同草案作为起点。

**为什么 A 能恢复区分度**:BigCodeBench-Hard 的官方难度本来就来自"只看规格一次写对边界"。
隐藏终验恢复了这一点,同时保留了 harness 的策略空间——自写探针测试、边界枚举、提交前
自审、利用少量可见测试校准理解——这正是 Q1/Q2/Q3 需要的"流程可以不同且优劣可分"的空间。
参考公开数据:BigCodeBench-Hard instruct 一次生成的模型通过率普遍在 20–40% 区间,而本仓库
实测"全可见+迭代"是 100%,两者之间有足够宽的带子容纳 50–80% 目标。

---

## 2. Canary 选择(设计问题 2)

**冻结选择:复用上一轮已冻结的同一批 5 道题**(`benchmarks/tddgen_hard/canary/_manifest.json`,
bigcode/bigcodebench-hard **v0.1.4**):

| task_id | 上轮全可见结果 | steps | executor tokens | libs |
|---|---|---|---|---|
| BigCodeBench/273 | PASS | 6 | 24,730 | http, cgi, json |
| BigCodeBench/274 | PASS | 8 | 43,466 | http, cgi, smtplib, json, email |
| BigCodeBench/854 | PASS | 4 | 9,881 | math, itertools, functools |
| BigCodeBench/928 | PASS | 4 | 8,653 | collections, itertools, string |
| BigCodeBench/990 | PASS | 6 | 24,536 | binascii, base64, urllib, codecs |

理由(同时回答"如何避免看结果挑题"):
1. **受控对比**:同一批题在"全可见"协议下已知 5/5。新协议下的任何下降都只能归因于
   信息边界,而不是换题带来的难度漂移。这是能直接检验 §0 诊断的最干净实验。
2. **零选题自由度**:题目在看到任何新协议结果之前已经冻结(上一轮就冻结了),
   不存在事后挑题空间。
3. **已验证**:stub-fail/oracle-pass 双向校验通过,依赖全部在当前环境可用,官方测试
   无持久外部副作用。
4. **无污染**:执行模型无状态、无跨会话记忆,重复使用同一题目不产生记忆性泄漏;
   会"记住"这些题的只有我们的 archive,而 archive 不喂给执行模型。
5. 这 5 题已被 canary 消耗,**永不进入正式 train/val**(见 §8)。

**难度依据说明**:数据集的 `score` 字段经核实是"任务与真实用户问题的相似度"(0.7–0.87),
**不是解题率,不能当难度依据**;难度依据是上表的实测(全可见下 haiku 需要 4–8 步、
9k–43k tokens 才能做对,说明有实际推理量)加上 BigCodeBench-Hard 官方筛选(长 prompt、
多库调用、低模型解出率)。

---

## 3. 校准机制:预注册难度阶梯(设计问题 3)

目标:v001 在 canary 上落入 50–80%,即 5 题 1 遍 **通过 3 或 4 题**。为避免"看结果调协议"
的无限自由度,只保留一个预注册旋钮——**可见测试数量 k**,且移动规则现在写死:

| 档位 | test_solution.py 内容 | 隐藏套件 |
|---|---|---|
| V2 | 官方套件源码顺序前 **2** 个 `test_` 方法(保留 setUp/tearDown/辅助函数/模块级代码) | 完整官方套件 |
| V1 | 前 **1** 个 `test_` 方法 | 同上 |
| V0 | **0** 个行为测试;只含一个冒烟测试(`import solution` 成功且 `task_func` 可调用) | 同上 |

**阶梯规则(预注册,首次模型运行前 commit 冻结)**:
1. 从 **V1** 开跑(1 遍,canary 协议)。
2. 结果 3–4/5 → 该档冻结为正式协议,进入 §8 扩题。
3. 结果 5/5 → 降一档(更难)重跑;结果 ≤2/5 → 升一档(更易)重跑。
4. 第二次运行落带 → 冻结该档;仍不落带 → 沿同方向再移一档(如果还有档)重跑一次。
5. **最多 3 次运行**。三次后仍不落带,或出现"V1=5/5 且 V0≤2/5"这类相邻档跨带的情形,
   判定"该题源在此模型上阶梯粒度不足",**停止、不扩题、回方案模式**;不允许现场发明
   V0.5 或换题。
6. 基础设施无效运行(§10 的 harness_error/env_error/tamper)不计入阶梯步数:修复后
   重跑**同一档**。
7. canary 全部为 1 遍,结果只用于校准判定,**不进入任何正式结论**。

---

## 4. 可见/隐藏信息边界(设计问题 4)

### 做题阶段可见(work_dir 内)
- `solution.py` stub:imports + 签名 + docstring(含官方 instruct_prompt 的规格与示例)。
- `test_solution.py`:当前档位的可见测试。
- executor 的自有产出(它写入 work_dir 的 solution.py 修改;工具合同禁止写其他文件)。

### 仅终验可用(harness/executor/proposer/builder 全程不可见)
- `_hidden/test_hidden.py`:完整官方套件。
- 官方 canonical_solution:**只在导入脚本的 oracle 校验中使用,从不落盘到 benchmarks/**
  (维持现状)。

### 三层防读取(防作弊合同增量)
1. **布局隔离**:`_hidden/` 是任务目录的子目录;`_eval_one.py` 复制任务到 work_dir 时只复制
   文件不复制目录(现有行为),因此隐藏套件从不出现在 work_dir。
2. **运行时路径护栏**(新增):`_eval_one.py` 把传给 harness 的 `tool_dispatch` 包一层 guard:
   `read_file`/`write_file` 的 `path` 与 `run_tests` 的 `test_path` 经 `resolve()` 后必须位于
   work_dir 之内,否则返回错误字符串(不抛异常),并累加 `contract_violations` 计数。
   `tools.py` 本体不动(工具实现仍冻结);护栏属于评测协议层,随本方案冻结。
3. **静态沙箱合同**(新增):`harness_source.py` 增加 `validate_sandbox_contract(code)`:
   import 白名单恰为 `{anthropic, json, os}`(与 proposer CONSTRAINTS 现有文字一致;
   已核实全部现存 harness 只用这三个);`os` 只允许 `os.environ` / `os.getenv` /
   纯路径拼接 `os.path.join`(P0 红测发现两份现存 builder0 使用它,冻结前收窄为精确例外);
   禁止调用 `open/exec/eval/compile/__import__/getattr/setattr/globals/vars`。
   `eval.py` 在 `check_model_lock` 之后对**所有**参赛 harness(含手写 v001)统一执行,
   不过则拒绝计分——生成物和对照组吃同一份合同。

### 时序与泄漏隔离
- 隐藏套件只在 `harness.run()` 返回、完整性校验与恢复完成**之后**,在**全新临时目录**
  (最终 solution.py + pristine 可见测试 + test_hidden.py)中由评分器运行;harness 留下的任何
  垃圾(pycache、注入文件——后者本就判 tamper)不影响终验。
- **隐藏结果只记计数,不记文本**:result JSON 的 hidden 字段为
  `{"passed": bool, "n_passed": int, "n_failed": int, "errored": bool}`;隐藏套件的 pytest 输出、
  测试名、assertion 消息一律不落盘。`test_output` 字段只含**可见**套件的输出。这样
  proposer 读 train traces(现有 `gather_history` 逻辑,不用改)在结构上就拿不到隐藏信息,
  满足"隐藏终验不得反馈给 proposer/Builder/Harness"——即使对 train 题也成立。
- 执行模型在对话里尝试越界读取会被护栏拦下并计数;计数>0 的 run 标记复核,不自动判
  tamper(模型好奇不等于 harness 作弊,且它拿不到任何内容);harness **代码本身**越界
  (绕过工具直接 open)已被静态合同挡在运行前。
- 残余风险坦白:harness 与评分器同进程,纯 Python 无法完美沙箱。三层合同针对的是
  "非对抗但会 reward-hacking 的生成代码";配合 trace 审计与 tamper 判定,残余风险可接受。
  若未来发现绕过,按 PROGRESS 惯例记为协议漏洞、隔离结果、修合同重跑。

---

## 5. 多文件写入(设计问题 5)

**本轮不开放**。可编辑文件仍然只有 `solution.py`,现有"恢复 + 哈希校验 + 注入 .py 判 tamper"
合同原样生效。理由:多文件不是恢复区分度的必要条件(§1),而它把防作弊面从 1 个文件扩大到
n 个文件 + import 图。附录 B 给出将来开放时的合同草案(白名单 manifest、逐文件快照、
禁止新建模块),仅作为下一轮设计的起点,本轮不实现。

---

## 6. 科学可比性(设计问题 6)

全部继承、逐条冻结:
- 执行模型:`eval.py` 的 `MODEL = "claude-haiku-4-5"` 锁不动。
- 路线:TokenRouter(`.env.local` → `config.py`)不动;成本来源不变。
- 重复:正式 3 遍取均值 ± pstdev;canary 1 遍且不进正式结论。
- 对照三臂在**新题库**上重赛:通用 v001(原文件,不改一字)、进化专用 harness
  (loop.py 在新 train 上从 v001 起进化)、builder0(读新 family card 零样本生成)。
- 判定线沿用 pilot 方案第 7 节的**差值**线并在新题库上重述:改进前提 = 专精−基准 train
  ≥ +15 点且大于波动;Q1 val ≥ +5 通法 / ≤ −5 应试;Q2 主客场差 ≥ +10;Q3 builder −
  基准 val 两族不降且至少一族 ≥ +10。首次正式运行前随本方案 commit 冻结。
- **旧题库 100% 只作"旧题饱和"参照行保留在 RESULTS.md**;新旧题库分数绝对值不可比,
  一切结论只看新题库内部的三臂差值。
- 新增协议项(路径护栏、静态沙箱合同、隐藏计数字段)对三臂**同时同样**生效,不构成
  臂间差异。

---

## 7. Canary 预注册表(设计问题 7)

| 项 | 冻结值 |
|---|---|
| 题目 | BigCodeBench/273, 274, 854, 928, 990(v0.1.4;§2 表) |
| harness | `harnesses/tddgen/v001/harness.py`,一字不改 |
| 档位与移动 | §3 阶梯:V1 起步,最多 3 次运行 |
| 通过带 | 单次运行通过 3–4/5(=50–80% 目标带) |
| 重复 | 1 遍;不进正式结论 |
| 单题硬超时 | 300s(沿用 `eval.py TASK_TIMEOUT`;上轮实测 35–48s/题,余量充足) |
| 可见套件 pytest 超时 | 60s(沿用 `tools.run_tests`,冻结) |
| 隐藏套件评分超时 | 120s(评分侧,不占 harness 步数) |
| 成本上限 | 每次阶梯运行 ≤ 400k executor tokens;canary 总计 ≤ 1.2M tokens(≈数美元)。超限即停,回方案模式 |
| 停止条件 | 落带冻结;3 次不落带停止;相邻档跨带停止;tamper>0 停止修复;成本超限停止 |
| 失败分类 | §10 规则;harness_error/env_error/tamper 不计阶梯步、不计能力分 |
| 运行前置 | 全部回归测试绿;import 脚本 stub/oracle 离线双验通过;manifest+本表 commit 冻结 |

超时归类细则(预注册):单题 300s 硬超时默认计 **capability 失败**(预算内做不完也是能力);
仅当 trace/日志显示网关 5xx、限速或断连时改判 env_error 并重跑该档。

---

## 8. Canary 达标后:正式题库组成(设计问题 8)

### 8.1 正式池与机械选题算法(冻结后逐字执行)

1. 题源:bigcode/bigcodebench-hard **v0.1.4** 全部 148 题,排除 5 道 canary → 候选 143。
2. 依赖过滤:`libs ⊆ ALLOWED_LIBS`。`ALLOWED_LIBS` = 冻结时刻 `.venv` 已装包 + Python 标准库,
   **减去**副作用黑名单 `{subprocess, socket, ftplib, smtplib, telnetlib, requests, flask,
   django, selenium, tkinter, turtle, multiprocessing, os(仅当任务用于文件系统重副作用——
   机械化为:libs 含 os 且官方测试写 tmp 之外路径的,由导入脚本的 oracle 校验直接拒绝)}`。
   若需要扩容,先离线安装 pinned 版本的 `numpy/pandas`(本地确定性,允许),**再**冻结
   ALLOWED_LIBS,之后不得再改。
3. 质量过滤(全离线、逐题机械执行,不看模型表现):stub 必须挂隐藏套件;oracle 必须过
   隐藏套件;可见子集(冻结档位 k)必须是隐藏套件的子集;测试运行两次结果一致(排除
   flaky)。不合格题**记录原因后剔除**,不得人工替换。
4. 排序与分割:对合格池按 `sha256(task_id)` 十六进制升序排序;交替分配:
   奇数位 → 家族 A,偶数位 → 家族 B;族内再按同序取前 10 题为 train、随后 12 题为 val,
   多余入冻结备用池(只用于题目被判 env 不合格时的**顺位递补**,递补顺序也已被排序定死)。
5. 以上算法连同 ALLOWED_LIBS、排序结果哈希写入 `_manifest.json` 并 commit,**先冻结后跑模型**。

### 8.2 两个任务族(Q2 需要两族)

- **家族 A:`tddgen_hidden`** —— 构造式:stub + 少量可见测试 + 隐藏终验(§1 形态,冻结档位)。
- **家族 B:`bugfix_hidden`** —— 审计式:solution.py 是**完整但含缺陷的实现**,由冻结的 AST
  变异算子(预注册算子表:边界比较符交换、常量 off-by-one、条件分支删除、默认值替换、
  聚合函数替换;固定种子、固定算子顺序)注入 canonical_solution;**接受条件:可见测试全过
  且隐藏套件失败**,取顺序第一个合格变异体。任务是从规格出发审计出边界缺陷——可见测试
  给不出失败信号,与家族 A 的最优工作流有真实差异,支撑 Q2。
- **家族 B 预注册回退**:若变异管线在族 B 题池上产不出 ≥ 22 道合格题(train10+val12),
  族 B 降级为 `specgen_hidden`(V0 档:零可见行为测试、纯规格构造)——同一题池、零新工具,
  与族 A 的差异退化为"信息形态差异",Q2 结论强度相应降级并在 RESULTS 中如实标注。
- 同源泄漏控制:canary ∩ A ∩ B 两两不相交(按 task_id);train/val 不相交由 §8.1 分割保证;
  BigCodeBench 题目为独立单函数,不存在仓库级同源;族 B 变异体源自与族 A 不相交的题目,
  不构成跨族泄漏。

### 8.3 三问映射

- Q1:族 A 上 v001 → 6 轮进化(loop.py,只见 train)→ train/val 前后对比,3 遍。
- Q2:族 A、族 B 各自的专精版互换考对方 val + v001 三方对比,3 遍。
- Q3:新写 `family_cards/tddgen_hidden.md`、`bugfix_hidden.md`(只描述任务族性质,
  **必须如实描述"多数测试隐藏,只在终验运行"这一反馈结构**,不含任何题目/分数/轨迹)
  → builder0 → 两族 train/val,3 遍。
- 正式阶段预算上限:executor ≤ 15M tokens、proposer/builder(sonnet-4-6)≤ 100 次调用,
  总成本估 $20–40;超限暂停并报告。

---

## 9. 代码最小改动(设计问题 9)

按迁移顺序列出;除 §9.6 外全部可离线回归验证,不消耗模型调用。

| # | 文件 | 改动 | 接口影响 |
|---|---|---|---|
| 1 | `harness_source.py` | 新增 `validate_sandbox_contract(code)`(import 白名单 {anthropic,json,os}、os 仅 environ/getenv/path.join、禁 open/exec/eval/compile/\_\_import\_\_/getattr/setattr/globals/vars);`parse_generated_harness` 串接调用 | 生成门禁收紧;对现存 harness 已验证兼容 |
| 2 | `eval.py` | `check_model_lock` 后调用 `validate_sandbox_contract`;summary 增加 `contract_violations`、`n_infra_invalid`、`category_counts` 聚合 | CLI 与 `evaluate()` 签名不变 |
| 3 | `_eval_one.py` | (a) `tool_dispatch` 包 work_dir 路径护栏;(b) 若 `task_dir/_hidden/test_hidden.py` 存在:恢复校验后在全新 tmp 目录跑可见套件(输出→`test_output`)与隐藏套件(只记计数);`passed` = 隐藏全绿;(c) 写 `visible_passed`、`hidden{...}`、`category`、`contract_violations` 字段 | 无 `_hidden/` 的旧题库走原路径,旧结果可复现 |
| 4 | `tools.py` | **不改**(冻结) | — |
| 5 | `scripts/import_bigcodebench_hidden.py`(新) | 参数化档位 k;AST 拆分可见子集(保留 setUp/辅助,按源码顺序留前 k 个 `test_` 方法);写 `_hidden/test_hidden.py`;§8.1 的过滤+双验+分割;manifest 记录算法与哈希 | 复用现 `import_bigcodebench_hard_canary.py` 的 fetch/校验骨架 |
| 6 | `scripts/mutate_bugfix_hidden.py`(新,canary 达标后) | §8.2 冻结变异算子管线 | — |
| 7 | `family_cards/tddgen_hidden.md`、`bugfix_hidden.md`(新) | 五要素卡,如实描述隐藏反馈结构 | — |
| 8 | `loop.py` | `FAMILY_DESCS` 增两族描述 | — |
| 9 | `proposer.py` | **不改**(泄漏隔离已由 result 结构保证);仅当族 B 启用时 CONSTRAINTS 中"only solution.py"文字核对适用 | — |
| 10 | `tests/` | 新增:路径护栏单测;隐藏评分单测(fixture_bench 加带 `_hidden/` 的 oracle/stub 假题);沙箱合同单测(现存 4 个 harness 全过 + 恶意样例全拒);导入拆分规则单测;旧题库回归(无 `_hidden` 行为不变) | — |
| 11 | 文档 | CLAUDE.md 架构小节(AGENTS.md 为 symlink,改一处即可)、README、TEST.md、RESULTS.md 追加轮次、PROGRESS.md | — |

数据格式:task 目录新增可选子目录 `_hidden/`(内含 `test_hidden.py`);benchmark 目录新增
`benchmarks/tddgen_hidden/{canary,train,val}`、`benchmarks/bugfix_hidden/{train,val}`;
result JSON 新增字段见 #3(旧字段全部保留)。

---

## 10. 失败分类(设计问题 10)

判定优先级从上到下,先命中先分类;`category` 随每个 task-run 落盘:

| category | 判定条件 | 计入能力分? |
|---|---|---|
| `tampered` | 完整性校验失败(改保护文件/注入 .py) | 计 0 分且全局计数,>0 触发停止复核 |
| `harness_error` | harness 抛异常 / 静态合同拒绝 / 返回结构不符 / 0 steps 且 0 tokens | **否**——基础设施无效,按 validate-generated-artifacts 门禁隔离、修复、重跑 |
| `env_error` | 隐藏或可见套件 collection/import 错误而该题 oracle 双验曾通过;网关 5xx/限速证据 | **否**——重跑;复发则题目按 §8.1 顺位递补 |
| `timeout` | 300s 硬超时 | **是**(capability),除非有网关故障证据(→env_error) |
| `capability` | 其余:跑完但隐藏套件未全绿 | **是** |

正式 summary 中 `n_infra_invalid = harness_error + env_error` 单列;任何包含 infra 无效
run 的 3 遍成绩在修复重跑完成前不得写入 RESULTS.md 结论表。这是 pilot "早期 0 分被
隔离"教训的制度化。

---

## 11. 分阶段执行顺序(设计问题 6 之流程 / 期望输出 6)

| 阶段 | 内容 | 模型调用 | 出口条件 |
|---|---|---|---|
| P0 | §9 #1–#3、#10 代码 + 回归测试;对现存 4 个 harness 跑沙箱合同 | 无 | 测试全绿;合同零误伤 |
| P1 | §9 #5 导入脚本;以 V1 档生成 `benchmarks/tddgen_hidden/canary/`(5 题);离线 stub/oracle 双验;commit 冻结 manifest + §7 预注册表 + 本方案定稿 | 无 | 冻结 commit 存在 |
| P2 | canary 阶梯(§3、§7),每次运行走 validate-generated-artifacts 门禁(先 1 题后 4 题) | haiku ×1 遍 ×≤3 | 落带 → P3;否则停止回方案模式 |
| P3 | §8.1 正式池导入与分割、§8.2 族 B 构建(或回退)、family cards;全部离线验证后 commit 冻结 | 无 | 两族 train/val manifest 冻结 |
| P4 | 新四格基准:v001 于 A/B × train/val 各 3 遍 → 两族并行 6 轮进化 → 期末考/互换考/builder0 考,全部 3 遍 | 正式预算内 | 判定线出三问结果 |
| P5 | RESULTS.md 追加本轮;PROGRESS.md 经验;文档同步 | 无 | — |

P2 与 P3 之间不需要再次人工确认(整套规则已预注册);但**本方案本身需要用户确认后才开始 P0**。

---

## 12. 风险清单与回退条件(期望输出 8)

| # | 风险 | 概率 | 预注册应对 |
|---|---|---|---|
| 1 | V1 canary 仍 5/5,V0 也 5/5 | 低 | §3 规则停止;结论"单函数形态对 haiku-4-5 饱和";回方案模式设计仓库级(附录 B 起点) |
| 2 | V2 仍 ≤2/5(过难) | 低 | §3 规则停止;回方案模式(考虑换更易题源或放宽步数——均属协议变更,不现场做) |
| 3 | 相邻档跨带(V1 满分且 V0 崩) | 中 | §3 规则停止,判"阶梯粒度不足",回方案模式 |
| 4 | 族 B 变异管线合格题不足 | 中 | §8.2 预注册回退 specgen_hidden,Q2 结论强度降级并如实标注 |
| 5 | 正式池过滤后 <44 题 | 中 | 预注册扩容:安装 pinned numpy/pandas 后重过滤再冻结;仍不足则族规模等比缩(最低 train8/val10)并标注功效下降 |
| 6 | 沙箱合同误伤未来生成物(如 getattr) | 中 | 合同文字进 proposer/builder prompt;拒绝走既有零样本合同修复循环;属 harness_error 不计能力分 |
| 7 | 隐藏套件评分侧 flaky | 低 | 导入时双跑一致性过滤;运行期按 env_error 重跑 |
| 8 | 越界读取绕过静态合同(动态技巧) | 低 | 路径护栏兜底 + trace 审计;发现即协议漏洞流程(隔离、修合同、重跑) |
| 9 | 成本超限 | 低 | §7/§8.3 上限硬停 |

全局回退条件:任一"回方案模式"触发时,保留全部已冻结产物与结果,输出交接 Prompt
(按 CLAUDE.md 约定),等用户决策;不得为继续跑而现场放宽任何冻结项。

---

## 13. 用户确认后的实施清单(期望输出 9)

按序执行,每步有绿灯条件:

1. [P0] `harness_source.py::validate_sandbox_contract` + 单测(含现存 4 harness 兼容性断言)。
2. [P0] `eval.py`:接入沙箱合同、summary 新字段;`tests/test_eval.py` 扩展。
3. [P0] `_eval_one.py`:路径护栏 + 隐藏终验评分 + category;`tests/fixture_bench` 加 `_hidden`
   假题;旧题库回归断言。
4. [P1] `scripts/import_bigcodebench_hidden.py`(V 档参数化拆分 + 双验 + manifest);
   `tests/test_bigcodebench_import.py` 扩展拆分规则单测。
5. [P1] 生成 V1 canary 5 题;离线双验;commit:代码 + 题目 + manifest + 本方案(冻结点 №1)。
6. [P2] canary 阶梯运行(先 1 题 canary-of-canary,再全 5 题;≤3 次;严格 §3/§7)。
7. [P2] 阶梯判定记录写入 `results/canary/` 与 PROGRESS.md。
8. [P3] 落带后:正式池导入、分割、族 B 构建(或回退)、family cards;commit(冻结点 №2)。
9. [P4] 新四格基准 → 双族进化 → 期末/互换/builder 三问全套(3 遍)。
10. [P5] RESULTS.md / PROGRESS.md / CLAUDE.md / README / TEST.md 同步;按任务生命周期
    merge + push。

---

## 附录 A:可见子集拆分规则(机械)

对官方 `test` 源码:AST 解析;收集所有 `unittest.TestCase` 子类中名字以 `test_` 开头的方法,
按源码行号排序;保留前 k 个,删除其余方法体;类结构、`setUp/tearDown/setUpClass`、辅助
方法、模块级 import 与常量全部保留;外层仍套现有 `TEST_TEMPLATE`(pytest-timeout 20s)。
k=0 时(V0)输出固定冒烟测试模板。隐藏套件 = 完整官方 `test` 套现有模板,不做删减。
拆分幂等且可由 manifest 中记录的 (dataset, split, task_id, k) 完整重建。

## 附录 B:多文件合同草案(本轮不实现,仅为下一轮起点)

- 任务目录含 `_editable.json` 白名单(相对路径列表);work_dir 复制含子目录。
- 快照:白名单外全部文件逐个 sha256;评分前恢复 + 校验;白名单外任何增删改 → tamper。
- 新建文件一律 tamper(含非 .py;conftest.py/pytest.ini 特别列为高危)。
- run_tests 固定入口文件;sys.path 只含 work_dir;评分在全新目录以白名单内终态文件重建。
