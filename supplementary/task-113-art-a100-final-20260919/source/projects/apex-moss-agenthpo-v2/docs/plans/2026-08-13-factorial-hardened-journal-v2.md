# Factorial Hardened Journal v2 合同草案（2026-08-13）

> 状态：**方案草案，未授权实现或执行。** 本文不会修改旧 `events.py`、不会迁移或混写历史 v1 ledger，
> 也不授予模型、Evaluator、GPU、CPU 或付费资源。待用户确认事务恢复与 physical-attempt 口径后冻结。

## 1. 目的与边界

新 AgentHPOBench/GDPevo factorial 实验需要同时满足：

- ledger、head、pending、grant 与 lock 全部 descriptor-relative，拒绝任意父级/目标 symlink 和非普通文件；
- 每个外部 side effect 先持有 exact schedule 与不可借硬预算 reservation；
- crash 后不会删除已经发生的调用事实、退款或重发同一 physical operation；
- 独立 verifier 只读且绝不自动修复；只有 controller 在独占锁下可按已持久化 pending 精确 redo；
- logical stage、physical attempt、artifact validation 和 typed skip 分层，不把 transport completion 当作合同通过；
- 旧 36-event CompilerGym canary 的 `events.py` AST 兼容证明保持不变。

因此 v2 必须是独立模块与独立产物根，不能原地扩展 v1：

```text
factorial_resource_authority.py
factorial_operation_journal_v2.py
factorial_scheduled_governor.py
factorial_stage_evidence_v2.py
```

旧 v1 ledger 只允许用旧 verifier 做历史只读重放，不进入新 factorial formal authority。

## 2. 存储布局

每个 formal segment 使用 controller-private 根，建议初始 mode `0700`：

```text
control/factorial-journal-v2/
  ledger.jsonl
  journal.lock
  resource.lock
  pending.json                 # 静止态必须不存在
  head.json
  authority.json              # 内容寻址 grant 快照，不可覆盖
  revocations/                # 追加式、不可变撤销 receipt；不改写 grant
```

所有入口保留调用方给出的 lexical absolute path，不调用 `Path.resolve()`。从 `/` 开始逐组件 `openat`：

- 目录：`O_DIRECTORY | O_NOFOLLOW | O_CLOEXEC`；
- 普通读取：`O_RDONLY | O_NOFOLLOW | O_NONBLOCK | O_CLOEXEC`；
- ledger append：`O_WRONLY | O_APPEND | O_CREAT | O_NOFOLLOW | O_NONBLOCK | O_CLOEXEC`；
- lock：`O_RDWR | O_CREAT | O_NOFOLLOW | O_NONBLOCK | O_CLOEXEC`。

打开后以 `fstat` 强制普通文件并核对保存的 `(st_dev, st_ino)`；正式目录要求 controller-only，writer 创建的
新文件为 `0600`。历史只读兼容不以精确 mode 拒绝旧文件。任何创建、link/replace 或 unlink 后都 `fsync`
对应目录；目录 `fsync` 不可用时 capability canary 失败关闭。

## 3. Authority 与资源绑定

`authority.json` 必须由独立、内容寻址的 execution-grant preparer 生成，并绑定：

- pinned source commit/tree、task authority bundle、formal plan、matrix 与 4,338-stage schedule SHA；
- exact physical-operation mapping schema；
- provider/model/evaluator/image/environment identity；
- global cap、逐 cell cap、每种 operation 的 exact reservation；
- canary evidence SHA、grant issuer、segment nonce 与固定到期时刻；
- journal schema、reducer/source SHA 与产物根 identity。

Grant 内容一旦写入不可改写；后续撤销只能由独立、追加式、内容寻址的 revocation receipt/registry 表达。
每次 reserve 同时重读 grant 快照与当前撤销集合，不能把可变撤销位塞回不可覆盖的 `authority.json`。

