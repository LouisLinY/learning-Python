# **修改pip镜像源为国内镜像源**

## 1.  概述

 pip命令行工具是Python 的[软件包安装程序](https://packaging.python.org/guides/tool-recommendations/)，作为python第三方库的主要安装方式（即通用的Python包管理工具）。提供了对python包的查找、下载、安装、卸载等功能。

命令使用格式如下：

```
pip <command> [options]
```

Commands：

- `install` ：安装包 （Install packages）

- `download` ：下载包 （Download packages）

- `uninstall` ：卸载包（Uninstall packages）

- `freeze` ：按需求格式安装的包的输出（Output installed packages in requirements format）

- `list` ：列出已安装的包（list installed packages）

- `show` ：显示已安装第三方包的信息（Show informations about installed packages）

- `check` ：检查已安装的第三方包是否具有兼容的依赖项（Verify installed packages have compatible dependencies）

- `config` ：配置管理本地和全局配置（Manage local and global configuration）

- `search` ：搜索PyPi查找包（Search PyPi for packages）

- `wheel` ：根据你的需要构建轮子（Build wheels from your requirements）

- `hash` ：包存档的哈希计算（Compute hashes ofpackages archives）

- `completion` ：用于命令完成的辅助命令（A heloer command used for command completion）

- `debug` ：显示对调试有用的信息（show information useful for debugging）

- `help` ： 显示命令的帮助（show help for commands）

  

## 2.  背景描述**

pip默认的镜像源为[官网源](https://pypi.python.org/simple)，国内很多网络环境下，访问不稳定，而且下载速率慢，有时候根本连接不上，另外国内也有镜像源，可以修改pip的镜像源为国内

### **2.1 常用国内镜像**

[豆瓣]( http://pypi.douban.com/simple)

[阿里云](http://mirrors.aliyun.com/pypi/simple/)

[中国科学院]( http://pypi.mirrors.opencas.cn/simple/)

[中国科技大学]( https://pypi.mirrors.ustc.edu.cn/simple/)

[清华大学 ](https://pypi.tuna.tsinghua.edu.cn/simple/)

### 2.2 临时指定软件源

通常来讲，如果想要手动指定临时软件源来安装软件的话，可是使用如下格式:

```shell
pip install packageName -i https://xxxx.com/simple  #（其中xx是指定的镜像源地址，可以指定为国内豆瓣源、阿里源、中国科学院、中国科技大学、清华大学）
```

例如，使用豆瓣源来安装pipenv包

```shell
    pip install pipenv -i https://pypi.douban.com/simple
```

### 2.3 永久指定软件源

 如果想要使pip的配置永久生效，就要使用配置文件方式。针对不同的系统，配置文件稍稍有所不同。 

#### 2.3.1 针对整个系统

 Unix/Linux配置文件 `/etc/pip.conf`，当然也可以是一个任何路径下的 “pip” 子目录，然后通过环境变量`XDG_CONFIG_DIRS`来指定, 例如：`/etc/example/pip/pip.conf`.。

 macOS 配置文件: `/Library/Application Support/pip/pip.conf` 

 Windows 7 及其更高版本的配置文件是隐藏的, 就可以在`C:\ProgramData\pip\pip.ini`中写入 

#### 2.3.2 针对当前用户

在UNIX系统中默认的配置文件是: **$HOME/.config/pip/pip.conf**。 which respects the XDG_CONFIG_HOME environment variable。

在macOS系统中配置文件是：**$HOME/Library/Application Support/pip/pip.conf**。在$HOME/Library/Application Support/pip/目录不存在的情况下，也可是是**HOME/.config/pip/pip.conf**。

在Windows系统中默认的配置文件是：**%APPDATA%\pip\pip.ini**。

pip也支持经典的每个用户一个配置文件的方式，具体的位置是：

Unix 和 macOS 配置文件: **$HOME/.pip/pip.conf**
        Windows t配置文件: **%HOME%\pip\pip.ini**
当然，也可是使用环境变量PIP_CONFIG_FILE来自定义配置文件位置

#### 2.3.3 针对虚拟环境

 Unix 和 macOS 下文件是: **$VIRTUAL_ENV/pip.conf**

Windows 下的文件是: **%VIRTUAL_ENV%\pip.ini** 

#### 2.3.4 配置文件的级别

If multiple configuration files are found by pip then they are combined in the following order:

The site-wide file is read
The per-user file is read
The virtualenv-specific file is read

Each file read overrides any values read from previous files, so if the global timeout is specified in both the site-wide file and the per-user file then the latter value will be used.

### 2.4  pip多镜像源配置文件内容

```ini
[global]
timeout=60
index-url=http://pypi.douban.com/simple
extra-index-url=http://mirrors.aliyun.com/pypi/simple/
		https://pypi.tuna.tsinghua.edu.cn/simple/
		http://pypi.mirrors.ustc.edu.cn/simple/
[install]
trusted-host=pypi.douban.com
             mirrors.aliyun.com
             pypi.tuna.tsinghua.edu.cn
             pypi.mirrors.ustc.edu.cn
[freeze]
timeout = 10
```

# 