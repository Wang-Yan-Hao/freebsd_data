FreeBSD 7.1-RELEASE 自述

The FreeBSD Project

版权 © 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007 The FreeBSD
Documentation Project

$FreeBSD: src/release/doc/zh_CN.GB2312/readme/article.sgml,v 1.3.2.2.2.1
2008/11/25 02:59:29 kensmith Exp $

FreeBSD 是 FreeBSD基金会的注册商标

Intel, Celeron, EtherExpress, i386, i486, Itanium, Pentium, 和 Xeon 是
Intel Corporation 及其分支机构在美国和其他国家的商标或注册商标。

Motif, OSF/1, 和 UNIX 是 The Open Group 在美国和其他国家的注册商标； IT
DialTone 和 The Open Group 是其商标。

Sparc, Sparc64, SPARCEngine, 以及 UltraSPARC 是 SPARC International, Inc
在美国和其他国家的商标。 包含 SPARC 商标的产品基于 Sun Microsystems,
Inc. 开发的架构。

许多制造商和经销商使用一些称为商标的图案或文字设计来彰显自己的产品。
本文档中出现的， 为 FreeBSD Project 所知晓的商标，后面将以 '™' 或 '®'
符号来标注。

<<<<<<< HEAD
=======
------------------------------------------------------------------------
>>>>>>> b1bb5fd9 (Processing txt files in data/doc)

  这份文档对 FreeBSD 7.1-RELEASE 作了一个简短的介绍， 还包括如何获取
  FreeBSD、FreeBSD 项目联系的多种方式， 以及一些其他的信息来源。

<<<<<<< HEAD
=======
------------------------------------------------------------------------
>>>>>>> b1bb5fd9 (Processing txt files in data/doc)

1 介绍

这个发行版本是 FreeBSD 7.1-RELEASE 的一个 release， 它是 7.1-STABLE
分支的最新版本。

<<<<<<< HEAD
=======
------------------------------------------------------------------------
>>>>>>> b1bb5fd9 (Processing txt files in data/doc)

1.1 关于 FreeBSD

FreeBSD 是一个基于 4.4 BSD Lite 的操作系统，支持 基于 AMD64 和 Intel
EM64T 的 PC 硬件 (amd64)， 基于 Intel, AMD, Cyrix 或 NexGen “x86” 的 PC
硬件 (i386)， 基于 Intel Itanium Processor 的计算机 (ia64)， NEC
PC-9801/9821 系列 PC 及其兼容机 (pc98)， 以及 UltraSPARC® 机器
(sparc64)。 支持 PowerPC® (powerpc) 和 MIPS® (mips)
硬件架构的的版本也正在开发中。 FreeBSD 支持各种各样的外围设备，
可以胜任软件开发、游戏，以及提供 Internet 服务等的各式应用。

这个版本的 FreeBSD 包含了运行这样一个系统所需要的每样东西，
在基本的发行中包含了完整的内核和所有的工具源代码。 只要安装了源代码，
您就可以用一条命令从头编译整个系统，
这对于那些想知道它是如何工作的学生、 研究人员或者用户来说非常有用。

包含大量已经移植的第三方软件集合 (“Ports Collection”) 让在 FreeBSD
上获取并安装所有您喜欢的传统 UNIX® 工具变得容易。 每个 “port”
是一些用一条命令就可以下载、配置、编译并安装软件的脚本。 超过 19,000 个
port，从编辑器到编程语言再到图形应用程序， 让 FreeBSD
成为一个大大扩展了很多商业 UNIX 版本所能提供的强大并且通用的操作环境。
大多数 port 也提供了预编译的 “package”， 可以用安装程序快速安装。

<<<<<<< HEAD
=======
------------------------------------------------------------------------
>>>>>>> b1bb5fd9 (Processing txt files in data/doc)

1.2 目标用户

FreeBSD 的这个 release 适用于所有用户。
它经历了一定时期的测试和质量检测来确保最高的可用性和可靠性。

<<<<<<< HEAD
=======
------------------------------------------------------------------------
>>>>>>> b1bb5fd9 (Processing txt files in data/doc)

2 获取 FreeBSD

FreeBSD 可以通过各种方式得到。 这一节关注那些可以获取完整的 FreeBSD
发行版本的主要方式， 而不是升级已经装好的系统。

<<<<<<< HEAD
=======
------------------------------------------------------------------------
>>>>>>> b1bb5fd9 (Processing txt files in data/doc)

2.1 CDROM 和 DVD

FreeBSD -RELEASE 发行版本可以从几个发行商那里以 CDROM 或者 DVD
的形式订购。 对于全新安装来说， 这通常是获取 FreeBSD 最方便的方式，
因为它提供了在必要时快速地重新安装系统的方法。
一些发行版本包含了一些来自 FreeBSD Ports 套件的可选的、 预编译的
“package” 以及其他资料。

