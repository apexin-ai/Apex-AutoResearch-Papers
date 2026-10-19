# v1r8 Harness 合同兼容与有效性门禁执行方案

## 目标

修复 v1r7 在 `swebench-verified:sphinx-doc__sphinx-8459` 上三臂均为 0 个有效轮的问题，且不把
无效轮伪装为性能分数。修复必须进入 Harness Builder 的初版生成规则，并可复用于 LCBench、
CompilerGym 和后续 task，而不是只给 SWE-bench 增加一次性提示。

## 已确认根因

1. v1r7 正式 SWE-bench codec 要求每个 diff section 都有 Git `index` 行，但正式 task card 没有给出
   精确模板，且 canary 的安全补齐逻辑没有进入正式模型候选边界。
2. 旧 round 只公开笼统的 `contract_rejected`，下一轮 Harness 不知道失败位于 response boundary、
   path、index、hunk、apply 还是 evaluator correctness。
3. B-online 虽绑定了 Experience Bank，静态 `excluded_task_ids` 却把所有 formal task 都排除，导致
   合法的前序题经验在 Harness compile 时被拒绝。
4. 旧报告把无效轮按 0 放入八轮分母，混淆了 Harness 可靠性与通过合同后的性能。

## v1r8 冻结变更

### 初版 Harness 规则

- Rule Registry v3 新增可信 operator `contract_compatibility`。
- 启用 v3 的每个 task 在 v001 必须使用该规则；Planner 仍选择 task-conditioned 角色、工具和 workflow，
  但必须从 reference root 开始，并包含 `task_semantics` 与 `verify_contract`。
- 每个 codec 向 Builder 暴露 task-bound capability card：响应边界、逐字模板、安全正规化、禁止变换和
  公开失败阶段。合同失败时后续轮再次强制选择该规则；通过格式边界后才进入正确性或性能搜索。

### 严格兼容层

- SWE-bench official/model patch 共用一个 compatibility layer。
- 只允许剥离一个完整外层 diff fence、补终止 LF，以及为缺失 metadata 的普通修改/新增/删除文件
  确定性插入 `index` 行。
- 每次正规化保存输入、抽取 diff、规范 diff 的 SHA 与插入计数，并声明
  `semantic_content_changed=false`。
- 路径、mode、hunk header、上下文、增删行、文件顺序、patch apply 和测试语义一律不修复，继续由严格
  validator/evaluator fail closed。

### Builder 记忆

- B-online 的跨题记录由 controller 按当前 stream index、checkpoint SHA、bank SHA、record IDs 和所有
  前序 eligible instance IDs 签发内容寻址 grant。
- 同题、未来题、未绑定记录或 grant 漂移继续拒绝；A 与 B-frozen 不获得该 grant。
- 精确合同原因码和 compatibility trace 进入公开失败轨迹，post-seal distillation 可把适配规律写入下一题
  的 Builder checkpoint，同题八轮之间仍不回收经验。

### 有效性门禁

- 单题单臂固定八次尝试；只有至少 `4/8` 个有效数值轮，才发布 valid-only mean 和 best。
- 未达 `4/8` 标记 `insufficient_validity`，保留八轮与所有失败原因，但均值、best 和臂间差值为 `null`。
- 每 benchmark 前六道学习题至少 `5/6` 道同时满足 B-frozen、B-online 的 `4/8`，才发布跨题平均、
  OLS 斜率、T6−T1 和相对优势；否则整个学习结论标记 `insufficient_validity`。
- 原始分数从不跨 benchmark 混合。

## 执行与准入

1. v1r7 保持不可变消费证据；不修改其 round、receipt、operation 或分数。
2. 新代码、Registry v3、schema v5 staging 和 source hashes 在 clean revision 中冻结。
3. 正式流前先运行独立资格段，只测失败题 `sphinx-doc__sphinx-8459` 的自适应 Harness 八轮；最多
   16 次模型调用、8 次 evaluator transaction、28,800 CPU evaluator 秒。
4. 资格段分数不得并入正式三臂结果。只有 `valid_rounds >= 4` 才允许启动 v1r8 平衡交错正式流；否则
   保留失败轨迹，继续修改通用 Harness 合同规则并用新 clean qualification segment 重测。
5. 准入后继续八个三-suite block 的平衡交错流；每个完整 task 报告三臂 mean/best 六值及有效轮计数。

## 验收

- 定向及全仓测试通过，`git diff --check`、compileall 通过。
- v1r7 归档 solution 重放证明安全兼容层能接收原先被格式门挡住的候选，同时攻击/畸形 diff 仍拒绝。
- 同题真实资格段达到至少 `4/8` 有效，并生成内容寻址 `qualification_summary.json`。
- v1r8 首个 formal durable round 产生后再宣布切换成功，并持续监控每五轮与每个完整 task 的六值。
