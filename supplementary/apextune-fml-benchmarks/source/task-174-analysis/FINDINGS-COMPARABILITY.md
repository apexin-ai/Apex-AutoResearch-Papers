# task-174 · commit 可比性取证报告

**日期**: 2026-09-18  **问题**: 协议标记 non-comparable 的两个原因之一——
"task config pin `cf4ed193` is not reproduced"(实际 checkout 为 `d2115a1`)——
是否实质影响我们与 AIDE 的分数可比性?

## 结论

**不影响。commit 差异是纯适配性的("作者的本地 setup 提交" vs "我们的本地
setup 提交"),评测路径逐字节等价,且有动态逐位复现证据。**

## 证据链(五条,强度递增)

### 1. 重建提交只做了一件事:新增一个惰性文件

`d2115a1 "setup for agent benchmark"` = 在公开上游 AIF360(`cd7e213`,
PR #544 "Replace np.NaNs",v0.6.1 后)之上**仅新增** `algorithm.py`(283 行,
基线算法在仓库根目录的一份副本,FML 通用任务接口的脚手架)。
**对 AIF360 库既有文件的修改:零。** 五个评测路径关键文件
(adversarial_debiasing.py / transformer.py / binary_label_dataset.py /
standard_dataset.py / classification_metric.py)与公开上游 0 行 diff。

### 2. 评测器从不导入那个新增文件

`train_eval_baseline.py` 中 `import algorithm` 出现次数 = 0。
新增文件在评测中不可达,不可能影响任何分数。

### 3. 评测器本体由基准仓库 SHA-256 钉死

评测五件套(train_eval_baseline.py、两个 backup 库文件、config.json、
prompt.json)的 SHA-256 由 fml-bench(官方 `d336651`,clean)钉死,
我们全部 14 轮 manifest 中的哈希与官方逐一一致。

### 4. COMPAS 数据与 ProPublica 官方逐字节一致

`compas-scores-two-years.csv` sha256 = `c451db85…`,与
`propublica/compas-analysis` 官方仓库同名文件**哈希完全相同**。

### 5. 动态逐位复现(决定性)

作者在**他们的 checkout(cf4ed193)+ 他们的环境**上测得基线并硬编码进
评测脚本的三个 17 位常数,在我们的重建 checkout 上跑官方 test 命令**全部
逐位复现**:

| 常数 | 作者硬编码 | 我们实测 | 逐位一致 |
|---|---|---|---|
| test abs_aod | 0.23986259586405548 | 0.23986259586405548 | ✅ |
| test disparate_impact | 0.6753074541440007 | 0.6753074541440007 | ✅ |
| test theil | 0.2058732707585479 | 0.2058732707585479 | ✅ |

50 个 epoch 的 GPU 对抗训练会放大任何代码/数据/数值环境差异;三个独立
指标同时精确到 1e-17 复现,意味着**整条评测链与作者运行时功能等同**。
(附:val 侧基线 abs_aod 0.2657268424611224 与我们 14 轮战役记录的
`baseline_primary_metric` 亦逐位一致——跨三周的内部确定性同样成立。)

注:脚本中 `baseline_cls_acc = 0.63510101010101` 与我们的基线 val 准确率
(0.6758)和 test 准确率(0.6429)均不相等——它是评测器自带的固定约束常数
(来源不明,可能出自作者更早的一次测量),对所有参赛者同一取值,由证据 3
的 SHA 钉死,不构成可比性差异。

## 为什么协议仍标 non-comparable(以及这为什么是对的)

`cf4ed193` 本体从未公开(作者本地提交),**形式上**无法对整棵树做字节比对,
所以 harness 按 fail-closed 纪律保留标记——这是溯源严谨性,不是实质差异的
证据。本报告穷尽了 commit 差异的所有可观察后果:全部为零。

## 净结论

可比性的两个扣分项中,**commit 轴已证实无实质影响**;唯一余下的实质缺口是
**模型轴**(gpt-5.6-sol vs 官方 gpt-5.4)。若未来要出可比成绩,只需换官方
模型重跑,checkout 无需任何处理。