一个已知的 CDROM 和 DVD 发行商列表列在使用手册的 “Obtaining FreeBSD”
中。

<<<<<<< HEAD
=======
------------------------------------------------------------------------
>>>>>>> b1bb5fd9 (Processing txt files in data/doc)

2.2 FTP

您可以使用 FTP 来从 ftp://ftp.FreeBSD.org/ 下载 FreeBSD
以及所有的可选软件包，这是官方的 FreeBSD 发行站点，或者从任何一个 “镜像”
下载。

FreeBSD 的镜像列表可以在使用手册的 FTP 站点一节， 或者在
http://mirrorlist.FreeBSD.org/ 网页上找到。 强烈推荐您从其中离您最近
(以网络的观点) 的镜像来下载发行版本。

我们非常欢迎您建立新的镜像站点。 联系 <freebsd-admin@FreeBSD.org>
了解成为官方镜像站点的更多细节。 也可以在如何为 FreeBSD 做镜像站点
这篇文章中找到关于镜像站点的更多有用的信息。

镜像站点通常会提供用于刻录 FreeBSD 发行版本的 CDROM 的 ISO 映像文件。
它们通常包括了软盘映像 (仅限支持的平台) 以及通过网络安装所需要的文件。
最后， 镜像站点通常还会提供最新发行版本对应的预编译软件包。

<<<<<<< HEAD
=======
------------------------------------------------------------------------
>>>>>>> b1bb5fd9 (Processing txt files in data/doc)

3 联系 FreeBSD 项目

3.1 电子邮件和邮件列表

有任何问题或者基本的技术支持，请发送邮件到 FreeBSD 一般问题邮件列表。

如果您正在跟随 7.1-STABLE 的开发过程， 您 必须 加入 FreeBSD-CURRENT
邮件列表， 以便及时了解可能影响您使用和维护系统方式的最新进展。

FreeBSD 很大程度上是一个志愿者项目， 它非常欢迎来自更多人的帮助 ────
来完成那些希望完成而没有时间加以完成的改进。 要联系开发者讨论技术问题，
或提供帮助， 请发送邮件到 FreeBSD 技术讨论邮件列表。

请注意这些邮件列表都可能有 可观的 通信量。 如果您访问邮件很慢或很昂贵，
或者您只对及时了解主要的 FreeBSD 活动感兴趣， 订阅 FreeBSD 公告邮件列表
可能更合适。

所有的邮件列表都可以如人们希望的那样自由加入。 请访问 FreeBSD Mailman
信息页。这里会提供有关加入各种列表、 访问存档等等的更多信息。
还有很多针对特定的兴趣群体的邮件列表在这里没有提及， 可以从 Mailman
页面或者 FreeBSD Web 站点的 邮件列表 一节获得更多信息。

  重要: 不要 发送邮件到列表要求订阅。 请使用 Mailman 界面来完成订阅。

<<<<<<< HEAD
=======
------------------------------------------------------------------------
>>>>>>> b1bb5fd9 (Processing txt files in data/doc)

3.2 提交问题报告

建议，bug 报告和代码捐献永远是有价值的
──请不要犹豫是否报告您可能会发现的任何问题。 当然附带了修正的 bug
报告会更受欢迎。

从一台能够收发 Internet 邮件的主机提交 bug 报告的首选方法是使用
send-pr(1) 命令。 用这种方式提交的“问题报告”(PR)会被归档并跟踪进度，
FreeBSD 开发者会尽最大努力尽快地对所有报告的 bug 做出反应。
所有尚未完全解决的 PR 列表可以在 FreeBSD Web 站点上找到，
这个列表可以用于查看其它用户可能遭遇的问题。

注意 send-pr(1) 本身是一个 shell 脚本， 因此很容易把它移植到非 FreeBSD
系统上。 极力推荐使用这个界面。 如果因为一些原因不能使用 send-pr(1)
来提交 bug 报告，您可以尝试把它发送到 FreeBSD 问题报告邮件列表。

要了解更多的信息，FreeBSD Web 站点上的“ 撰写 FreeBSD
问题报告”对撰写并提交有效的错误报告有很多有用的提示。

<<<<<<< HEAD
=======
------------------------------------------------------------------------
>>>>>>> b1bb5fd9 (Processing txt files in data/doc)

4 进一步阅读

有很多关于 FreeBSD 的信息资源，一些包含在发行版中，
另一些则以在线或印刷版本的方式提供。

<<<<<<< HEAD
=======
------------------------------------------------------------------------
>>>>>>> b1bb5fd9 (Processing txt files in data/doc)

4.1 发行文档

许多其它的文档提供了有关这个 release
发行版本的更加详细的信息。这些文件提供了各种各样的格式。
大多数发行版本会包含 ASCII 文本 (.TXT) 和 HTML (.HTM)
格式。有一些发行版本也可能包含其它的格式， 比如 Portable Document Format
(.PDF)。