`FactorialScheduledGovernor` 不暴露任意 `reserve(operation_id, resource)`。唯一入口接受 trusted schedule 中的
`FactorialPotentialOperation` 加 typed `PhysicalOperationBinding`，每次 reserve 前重读 authority、source、plan、
schedule、environment 与剩余额度。运行时 caller 不能更换 cap、kind、cell 或 reservation。

## 4. Logical 与 physical operation

logical stage 仍是预注册的 4,338 项。每次真实调用使用独立 physical ID：

```text
<logical_operation_id>:attempt-0001
<logical_operation_id>:attempt-0002
```

`PhysicalOperationBinding` 至少绑定：

- logical/physical ID、attempt index、cell/stage/kind；
- schedule operation SHA、authority SHA、reservation；
- previous physical terminal/attempt receipt；
- environment SHA 与 environment-check receipt；
- retry eligibility 与 retry budget。

推荐冻结规则：

- attempt 1 是默认物理调用；
- 环境资格是独立、预注册的 pre-start gate operation；只有该 gate 在对应 provider/evaluator physical operation
  尚为 `ABSENT` 时产生 typed `ENVIRONMENT_INVALID` terminal，且新 environment SHA 不同，才允许 attempt 2；
- 任何已经 `started` 的 physical operation 永不使用同一 ID 重发；
- 所有 physical records 都进入预算与报告；logical disposition 绑定完整 physical chain；
- 非环境错误、合同拒绝、provider failure、started-without-artifact 均不获得 retry。

这一规则仍需用户确认；在确认前 v1 semantic disposition 明确只接受 logical direct ID，并保持 `NOT_READY`。

## 5. Event 与 reducer

v2 event schema 独立版本化，至少包含：

- sequence、event type、event ID、previous/event SHA；
- logical/physical operation ID；
- authority、schedule-operation、cell、stage、kind；
- reservation/committed usage；
- artifact SHA、usage-known、terminal reason；
- pending transaction ID。

状态机：

```text
ABSENT → RESERVED → STARTED → COMPLETED | FAILED
```

- `RESERVED` 尚无 side effect；恢复是否继续必须由同一 physical binding 决定；
- `STARTED` 一律按全 reservation 计费。若没有可信 terminal artifact，封存为 typed
  `STARTED_WITHOUT_ARTIFACT`，永不重发；
- provider 成功返回只是 `COMPLETED` transport fact；JSON/schema/compile/candidate validation 是本地 typed gate，
  不伪装为 `FAILED`；
- `FAILED` 表示 provider/evaluator operation terminal failure；unknown usage 收满 reservation；
- local gate rejection 触发 ITT floor 和 immediate-child skip，不产生伪 evaluator operation。
- 环境 gate 使用独立 operation/state machine，不把 provider/evaluator 的 `RESERVED` 伪装为可取消 terminal；
  `ENVIRONMENT_INVALID` 时对应 side-effect operation 必须仍为 `ABSENT`。因此 §9 的 reserved-only 同 ID 继续与
  attempt-0002 资格不冲突。

## 6. Pending-WAL 事务

每次追加一个 event 的 pending 记录绑定：

- journal/authority/segment identity；
- old event count/head 与旧 ledger byte length；
- 完整 next-event canonical bytes/hash；
- new count/head；
- pending transaction ID。

提交顺序固定：

1. 独占 `journal.lock`，验证 authority、ledger/head 静止态与无 pending；
2. no-replace 发布 `pending.json`，fsync pending 文件与目录；
3. append 完整 next-event bytes，fsync ledger 与 journal directory；
4. replace `head.json`，fsync head 文件与目录；
5. unlink pending，fsync pending 所在目录；
6. 重新只读核验新 ledger/head 后才返回成功。

controller 恢复只接受以下精确状态：

| Ledger | Head | Pending | 动作 |
|---|---|---|---|
| old | old | exact | 追加 exact event，再完成提交 |
| old + event 的精确前缀 | old | exact | 只补齐剩余 bytes，再完成提交 |
| old + exact event | old | exact | 只发布 new head |
| old + exact event | new | exact | 只清理 pending |
| old + exact event | new | absent | 静止成功 |

