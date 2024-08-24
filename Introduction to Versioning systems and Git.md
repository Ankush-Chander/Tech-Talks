---
delivery date: 2024-08-24
---
## Introduction to Versioning systems and Git
By Ankush Chander  
Gandhinagar ML-NLP Group

---
### What is Version Control?
Version Control = Time travel over file system

![](https://qph.cf2.quoracdn.net/main-qimg-f2d019b7769d19f201a47f8f9d00cfb5.webp)

Pic credits: [Quora](https://www.quora.com/I-have-watched-the-movie-Interstellar-3-times-now-but-I-still-dont-get-it-How-was-Cooper-TARS-understanding-the-singularity-when-he-it-fell-through-the-black-hole-How-can-you-explain-the-singularity-in-simpler-terms)

---
A **Version Control System (VCS)** is a tool that helps software developers keep track of how their software development projects - desktop applications, websites, mobile apps, etc - change over time.

---
#### History
![](https://initialcommit.com/img/initialcommit/vcs-timeline.png)

Picture credit: [Version Control Systems | A Technical Guide](https://initialcommit.com/blog/Technical-Guide-VCS-Internals)

---

#### Generations of VCs 
- First Generation - Local Version Control Software
	- SCCS
	- RCS
-  Second Generation - Centralized Version Control Tools
	- CVS (Concurrent Versions System)
	- SVN (Apache Subversion)
	- Perforce Helix Core
- Third Generation - Distributed Version Control Systems
	- Git
	- Mercurial
	- and more
---
#### Problems before Version control
- Source code takes up too much space because it is repeated in every version.
- It is hard to acquire information about when and where changes occurred.
- Finding the exact version which the client has problems with is difficult.
---
####  Source Code Control System (SCCS)
- developed by Marc Rochkind at [[Bell Labs]] in 1972.
- Key ideas:
	- Worked on individual files. So each file had their own version
	- *Checksum* to ensure file integrity
	- *Delta* : Rather than storing entire files in different versions, store the differences
	- *Interleaved Deltas*: to give constant time checkout of any version ie. older versions take same time as newer versions to be checked out.

---
#### Revision Control System (RCS)
- written in C by Walter Tichy in 1982 as an alternative to SCCS as it was not open source at the time.
- Key ideas
	- *Reversed delta*: this made recent revisions to be fetched faster than the older versions.
	- No checksum was stored, so no gaurantee of file integrity.
---

#### CVS - Concurrent Versions System(Second Generation)

- created by Dick Grune in 1986 with the goal of adding a *networking element* to version control. It is also written in C.
- provides a set of commands for interacting with files in a project, but uses RCS as backend.
- Key ideas:
	- centralized repository model: allowed multiple developers across geography to work on a software project

---
#### SVN - Subversion - Second Generation

- created in 2000 by Collabnet Inc and is now maintained by the Apache Software Foundation.
- Key ideas:
	-  *atomic commits* which ensured that a commit would either fully succeed, or be completely abandoned if an issue occurred.
	- *FSFS(File System atop the File System)*: it creates its database structure using a file and directory structure that match the operating system file system it is running on.
	- the *deltas are compressed* using `lz4` or `zlib` compression algorithms to further reduce their size.

---
#### Git(1)
- created in 2005 by Linus Torvalds (also the creator of [Linux](https://www.linux.org/forums/linux-beginner-tutorials.123/)) and is written primarily in C combined with some shell scripts.
- Key ideas:
	- Distributed Version Control: uses a distributed model instead of centralized model. Every developer has a complete local copy of the entire repository, including the full history. Making offline work possible.
	- *Snapshots Instead of Deltas:* Instead of storing differences (deltas) between file versions, Git stores snapshots of the entire project state at each commit. 
---
#### Git(continued)
- *Efficient Storage:* Despite storing complete snapshots, Git is storage-efficient due to the use of content-addressable storage and compression.
- *Content-Addressable Storage*: Git uses SHA-1 hashes to identify objects (blobs, trees, commits, tags), ensuring content integrity and allowing easy identification of changes. Each object’s hash is based on its content, making it easy to detect duplicates or changes.
- 
---
#### How to use Git? 
Key definitions:
- **Working Directory:** The directory on your computer where you are making changes to your project.
 - **Repository**: A storage location where your project lives, containing all the files and revision history. (local vs remote)
  - **Commit**: A snapshot of your changes, saved to your local repository. Each commit is uniquely identified by a checksum.
  - 
---
##### Setting up git
```bash
# installation 
sudo apt update
sudo apt install git
git --version # git version 2.45.2
# global settings
git config --global user.name "Your Name"
git config --global user.email "youremail@domain.com"
```

---
##### Git Workflow
![](https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fwebipedia.es%2Fwp-content%2Fuploads%2F2018%2F09%2F26_FlujoTrabajo.jpg&f=1&nofb=1&ipt=f33c28b30114bec9fdbdbaf9d49745c39d791238760c583bab1e2dddeb619825&ipo=images)
Pic credit: [Git introduction](https://zigabrencic.com/blog/2020-02-18)

---
#### Working folder <=> staging area 
1. How to bring a folder under git"s jurisdiction?
```bash
git init .
```
2. How to start tracking file changes?
```bash
# add file to staging area
git add /path/to/file
```
3. How to investigate staging area?
```bash
# view 
git status
# view changes
git diff /path/to/file
```
4. How to discard untracked changes in working folder?
```bash
git restore /path/to/file
```
---
#### Staging area <=> Local repository
1. How to commit all files in staging area to local repository? 
```bash
# staging area -> local repository
git commit -m"commit message"
```
2. How to view commit history?
```bash
git log
```
3. How to checkout working directory to a previous commit?
```bash
# local repository -> working directory
git checkout commit_id
```
---
#### Local repository <=> Remote repository
1. How to add a remote repository?
```bash
git remote add origin git@github.com:Ankush-Chander/git_demo.git
```
2. Push changes to remote repository
```bash
git push origin main
```
3. Pull latest changes from remote repository
```bash
git pull origin main
```
4. How to create a local repository out of existing remote repository?
```bash
git clone git@github.com:path/to/remote/repository
```
---
#### Branches
![branch](https://i2.wp.com/digitalvarys.com/wp-content/uploads/2019/06/GIT-Branchand-its-Operations.png)
Pic credit: [https://digitalvarys.com](https://digitalvarys.com/git-branch-and-its-operations)

---
1. Create and switch to new branch
```bash
 git checkout -b <my branch name>
```
3. Merge feature branch into main
```bash
# switch to main branch
git checkout main
# merge feature branch
git merge <my branch name>
```
4. Push branch code to remote repo
```bash
git push origin <my branch name>
```
---
#### Pull requests
**A pull request (or PR)** is a way to alert a repo's owners that you want to make some changes to their code. It allows them to *review the code* and *make sure it looks good* before putting your changes on the primary branch.

---
#### Github + mkdocs
MkDocs is a **fast**, **simple** and **downright gorgeous** static site generator that's geared towards building project documentation. You can also use it to *create your own homepage* and host it on github pages.
```bash
# install mkdocs
pip install mkdocs
# setup mkdocs for current folder
mkdocs new .
# host site locally for debugging
mkdocs serve
# build static website
mkdocs build
# host on github-pages
mkdocs gh-deploy
```



---
#### Github tips
1. Use default README.md to introduce yourself.
2. Use mkdocs + github to host your homepage
3. Make yourself reachable by adding  link to other profiles(Linkedin, Twitter etc) and vice versa
4. Actively code in public, push on github and seek feedback. Can be anything, your assignments, toy projects.
---
#### Suggested followup reads
1. [How To Become A Hacker by Eric Steven Raymond](https://www.catb.org/~esr/faqs/hacker-howto.html) on mindset, approach, practices towards programming.

---
### References
1. [Version Control Systems | A Technical Guide](https://initialcommit.com/blog/Technical-Guide-VCS-Internals)
2. [Git - Book](https://git-scm.com/book/en/v2)
3. [MkDocs - Documentation](https://www.mkdocs.org)
4. [5 tips for making your GitHub profile page accessible - The GitHub Blog](https://github.blog/developer-skills/github/5-tips-for-making-your-github-profile-page-accessible)
