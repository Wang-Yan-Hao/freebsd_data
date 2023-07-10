FreeBSD 5.0-DP1 README

The FreeBSD Project

Copyright © 2000, 2001, 2002 by The FreeBSD Documentation Project

$FreeBSD: src/release/doc/en_US.ISO8859-1/readme/article.sgml,v 1.14
2002/02/25 19:51:34 keramida Exp $

<<<<<<< HEAD
=======
------------------------------------------------------------------------
>>>>>>> b1bb5fd9 (Processing txt files in data/doc)

  This document gives a brief introduction to FreeBSD 5.0-DP1. It
  includes some information on how to obtain FreeBSD, a listing of
  various ways to contact the FreeBSD Project, and pointers to some
  other sources of information.

<<<<<<< HEAD
=======
------------------------------------------------------------------------
>>>>>>> b1bb5fd9 (Processing txt files in data/doc)

1 Introduction

FreeBSD 5.0-DP1 is a ``developer preview'', which is based on the state
of FreeBSD 5-CURRENT on 15 March 2002. A small number of changes have
been made to the system, primarily to improve its stability so that more
of its features can be used and tested.

There are two main goals behind FreeBSD 5.0-DP1 (``Developer Preview
1''). The first is to give the wider FreeBSD community a preview of some
of the new features of 5.0-RELEASE, which is scheduled for release late
in 2002. The second goal of the developer preview is solicit test
reports and feedback on both new and old features.

This developer preview is not for production use; it contains known bugs
and instabilities that should be fixed before FreeBSD 5.0-RELEASE. It is
best considered a ``polished snapshot''. Users testing 5.0-DP1 are
highly encouraged to read the errata file, which lists some of the known
problems, as well as areas of the system that could benefit from some
extra attention during testing.

<<<<<<< HEAD
=======
------------------------------------------------------------------------
>>>>>>> b1bb5fd9 (Processing txt files in data/doc)

1.1 About FreeBSD

FreeBSD is an operating system based on 4.4 BSD Lite for Intel, AMD,
Cyrix or NexGen ``x86'' based PC hardware, Compaq (formerly DEC) Alpha
computers, and UltraSPARC machines. Versions for the IA64 and PowerPC
architectures are currently under development as well. FreeBSD works
with a wide variety of peripherals and configurations and can be used
for everything from software development to games to Internet Service
Provision.

This release of FreeBSD contains everything you need to run such a
system, including full source code for the kernel and all utilities in
the base distribution. With the source distribution installed, you can
literally recompile the entire system from scratch with one command,
making it ideal for students, researchers, or users who simply want to
see how it all works.

A large collection of third-party ported software (the ``Ports
Collection'') is also provided to make it easy to obtain and install all
your favorite traditional UNIX utilities for FreeBSD. Each ``port''
consists of a set of scripts to retrieve, configure, build, and install
a piece of software, with a single command. Over 6,600 ports, from
editors to programming languages to graphical applications, make FreeBSD
a powerful and comprehensive operating environment that extends far
beyond what's provided by many commercial versions of UNIX. Most ports
are also available as pre-compiled ``packages'', which can be quickly
installed from the installation program.

<<<<<<< HEAD
=======
------------------------------------------------------------------------
>>>>>>> b1bb5fd9 (Processing txt files in data/doc)

1.2 Target Audience

This snapshot is aimed primarily at early adopters and various other
users who want to get involved with the ongoing development of FreeBSD.
While the FreeBSD development team tries its best to ensure that each
snapshot works as advertised, 5-CURRENT is very much a work-in-progress.

The basic requirements for using this snapshot are technical proficiency
with FreeBSD and an understanding of the ongoing development process of
FreeBSD 5-CURRENT (as discussed on the FreeBSD-current mailing list
<freebsd-current@FreeBSD.org>).

For those more interested in doing business with FreeBSD than in
experimenting with new FreeBSD technology, formal releases (such as
4.5-RELEASE) are frequently more appropriate. Releases undergo a period
of testing and quality assurance checking to ensure high reliability and
dependability.

<<<<<<< HEAD
=======
------------------------------------------------------------------------
>>>>>>> b1bb5fd9 (Processing txt files in data/doc)

2 Obtaining FreeBSD

FreeBSD may be obtained in a variety of ways. This section focuses on
those ways that are primarily useful for obtaining a complete FreeBSD
distribution, rather than updating an existing installation.

<<<<<<< HEAD
=======
------------------------------------------------------------------------
>>>>>>> b1bb5fd9 (Processing txt files in data/doc)

2.1 CDROM and DVD