任何其他组合——包括无 pending 的 anchor lag、非精确 suffix、额外完整合法 event、损坏 pending、head 超前、
ledger 被截断——全部失败关闭。绝不根据可自行计算的 hash suffix 自动推进 head，也绝不截断 ledger。
独立 verifier 发现 pending 时只报告 `NON_QUIESCENT`，不写任何文件。

fault injection 固定覆盖六个提交边界：pending 发布前、pending fsync 后、ledger 部分 append 后、ledger 完整
append/fsync 后、head replace/fsync 后、pending unlink/fsync 后。每个边界都必须重放上表并证明不会重复 event、
不会漏记已发生事实、不会在无 exact pending 时自行修复。

## 7. Stage evidence 与 exact seal

正式 v2 evidence 必须从一次锁内、descriptor-relative hardened replay 派生：

- observed physical records 必须是 authority 授权 physical set 的子集，并与 executed/terminal dispositions
  精确相等；未实例化的 potential operation、合法 skip 与未触发 retry 由 typed not-issued/skip disposition 证明，
  不要求为了集合相等制造 journal record；
- 每个 physical record 逐项匹配 schedule/cell/kind/reservation；
- artifact bytes 通过内容寻址 no-follow resolver 与 typed gate 复核；
- logical stage 聚合完整 physical chain；
- stage 只能是 executed、typed-gate rejected、started-without-artifact、terminal failed 或 immediate-parent skip；
- skip 只走 `update? → solution → evaluator` 的直接边；A post-v001 没有虚构 update；
- 4,338 个潜在 stage 恰好各一 disposition，且 1,566 个 scoring slot 各有 ITT score/report row；
- report 只输出 benchmark-native raw score，并完整披露 cost/validity/failure。

当前 `factorial_stage_disposition.py` 只验证 semantic fixture：它继承 v1 reader 的存储缺口，未绑定 physical retry、
resource grant、typed gate 或 provider dispatch，因此即使 4,338 exact-set 通过也固定
`formal_execution_ready=false`、`NOT_READY/NOT_GRANTED` 与零 entitlement。

## 8. 必须通过的实现证据

1. symlink/broken symlink、FIFO、directory、socket、device、父目录替换、lock unlink/recreate 全部快速拒绝；
2. ledger 首建、head replace、pending publish/unlink 精确目录 fsync；
3. WAL 上述六个精确 crash injection point 与恢复矩阵全部通过，任何一字节漂移失败；
4. 两进程 cap=1 并发 reserve 只有一个成功；同 physical ID 幂等且不重复调用；
5. started-without-artifact 全额扣费、永久不重发；reserved-only 不冒充 executed；
6. schedule/cap/grant/environment/source 任一漂移在 reserve 前拒绝；
7. 4,338-stage exact physical/logical disposition 与 1,566 score/report dispatch 一对一；
8. 历史 `events.py` 字节/AST 与 CompilerGym 36-event rebind 测试保持不变；
9. canary 测出 CPU/GPU envelope 后才可把 entitlement 从零改成内容寻址非零 grant；
10. 全量 pytest、独立攻击审计和真实 reference/negative/isolation canary 全部通过后，才允许 formal execute CLI。

## 9. 待用户冻结的选择

推荐确认：

1. 采用本 pending-WAL exact-redo；无 pending 的不一致只允许新 segment/manual incident，不自动修复；
2. provider 返回但本地合同拒绝记为 operation `COMPLETED` + typed gate rejection；
3. started-without-artifact 保留已消费事实并封存，不新增可重发语义；
4. reserved-only 可在同一 physical ID 下继续 start，但不得更换 binding；
5. physical retry 只允许独立 pre-start environment gate 的 `ENVIRONMENT_INVALID`，对应 side-effect operation
   必须仍为 `ABSENT`；最多一次且环境 SHA 必须变化；
6. accepted compile 在后续 solution/evaluator 中断时推进 accepted Harness head，但 physical terminal 与 compile head
   分离记录；
7. reason-code 闭集由 typed gate/adapter schema分别维护，不在 journal transport 层自由解释。
