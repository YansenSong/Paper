# PaperWriting · Agent-Friendly LaTeX Research Template

一个面向 **科研论文 + Coding Agent 协作** 的 LaTeX 仓库模板。

它的核心思想不是把所有论文都塞在 `main`，而是让：

- `main` 永远保持为可复用的论文骨架；
- 每篇具体论文使用自己的长期 `paper/...` 分支；
- Codex、Claude Code 等 Agent 在清晰的目录、编译命令和行为约束下工作；
- 论文特定的标题、实验、结论、引用、图片和投稿格式不会污染通用模板。

## Repository model

```text
main
 └─ reusable LaTeX scaffold

paper/icml-2027-my-method
 └─ one concrete paper

paper/iros-2027-robot-agent
 └─ another concrete paper
```

**不要把具体论文内容合回 `main`。**

适合回到 `main` 的只有真正跨论文可复用的改进，例如：

- 通用编译脚本；
- 引用检查工具；
- 通用 Agent 工作规范；
- 更好的目录组织；
- 不包含论文特定内容的 LaTeX tooling。

## 目录结构

```text
PaperWriting/
├── main.tex             # 论文总入口
├── refs.bib             # BibTeX 文献库
├── sections/            # 各章节 TeX
├── figures/             # 图片资源
├── tables/              # 表格资源 / 片段
├── notes/               # 研究笔记、TODO、草稿材料
├── scripts/
│   └── check_refs.py    # 引用 key 检查
├── Makefile             # 编译 / 清理 / 引用检查
├── AGENTS.md            # 通用 Coding Agent 规则
├── CLAUDE.md            # Claude Code 规则
└── README.md
```

## 环境要求

至少需要：

- Git
- Python 3（用于引用检查脚本）
- 一套 LaTeX 发行版
- `latexmk`

Ubuntu / Debian 示例：

```bash
sudo apt update
sudo apt install latexmk texlive-latex-extra texlive-fonts-recommended
```

不同投稿模板可能还需要额外 LaTeX package，请以具体论文分支的编译错误和 venue 模板要求为准。

## 快速开始一篇新论文

### 1. 从最新 main 创建论文分支

```bash
git switch main
git pull
git switch -c paper/icml-2027-my-method
```

推荐命名：

```text
paper/<short-name>
paper/<venue>-<year>-<short-name>
```

例如：

```text
paper/iros-2027-agentic-navigation
paper/icra-2027-multi-robot
paper/my-new-method
```

### 2. 修改论文内容

常见入口：

```text
main.tex
sections/
refs.bib
figures/
tables/
```

把论文特有内容全部留在当前 `paper/...` 分支。

### 3. 编译

```bash
make
```

或显式：

```bash
make pdf
```

Makefile 实际调用：

```text
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

因此 LaTeX 错误会直接导致构建失败，而不是悄悄生成不完整 PDF。

### 4. 检查引用

```bash
make check-refs
```

该命令执行：

```bash
python3 scripts/check_refs.py
```

用于发现正文引用和 `refs.bib` 之间的 key 问题。

### 5. 清理构建产物

普通清理：

```bash
make clean
```

更彻底：

```bash
make distclean
```

## 多人 / 多 Agent 协作

如果一篇论文需要更细的任务分支，不要从 `main` 随便开，而应该从对应 `paper/...` 分支继续：

```text
paper/icml-2027-my-method
 ├─ work/my-method/introduction
 ├─ work/my-method/experiments
 ├─ work/my-method/figures
 └─ work/my-method/reviewer-response
