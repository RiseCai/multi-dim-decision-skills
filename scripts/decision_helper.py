#!/usr/bin/env python3
"""
多维度决策辅助脚本
Usage: python3 decision_helper.py --problem "问题描述" --attempt 1|2|3
"""

import argparse
import sys

def analyze_problem(problem, attempt):
    """根据尝试次数给出决策建议"""
    
    print(f"\n{'='*60}")
    print(f"🎯 问题: {problem}")
    print(f"📝 当前尝试: 第 {attempt} 次")
    print(f"{'='*60}\n")
    
    # 大事化小
    print("📐 原则1: 大事化小 (Break Big into Small)")
    print("-" * 40)
    print("建议拆解维度:")
    print("  1. 代码层 - 语法、类型、逻辑错误")
    print("  2. 配置层 - 依赖、版本、环境变量")
    print("  3. 环境层 - 系统、网络、权限")
    print("  4. 流程层 - 构建、测试、部署")
    print()
    
    # 事不过三
    print("⚡ 原则2: 事不过三 (No More Than Three)")
    print("-" * 40)
    if attempt == 1:
        print("✅ 第1次尝试 - 使用直接方法")
        print("   如果失败: 记录问题，准备优化方案")
    elif attempt == 2:
        print("⚠️  第2次尝试 - 优化调整")
        print("   如果失败: 必须分析根本原因，准备彻底改变策略")
    elif attempt == 3:
        print("🚨 第3次尝试 - 彻底改变策略!")
        print("   建议:")
        print("   • 放弃当前解决路径")
        print("   • 寻求替代方案")
        print("   • 咨询他人意见")
        print("   • 暂时搁置，换思路后再来")
    else:
        print("❌ 已超过3次尝试!")
        print("   必须停止当前方法，彻底改变策略")
    print()
    
    # 举一反三
    print("🔍 原则3: 举一反三 (Learn from One, Apply to Many)")
    print("-" * 40)
    print("检查清单:")
    print("  □ 这个问题在其他地方是否也存在?")
    print("  □ 同类文件/模块是否有相似问题?")
    print("  □ 修复方案是否可以批量应用?")
    print("  □ 是否需要更新规范/流程避免复发?")
    print()
    
    # 小事化了
    print("✨ 原则4: 小事化了 (Resolve Small Completely)")
    print("-" * 40)
    print("完成标准:")
    print("  □ 找到根本原因，不是表面修复")
    print("  □ 修复方案彻底，无临时方案")
    print("  □ 验证修复有效")
    print("  □ 添加监控/预防措施")
    print("  □ 经验已记录分享")
    print()
    
    print("="*60)
    print("💡 记住: 事不过三，第三次必须改变策略!")
    print("="*60)

def main():
    parser = argparse.ArgumentParser(description='多维度决策辅助')
    parser.add_argument('--problem', required=True, help='问题描述')
    parser.add_argument('--attempt', type=int, default=1, help='当前尝试次数 (1-3)')
    args = parser.parse_args()
    
    analyze_problem(args.problem, args.attempt)

if __name__ == '__main__':
    main()