FreeBSD -RELEASE distributions may be ordered on CDROM or DVD from
several publishers. This is frequently the most convenient way to obtain
FreeBSD for new installations, as it provides a convenient way to
quickly reinstall the system if necessary. Some distributions include
some of the optional, precompiled ``packages'' from the FreeBSD Ports
Collection.

A list of the CDROM and DVD publishers known to the project are listed
in the ``Obtaining FreeBSD'' appendix to the Handbook.

<<<<<<< HEAD
=======
------------------------------------------------------------------------
>>>>>>> b1bb5fd9 (Processing txt files in data/doc)

2.2 FTP

You can use FTP to retrieve FreeBSD and any or all of its optional
packages from ftp://ftp.FreeBSD.org/, which is the official FreeBSD
release site, or any of its ``mirrors''.

Lists of locations that mirror FreeBSD can be found in the FTP Sites
section of the Handbook, or on the http://mirrorlist.FreeBSD.org/ Web
pages. Finding a close (in networking terms) mirror from which to
download the distribution is highly recommended.

Additional mirror sites are always welcome. Contact
<freebsd-admin@FreeBSD.org> for more details on becoming an official
mirror site. You can also find useful information for mirror sites at
the Mirroring FreeBSD article.

Mirrors generally contain the floppy disk images necessary to begin an
installation, as well as the distribution files needed for the install
process itself. Many mirrors also contain the ISO images necessary to
create a CDROM of a FreeBSD release.

<<<<<<< HEAD
=======
------------------------------------------------------------------------
>>>>>>> b1bb5fd9 (Processing txt files in data/doc)

3 Contacting the FreeBSD Project

3.1 Email and Mailing Lists

For any questions or general technical support issues, please send mail
to the FreeBSD general questions mailing list
<freebsd-questions@FreeBSD.org>.

If you're tracking the 5-CURRENT development efforts, you must join the
FreeBSD-current mailing list <freebsd-current@FreeBSD.org>, in order to
keep abreast of recent developments and changes that may affect the way
you use and maintain the system.

Being a largely-volunteer effort, the FreeBSD Project is always happy to
have extra hands willing to help--there are already far more desired
enhancements than there is time to implement them. To contact the
developers on technical matters, or with offers of help, please send
mail to the FreeBSD technical discussions mailing list
<freebsd-hackers@FreeBSD.org>.

Please note that these mailing lists can experience significant amounts
of traffic. If you have slow or expensive mail access, or are only
interested in keeping up with major FreeBSD events, you may find it
preferable to subscribe instead to the FreeBSD announcements mailing
list <freebsd-announce@FreeBSD.org>.

All of the mailing lists can be freely joined by anyone wishing to do
so. Send mail to <majordomo@FreeBSD.org> and include the keyword help on
a line by itself somewhere in the body of the message. This will give
you more information on joining the various lists, accessing archives,
etc. There are a number of mailing lists targeted at special interest
groups not mentioned here; more information can be obtained either
through majordomo or the mailing lists section of the FreeBSD Web site.

  Important: Do not send email to the lists asking to be subscribed. Use
  the <majordomo@FreeBSD.org> address instead.

<<<<<<< HEAD
=======
------------------------------------------------------------------------
>>>>>>> b1bb5fd9 (Processing txt files in data/doc)

3.2 Submitting Problem Reports

Suggestions, bug reports and contributions of code are always
valued--please do not hesitate to report any problems you may find. Bug
reports with attached fixes are of course even more welcome.

The preferred method to submit bug reports from a machine with Internet
mail connectivity is to use the send-pr(1) command or use the Web form
at http://www.FreeBSD.org/send-pr.html. ``Problem Reports'' (PRs)
submitted in this way will be filed and their progress tracked; the
FreeBSD developers will do their best to respond to all reported bugs as
soon as possible. A list of all active PRs is available on the FreeBSD
Web site; this list is useful to see what potential problems other users
have encountered.

Note that send-pr(1) itself is a shell script that should be easy to
move even onto a non-FreeBSD system. Using this interface is highly
preferred. If, for some reason, you are unable to use send-pr(1) to
submit a bug report, you can try to send it to the FreeBSD problem
reports mailing list <freebsd-bugs@FreeBSD.org>.

For more information, ``Writing FreeBSD Problem Reports'', available on
the FreeBSD Web site, has a number of helpful hints on writing and
submitting effective problem reports.

<<<<<<< HEAD
=======
------------------------------------------------------------------------
>>>>>>> b1bb5fd9 (Processing txt files in data/doc)

4 Further Reading

There are many sources of information about FreeBSD; some are included
with this distribution, while others are available on-line or in print
versions.