```

这样：

```text
main                    = 通用模板
paper/...               = 某篇论文的集成分支
work/...                = 该论文的局部任务分支
```

论文完成后，也不需要把 `paper/...` merge 回 `main`。

## Agent workflow

在让 Codex / Claude Code 修改论文前，推荐流程：

```text
1. 确认当前 Git 分支
2. 阅读 AGENTS.md / CLAUDE.md
3. 阅读 main.tex 与相关 section
4. 对结构性修改先理解全文上下文
5. 做局部、可审阅的修改
6. make
7. make check-refs
8. git diff
9. 人类作者最终审阅
```

### 为什么一定先检查分支

如果 Agent 在 `main` 上开始写具体论文：

```text
标题
摘要
方法
实验结果
venue 模板
```

那么通用骨架就会被污染，下一篇论文无法干净复用。

因此对具体论文任务，第一件事应是：

```bash
git branch --show-current
```

如果输出是 `main`，先创建或切换到对应论文分支。

## Agent 可以帮助什么

比较适合交给 Coding Agent 的任务：

- 调整 LaTeX 结构；
- 修复编译错误；
- 统一符号 / notation；
- 检查章节交叉引用；
- 查找重复定义；
- 重构表格 / figure 布局；
- 根据**已有真实数据**整理结果表；
- 检查 BibTeX key；
- 改善语言表达；
- 根据作者给出的实验结果生成 LaTeX 表格；
- 整理 reviewer response 草稿；
- 检查全文术语一致性。

## Agent 不应该做什么

科研仓库最重要的约束：**不要为了让论文“完整”而编造科学事实。**

Agent 不得自行捏造：

- citation；
- DOI；
- 作者；
- 数据集；
- baseline；
- 实验结果；
- p-value；
- benchmark 数字；
- 消融实验；
- 用户研究人数；
- hardware 规格；
- 论文已被某 venue 接收等事实。

如果数据缺失，应写 TODO / 明确缺口，而不是生成一个看起来合理的数字。

## 引用工作流

推荐：

```text
找到真实论文
    │
    ▼
核对标题 / 作者 / venue / year
    │
    ▼
加入 refs.bib
    │
    ▼
正文 \cite{...}
    │
    ▼
make check-refs
    │
    ▼
make
```

不要让 Agent 直接凭模型记忆写 BibTeX 后就当作真实来源。

## Figures

建议把最终论文引用的图放在：

```text
figures/
```

注意区分：

- 源图 / 可编辑工程文件；
- 论文实际引用的 PDF / PNG；
- 临时实验截图。

临时文件不应长期堆在 `figures/` 根目录。

如果图来自实验脚本，最好能在论文分支中保留生成方式或数据来源说明，以便复现。

## Tables

复杂表格可以拆到：

```text
tables/
```

例如：

```latex
\input{tables/main_results}
```

这样 `sections/experiments.tex` 不会被超长 `tabular` 淹没，也方便 Agent 单独修改表格布局。

## Notes

`notes/` 适合保存：

- 研究问题；
- 实验 TODO；
- reviewer feedback；
- 论文结构草案；
- 待核验 citation；
- 写作决策；
- 不应该直接出现在正文的工作记录。

把“思考过程”和“最终论文文本”分开，会让 Agent 更容易理解哪些内容可以直接改正文，哪些只是内部备忘。

## 推荐的论文分支检查清单

提交前：

```bash
make
make check-refs
git diff --check
git status
```

然后人工检查：

1. PDF 是否能从头到尾正常生成；
2. Figure / Table 编号是否正确；
3. 所有 citation 都是真实且对应正确；
4. 数字与实验源数据一致；
5. 摘要、正文、结论中的主要 claim 一致；
6. 方法符号在全文含义一致；
7. venue 的页数、匿名、格式要求满足；
8. 没有把本地临时文件或隐私数据提交进仓库。

## 更新模板 main 的原则

可以进入 `main`：

```text
更好的 Makefile
通用 lint / check script
Agent guideline 改进
跨论文通用 LaTeX 结构
通用 .gitignore
```

不应该进入 `main`：

```text
某篇论文标题
某个方法名
实验数字
specific refs
submission-specific style
reviewer response
论文专用 figure
```

如果在具体论文分支发现了一个真正通用的改进，建议单独回到 `main` 重做那个小改动，而不是把整条 paper branch 合并回来。

## Current template philosophy

这个仓库的目标不是成为一个复杂的论文管理框架，而是提供几个稳定约束：

- Git 分支隔离论文；
- LaTeX 文件结构清晰；
- 编译命令固定；
- 引用可检查；
- Agent 有明确工作规则；
- 科学事实必须由真实来源和人类作者负责。

越简单，越容易被不同论文、不同 venue 和不同 Coding Agent 复用。

## License

仓库当前未提供独立 License 文件。如计划把这个模板作为公共模板供他人复制，建议补充明确的软件 / 模板许可证，并确认未来加入的 venue 模板文件是否有独立授权要求。
