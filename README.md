# SkillHub Weekly

SkillHub 的公开开源周报站点。默认入口展示最新一期，总览控制在约 2—3 屏；项目健康、Issue/PR 和统计口径通过 Tab 查看。

## 本地预览

```bash
python3 scripts/build_site.py
python3 scripts/validate_site.py _site
python3 -m http.server 4173 --directory _site
```

打开 `http://localhost:4173/`。

## 新增一期周报

1. 在 `site/reports/<YYYY-Www>/index.html` 新增自包含 HTML。
2. 在 `site/reports.json` 追加报告元数据，并更新 `latest`。
3. 运行构建和校验命令。
4. 合并到 `main` 后，GitHub Actions 使用官方 Pages artifact 自动发布。

报告遵循以下内容顺序：

1. 仓库关键信息
2. 功能迭代信息
3. 生态相关进展

总览只放决策信息；健康明细和 Issue/PR 队列放入独立 Tab。缺失数据标为“未取得”，不能写成 0；统计期、当前快照与期后进展必须分开。

## 目录

```text
site/
├── reports.json
└── reports/<week>/index.html
scripts/
├── build_site.py
└── validate_site.py
```

`scripts/build_site.py` 会生成 `_site/index.html`、`_site/archive.html` 和 `.nojekyll`。`_site/` 是临时构建产物，不提交。
