# 第四阶段 报告生成与社区技能包需求设计文档

## 1. 背景

InvestFlow 已经具备 skills、模板、示例、CLI 和只读数据能力。第四阶段需要提升输出体验，并为社区贡献不同风格的 skill pack 预留结构。

## 2. 目标

第四阶段目标是：

- 提供 Markdown 投研报告到 HTML 的本地生成能力。
- 生成报告时保留免责声明和 InvestFlow 边界提示。
- 提供社区 skill pack 目录结构与 manifest 规范。
- 提供 CLI 命令列出和校验社区 skill pack。

## 3. 非目标

第四阶段不做：

- 不生成 PDF。
- 不调用外部排版服务。
- 不自动发布报告。
- 不允许社区包绕过合规边界。
- 不允许社区包包含交易执行能力。

## 4. 报告生成

### 4.1 CLI 命令

```bash
./scripts/investflow render report.md --output report.html
```

规则：

- 输入必须是本地 Markdown 文件。
- 默认输出 HTML。
- HTML 必须包含 InvestFlow disclaimer。
- HTML 必须转义用户 Markdown 内容中的 HTML。
- 渲染前应复用 `validate` 的结构校验；校验失败则拒绝生成，除非显式使用 `--force`。

### 4.2 输出 HTML 要求

输出必须包含：

- `<html>`
- 报告正文
- `InvestFlow`
- `not investment advice`
- 生成时间

## 5. 社区技能包

### 5.1 目录结构

```text
packs/community/
├── README.md
└── long-term-investing/
    ├── pack.json
    └── skills/
```

### 5.2 `pack.json` 字段

- `name`
- `display_name`
- `description`
- `version`
- `author`
- `license`
- `skills`
- `boundaries`

### 5.3 CLI 命令

```bash
./scripts/investflow pack list
./scripts/investflow --json pack list
./scripts/investflow pack validate packs/community/long-term-investing
```

校验规则：

- 必须存在 `pack.json`。
- 必须声明 `boundaries`。
- `boundaries` 必须包含 `not_investment_advice`。
- 不允许声明交易执行能力。

## 6. 验收标准

第四阶段 MVP 完成时，应满足：

- `render` 可将合格 Markdown 报告生成 HTML。
- `render` 默认拒绝结构不合格报告。
- `render --force` 可渲染结构不完整报告，但仍保留免责声明。
- `pack list` 可列出社区 skill pack。
- `pack validate` 可校验社区 skill pack。
- 示例社区包存在。
- `scripts/validate.sh` 覆盖第四阶段测试。
