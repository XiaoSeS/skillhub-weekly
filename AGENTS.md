# AGENTS.md

## 项目目的

本仓库发布 SkillHub 开源周报静态站。读者默认先看到 2—3 屏总览，再通过 Tab 查看项目健康、Issue/PR 和数据说明。

## 内容规则

- 总览只保留“仓库关键信息、功能迭代信息、生态相关进展”，顺序固定。
- 同一事实只表达一次；详细指标放入对应 Tab。
- 明确区分统计期、当前快照和期后进展。
- 缺失数据写“未取得”或说明缺失原因，不能用 0 代替。
- 推广动作由维护者提供，必须保留原始链接。
- HTML 必须自包含，不引用外部 CSS、JavaScript、图片或字体。

## 修改与验证

- 报告存放在 `site/reports/<YYYY-Www>/index.html`。
- 新增报告时同步更新 `site/reports.json` 的列表和 `latest`。
- 不手工修改 `_site/`；它由 `scripts/build_site.py` 生成。
- 修改后运行：

```bash
python3 scripts/build_site.py
python3 scripts/validate_site.py _site
```

- 页面改动还需在桌面和窄屏验证 Tab、表格横向滚动、键盘焦点和打印样式。

## GitHub Pages

`.github/workflows/pages.yml` 是唯一发布入口。使用 GitHub 官方 Pages artifact，不新增 `gh-pages` 分支发布流程。