-   README.TXT：这个文件提供了有关 FreeBSD 的一些简要的信息，
    还有一些有关获取发行版本的粗略的注解。

-   RELNOTES.TXT： 发行说明， 展示了相对于前一版本 (FreeBSD
    7.0-RELEASE)， FreeBSD 7.1-RELEASE 中的创新和差异。

-   HARDWARE.TXT：硬件兼容列表， 展示了 FreeBSD
    已经测试并已知可以使用的设备。

-   ERRATA.TXT：发行勘误。 提供新近发现的、 发行之后发现的问题等信息，
    主要适用于发行版本(相对于 snapshot)。 在安装 FreeBSD 的一个 release
    之前参考这个文件是非常重要的， 因为它包含了自从 release
    创建以来发现并修正问题的最新的信息。

在支持 sysinstall(8) 的平台上 (目前有 amd64、 i386、 ia64、 pc98 以及
sparc64)， 这些文档在安装时都可以通过 Documentation 菜单访问。
一旦系统已经安装，您可以通过重新运行 sysinstall(8) 工具来重新访问菜单。

  注意: 在安装您拿到的任何发行版之前阅读勘误是非常重要的，
  它能帮助您了解那些在发布工程 “后期发现的” 以及发布之后发现的问题。
  随每个发行自带的勘误文件总是不够精确的， 但是其它的副本会通过 Internet
  保持更新并作为 这个发行的 “最新勘误” 参考。 这些其它的勘误副本放在
  http://www.FreeBSD.org/releases/
  (还有保持更新的任何镜像站点的同一位置)。

<<<<<<< HEAD
=======
------------------------------------------------------------------------
>>>>>>> b1bb5fd9 (Processing txt files in data/doc)

4.2 联机手册

像所有的类 UNIX 操作系统一样，FreeBSD 附带一套在线联机手册， 可以通过
man(1) 命令或者通过 FreeBSD Web 站点上的超文本联机手册网关 访问。
一般情况下，联机手册为 FreeBSD 用户提供不同命令和 API 的信息。

有时，联机手册还提供特定主题的信息。 一个不太恰当的例子就是 tuning(7)
(性能调整向导)、 security(7) (FreeBSD 一个关于安全的介绍) 还有 style(9)
(内核代码规范指南)。

<<<<<<< HEAD
=======
------------------------------------------------------------------------
>>>>>>> b1bb5fd9 (Processing txt files in data/doc)

4.3 书籍和文章

两个由 FreeBSD 项目维护的非常有用的 FreeBSD 相关的信息集合， 是 FreeBSD
使用手册和 FreeBSD FAQ (频繁被问到的问题)。 使用手册 和 FAQ
的在线版本可以从 FreeBSD 文档页面 或者它的镜像上得到。 如果安装了 doc
发行集， 则可以在本地使用 Web 浏览器来阅读使用手册和 FAQ。
值得一提的是， 在使用手册中提供了如何安装 FreeBSD 的详细说明。

许多在线书籍和文章也由 FreeBSD 项目维护， 涵盖了更专业的、FreeBSD
相关的主题。 这些文章题材广泛，从邮件列表的有效使用到双重启动 FreeBSD
和其它操作系统，再到给新 committer 的指南。 同使用手册和 FAQ
一样，这些文档可以从 FreeBSD 文档页面或者 doc 分类中得到。

有关 FreeBSD 的其它书籍和文档的列表可以在 FreeBSD 使用手册的参考书目
一章找到。由于 FreeBSD 固有的 UNIX 传统， 许多为 UNIX
系统撰写的文章和书籍也是适用的， 其中一些也被列在参考书目中。

<<<<<<< HEAD
=======
------------------------------------------------------------------------
>>>>>>> b1bb5fd9 (Processing txt files in data/doc)

5 感谢

FreeBSD 有全世界的成百上千的人工作无数个小时才带来这个 release。要查看
FreeBSD 开发者和捐献者的完整列表，请查看 FreeBSD Web
站点或者任何一个镜像站点上的 “FreeBSD 捐献者”。

在此也要特别感谢众多的 FreeBSD 用户和全世界的测试人员，
没有他们就根本不会有这个 release。

<<<<<<< HEAD
=======
------------------------------------------------------------------------
>>>>>>> b1bb5fd9 (Processing txt files in data/doc)

这份文档，以及其他与FreeBSD发行版本有关的文档，都可以在
ftp://ftp.FreeBSD.org/下载。

在遇到关于FreeBSD的技术问题时，请首先阅读 文档 之后再考虑联系
<questions@FreeBSD.org>。

所有 FreeBSD 7.1-STABLE 的用户都应该订阅 <stable@FreeBSD.org> 邮件列表。

关于这份文档的任何问题，请致信 <doc@FreeBSD.org>。