<<<<<<< HEAD
=======
------------------------------------------------------------------------
>>>>>>> b1bb5fd9 (Processing txt files in data/doc)

4.1 Release Documentation

A number of other files provide more specific information about this
snapshot distribution. These files are provided in various formats. Most
distributions will include both ASCII text (.TXT) and HTML (.HTM)
renditions. Some distributions may also include other formats such as
PostScript (.PS) or Portable Document Format (.PDF).

-   README.TXT: This file, which gives some general information about
    FreeBSD as well as some cursory notes about obtaining a
    distribution.

-   RELNOTES.TXT: The release notes, showing what's new and different in
    FreeBSD 5.0-DP1 compared to the previous release (FreeBSD
    4.0-RELEASE).

-   HARDWARE.TXT: The hardware compatibility list, showing devices with
    which FreeBSD has been tested and is known to work.

-   INSTALL.TXT: Installation instructions for installing FreeBSD from
    its distribution media.

-   ERRATA.TXT: Release errata. For this developer preview, this file
    lists some outstanding issues and problems, as well as a list of
    features that could benefit from some wider testing. Unlike the
    errata file for a regular FreeBSD release, this file will not be
    updated after 5.0-DP1 is ``frozen''.

  Note: Several of these documents (in particular, RELNOTES.TXT,
  HARDWARE.TXT, and INSTALL.TXT) contain information that is specific to
  a particular hardware architecture. For example, the alpha release
  notes contain information not applicable to the i386, and vice versa.
  The architecture for which each document applies will be listed in
  that document's title.

On platforms that support sysinstall(8) (currently the i386 and alpha),
these documents are generally available via the Documentation menu
during installation. Once the system is installed, you can revisit this
menu by re-running the sysinstall(8) utility.

<<<<<<< HEAD
=======
------------------------------------------------------------------------
>>>>>>> b1bb5fd9 (Processing txt files in data/doc)

4.2 Manual Pages

As with almost all UNIX-like operating systems, FreeBSD comes with a set
of on-line manual pages, accessed through the man(1) command or through
the hypertext manual pages gateway on the FreeBSD Web site. In general,
the manual pages provide information on the different commands and APIs
available to the FreeBSD user.

In some cases, manual pages are written to given information on
particular topics. Notable examples of such manual pages are tuning(7)
(a guide to performance tuning), security(7) (an introduction to FreeBSD
security), and style(9) (a style guide to kernel coding).

<<<<<<< HEAD
=======
------------------------------------------------------------------------
>>>>>>> b1bb5fd9 (Processing txt files in data/doc)

4.3 Books and Articles

Two highly-useful collections of FreeBSD-related information, maintained
by the FreeBSD Project, are the FreeBSD Handbook and FreeBSD FAQ
(Frequently Asked Questions document). On-line versions of the Handbook
and FAQ are always available from the FreeBSD Documentation page or its
mirrors. If you install the doc distribution set, you can use a Web
browser to read the Handbook and FAQ locally.

A number of on-line books and articles, also maintained by the FreeBSD
Project, cover more-specialized, FreeBSD-related topics. This material
spans a wide range of topics, from effective use of the mailing lists,
to dual-booting FreeBSD with other operating systems, to guidelines for
new committers. Like the Handbook and FAQ, these documents are available
from the FreeBSD Documentation Page or in the doc distribution set.

A listing of other books and documents about FreeBSD can be found in the
bibliography of the FreeBSD Handbook. Because of FreeBSD's strong UNIX
heritage, many other articles and books written for UNIX systems are
applicable as well, some of which are also listed in the bibliography.

<<<<<<< HEAD
=======
------------------------------------------------------------------------
>>>>>>> b1bb5fd9 (Processing txt files in data/doc)

5 Acknowledgments

FreeBSD represents the cumulative work of many hundreds, if not
thousands, of individuals from around the world who have worked
countless hours to bring about this snapshot. For a complete list of
FreeBSD developers and contributors, please see ``Contributors to
FreeBSD'' on the FreeBSD Web site or any of its mirrors.

Special thanks also go to the many thousands of FreeBSD users and
testers all over the world, without whom this snapshot simply would not
have been possible.

<<<<<<< HEAD
=======
------------------------------------------------------------------------
>>>>>>> b1bb5fd9 (Processing txt files in data/doc)

This file, and other release-related documents, can be downloaded from
ftp://current.FreeBSD.org/pub/FreeBSD/.

For questions about FreeBSD, read the documentation before contacting
<questions@FreeBSD.org>.

All users of FreeBSD 5-CURRENT should subscribe to the
<current@FreeBSD.org> mailing list.

For questions about this documentation, e-mail <doc@FreeBSD.org>.
