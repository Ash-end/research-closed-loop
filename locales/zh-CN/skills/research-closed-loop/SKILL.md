---
name: research-closed-loop
description: "Guide an observation-led empirical research project from quantified problem through bottleneck diagnosis, literature gap, minimal prototype, rigorous validation and resource-aware portfolio decisions. Use for the full research loop or choosing its next stage; not competition coaching or an authorization to run experiments."
---

# 观测驱动科研闭环

把实际现象变成可检验的问题，再形成“问题 → 原因假说 → 设计 → 证据 → 修正”的逻辑链。默认用于实验与工程驱动科研；不把观测起点强加给理论研究、探索性研究或用户明确选择的假设驱动研究。

## 先判断当前位置

读取用户提供的现象、日志、方法或已有结果，以及当前项目中直接相关的材料；不要扫描无关项目。信息不足时给出暂定判断与最低成本补证方案，不编造数据，不先发完整问卷。

按当前决策只加载需要的阶段，不默认读完或执行全部阶段：

只有主题、尚无数据时也可启动：先用问题定位阶段给出暂定任务、操作性定义、合法数据/测量准备和最低成本观察方案；不能检索时把前作/创新判断列为待核实。不捏造异常，也不因尚未量化而拒绝提供启动计划。

| 当前需要 | 阶段技能 | 交付重点 |
|---|---|---|
| 模糊现象，尚不清楚问题在哪里 | [research-problem-localization](../research-problem-localization/SKILL.md) | 带分母、边界和实际代价的问题陈述 |
| 问题明确，原因尚未区分 | [research-bottleneck-diagnosis](../research-bottleneck-diagnosis/SKILL.md) | 竞争解释、区分性测试与瓶颈证据 |
| 需要了解已有解法与创新空间 | [research-gap-mapping](../research-gap-mapping/SKILL.md) | 主张—来源—适用条件—缺口映射 |
| 有机制想法，需要低成本试错 | [research-minimal-prototype](../research-minimal-prototype/SKILL.md) | 最小可判别验证及继续/修订/停止条件 |
| 原型值得深入，需完整证据体系 | [research-validation-design](../research-validation-design/SKILL.md) | 公平基线、独立评估、消融和局限 |
| 多个方向竞争资源，或主线受阻 | [research-portfolio-management](../research-portfolio-management/SKILL.md) | 主线/备选、资源预算与切换理由 |

阶段可以交叉和回退：文献可帮助定义问题；原型失败可回到测量或归因；完整验证失败应缩小主张、修改机制或停止，而不是无条件加模块。

## 共用约束

- 区分原始观测、复核结果、推断、待检验假说和文献报告；未测量的数字写“待测”，用户例子的 80%/32×32 不当成项目结果。
- 消融在具体协议下支持组件贡献，不自动证明真实世界因果；多数据集只支持已测试范围，不证明普遍泛化。
- 查到文献不等于文献支持主张；未检索到不等于没有前人。无实时检索能力时交付待核实的检索计划。
- 研究计划不等于执行许可。仅解释/诊断/设计时不修改实验代码，不启动训练、付费接口、远程任务或额外代理。实际执行按本次用户授权和预算，失败重试须有边界。
- 这是科研技能集：不引入竞赛获奖标准、自媒体写作目标或雅思教学规范。目录分类不是权限沙箱。
- 使用已有项目记录，避免建立重复目录。用户需要落地文件时可采用 [项目记录模板](assets/research-state.md)，不强制所有字段或每次保存文件；仅在用户指定项目范围写入。

## 交付与闭环

每次输出与当前任务相称的结果，并说明：当前证据支持什么、不支持什么；最关键的未知；下一项最能改变判断的行动；什么结果会使当前判断反转。完整流程请求再给阶段间依赖、资源上限和回退点，不保证论文录用或性能提升。

涉及比例、消融或失败解释时，按需读 [判读边界](references/decision-boundaries.md)。需要核对方法依据时读 [方法来源](references/method-sources.md)。本技能不依赖外部 MCP、付费模型或特定 Python 包；真实计算和检索可使用当前可用工具，但如实报告限制。

本集合可独立使用，不依赖其他科研技能；按当前任务选择工具，不因名字相近继承其他流程的固定步骤或执行权限。
