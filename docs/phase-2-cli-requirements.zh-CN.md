# 第二阶段 CLI 需求设计文档

## 1. 背景

InvestFlow 第一阶段已经完成 skills framework、模板、示例和边界测试。第二阶段需要提供一个轻量 CLI，让用户可以在本地快速生成投研报告骨架，并校验报告是否符合 InvestFlow 的边界要求。

## 2. 目标

CLI 的目标是：

- 快速查看项目内置 skills、templates、examples。
- 基于模板生成报告骨架。
- 校验 Markdown 报告是否包含必要结构。
- 提供一条命令的 quickstart，本地生成可校验、可渲染的示例报告。
- 调用现有安装脚本，同步 Codex skills。
- 提供 `doctor` 命令检查项目状态。

## 3. 非目标

第二阶段 CLI 不做：

- 不接入行情、财报、新闻或交易数据。
- 不生成投资建议。
- 不输出 standalone 买入 / 卖出结论。
- 不连接券商账户。
- 不执行交易。
- 不做 MCP 或数据连接器。

## 4. 命令设计

### 4.1 `investflow doctor`

检查项目是否具备运行条件。

输入：

```bash
./scripts/investflow doctor
./scripts/investflow --json doctor
```

输出：

- 项目根目录
- skills 数量
- templates 数量
- examples 数量
- Codex plugin manifest 是否存在
- Codex 安装脚本是否存在

JSON 输出示例：

```json
{
  "ok": true,
  "skills": 8,
  "templates": 4,
  "examples": 7,
  "plugin_manifest": true,
  "codex_installer": true
}
```

### 4.2 `investflow quickstart`

快速生成本地示例报告，帮助新用户跑通报告搭建、校验和渲染链路。

输入：

```bash
./scripts/investflow quickstart
./scripts/investflow quickstart --output-dir work/demo
./scripts/investflow quickstart --force
./scripts/investflow --json quickstart --output-dir work/demo
```

输出：

- `thesis.md`：基于 thesis 模板生成的 Markdown 报告。
- `thesis.html`：由 Markdown 渲染出的 HTML 报告。
- 后续可执行命令提示。

规则：

- 默认输出到 `work/quickstart`。
- 如果目标文件已存在，默认拒绝覆盖。
- 使用 `--force` 才允许覆盖。
- JSON 模式输出生成文件路径、校验结果和后续命令。

### 4.3 `investflow list`

查看可用资源。

输入：

```bash
./scripts/investflow list skills
./scripts/investflow list templates
./scripts/investflow list examples
./scripts/investflow --json list skills
```

输出：

- `skills`：列出 skill 名称。
- `templates`：列出模板文件。
- `examples`：列出示例文件。

### 4.4 `investflow new`

基于模板生成报告骨架。

输入：

```bash
./scripts/investflow new brief --output work/research-brief.md
./scripts/investflow new thesis --output work/thesis.md
./scripts/investflow new risk-review --output work/risk-review.md
./scripts/investflow new postmortem --output work/postmortem.md
```

规则：

- 如果目标文件已存在，默认拒绝覆盖。
- 使用 `--force` 才允许覆盖。
- 不传 `--output` 时输出到 stdout。

### 4.5 `investflow validate`

校验 Markdown 报告结构。

输入：

```bash
./scripts/investflow validate report.md
./scripts/investflow --json validate report.md
```

校验内容：

- 是否包含 `## 投资判断`
- 是否包含 `## 关键依据`
- 是否包含 `## 反方最强质疑`
- 是否包含 `## 主要风险`
- 是否包含 `## 仓位与风控`
- 是否包含 `## 最终结论`
- 是否没有 standalone `买入` / `卖出` 标题式结论

JSON 输出示例：

```json
{
  "ok": false,
  "missing": ["## 反方最强质疑"],
  "violations": ["standalone buy/sell conclusion"]
}
```

### 4.6 `investflow install codex`

调用现有安装脚本，将 skills 同步到 Codex。

输入：

```bash
./scripts/investflow install codex
```

行为：

- 调用 `scripts/install-codex-skills.sh`
- 支持通过环境变量 `CODEX_SKILLS_DIR` 指定安装目录

## 5. 输出边界

CLI 必须遵守：

- 不提供投资建议。
- 不生成买入 / 卖出命令。
- 不联网获取行情。
- 不隐藏缺失信息。
- 所有报告模板保留风险、反方观点、失效条件和复盘条件。

## 6. 验收标准

第二阶段 MVP 完成时，应满足：

- `./scripts/investflow --help` 可用。
- `./scripts/investflow doctor` 可用。
- `./scripts/investflow --json doctor` 输出稳定 JSON。
- `quickstart` 可生成 `thesis.md` 和 `thesis.html`。
- `quickstart` 默认不覆盖已有文件。
- `--json quickstart` 输出稳定 JSON。
- `list skills/templates/examples` 可用。
- `new brief/thesis/risk-review/postmortem` 可输出模板。
- `new ... --output` 可写文件，且默认不覆盖已有文件。
- `validate` 可识别缺失章节。
- `validate` 可识别 standalone `买入` / `卖出` 结论。
- `install codex` 可调用现有安装脚本。
- `./scripts/validate.sh` 覆盖 CLI 测试。
- GitHub Actions 自动运行 CLI 测试。
