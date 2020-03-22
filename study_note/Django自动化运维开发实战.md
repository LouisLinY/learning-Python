# Django自动化运维开发实战

## Python运维场景实战

互联网的飞速发展，普及率上升的结果：

- 网站用户规模、使用快速上升
- 要求庞大系统支撑能力（庞大的系统去支撑起海量的用户）
- 更快速的运维效率应对突发流量
- 更加自动化的方式减少人员的投入成本
- 更可靠的技术手段，保障系统的稳定

云技术已经渗透到各领域，结果：

- 大部分技术架构设计不再以网络设计、IDC、和系统硬件等方面作为重点
- 运维基础的、繁琐的工作逐步减少
- 小公司也不再需要一个运维工程师或者系统工程师

运维自动化技术

Python（模块支持丰富、语法通俗易懂）+Django（成熟的WEB框架）

开发人员：没有系统管理、网络管理等相关运维工作经验，项目设计往往是大打折扣

运维人员：不具备开发能力、没有项目的开发经验或者能力

做好一个DEVOPS=2年运维工作+2年开发



DevOps构建之路、自动化资产扫描发现（资产扫描作用、nmap存活扫描、telnetlib端口扫描、pexpect登录探测、paramiko登录探测）、ansible自动化任务（核心类调用、ansible playbook、api接口封装、方法改写、redis消息存储、Mongo事件日志）



**资产自动化扫描发现**

用python程序扫描发现企业内部的所有资产，当资产出现变化能自动及时的发现并完成资产变更。

资产包括：KVM虚拟机、VM虚拟机、docker容器、网络设备等

资产信息：（硬件型号、SN、MAC、系统版本等）

定时扫描、自动化发现



**ansible自动化任务执行**

使用ansible的ad-hoc和playbook实现批量主机的自动化任务。

KVM\ESX\Docker\Machine\NetWork



信息收集-》数据收集-》关联平台



数据接收-》数据校验-》数据清洗转化-》逻辑处理-》数据入库-》任务触发-》校验审核



后台展示页面：

资产信息、报表信息、状态信息、信息变更、信息录入



工程代码：https://github.com/iopsgroup/imoocc

Mongo：日志和事件存储

redis：消息队列

mysql创建用户及授权:grant all on imoocc.* to imoocc@'127.0.0.1' identified by '123456';

flush privileges;

修改mysql字符集：

[client]

default-character-set=utf8

[mysqld]

character-set-server=utf8

collation-server=utf8_general_ci



























