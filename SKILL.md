---
name: multi-dim-decision
description: Multi-dimensional decision-making framework for problem solving. Use when facing complex problems requiring structured analysis, needing to avoid repeated mistakes, wanting to break down large problems, or seeking to simplify and resolve issues efficiently. Implements four core principles including learn from one case and apply to many, limit retries to three, break big problems into small ones, and resolve small issues completely.
---

# 多维度决策思维技能

## 核心原则

### 1. 举一反三 (Learn from One, Apply to Many)

**含义:** 从一个问题中提炼通用规律，应用到同类问题

**执行步骤:**
1. 分析当前问题的根本原因
2. 抽象出通用模式/规律
3. 检查其他可能受影响的领域
4. 批量修复同类问题

**示例:**
```
问题: storage_service.dart 第139行多了一个)
举一反三: 检查所有 .dart 文件是否有类似语法错误
结果: 发现并修复了其他3个文件的同类问题
```

---

### 2. 事不过三 (No More Than Three)

**含义:** 同一方法尝试不超过三次，第三次必须改变策略

**执行步骤:**
1. **第一次尝试:** 直接方法
2. **第二次尝试:** 优化调整
3. **第三次尝试:** 彻底改变策略（换思路/工具/方案）

**决策矩阵:**

| 尝试次数 | 策略 | 如果失败 |
|---------|------|---------|
| 1 | 直接修复 | 记录问题，准备优化 |
| 2 | 优化方案 | 分析根本原因，准备改变策略 |
| 3 | 彻底改变 | 放弃当前路径，寻求替代方案 |

**示例:**
```
尝试1: 直接修改代码 → 失败
尝试2: 添加类型转换 → 失败  
尝试3: 重构数据结构 → 成功 ✅
```

---

### 3. 大事化小 (Break Big into Small)

**含义:** 将复杂大问题拆解为可管理的小任务

**执行步骤:**
1. **识别大问题:** 明确最终目标
2. **分层拆解:** 按维度/模块/阶段拆分
3. **优先级排序:** 确定依赖关系和紧急程度
4. **逐个击破:** 完成小任务，积累小胜利

**拆解维度:**
- 时间维度: 长期/中期/短期
- 模块维度: 前端/后端/数据库
- 风险维度: 高风险/中风险/低风险
- 依赖维度: 阻塞项/非阻塞项

**示例:**
```
大问题: CI构建失败
拆解:
  ├── 代码层: 语法错误、类型错误
  ├── 配置层: workflow配置、依赖版本
  ├── 环境层: Flutter版本、Android SDK
  └── 测试层: 单元测试、集成测试
```

---

### 4. 小事化了 (Resolve Small Completely)

**含义:** 小问题解决要彻底，不留尾巴，避免复发

**执行步骤:**
1. **定位根源:** 找到问题的根本原因，不是表面现象
2. **彻底修复:** 修复当前问题 + 预防措施
3. **验证闭环:** 验证修复有效，监控不再复发
4. **知识沉淀:** 记录经验，更新文档/流程

**检查清单:**
- [ ] 问题根本原因已找到
- [ ] 修复方案彻底，无临时方案
- [ ] 已验证修复有效
- [ ] 已添加监控/预防措施
- [ ] 经验已记录分享

**示例:**
```
问题: 类型错误导致构建失败
小事化了:
  ✅ 根本原因: 缺少类型转换
  ✅ 彻底修复: 添加 (obj as String?)
  ✅ 验证: Run #55 构建成功
  ✅ 预防: 添加类型检查到代码规范
  ✅ 沉淀: 更新 error_patterns.md
```

---

## 综合应用流程

```
遇到问题
    ↓
[维度1: 分类] → 识别问题类型
    ↓
[维度2: 聚类] → 匹配历史相似问题
    ↓
[维度3: 降维] → 提取关键特征
    ↓
大事化小 → 拆解为小任务
    ↓
[维度4: 信息增益] → 判断是否值得继续
    ↓
事不过三 → 最多尝试3次解决
    ↓
[维度6: 因果] → 追溯根本原因
    ↓
举一反三 → 检查同类问题
    ↓
[维度5: 抽象] → 生成通用方案
    ↓
[维度7: 回归] → 预测成功率（禁止100%）
    ↓
[维度8: 约束满足] → 评估可行性
    ↓
    ┌─────────────────────────────┐
    │      维度9: 前置验证 PV      │
    │   必须 PV = 1.0 才能继续     │
    └─────────────┬───────────────┘
                  │
            PV = 1.0?
           是 ↓      ↓ 否
    小事化了 → 彻底解决  返回优化
    ↓
知识沉淀 → 更新文档，分享经验
```

**完整维度表详见:** [references/dimension-table.md](references/dimension-table.md)

## Scripts

### decision_helper.py

辅助决策脚本，帮助应用四个原则。

Usage:
```bash
python3 scripts/decision_helper.py --problem "CI构建失败" --attempt 2
```

See [scripts/decision_helper.py](scripts/decision_helper.py)

## References

- [九维决策维度表](references/dimension-table.md) - 完整数学化维度表
- [决策案例库](references/case_studies.md) - 实际应用案例
- [检查清单](references/checklists.md) - 各原则执行清单
- [常见陷阱](references/pitfalls.md) - 需要避免的错误

## 使用示例

```
用户: "CI构建又失败了"

应用多维度决策:
1. 大事化小: 拆解为代码错误、配置问题、环境问题
2. 事不过三: 这是第2次尝试，还可以试1次
3. 举一反三: 检查是否有其他文件有类似错误
4. 小事化了: 彻底修复 + 添加监控
```
