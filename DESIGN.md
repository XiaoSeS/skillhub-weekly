---
name: SkillHub Weekly
description: Notion-inspired light weekly open-source report
colors:
  canvas: "#ffffff"
  warm-surface: "#f6f5f4"
  ink: "#0d0d0d"
  ink-soft: "#31302e"
  muted: "#615d59"
  faint: "#76716c"
  line: "#e5e3e1"
  link: "#0075de"
  link-active: "#005bab"
  focus: "#097fe8"
  success: "#147a33"
  success-surface: "#e9f7ec"
  warning: "#b84d00"
  warning-surface: "#fdf0e3"
  risk: "#b52d25"
  risk-surface: "#fdecea"
typography:
  display:
    fontFamily: "Inter, -apple-system, BlinkMacSystemFont, Segoe UI, PingFang SC, Microsoft YaHei, sans-serif"
    fontSize: "clamp(2rem, 4vw, 2.75rem)"
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: "-0.025em"
  headline:
    fontFamily: "Inter, -apple-system, BlinkMacSystemFont, Segoe UI, PingFang SC, Microsoft YaHei, sans-serif"
    fontSize: "1.625rem"
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: "-0.02em"
  title:
    fontFamily: "Inter, -apple-system, BlinkMacSystemFont, Segoe UI, PingFang SC, Microsoft YaHei, sans-serif"
    fontSize: "1.125rem"
    fontWeight: 700
    lineHeight: 1.35
  body:
    fontFamily: "Inter, -apple-system, BlinkMacSystemFont, Segoe UI, PingFang SC, Microsoft YaHei, sans-serif"
    fontSize: "0.9375rem"
    fontWeight: 400
    lineHeight: 1.65
  label:
    fontFamily: "Inter, -apple-system, BlinkMacSystemFont, Segoe UI, PingFang SC, Microsoft YaHei, sans-serif"
    fontSize: "0.75rem"
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: "0.01em"
rounded:
  control: "4px"
  surface: "8px"
  card: "12px"
  pill: "9999px"
spacing:
  xs: "4px"
  sm: "8px"
  md: "16px"
  lg: "24px"
  xl: "32px"
  section: "48px"
components:
  tab-active:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.label}"
    padding: "14px"
  card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink-soft}"
    rounded: "{rounded.card}"
    padding: "20px"
  metric:
    backgroundColor: "{colors.warm-surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.surface}"
    padding: "16px"
  status-warning:
    backgroundColor: "{colors.warning-surface}"
    textColor: "{colors.warning}"
    rounded: "{rounded.pill}"
    padding: "4px 10px"
---

# Design System: SkillHub Weekly

## Overview

**Creative North Star: "The Maintainer's Notion Page"**

页面像一份经过维护者整理的浅色 Notion 文档：白色画布、暖灰分区、近黑正文、轻量边界和极少的蓝色交互强调。内容密度由排版、留白和数据可视化共同承担，而不是由深色品牌块或大量卡片承担。

这是一份治理报告，不是营销页面。图表必须回答具体问题，例如 Issue 是否老化、CI 失败集中在哪里、Release 是否达成；无法形成判断的数据不生成图表。

**Key Characteristics:**

- 白色主画布与 `warm-surface` 交替形成阅读节奏。
- 近黑标题、暖灰正文和单一蓝色链接保持 Notion 式克制。
- 健康卡片、分段条、横向柱图和圆环图提供可视化证据。
- 总览为 2—3 屏，详细信息通过可访问 Tab 渐进披露。
- 模块无内容时连标题、图表和 Tab 一起省略。

## Colors

核心是近黑与暖灰的浅色体系；蓝色仅用于链接、焦点和当前 Tab，状态色只承担语义。

### Primary

- **Notion Link Blue**：链接、当前 Tab 和图表主数据。

### Secondary

- **Semantic Green / Orange / Red**：稳定、需关注与风险。每个颜色旁必须出现文字状态或数值。

### Neutral

- **Canvas White**：页面和卡片表面。
- **Warm Surface**：元信息、指标块和交替模块背景。
- **Near-black Ink**：标题与关键数字。
- **Warm Gray**：说明文字、标签和次级信息。
- **Whisper Line**：表格、卡片和分隔线。

**The Single Accent Rule.** 非状态交互只使用 Link Blue；不得重新引入深蓝大面积品牌色。

## Typography

**Display Font:** Inter 与系统无衬线回退
**Body Font:** Inter 与中文系统无衬线回退

**Character:** 单一无衬线字体通过 400—700 字重、紧凑标题字距和舒展正文行高建立层级。页面不加载外部字体，确保 GitHub Pages、离线和打印一致。

### Hierarchy

- **Display**（700，32—44px，1.15）：报告周次。
- **Headline**（700，26px，1.25）：模块标题。
- **Title**（700，18px，1.35）：健康卡片和图表标题。
- **Body**（400，15px，1.65）：正文，行长控制在 75ch 左右。
- **Label**（600，12px）：状态、元信息和表头，不使用大段全大写。

**The Evidence Weight Rule.** 结论和数值使用 600—700；解释使用 400，不能依靠字号堆叠制造层级。

## Elevation

页面以色块和 1px 轻边框建立层次。阴影只用于需要从暖灰背景中浮起的健康卡片和图表容器，且保持接近不可见；表格和普通模块使用边框，不叠加宽模糊阴影。

### Shadow Vocabulary

- **Card Whisper**（`0 2px 8px rgba(0,0,0,.04)`）：暖灰背景上的白色健康卡片或图表。
- **Flat**（无阴影）：表格、Tab、指标块和主内容模块。

**The Flat-by-default Rule.** 如果边框已经能说明结构，就禁止再加阴影。

## Components

### Buttons

- **Shape:** Tab 保持直角透明背景；其他控制使用轻微圆角（4px）。
- **Primary:** 本站没有营销 CTA；蓝色只用于文本链接和当前状态。
- **Hover / Focus:** Hover 加深文字；键盘焦点使用 2px 蓝色轮廓。

### Chips

- **Style:** 语义色文字配同色浅背景，完整胶囊圆角。
- **State:** 必须带状态文字和小圆点，不只靠颜色传达。

### Cards / Containers

- **Corner Style:** 指标块 8px，健康卡片和图表 12px。
- **Background:** 白色卡片置于暖灰模块上，或暖灰指标块置于白色模块上。
- **Shadow Strategy:** 仅健康卡片和图表可使用 Card Whisper。
- **Border:** 1px Whisper Line；不得使用粗侧边强调线。
- **Internal Padding:** 16—22px。

### Navigation

- 白底粘性 Tab，底部 1px 分隔线。
- 当前 Tab 使用近黑文字与 2px 黑色下划线。
- 窄屏横向滚动；方向键、Home、End 和 URL hash 均可操作。

### Health Charts

- 分段条表示 Actions 结果组成，同时列出成功、失败、等待授权和跳过数。
- 横向柱图表示 Issue/PR 年龄结构，最长数据项占满轨道，其他按比例缩放。
- 圆环图只用于有明确分母的构成数据，例如 `needs-info / 当前开放 Issue`。
- 每张图必须有 `role="img"`、完整 `aria-label`、数值标签和相邻文字结论。

## Do's and Don'ts

### Do:

- **Do** 使用白色画布、暖灰分区、近黑文字和单一蓝色交互强调。
- **Do** 让健康状态同时具备文字结论、原始数值和图表。
- **Do** 保持总览精炼，并把工作流明细与价值队列放入 Tab。
- **Do** 在模块无内容时整块省略，确保后续周报不会出现空标题或空图表。
- **Do** 保持 W29、W30 与后续报告的 Token、组件和响应式行为一致。

### Don't:

- **Don't** 做成“深蓝色公文、纯文字长文、卡片堆叠式 SaaS 仪表盘或营销落地页”。
- **Don't** 使用粗侧边色条、渐变文字、玻璃拟态或装饰性动画。
- **Don't** 用零值替代未取得数据，也不要生成空坐标轴、空圆环或占位卡片。
- **Don't** 重复同一个 KPI，或把 Fork、下载、Issue 作者和 PR 作者画成无 cohort 依据的漏斗。
